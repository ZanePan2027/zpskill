# Continue later: background, outputs, and feedback

[简体中文](continue.md) · [First task](first-task.en.md) · [Manual](README.en.md)

Continuity depends on workspace files you authorize and the content your current Agent can actually access. Installing zpskill does not create automatic shared memory across AI clients.

Open a folder you plan to keep using and ask:

```text
Use zp-workspace to connect or create a minimal life workspace in this folder.
Preserve existing files and rules. Keep the background, current judgment, and outputs useful for continuing.
Then help with the thing I brought today: …
```

The Skill directory stores methods; your workspace stores personal material and progress. Keeping them separate prevents a Skill update from treating personal files as installation files. Existing material can be reused without creating a second profile.

Before stopping, ask the Agent to save confirmed background, the current judgment, usable outputs, and where to resume. Keep its guesses separate from facts you confirmed and distinguish plans from actions already taken. What gets saved depends on your wishes and the host's permissions. You can correct or withdraw a saved understanding; dependent advice should change too.

Next time, open the same project:

```text
Continue from last time. Find the task, its background, outputs, and where we stopped.
Here is new feedback: … . Revise the earlier judgment before continuing.
```

A good continuation identifies the task and explains what the new feedback changes. If the Agent cannot find the files, locate them rather than asking it to pretend it remembers. A different client needs access to the same workspace, or selected material you choose to transfer; installing Skills alone transfers neither private files nor chat history.

Check progress against reality. If you only drafted a message, the conversation has not happened yet. Whether the advice changes after feedback matters more than how many records were created.

Files stay in the location you choose. External models and cloud Agents still process data according to their own client and service arrangements; provide only what the task needs. See [Install and update](install.en.md) and [Workspace structure](architecture.en.md).
