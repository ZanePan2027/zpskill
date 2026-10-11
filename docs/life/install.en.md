# Installation and updates

[简体中文](install.md)

## Supported Agents

Doubao, WorkBuddy, Claude Code, Codex, and other Agents that support Skills. Choose the installation method for your client below.

## Quick installation

For Agents listed in the installer, such as Codex and Claude Code, run in a terminal with Node.js and `npx` available:

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zp-life zp-workspace zp-question zp-judge zp-check zp-partner zp-self zp-support zp-perspective zp-awaken zp-guide
```

`--all` installs all Skills into every Agent the installer supports, with no prompts; reload Skills if the client requires it. To install into one Agent only, use `--skill "*" --agent <name>` instead. Omit `-g` to install only in the current project.

Or ask your Agent:

```text
Install the Life Skills (11: zp-life, zp-workspace, zp-question, zp-judge, zp-check, zp-partner, zp-self, zp-support, zp-perspective, zp-awaken, zp-guide) from https://github.com/ZanePan2027/zpskill.
Then use zp-life to help me with this: ...
```

## Doubao and WorkBuddy

Send the installation request above in your client and tell the Agent which client you use.

| Client | Installation and discovery |
| --- | --- |
| WorkBuddy | Ask the Agent to install each folder under the repository's `skills/` into `.workbuddy/skills/` in your user home directory, including all files within it. Open the Skills page, go to your installed skills, find `zp-life`, and enable it. |
| Doubao for macOS · local computer | Start a local-computer work task and ask the Agent to install each Skill folder into `~/.agents/skills/`. Find them under the local section of Skills management, then invoke them in a work task. |
| Doubao web · cloud computer | Open [Doubao web](https://www.doubao.com/chat/), select Work → Cloud computer, and send the installation request. Ask the Agent to identify the supported persistent cloud skill directory before installing. |

Doubao cloud and local computers have separate Skill installations. For persistent cloud Skills, use the platform's skill management mechanism or its `user_skills` directory; installations elsewhere in the temporary sandbox may be removed when it is cleared. Browser-based work tasks are described in Doubao's official [access guide](https://www.doubao.com/work/docs/zh-cn/articles/462191106451-access) and [work task guide](https://www.doubao.com/work/docs/zh-cn/articles/047323472965-work-task-mode).

If these clients are absent from the installer's list, use the method above. The entry should be `<skills-directory>/zp-life/SKILL.md`, without an extra repository folder in between. Start a new conversation and ask: “Use zp-life to help me with …”.

## Start using it

Start by asking `zp-life` to help with your current concern. When you want to save and continue, open the folder you want to keep using and ask the Agent to connect or create your life workspace there. Existing rules and material are reused; an empty folder also works. If no location is chosen, the Agent helps you choose one once. Add relevant files without sorting them first, then start your current task. One-off questions do not require setup. Follow the [walkthrough](guide.en.md).

## Update and save work

Ask your Agent to compare the installed files with this repository and preserve your local edits before updating. Check the actual revision and content, even when the version number is unchanged.

The Skill directory holds methods. Your workspace holds personal material and results. Continue in the same project without repeating the folder path. A location is needed again only when the project changes, access is lost, or the workspace is ambiguous. When changing tools, open or authorize access to that same folder.

[Back to the manual index](README.en.md)

## Claude Code plugin

```bash
claude plugin marketplace add ZanePan2027/zpskill
claude plugin install zp-life@zpskill
```

Start with `/zp-life:zp-life`. Update it through Claude Code's plugin manager, or ask your Agent to update the workbench using your current installation method.
