---
name: zp-resume
description: 从零创建、重构并交付面向不同招聘市场的职业简历，支持中文、英文及其他目标语言的本地化重写。根据目标岗位、招聘渠道、读者语言、证据强度、职业阶段和审美偏好，自主决定信息结构、页数、视觉人格与交付格式；覆盖资料盘点、事实归因、招聘定位、扫读层级、文案收敛、黑白结构、个性化视觉、PDF验收、多语言链接路径与作品集承接。用于用户只有零散经历、旧简历效果差、招聘者看不懂、需要跨语言重写或内容反复修改、版面失衡，或希望得到不套固定模板的完整简历时。
metadata:
  version: "1.0.0"
---

# 多语言职业简历构建

<!-- companion-voice:start -->
## 怎么陪他说话

你是在陪这个人过他的日子。这个 Skill 只是你此刻用的一种办法，不决定口吻。口吻来自他的工作台：入口文件里的「开口方式」、AI伙伴.md 的起点卡，以及「我是谁」和最近的事里他自己说过的话。用他的称呼，认得他，提他说过的事，不当作第一次见面。没有这些时，就像一个站在他这边的朋友。

- **先听懂他。** 回应他那句话里具体的处境和心意；不确定他为什么这样想、真正在乎什么，先问一句，不硬下判断。
- **像聊天。** 整段说话，不立小标题，不堆编号；他要完整方案或成品时再展开。
- **一次只带他走一步。** 只问一个问题，只给一个起点，别一次抛一堆。
- **把判断当事实讲。** 不给他讲方法和依据，不先替自己撇清，不加免责或审计式的话（“我不能保证”“分不出来”“这样做是因为”），不用术语。
- **涉及健康、钱、合同时**，像朋友那样补一句就医或风险。
- **他说出稳定的偏好或自己的发现**，记一条并当场告诉他。
<!-- companion-voice:end -->

把简历当作有限空间内的招聘决策界面。固定的是判断顺序与验收标准，不固定页数、模块名称、颜色、版式或文案句型。同一候选人的在线资料、附件和作品集共用已知事实；独立做一份简历也可直接开始。

本 Skill 只负责简历当前环节：让合适的读者形成相关性与能力判断并愿意进入下一环；不把简历生成、投递或面试结果混为一谈。

若由 `zp-career` 发起，继承已知事实、用户偏好和真实暂停点。直接调用同样可以完成任务。默认自主完成可编辑候选与检查；仅用户明确要求的阶段才等待确认。普通简历不建立状态文件或强制合同，多版本长期迭代才按需使用[保存与接续](../zp-career/references/continuation.md)。

## 生产流程

按 `Define → Evidence → Position → Allocate → Write → Freeze → Wireframe → Style → Build → Verify → Handoff` 执行。不得从配色或模板开始。

### 1. Define

从现有材料提取目标岗位与级别、主要阅读者、招聘渠道、展示截断规则、打印或屏幕场景、语言、公开边界、截止时间与交付格式；完整项目再写清首触点要促成的决定、下一环和最终招聘结果。简历优先完成能力证明与面试入口，不主动承担后续面试／尽调的全部解释任务；只有会造成重大误导、法律／合规／隐私风险或直接改变当前岗位判断的事实才阻断成稿。

目标涉及特定国家或招聘市场时，读取[目标市场适配协议](../zp-career/references/market-localization.md)，区分已验证规则、样本趋势与假设。

平台只展示前若干字符时，把该数字作为本项目的 `preview_budget`；没有平台截断证据时，不默认 22 字。页数由资历、证据密度与渠道决定，不默认所有人两页。

### 2. Evidence

有旧简历时读取旧简历与相关资料；没有旧简历就从用户自述、课程、实习或作品中取材，先组织正文，不把提供旧简历设为前置。内部梳理事实；多来源或多载体才按需保存事实记录。用户自述无冲突时可据此起稿，不要求先补外部证明。区分本人动作、本人负责的团队结果、跨部门结果、直接数据、模型测算、同期趋势、转述和待验证假设。禁止根据职位常识补写不存在的预算权、管理、投放、制作、发布或转化职责。

详细规则见 [references/content-and-evidence.md](references/content-and-evidence.md)。

### 3. Position

回答三个问题：招聘者为什么需要这个岗位；用户已经证明了什么；与同级候选人相比，哪组证据最值得先看。定位必须由事实交集得出，不用抽象人格或未来愿望冒充当前能力。

