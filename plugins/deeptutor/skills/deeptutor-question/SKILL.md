---
name: deeptutor-question
description: Use the DeepTutor question-generation workflow when the user asks to generate quizzes, interview questions, review questions, mock questions, or mimic an existing paper from provided files, conversation material, or accessible knowledge sources. Supports Custom, Mimic, and Follow-up modes.
---

# DeepTutor Question Workflow

Use `references/workflow-and-prompts.md` as the authoritative workflow and prompt reference for this skill.

## Core behavior

1. Determine the mode:
   - **Custom**: default. Generate questions from the requested topic/material.
   - **Mimic**: use only when a reference paper/question set is supplied and the user asks to imitate its style, structure, difficulty, or knowledge points.
   - **Follow-up**: answer or explain an already generated question rather than starting a new generation pipeline.
2. For Custom generation, execute **Explore → Plan → Quiz**:
   - Explore the actual accessible material first. Do not write questions during exploration.
   - Plan exactly the requested number of non-duplicate question templates, respecting type and difficulty constraints.
   - Generate each question from its template, checking against previously generated questions.
3. Never claim to have read a knowledge base, file, API, or source that is not actually accessible in the current run.
4. Use real available tools for retrieval. Do not print or simulate DeepTutor's internal `THINK / TOOL / FINISH` protocol as if tool calls occurred.
5. If the user supplies source material, prioritize it over general knowledge unless the user explicitly requests supplementation.
6. Respect requested output format. If none is specified, return a clear readable question set with answers and concise explanations.

## Question constraints

Supported types: `choice`, `concept`, `fill_in_blank`, `short_answer`, `written`, `coding`.

- `choice`: exactly four non-empty options A/B/C/D; answer is one of A/B/C/D.
- `concept`: a single true/false proposition; answer is lowercase `true` or `false`.
- `fill_in_blank`: exactly one `____`; answer is one canonical word or phrase.
- `short_answer`: concise conceptual response; no options.
- `written`: longer explanation/solution; no options.
- `coding`: reference code, pseudocode, or algorithm; no options.

Before final output, verify count, type allocation, difficulty, topic coverage, duplicates, answers, and explanations.

## Detailed reference

Read `references/workflow-and-prompts.md` when performing question generation, especially for detailed planning rules, Mimic behavior, validation/repair rules, and the upstream DeepTutor prompt semantics.
