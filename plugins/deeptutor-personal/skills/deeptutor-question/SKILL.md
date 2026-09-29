---
name: deeptutor-question
description: Use the user's personal DeepTutor deployment to read knowledge bases and generate quizzes, interview questions, review questions, mock questions, explanations, or mimic an existing paper. The deployment is fixed at https://deeptutor.cliproxy.com.cn. Supports Custom, Mimic, and Follow-up modes and the Explore → Plan → Quiz workflow.
---

# DeepTutor Personal Question Workflow

This skill is for a **single-user private DeepTutor deployment**. The server address is fixed and must not be requested from the user.

## Fixed deployment

- HTTP base URL: `https://deeptutor.cliproxy.com.cn`
- WebSocket: `wss://deeptutor.cliproxy.com.cn/api/v1/ws`
- API family for this deployment: `/api/v1/...`
- Public access is only through `/api/*`.
- The bundled deployment references take precedence over upstream DeepTutor documentation.

## Connection behavior

When the user's request refers to DeepTutor, the user's knowledge base, or asks to generate material from DeepTutor content, proactively use the fixed deployment instead of asking for the documents again.

Start with:

1. `GET https://deeptutor.cliproxy.com.cn/api/v1/auth/status`
2. If authentication is disabled, continue without credentials.
3. `GET https://deeptutor.cliproxy.com.cn/api/v1/knowledge/list`.
4. For a selected KB, call `GET /api/v1/knowledge/{kb_name}/files`.
5. Read relevant documents through `GET /api/v1/knowledge/{kb_name}/file-preview-text/{filename}`.

Use actual network/browser/tool access available in the current Work run. Never pretend a request succeeded.

## Question workflow

Read `references/workflow-and-prompts.md` as the authoritative question-generation workflow.

For Custom generation execute **Explore → Plan → Quiz**:

1. **Explore** — retrieve and study the actual knowledge material. Do not write questions yet.
2. **Plan** — produce exactly the requested number of non-duplicate templates, respecting topic, type, difficulty, and requested distribution.
3. **Quiz** — generate each question from its template and check it against earlier questions for overlap.

Supported types: `choice`, `concept`, `fill_in_blank`, `short_answer`, `written`, `coding`.

## Mutating the DeepTutor server

Reading is allowed by default when required for the task. Do **not** create, update, delete, upload, rename, or write question-notebook entries unless the user explicitly asks for that mutation.

## Reference priority

1. `references/current-deployment-api.md`
2. `references/http-index-1.md` and `references/http-index-2.md`
3. `references/workflow-and-prompts.md`