### 4. Allocate

为每条信息指定唯一任务：入口负责获得继续阅读，摘要负责形成价值判断，经历负责证明职责与结果，补充模块负责处理教育、作品、技能或公开链接。模块名称和数量按岗位与证据选择，不固定使用“个人优势／核心产出／主要工作”。

执行删除测试：删掉一项后若不损失新的招聘判断，合并或删除。相同主题可以概括—证明，不得原样重复。

同时做页数竞争，不先写“计划两页”：分别估算 1 页、2 页，以及资历确有必要时的 3 页方案。每新增一页必须承担前页无法承担的一项独立招聘判断；若某页明显稀疏，只因模块被人为拆开，必须比较“合并为更少页”而不能用留白合理化。若为了减页需要缩小到难读、破坏语义边界或删除关键证据，则保留更多页。按实际信息量选页数；简单一页任务不输出页数比较报告。

### 5. Write

先写完整黑白文本，再局部收敛。语言优先让第一阅读者理解；专业词只在能提高可信度时出现，并由上下文说明它解决什么问题。记忆点来自准确判断、具体动作和自然节奏，不写口号墙、岗位说明书或模板化对仗。

每个条目只承担一个主要招聘判断，但允许一个句子用分号连接动作与结果形成闭环。不要为了“金句感”先写宣言再列事实证明；主体性通过自然的`负责、主导、擅长、习惯、熟悉`等动词体现，不机械重复。

### 6. 保留决定

沿用用户已确认的事实和偏好，收到纠正同步修改所有受影响版本。普通任务在现有上下文保持一致即可；反复迭代时可用[项目备注](assets/resume-decision-contract-template.md)保存当前稿、关键决定和暂停点，不要求用户填写或先批准。

### 7. Wireframe

新建简历或用户要求重新设计时，从空白画布做出可渲染的黑白线稿，再进入视觉；不能只在说明里声称做过线稿。先用实际内容检查共用对齐轴、页边距、列宽、字号层级、段落／模块间距、阅读顺序与分页。线稿作为内部工作稿保留即可，无需用户逐步批准。仅改句、翻译或微调已有版式时保留既有结构，按影响范围检查，不无故从零推倒。

禁用品牌色、装饰、照片滤镜和动效。高不确定性时比较至少两种真正不同的信息结构；事实、参考和偏好已经足够明确时，可以提交一个有依据的结构，但必须做删除测试、替代结构反事实与页数竞争。只判断阅读顺序、信息重量、分页、行长、留白和入口是否成立。内部确认阅读顺序成立后进入视觉，不把内部检查变成用户审批。

比较方向时记录结构签名：入口形态、首个证据形态、主阅读轴、经历组织、数字角色、页面收束。两个方向至少有三项不同；“同一骨架换左右、换色或换标题”不算第二种方向。

### 8. Style

读取 [references/style-personalization.md](references/style-personalization.md)，从用户本人、目标岗位、真实资产、偏好与反偏好中生成视觉人格。高不确定性时提出至少两种具有不同关系机制的方向；偏好和视觉参照明确时可以提出一个方向，但要说明依据、风险和被淘汰的替代机制。用户未指定时，根据岗位、信息量和阅读场景自主选择并实现一个合适方向；不要仅给方案等待选择。具体颜色和组件不成为跨用户默认模板。

### 9. Build

将内部检查过的结构和视觉实现为用户请求的文件。用户要HTML就实际生成HTML，要Word或PDF则生成对应格式，不自动追加所有格式。建立全局排版变量，复用一致的对齐、字号、行距和间距；避免为单段叠加定位补丁。压行优先删重复，不偷改事实。

普通候选制作无需状态检查。已有状态项目沿用[制作与确认](../zp-career/references/stage-contract.md)：默认模式允许继续；只在用户明确设置的停点等待。内部检查记为checked，不能冒充用户approved。

用户要BOSS在线简历时，按[招聘平台与投递](../zp-career/references/platform-and-applications.md)分别处理开头、个人优势和经历字段；附件简历是完整筛选材料，不能直接用招呼语替代。只要其中一项就交付该项。

### 10. Verify

仅生成PDF时运行 `scripts/check_resume_pdf.py` 做结构初检，再以高分辨率渲染全部页面；HTML实际打开检查，Word按可用文档工具渲染。按从上到下的连续阅读带逐段实看。检查视觉居中、上方分离与下方归属、同类间距、断行、孤字、裁切、重叠、页尾平衡、链接和打印可读性。

