# DeepTutor 后端接口手册（当前部署版）

本目录描述**服务器上正在运行的那一份** DeepTutor 后端接口，供其他 Agent 直接调用。它与 [官方版手册](../official-v1.6.12/README.md) 不是同一套契约，**路由前缀、鉴权方式、WebSocket 协议都不同**，不要混用。

| 项 | 值 |
| --- | --- |
| 对外基址 | `https://deeptutor.cliproxy.com.cn` |
| 代码来源 | 本地定制分支 `main`（工作树，导出日 2026-09-28） |
| 契约规模 | 263 条路径 / 322 个操作 |
| 契约文件 | [openapi.json](openapi.json)，sha256 `5cd1826d91de427af6268c0b71170c5a540a3417c6206a11ef33c4e3a8c3c4dc` |
| 服务器镜像 | `deeptutor:custom-20260818-2234-v1.5.11-d41f19c9` |
| 实测日期 | 2026-09-28（下文标 ✅ 的结论均有当日线上实测） |

## 目录

| 文件 | 内容 |
| --- | --- |
| [openapi.json](openapi.json) | 本部署的 OpenAPI 3.1 契约（由 `deeptutor.api.main:app` 直接导出，未手工修改） |
| [http-index-1.md](http-index-1.md) / [2](http-index-2.md) | 全量 HTTP 接口索引（方法、精确路径、参数、请求体类型、状态码、operationId） |
| 本文件 | 调用前必读：基址、鉴权现状、WS 协议、流式接口、踩坑清单 |

## 一、基址与网络拓扑

对外只有**一个**可用基址：`https://deeptutor.cliproxy.com.cn`。链路是：

```
客户端 → Cloudflare → nginx(443) → Next.js(127.0.0.1:3782) → /api/* 重写 → 后端(127.0.0.1:8001)
```

- ✅ 响应头带 `x-middleware-rewrite: http://127.0.0.1:8001/api/v1/auth/status`，说明 `/api/*` 由 Next.js 中间件整段转发到后端。
- 后端 8001 与 Next.js 3782 都只监听回环地址，**不能直连**，必须走域名。
- **公网只暴露 `/api/*`**。这是本部署最关键的一条限制：

| 前缀 | 公网可达 | 说明 |
| --- | --- | --- |
| `/api/v1/...` | ✅ | 主体业务接口 |
| `/api/outputs/{output_path}` | ✅ | 输出文件（官方版是 `/files/outputs/...`） |
| `/api/attachments/{session_id}/{attachment_id}/{filename}` | ✅ | 会话附件（官方版是 `/files/attachments/...`） |
| `/api/...`（其他） | ✅ | 任意 `/api/` 下的路径都会转发到后端，不存在的前缀返回后端 JSON 404 |
| `/files/...` | ❌ 404 | 官方版的文件前缀在本部署不存在 |
| `/openapi.json`、`/docs`、`/redoc` | ❌ 404 | 后端其实提供（`app.routes` 里有），但没被转发出来，取契约只能用本目录的 `openapi.json` |
| `/health/...` | ❌ 404 | 本分支没有 `/health` 路由 |
| `/` | ⚠️ 200 | 返回的是**网页 HTML**，不是后端的 `GET /`（那个 `{"message": "Welcome to DeepTutor API"}` 被网页占用） |

✅ 判据：`/api/v1/__nope__` 与 `/api/__nope__` 都返回 `{"detail":"Not Found"}`（后端 JSON）；`/files/library/1/download` 返回 404。

## 二、认证现状：当前关闭

✅ `GET /api/v1/auth/status` 实测返回：

```json
{"enabled":false,"authenticated":true,"user_id":"local-admin","username":"local","role":"admin","is_admin":true,"avatar":""}
```

服务端 `AUTH_ENABLED=false`，此时**所有请求都按本地管理员处理，无需任何凭证**，`require_admin` 也直接放行。Agent 现在可以直接调所有接口。

与关闭状态相关的两个坑：

| 接口 | 关闭鉴权时的实际行为（✅ 实测） |
| --- | --- |
| `POST /api/v1/auth/token` | **409**，`{"detail":"Authentication is disabled; no access token is required."}`。拿 token 的调用要先看 `auth/status` |
| `POST /api/v1/auth/login` | 200，`{"ok":true,"message":"Auth is disabled — no login required."}`，不下发 Cookie |

