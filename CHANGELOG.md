# 2026-10-11 · 把话说出去 / Saying it

- `zp-life` 新增「把话说出去」：现写、用你的口吻、不套话术。
- `zp-life` adds “Saying it”: fresh drafts in your own voice, no canned scripts.

# 2026-10-11 · 补充心理援助渠道 / Support lines added

- `zp-support` 补上中国大陆非紧急心理援助渠道（12356、12355、12338），说明用途与限制。
- `zp-support` lists non-emergency support lines for mainland China with their limits.

# 2026-10-11 · 看见你自己，也看见对方 / See yourself, and the other side

- 新增 `zp-perspective`（视角互换）：站到对方的位置看事情，异性、老板与员工、买家与卖家都适用。`zp-self` 新增发现独有优势，以及觉得没价值、没意义时先确认安全再找小入口；`zp-support`、`zp-judge`、`zp-life` 配套补强。起步只带一个问题就行，第一次会问怎么称呼你。
- Added `zp-perspective` (see the other side's position). `zp-self` finds what is distinctly yours and, when you feel worthless, checks safety first; `zp-support`, `zp-judge`, `zp-life` are strengthened to match. Starting needs only one question; it asks what to call you.

# 2026-10-09 · 新增判断与复核 / Judgment and re-check added

- 新增 `zp-judge`：对“要不要改／做”先判断成不成立，对做与不做都让反方说满，再给改、不改或再观察，附翻转条件和一个最小实验。
- 新增 `zp-check`：复核 AI 的进展和产出——AI 说做完了怎么确认、越聊越偏怎么重开、AI 总说好怎么办。
- `zp-question` 补充：说不清时最多问两个问题，并同时给出可填空的问题模板。
- Added `zp-judge` (decisions under thin evidence) and `zp-check` (re-checking AI claims and drifting chats); `zp-question` now asks at most two questions and always gives a fill-in template.

# 2026-10-09 · 更新前先告诉你这次改了什么 / Updates now tell you what changed

- 新增 `UPDATE.json`：更新时先读它，告诉你当前版本、最新版本和这次改了什么，再更新。
- 之后的提交说明用中文写成更新公告，直接看[提交记录](https://github.com/ZanePan2027/zpskill/commits/main)就能知道每次改了什么。
- Updating now first reads `UPDATE.json` and tells you the installed and latest versions and what changed. Commit messages are written as plain update notes (in Chinese).

# 2026-10-09 · Skill 改名 / Skills renamed

所有 Skill 改用统一前缀 `zp-` 加一个说明用途的短词，方便输入和记忆。Skill 的内容没有改变。已安装旧名字的人，请用新名字重新安装。
All Skills now use the `zp-` prefix plus a short purpose word. Contents are unchanged; reinstall to get the new names.

| 旧名 / Old | 新名 / New |
|---|---|
| zane-workbench | zp-life |
| zane-workbench-curator | zp-workspace |
| zane-question-intent-translator | zp-question |
| zane-agent-identity-card-builder | zp-partner |
| zane-self-insight | zp-self |
| zane-psychological-support | zp-support |
| life-decision-guide | zp-guide |
| zane-career-assets | zp-career |
| zane-career-portfolio-builder | zp-materials |
| zane-career-resume-builder | zp-resume |
| zane-career-application-greeting | zp-greeting |
| zane-career-portfolio-architecture | zp-portfolio |
| zane-career-portfolio-website-design | zp-site |
| zane-career-case-editor-zh | zp-editor |
| zane-evidence-weighted-case-storytelling | zp-story |
| zane-portfolio-multi-format-qa | zp-qa |
| zane-former-employer-data-redactor | zp-redact |
| zane-design-reference-to-prompt | zp-design-prompt |

# 2026-10-09 · 合并为 zpskill / Merged into one repository

- 「过好你的人生」（原 zane-life-workbench）与「走出象牙塔」（原 zane-career-skills）合并为同一个仓库 zpskill，Skill 内容不变。
- 安装命令改为 `--skill` 指定其中一套，或 `--all` 两套都装；Claude Code 插件市场改为 zpskill。
- 各产品的版本与更新记录移到 [docs/life](docs/life/CHANGELOG.md) 和 [docs/career](docs/career/CHANGELOG.md)。
- Both products now live in one repository with their Skills unchanged; install one set with `--skill` or both with `--all`. Per-product versions and changelogs moved under `docs/`.
