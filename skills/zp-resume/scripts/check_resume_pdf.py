#!/usr/bin/env python3
"""Run structural checks on a resume PDF; never replace visual QA."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:  # Optional; a Poppler fallback is available below.
    PdfReader = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--pages", type=int, default=None,
                        help="Expected page count. Omit when the project contract does not fix it.")
    parser.add_argument("--require", action="append", default=[])
    parser.add_argument("--forbid", action="append", default=[])
    parser.add_argument("--require-link", action="store_true")
    parser.add_argument("--a4-tolerance", type=float, default=3.0,
                        help="Allowed page-size difference in PDF points.")
    parser.add_argument("--text-layer", action="store_true",
                        help="Also check what a machine reads: reading order, standard headings, "
                             "contact details, split characters, smallest type, page-bottom fill. "
                             "Results are hints, not pass/fail for design.")
    return parser.parse_args()


def annotation_subtype(annotation) -> str:
    try:
        return str(annotation.get_object().get("/Subtype", ""))
    except Exception:
        return ""


HEADINGS = ("教育", "工作经历", "实习", "项目", "技能", "Education", "Experience", "Skills", "Projects")


def text_layer_hints(reader) -> list[str]:
    """What a parser sees: order, headings, contact, split headings, smallest body type, bottom fill.

    Built on pypdf visitor_text; coordinates are PDF points. Hints only: a person still
    reads the rendered pages. Tuned against real resumes: page numbers, running footers and
    per-glyph body text (common in generated PDFs) are not reported as problems.
    """
    hints: list[str] = []
    runs: list[tuple[int, float, float, float, str]] = []  # page, y, x, size, text
    for index, page in enumerate(reader.pages, start=1):
        page_h = float(page.mediabox.height)
        def visit(text, cm, tm, font_dict, font_size, _i=index, _h=page_h):
            if text and text.strip():
                x = tm[4] * cm[0] + tm[5] * cm[2] + cm[4]
                y = tm[4] * cm[1] + tm[5] * cm[3] + cm[5]
                size = abs(font_size * (tm[3] if tm[3] else 1) * (cm[3] if cm[3] else 1))
                runs.append((_i, y, x, size, text.strip()))
        try:
            page.extract_text(visitor_text=visit)
        except Exception:
            return ["could not read text positions; skip text-layer hints"]
    if not runs:
        return ["no text positions found (scanned or outlined text?)"]

    # page numbers / running footers: short "1 / 2", "- 1 -", "Page 1" near the page edge are ignored
    pagenum = re.compile(r"^(\d+\s*/\s*\d+|[-–—]?\s*\d+\s*[-–—]?|page\s*\d+)$", re.I)
    body = [r for r in runs if not pagenum.match(r[4])]
    if not body:
        return ["only page numbers were extracted"]

    full = "\n".join(r[4] for r in body)
    low = full.lower()
    if not any(h in low for h in ("工作经历", "实习", "experience", "经历")):
        hints.append("no standard experience heading found (工作经历 / 实习 / Experience); parsers may not segment sections")
    if not any(h in low for h in ("教育", "education", "学历")):
        hints.append("no standard education heading found (教育 / Education)")
    head = " ".join(r[4] for r in body[:12])
    if not re.search(r"1[3-9]\d{9}|@[\w.-]+\.\w+|https?://|\+\d{1,3}[ \d-]{8,}", head):
        hints.append("no phone / email / link among the first extracted lines; contact may be read last or lost")

    # reading order: jump back UP the page by a lot, across columns, ignoring page numbers
    jumps = 0
    prev = None
    for page_no, y, x, size, t in body:
        if prev and prev[0] == page_no and y - prev[1] > 150 and abs(x - prev[2]) > 100:
            jumps += 1
        prev = (page_no, y, x, size, t)
    if jumps:
        hints.append(f"extraction order jumps back up the page {jumps} time(s) across columns; sidebar / two-column text may be read out of order")

    # split headings: a short heading drawn one glyph at a time on the same baseline with big gaps
    split = 0
    by_line: dict[tuple[int, int], list[tuple[float, str]]] = {}
    for page_no, y, x, size, t in body:
        if len(t) == 1:
            by_line.setdefault((page_no, round(y)), []).append((x, t))
    for glyphs in by_line.values():
        glyphs.sort()
        if 2 <= len(glyphs) <= 8 and all(b[0] - a[0] > 14 for a, b in zip(glyphs, glyphs[1:])):
            split += 1
    if split:
        hints.append(f"{split} heading-like line(s) drawn one glyph at a time with wide gaps; letter-spaced headings may be split by parsers")

    # smallest type of body text (page numbers excluded; the smallest 5% are treated as labels)
    sizes = sorted(r[3] for r in body if r[3] > 0)
    if sizes:
        floor = sizes[max(0, int(len(sizes) * 0.05))]
        if floor < 7:
            hints.append(f"small type around {floor:.1f} pt; check readability when printed")

    last = [r for r in body if r[0] == len(reader.pages)]
    if last:
        page_h = float(reader.pages[-1].mediabox.height)
        fill = 1 - min(r[1] for r in last) / page_h
        hints.append(f"last page: content reaches {fill:.0%} of page height from the top (page-bottom balance is a visual call; see visual-and-pdf-qa)")
    return hints


def run_pdfinfo(pdf: Path, *options: str) -> str:
    result = subprocess.run(
        ["pdfinfo", *options, str(pdf)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "pdfinfo failed")
    return result.stdout


def fallback_with_pdfinfo(args: argparse.Namespace) -> int:
    """Run a transparent, narrower check when pypdf is unavailable."""
    if shutil.which("pdfinfo") is None:
        print(
            "BLOCKED: install pypdf or provide Poppler pdfinfo; no PDF parser is available",
            file=sys.stderr,
        )
        return 2

    errors: list[str] = []
    limitations: list[str] = []
    try:
        info = run_pdfinfo(args.pdf, "-box")
        struct_text = run_pdfinfo(args.pdf, "-struct-text")
        urls = run_pdfinfo(args.pdf, "-url")
    except Exception as exc:
        print(f"FAIL: pdfinfo fallback cannot inspect PDF: {exc}", file=sys.stderr)
        return 2

    page_match = re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)
    if not page_match:
        errors.append("cannot determine page count with pdfinfo")
        page_count = 0
    else:
        page_count = int(page_match.group(1))
        if args.pages is not None and page_count != args.pages:
            errors.append(f"expected {args.pages} pages, found {page_count}")

    size_matches = re.findall(
        r"^(?:Page(?:\s+\d+)? size):\s+([\d.]+) x ([\d.]+) pts",
        info,
        re.MULTILINE,
    )
    if not size_matches:
        errors.append("cannot determine page size with pdfinfo")
    else:
        a4_width, a4_height = 595.276, 841.890
        for index, (width_raw, height_raw) in enumerate(size_matches, start=1):
            width, height = float(width_raw), float(height_raw)
            if not (abs(width - a4_width) <= args.a4_tolerance and
                    abs(height - a4_height) <= args.a4_tolerance):
                errors.append(
                    f"page {index} is not portrait A4: {width:.1f} x {height:.1f} pt"
                )

    if not struct_text.strip():
        errors.append("PDF has no tagged extractable text in pdfinfo fallback")
    for phrase in args.require:
        if phrase not in struct_text:
            errors.append(f"required text missing in tagged-text fallback: {phrase!r}")
    for phrase in args.forbid:
        if phrase in struct_text:
            errors.append(f"forbidden text present: {phrase!r}")

    url_lines = [line for line in urls.splitlines() if re.search(r"https?://|mailto:|tel:", line)]
    if args.require_link and not url_lines:
        errors.append("no URL found by pdfinfo -url")
    limitations.append("fallback uses tagged structure text; character extraction may differ from pypdf")

    if errors:
        print("FAIL (pdfinfo fallback)")
        for error in errors:
            print(f"- {error}")
        for limitation in limitations:
            print(f"- limitation: {limitation}")
        return 1

    print(f"PASS WITH LIMITATIONS: {args.pdf}")
    print(f"- pages: {page_count} portrait A4")
    print(f"- URL objects: {len(url_lines)}")
    for limitation in limitations:
        print(f"- limitation: {limitation}")
    print("- structural checks only; render and review every page as continuous reading bands")
    return 0


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    if not args.pdf.is_file():
        print(f"FAIL: file not found: {args.pdf}", file=sys.stderr)
        return 2


    if PdfReader is None:
        return fallback_with_pdfinfo(args)

    try:
        reader = PdfReader(str(args.pdf))
    except Exception as exc:
        print(f"FAIL: cannot open PDF: {exc}", file=sys.stderr)
        return 2

    if args.pages is not None and len(reader.pages) != args.pages:
        errors.append(f"expected {args.pages} pages, found {len(reader.pages)}")

    texts: list[str] = []
    link_count = 0
    a4_width, a4_height = 595.276, 841.890
    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        is_a4 = (abs(width - a4_width) <= args.a4_tolerance and
                 abs(height - a4_height) <= args.a4_tolerance)
        if not is_a4:
            errors.append(f"page {index} is not portrait A4: {width:.1f} x {height:.1f} pt")
        text = page.extract_text() or ""
        texts.append(text)
        if not text.strip():
            errors.append(f"page {index} has no extractable text")
        for annotation in page.get("/Annots", []):
            if annotation_subtype(annotation) == "/Link":
                link_count += 1

    full_text = "\n".join(texts)
    for phrase in args.require:
        if phrase not in full_text:
            errors.append(f"required text missing: {phrase!r}")
    for phrase in args.forbid:
        if phrase in full_text:
            errors.append(f"forbidden text present: {phrase!r}")
    if args.require_link and link_count == 0:
        errors.append("no PDF link annotation found")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {args.pdf}")
    print(f"- pages: {len(reader.pages)} portrait A4")
    print(f"- extractable characters: {len(full_text.strip())}")
    print(f"- link annotations: {link_count}")
    if args.text_layer:
        print("- text-layer hints (machine reading, not a design verdict):")
        for hint in text_layer_hints(reader):
            print(f"  * {hint}")
    print("- structural checks only; render and review every page as continuous reading bands")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