**将来开启鉴权后**（`AUTH_ENABLED=true`）需要按下面这套走，契约里已经标注了哪些路由受保护：

- `POST /api/v1/auth/login` 校验用户名密码，通过后 `Set-Cookie: dt_token=<JWT>`（HttpOnly），响应体为 `{"ok":true,"user_id","username","role","is_admin"}`，**没有 `access_token` 字段**。
- 原生客户端改用 `POST /api/v1/auth/token`，响应体是 `{"access_token","expires_in","user":{...}}`，且**不写 Cookie**（响应带 `Cache-Control: no-store`）。
- HTTP 携带方式二选一：`Cookie: dt_token=<JWT>` 或 `Authorization: Bearer <JWT>`。
- WebSocket 携带方式二选一：连接时带 Cookie，或查询串 `?token=<JWT>`；失败以关闭码 **4001** 断开。
- 契约里 **322 个操作中有 314 个带 `cookie:dt_token` 参数**（见 [http-index-1.md](http-index-1.md)），表示该路由由鉴权依赖保护；开启鉴权后未带凭证会 401。不带这个参数的只有 8 个：`GET /`、`POST /api/v1/auth/login`、`POST /api/v1/auth/logout`、`POST /api/v1/auth/register`、`POST /api/v1/auth/token`、`GET /api/v1/auth/is_first_user`、`GET /api/v1/auth/openai-codex/callback`、`GET /api/v1/settings/ui`。
- 注意：`/api/v1/partners/*` 整组挂的是管理员依赖（`require_admin`），开启鉴权后非管理员会 403。

## 三、HTTP 常用调用链路（均已线上实测）

```bash
BASE=https://deeptutor.cliproxy.com.cn

# 1) 鉴权状态（先看 enabled）
curl -s $BASE/api/v1/auth/status

# 2) 服务与依赖状态
curl -s $BASE/api/v1/system/status          # LLM / Embedding / Search 等组件健康
curl -s $BASE/api/v1/system/runtime-topology
curl -s $BASE/api/v1/system/memory

# 3) 会话
curl -s "$BASE/api/v1/sessions?limit=20&offset=0"
curl -s $BASE/api/v1/sessions/<session_id>
curl -s -X PATCH $BASE/api/v1/sessions/<session_id> -H 'Content-Type: application/json' -d '{"title":"新标题"}'
curl -s -X DELETE $BASE/api/v1/sessions/<session_id>
# 历史消息的推理内容单独拉取（会话详情默认已剥离 thinking，体积大幅缩小）
curl -s $BASE/api/v1/sessions/<session_id>/messages/<message_id>/thinking

# 4) 知识库
curl -s $BASE/api/v1/knowledge/list
curl -s $BASE/api/v1/knowledge/configs
curl -s $BASE/api/v1/knowledge/health

# 5) 移动端答题记录 / 学习进度
curl -s $BASE/api/v1/mobile/attempts
curl -s $BASE/api/v1/learning/progress

# 6) 能力与工具
curl -s $BASE/api/v1/capabilities/settings
curl -s $BASE/api/v1/tools
```

响应大小提示：会话详情走过 gzip 与 thinking 剥离（16.7 MB → 约 46 KB 量级）。客户端请发送 `Accept-Encoding: gzip`；排查问题时可用 `-H 'Accept-Encoding: identity'` 看原始体积。

## 四、统一 WebSocket：`/api/v1/ws`

会话问答、出题、评判的主链路。✅ 握手实测 `HTTP/1.1 101 Switching Protocols`。

| 项 | 值 |
| --- | --- |
| 地址 | `wss://deeptutor.cliproxy.com.cn/api/v1/ws`（本地开发 `ws://127.0.0.1:8001/api/v1/ws`） |
| 认证 | 当前关闭；开启后为 Cookie 或 `?token=<JWT>` |
| 帧格式 | 文本帧，每帧一个 JSON 对象 |
| 协议版本 | **无需 `protocol_version` 字段**（官方 2.0 协议要求带 `"protocol_version":"2.0"`，本分支不校验，带了也不报错） |

### 4.1 客户端命令