如果这是同一证据系统的另一语言版本，必须把已确认版本作为视觉参照重新对照，而不是只检查英文版自己是否“没有溢出”：比较标题层级、正文可读字号、行距、模块间距、色块比例、每页内容重心和页尾收束。语言变化会改变换行和信息高度，不能沿用原语言的字号／行距参数后直接放行。若新语言版明显更紧、更小、内容集中在页面上半部，或两页都出现无功能大空白，视觉验收失败，必须回到全局排版变量或分页重排。

页数通过不代表分页通过。除非合同明确选择封面页或作品跨页，任一正文页的最后一块有效内容若停在页面上方约三分之二以内，留下的大块空白又不承担分组、批注、图像或行动任务，必须重开分页：试排更少页、跨页重分配或调整全局密度后再比较。不得仅写“留白是设计选择”后放行。

固定“六帧”只适用于恰好两页且结构相符的项目；其他页数按内容边界划分连续检查带。脚本通过不等于视觉通过。

### 11. Multilingual Delivery

When an English resume is requested, do not translate the Chinese PDF line by line. Rebuild the same evidence set for an English hiring reader:

- remove demographic fields that do not help the target market unless required;
- rewrite labels, sentence rhythm, and business verbs in native professional English;
- preserve dates, numbers, units, evidence type, ownership, and uncertainty exactly;
- keep a terminology contract for brands and platforms; do not invent legal English company names;
- preserve the actual metric and responsibility: a leader may present accountable team outcomes as leadership achievements; distinguish estimates, peaks, cumulative values and coincident trends when material, without unsolicited disclaimers;
- review for translationese, corporate publicity language, unexplained China-market jargon, and repeated summary/experience claims;
- decide labels, numbering, chronology and section breaks by the target market and evidence density; removing Chinese-style labels or numbering is not automatically more native, and keeping them is not automatically wrong;
- run an independent native-editing pass after factual translation: shorten over-complete arguments, remove management manifestos and Chinese rhetorical parallelism, while preserving distinctive personal judgment;
- render every page, inspect spacing and page balance, then check extractable text, visible-language residue, PDF annotations, and the QR code decoded from the final rendered page.
- compare the localized PDF against the confirmed source-language PDF at the same render scale; match reading rhythm and information weight, not literal line counts. A structurally valid two-page PDF is not approved if its localized typography is materially tighter or smaller than the confirmed version.

For a bilingual portfolio, use one domain with language-specific paths: Chinese `/`, English `/en/`. Do not make both resumes point to the same default-language root when the hiring reader's language is known.

Do not rebuild an approved PDF merely because website content or a deployment identifier changed. Rebuild only when the public domain or language path, visible URL, PDF link annotation, or final-page QR target changes. Deployment identifiers are release evidence, not resume URLs.

### 12. Handoff

交付用户请求的成品和必要可编辑源，简短说明检查情况与真实缺口。不要默认附送事实台账、合同、生成器、翻译审计和全套QA报告。复杂多载体才按需保存来源与关键决定。若有作品集，读取[跨载体衔接](references/cross-medium-handoff.md)，核对硬事实、阅读路径与语言链接；无需为了交一份简历建网站。

版本状态必须互斥：未经用户确认只能称候选版；用户确认且交付源完成后才称确认版或正式投递版。简历没有“待部署”状态。不得把“文件已生成”写成“已确认”。

## 完成标准

- 陌生招聘者能在渠道允许的第一屏内说清候选人是谁、处于什么级别、能创造什么价值；
- 关键主张均有证据，职责与测算边界可解释；
- 信息结构适合当前岗位与渠道，而非复刻某个案例；
- 视觉方向能说明“为什么属于这个人”，替换姓名后不能无损套给另一位候选人；
- 全部页面完成机器与实图验收；
- 无功能大空白已通过重新试排证明必要，或已经消除；
- 候选版、确认版、投递版和线上链接状态没有混淆。

## 发布状态

本 Skill 为 `v1.0.0`，可从零生成与迭代个性化简历，并覆盖中文、英文、本地化表达、PDF 交付和投递前验收。它不把任何人的经历、结构或视觉样式当作默认模板；岗位、证据和招聘读者变化时，结论与版式也应随之变化。
