## 2026-10-26 · 人生搭子称呼更新

- 按作者最新决定，公开介绍中的「永生搭子」改为「人生搭子」；英文改为 AI companion for life's journey。中文与英文首页、教程、作者与媒体资料、SVG 配图、插件说明和主 Skill 描述已同步。
- 「24小时重启人生」「陪伴你过好人生」、Skill ID、安装命令与 1.5.0 版本保持原样。图片文件路径保留以维持已有链接。

## 2026-10-24 · 24小时重启人生与永生搭子

- 产品介绍统一为「24小时重启人生」，AI 的关系定位统一为「永生搭子，陪伴你过好人生」。
- 更新中英文首页、作者与引用介绍、主线手册、开场与长期接续文案，以及插件中的产品介绍。
- 新增中英文首页主图，重绘共同生活与共同记忆流程图，并统一求职图的陪伴视角。
- 新增「和永生搭子开始的第一天」中英文教程，保留从眼前一个问题开始的入口。
- 这是定位、文案与视觉更新；功能版本沿用 1.5.0，安装命令与 Skill ID 不变。

## 1.5.0 · 2026-10-17 · 从第一次使用到现实反馈

- 仓库与作者介绍统一为「zpskill · Zane的人生经营 Skills」，明确长期 AI 人生参谋的用途，保留现有仓库地址和安装入口。
- 新增首次使用、长期接续、回避循环三条中英文教程；补作者说明与第三方引用材料。教程示例明确标为虚构，不作真人效果宣称。
- `zp-awaken` 0.3.0：先认真实障碍，区分事实与预测，借鉴 CBT 共同检验；按本人意愿做有限尝试，反馈允许支持、削弱预测或仍然未知。休息、学习、价值选择和工具建设不自动判为逃避。
- 记忆接续依赖使用者授权的工作台与宿主文件访问，不宣称安装后自动跨客户端共享记忆。
- Aligned the project and author descriptions, added three bilingual tutorials and a third-party fact sheet, and updated `zp-awaken` to 0.3.0 for collaborative checking of predictions and real constraints. Examples are fictional, and no search ranking or clinical effectiveness is claimed.

# 2026-10-12 · 为你放大优势，等面试再补细节 / Amplify, then explain in the interview

- 简历和作品集的任务是放大你的优势、让 HR 想约你面试：证据级别、口径、边界留在底稿，成品里不写防御和解释，需要二次说明的留到面试当面补。
- 每个岗位的“可信”长得不一样：设计师靠作品和版式，销售靠客户和数字，程序员靠代码和文档；视觉不预设克制，从你的岗位和审美里一步步走出来。你可以接入自己找的设计 Skill 做视觉层（文字和事实不动），也可以把作品集和简历合成一份 PDF。
- 稿子里的每个动词和数字都要能在你给的原话里找到，写完逐句自检。
- 回复里不再说“我读了指南第几章”“我已记在事项里”，也不一次倒出你的旧事。
- Résumés and portfolios exist to amplify your strengths and earn an interview: evidence grades and caveats stay in working notes, details wait for the interview. Visual style follows your role, not a default of restraint; you may plug in your own design Skill for the visual layer.

# 2026-10-11 · 机器阅读检查校准 / Text-layer check tuned

- `check_resume_pdf.py --text-layer` 用真实两页简历校准：页码、页脚小字、逐字绘制的中文正文不再误报。
- `--text-layer` tuned on real resumes: page numbers, footers and per-glyph body text no longer raise false alarms.

# 2026-10-11 · 走出象牙塔：底稿与成品分离 / Working notes vs. the finished piece

- 简历、作品集、案例的成品里只留一个口径词、必要的时间词和正向表述，证据级别、取数口径、归因限制留在底稿和面试口径里；不再出现“不能作为……证据”“尚未验证”“证据等级”这类句子。
- 反推自本人认可的最终简历与作品集：经历“结果在前、动作在后”、标题行放职位｜汇报线｜团队规模、摘要“一句本人判断加一个硬锚点”、中英文结构同构；案例首屏用“问题—决定—结果”摘要卡，多篇深读页串成单线阅读；本人立场句保留，只删无主体的升华。
- 新增面试素材库、逐轮存档与撤回清单；offer、合同读法；应届生三方协议与违约成本的判断顺序；`check_resume_pdf.py --text-layer` 检查机器会怎样读简历。
- 动效改为“底线必须守、数值作建议”；颜色一色一义；zp-redact 对精确经营数据改为提示一次、由本人决定。
- Working notes (evidence grades, sourcing, attribution limits) stay out of the finished resume and portfolio; only one short qualifier word and positive phrasing remain. Derived from the owner-approved final resume and portfolio.

# 2026-10-11 · 自动调用接通 / Auto-routing

- `zp-life` 入口表补上：找工作交给 `zp-career`、被裁和合伙等场景的路径、要说具体规定时先读 `zp-guide`；所有 Skill 的共同口吻加入同一条规则。`zp-guide` 新增章节速查，联不了网时可用已标明出处的转述。
- `zp-life` now routes job search to `zp-career`, adds paths for layoffs and partnerships, and reads `zp-guide` before stating concrete rules. `zp-guide` gains a chapter map and can fall back to attributed summaries offline.

# 2026-10-11 · 认知觉醒 / Awareness

- 新增 `zp-awaken`：一层一层往下看，发现想不到的出路，落到小实验。主线 11 个、全库 22 个。
- Added `zp-awaken`: look layer by layer to find the unseen way out, ending in a small experiment. 11 main-line Skills, 22 in total.

# 2026-10-11 · 设定你自己的 AI 小伙伴 / Set up your own AI partner

- `zp-partner` 先用一张四行的起点卡设定，按相处阶段轻轻邀请，不在第一次对话就要求设定。
- `zp-partner` starts from a four-line card and invites gradually, never in the first conversation.

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