| `type` | 作用 | 关键字段 |
| --- | --- | --- |
| `message` / `start_turn` | 发起一轮对话 | `content` 必填；可选 `session_id`（省略或 `null` 为新建）、`capability`、`tools`、`knowledge_bases`、`language`、`config`、`attachments`、`notebook_references`、`history_references`、`question_notebook_references`、`book_references`、`persona`、`llm_selection`、`parent_message_id`（编辑分叉） |
| `subscribe_turn` | 订阅已有轮次事件 | `turn_id`，可选 `after_seq` |
| `subscribe_session` | 订阅会话当前活跃轮次 | `session_id`，可选 `after_seq` |
| `resume_from` | 断线续传 | `turn_id` + `seq`（从该序号之后续传） |
| `unsubscribe` | 取消订阅 | `turn_id` 或 `session_id` |
| `cancel_turn` | 取消轮次 | `turn_id` |
| `check_active_turn` | 查会话是否有在跑的轮次 | `session_id` → 回 `active_turn_info` |
| `submit_user_reply` | 回应 `ask_user` 暂停 | `turn_id` + `text`（单题）或 `answers:[{questionId,text}]`（多题，二者都有时以 `answers` 为准） |
| `user_input` | 向进行中的轮次补送输入 | `turn_id` + `content` |
| `regenerate` | 重跑最后一条用户消息 | `session_id`，可选 `overrides` |
| `ping` | 心跳 | 无 → 回 `{"type":"pong"}` |

✅ 实测帧（2026-09-28 线上）：

```
→ {"type":"ping"}
← {"type":"pong"}
→ {"type":"check_active_turn","session_id":"__probe__"}
← {"type":"active_turn_info","turn_id":"","status":"none"}
→ {"type":"no_such_type"}
← {"type":"error","content":"Unknown type: no_such_type"}
```

### 4.2 服务端事件

`start_turn` 成功后服务端自动订阅该轮次并逐条推事件，每条是 Python `StreamEvent` 序列化结果：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | string | 见下表 |
| `source` | string | 产生事件的来源 |
| `stage` | string | 阶段名，`stage_start` / `stage_end` 用它配对 |
| `content` | string | 文本内容（`content` 事件即增量正文） |
| `metadata` | object | 附加信息，含 `turn_terminal` 等终止标记 |
| `session_id` / `turn_id` | string | 所属会话与轮次 |
| `seq` | number | 单调递增序号，续传用 |
| `timestamp` | number | 时间戳 |

`type` 取值（与前端 `StreamEventType` 镜像）：`stage_start`、`stage_end`、`thinking`、`observation`、`content`、`tool_call`、`tool_result`、`progress`、`sources`、`result`、`error`、`session`、`session_meta`、`done`。

控制类帧（不是 StreamEvent，字段更少）：`pong`、`active_turn_info`（`{turn_id,status}`）、`error`（`{type:"error",content:"...",source?,stage?,metadata?,session_id?,turn_id?,seq?}`）。

要点：

- 轮次是否结束看 `done` / `error`，或事件 `metadata.turn_terminal`。
- `error` 帧既用于协议层错误（如 `Unknown type: x`、`Missing turn_id.`），也用于业务失败，靠 `content` 与 `metadata` 区分。
- 本分支**没有**官方的 `command_ack` 与 `protocol_error` 帧，不要等它们。

### 4.3 连接管理建议

- 心跳：前端实现是每 30 s 发一次 `ping`，45 s 没收到任何帧就判定断线（`HEARTBEAT_INTERVAL_MS=30000`、`HEARTBEAT_TIMEOUT_MS=45000`）。
- 重连：最多 5 次退避重连（起始 200 ms），重连后用 `resume_from` + 上次 `seq` 续传，不要重放开头的全量内容。
- 恢复会话前先 `check_active_turn`：返回 `status:"none"` 表示没有在跑的轮次；服务端会把重启后残留的僵尸轮次标成 `cancelled`。
- 拿到 `wait_for_input` 事件后用 `submit_user_reply` 回复；回复不被接受时服务端回 `error` 且 `metadata.ask_user_submission_rejected=true`。

最小可用示例：

```python
import asyncio, json, websockets

async def main():
    async with websockets.connect("wss://deeptutor.cliproxy.com.cn/api/v1/ws") as ws:
        await ws.send(json.dumps({
            "type": "start_turn",
            "content": "解释一下傅里叶变换",
            "capability": "chat",
            "session_id": None,
        }, ensure_ascii=False))
        while True:
            event = json.loads(await ws.recv())
            print(event["type"], str(event.get("content", ""))[:80])
            if event["type"] in {"done", "error"}:
                break

asyncio.run(main())
```

