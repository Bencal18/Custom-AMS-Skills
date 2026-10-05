---
name: <skill-name>
description: <What the skill does and when to use it, in the words a coach would use to ask for the task. Name the metrics, devices, and file types it covers. Keep it under 200 characters, because some Claude apps reject longer descriptions.>
license: CC-BY-4.0. Scripts are MIT.
metadata:
  version: "1"
---

# <Skill title>

<One or two sentences on what this skill helps the user do.>

## When to use

Use this skill when the user asks to:

- <Task, in the user's words.>
- <Task, in the user's words.>

This skill covers these metrics:

| Metric | Reference file |
|---|---|
| <Metric> | [references/<metric>.md](references/<metric>.md) |

## Steps

Follow these steps:

1. Ask which device or form the data came from, if the user has not said. Load the device export reference when one exists for that device.
2. Load the reference file for each metric the user asks about.
3. <Method step. One action per step.>
4. <Method step.>
5. Show the formula you used, the variant name, and the units next to the result.

## Checks before answering

Run these checks on your own result before you show it:

- <Range check: compare each value to the typical range in the reference file. Flag values outside it.>
- <Unit check.>
- <Count check: confirm the number of athletes, sessions, or trials matches the input.>

If a check fails, say which check failed and why. Do not hide the result.

## Limits

Follow these limits:

- Frame every result as decision support. Do not make clearance, return-to-sport, injury-risk, or training decisions. Leave those to the practitioner.
- Do not invent a threshold or range. Use only the figures in the reference files, and name the source.
- <Skill-specific limit.>

## References

Load these files when needed:

- [references/<metric>.md](references/<metric>.md): <metric>.
- [references/<device>.md](references/<device>.md): how to read <device> exports.
