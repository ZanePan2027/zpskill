# 安装与更新

用户要求更新本产品时，定位当前安装位置、官方仓库ZanePan2027/zpskill及安装方式；读取当前修订，与本地内容比较。已授权更新即可继续，保留用户对Skill的本地修改与可恢复副本，再按当前客户端更新本产品。

更新前先读仓库根目录的 `UPDATE.json`（https://raw.githubusercontent.com/ZanePan2027/zpskill/main/UPDATE.json）：对比 `version` 与本地已装版本，把 `notice` 里写的这次改了什么告诉用户，版本一致就说已是最新；详情看 `details_url` 的提交记录。读取失败时直接按下面的步骤更新，并说明没能读到更新说明。

标准安装命令：`npx -y skills add ZanePan2027/zpskill -g --skill zp-life zp-workspace zp-question zp-judge zp-check zp-partner zp-self zp-support zp-perspective zp-guide`（仓库同时收录求职工具箱，只装本产品就用 --skill 指定；旧仓库名 zane-life-workbench 已自动跳转）。项目级安装省略-g，用户选择原宿主。插件安装使用Claude Code插件管理器更新zpskill市场中的zp-life等插件。手动安装只替换本产品对应Skill目录，实际文件清单以仓库为准。

更新后读回主入口、引用方法和工具，处理实际变更，告诉用户已更新的用途及继续方式。个人工作台资料和事件沿原位置读取；方法更新与用户主动要求的目录迁移分别执行。