## 五、其他 WebSocket 入口

本部署共 8 个 WS 入口（由 `app.routes` 实测枚举），除 `/api/v1/ws` 外都**不遵循**统一 turn 协议，消息结构各不相同：

| 地址 | 用途 | 首帧字段（源码为准） |
| --- | --- | --- |
| `/api/v1/ws` | 统一对话/出题主链路 | 见上一节 |
| `/api/v1/chat` | 旧版聊天流（保留的兼容通道，非 turn 协议） | 每帧 `message` 必填，可选 `session_id`、`history`、`kb_name`、`enable_rag`、`enable_web_search`、`language`；`session_id` 不存在时会自动建会话 |
| `/api/v1/question/mimic` | 仿写试卷出题 | `mode`（`upload` / `parsed`）+ `kb_name`；upload 另需 `pdf_data`（base64）+ `pdf_name`，parsed 需 `paper_path`，可选 `max_questions` |
| `/api/v1/question/generate` | 按需求批量出题 | `requirement` + `kb_name`（默认 `ai_textbook`）等 |
| `/api/v1/question/judge` | 单题 AI 评判 | `question`、`question_type`、`correct_answer`、`explanation`、`user_answer`，可选 `options`、`user_answer_images:[{base64/url,filename,mime_type}]`（旧版 `user_answer_image` 仍兼容）、`language`。服务端回 `started` → 若干 `{type:"text",content}` → `done` / `error` |
| `/api/v1/knowledge/{kb_name}/progress/ws` | 知识库处理进度 | 无需首帧，连上即推进度 |
| `/api/v1/book/ws` | 书籍学习流 | 订阅/操作类帧 |
| `/api/v1/partners/{partner_id}/ws` | Partner 对话 | 需要管理员权限（`_admin` 依赖） |

## 六、SSE 与 NDJSON（不能用普通 JSON 客户端解析）

响应体是流式文本，必须逐行读，不能先 `json.loads(整个响应)`：

| 接口 | 媒体类型 | 事件 / 结束语义 |
| --- | --- | --- |
| `POST /api/v1/co_writer/edit_react/stream` | `text/event-stream` | `stream` 增量 → `result` 最终结果 → 出错 `error` |
| `POST /api/v1/notebook/add_record_with_summary` | `text/event-stream` | `summary_chunk` 增量输出摘要 |
| `POST /api/v1/partners/{partner_id}/chat/execute-stream` | `text/event-stream` | `session` → 若干 `thinking` → `content` → `done`，出错 `error` |
| `POST /api/v1/plugins/tools/{tool_name}/execute-stream` | `text/event-stream` | 工具执行过程事件流 |
| `POST /api/v1/plugins/capabilities/{capability_name}/execute-stream` | `text/event-stream` | 能力执行过程事件流 |
| `GET /api/v1/knowledge/tasks/{task_id}/stream` | `text/event-stream` | 知识库任务进度 |
| `GET /api/v1/memory/runs/{run_id}/events` | `text/event-stream` | 记忆整理运行事件，支持 `since` 游标续读 |
| `GET /api/v1/settings/tests/{service}/{run_id}/events` | `text/event-stream` | 设置自检事件，含 `heartbeat` 保活帧 |
| `POST /api/v1/subagents/connections/{name}/message` | `application/x-ndjson` | 每行一个 JSON：`user_question` → 若干 `{channel,text}` → 错误行为 `error` |

注意：本分支**没有全站 gzip 中间件**，只有 `sessions.py` 的两个读接口手动 gzip。SSE 端点是逐块冲刷的，客户端不要对它们做整体缓冲。

## 七、文件上传与下载

| 场景 | 接口 | 说明 |
| --- | --- | --- |
| 知识库上传 | `POST /api/v1/knowledge/{kb_name}/upload` | `multipart/form-data` |
| 语音转文字 / 合成 | `POST /api/v1/voice/stt`、`POST /api/v1/voice/tts` | STT 为 `multipart/form-data`：`file` 必填 |
| 输出文件下载 | `GET /api/outputs/{output_path}`（另有 `HEAD`） | 公网路径就是 `/api/outputs/...` |
| 会话附件下载 | `GET /api/attachments/{session_id}/{attachment_id}/{filename}` | 公网路径 `/api/attachments/...` |
| 知识库文件预览 | `GET /api/v1/knowledge/{kb_name}/file-preview-text/{filename}` | 提取文本预览 |

源码里用 `:path` 转换器声明的参数**可以包含 `/`**，但 `openapi.json` 里只显示为普通 `{name}`。生成客户端时要保留 `/`、不要整体百分号编码：

| 源码路径（含 `:path`） | 方法 |
| --- | --- |
| `/api/outputs/{output_path:path}` | `GET`、`HEAD` |
| `/api/attachments/{session_id}/{attachment_id}/{filename:path}` | `GET` |
| `/api/v1/knowledge/{kb_name}/files/{filename:path}` | `GET`、`DELETE` |
| `/api/v1/knowledge/{kb_name}/file-preview-text/{filename:path}` | `GET` |

## 八、调用约束（容易踩的坑）

1. **前缀必须带 `/api/v1`**：`/api/v1/sessions` 是 200，`/api/sessions` 是 404。例外是 `/api/outputs` 与 `/api/attachments`（它们不在 `v1` 下）。
2. **只有 `/api/*` 出得去**：`/files/...`、`/openapi.json`、`/health/...` 在公网一律 404，别照官方文档去调。
3. **根路径 `/` 是网页**，不是后端根接口。
4. **`redirect_slashes=False`**：服务端不会自动补尾斜杠，路径必须与契约逐字一致。
5. **导出契约时有一个 operationId 重复**：`/api/outputs/{output_path}` 的 `GET` 与 `HEAD` 共用 `read_output_api_outputs__output_path__get`。按 operationId 生成客户端代码的工具需要容忍这一个冲突。
6. **鉴权关闭不等于契约里没有鉴权**：契约中 314 个操作声明了 `cookie:dt_token`，这是"开启鉴权后受保护"的标记，现在调用不需要带。
7. **不要把 OpenAPI 当完整说明书**：WebSocket 协议、SSE/NDJSON 消费方式、`HEAD`/流式下载行为都超出 OpenAPI 表达范围，以本文件为准。
8. **契约与线上镜像可能有极小偏差**：本目录契约导出自 `main` 工作树，而服务器跑的是 `custom-20260818-2234-v1.5.11-d41f19c9`。已实测确认线上包含 `GET /api/v1/sessions/{id}/messages/{mid}/thinking`（该端点属 8-18 hotfix）。若某个接口线上 404 而契约里有，先怀疑版本差而不是自己拼错了路径。

## 九、推荐的接入顺序

1. `GET /api/v1/auth/status` → 看 `enabled` 判断要不要登录。
2. `GET /api/v1/system/status` → 确认 LLM / Embedding / Search 可用。
3. 读 [http-index-1.md](http-index-1.md) / [2](http-index-2.md) 定位目标接口，再到 `openapi.json` 查参数与响应结构。
4. 会话类交互走 `/api/v1/ws`：`start_turn` → 消费事件 → `done`；实现 30 s `ping` 与 `resume_from` 续传。
5. 每一跳都显式处理 `401` / `403` / `409`（token 接口）/ `503` / WS 关闭码 `4001`。

## 十、来源与复现

契约不是手工写的，用下面两条命令可重建（在项目根目录、装了项目依赖的 Python 环境中执行）：

```bash
# 1) 导出契约（本分支没有官方那个 contracts/export.py，直接取 app 的 openapi）
.venv/bin/python -c "import json;from deeptutor.api.main import app;open('docs/api/deployed-main-20260928/openapi.json','w',encoding='utf-8').write(json.dumps(app.openapi(),ensure_ascii=False,indent=2))"
# 2) 校验一致性
sha256sum docs/api/deployed-main-20260928/openapi.json   # 应为 5cd1826d91de427af6268c0b71170c5a540a3417c6206a11ef33c4e3a8c3c4dc
```

导出时会有一条 FastAPI 告警（`Duplicate Operation ID read_output_api_outputs__output_path__get`），属已知情况，见第八节第 5 条。

升级或重新部署后端后应重新导出本目录，不要手工编辑 `openapi.json`。

> 注意：本仓库 `.gitignore` 含 `/docs/`，`docs/api/` 下文件默认不被 Git 跟踪。若要提交，需 `git add -f docs/api`。