# HTTP 接口索引 2/3

来源：官方 v1.6.12，提交 `ef2d9e5c3c99fd073742c5aadc2bb9584b1e503b`。由同目录 `openapi.json` 提取，未使用本地定制代码。

[调用指南](README.md) · [索引 1](http-index-1.md) · [索引 2](http-index-2.md) · [索引 3](http-index-3.md)

本表是导航，不是权限清单。参数的类型、默认值、约束、枚举和响应结构请按 operationId 在 OpenAPI 中查阅。必填参数标 `*`；公共 Authorization/Cookie 参数省略。

响应列仅为官方 schema 已声明的 HTTP 状态码，未覆盖全部运行时错误。部分 SSE/文件接口在 schema 中仍显示 JSON，实际行为见调用指南。

| 方法 | 精确路径 | 分组 / 官方摘要 | 参数位置与名称 | 请求体媒体类型 | 声明状态码 | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | `/api/memory/doc/{layer}/{key}/update` | memory / Update Doc | path:layer*, path:key* | application/json | 200, 422 | `update_doc_api_memory_doc__layer___key__update_post` |
| GET | `/api/memory/overview` | memory / Get Overview | — | — | 200, 422 | `get_overview_api_memory_overview_get` |
| GET | `/api/memory/resolve_entry/{entry_id}` | memory / Resolve Entry | path:entry_id* | — | 200, 422 | `resolve_entry_api_memory_resolve_entry__entry_id__get` |
| GET | `/api/memory/runs` | memory / List Runs | query:layer, query:key | — | 200, 422 | `list_runs_api_memory_runs_get` |
| POST | `/api/memory/runs/start` | memory / Start Run | — | application/json | 200, 422 | `start_run_api_memory_runs_start_post` |
| GET | `/api/memory/runs/{run_id}` | memory / Get Run | path:run_id* | — | 200, 422 | `get_run_api_memory_runs__run_id__get` |
| POST | `/api/memory/runs/{run_id}/cancel` | memory / Cancel Run | path:run_id* | — | 200, 422 | `cancel_run_api_memory_runs__run_id__cancel_post` |
| GET | `/api/memory/runs/{run_id}/events` | memory / Stream Run Events | path:run_id*, query:since | — | 200, 422 | `stream_run_events_api_memory_runs__run_id__events_get` |
| POST | `/api/memory/runs/{run_id}/undo` | memory / Undo Run Edit | path:run_id* | — | 200, 422 | `undo_run_edit_api_memory_runs__run_id__undo_post` |
| GET | `/api/memory/settings` | memory / Get Memory Settings Endpoint | — | — | 200, 422 | `get_memory_settings_endpoint_api_memory_settings_get` |
| PUT | `/api/memory/settings` | memory / Put Memory Settings | — | application/json | 200, 422 | `put_memory_settings_api_memory_settings_put` |
| GET | `/api/memory/snapshot/{surface}` | memory / Get Snapshot | path:surface* | — | 200, 422 | `get_snapshot_api_memory_snapshot__surface__get` |
| DELETE | `/api/memory/snapshot/{surface}/changes` | memory / Clear Snapshot Changes | path:surface* | — | 200, 422 | `clear_snapshot_changes_api_memory_snapshot__surface__changes_delete` |
| GET | `/api/memory/snapshot/{surface}/changes` | memory / Get Changes | path:surface*, query:limit, query:offset | — | 200, 422 | `get_changes_api_memory_snapshot__surface__changes_get` |
| POST | `/api/memory/snapshot/{surface}/refresh` | memory / Refresh Snapshot | path:surface* | — | 200, 422 | `refresh_snapshot_api_memory_snapshot__surface__refresh_post` |
| DELETE | `/api/memory/trace/{surface}` | memory / Clear Trace | path:surface* | — | 200, 422 | `clear_trace_api_memory_trace__surface__delete` |
| GET | `/api/memory/trace/{surface}` | memory / Get Trace | path:surface*, query:limit, query:offset | — | 200, 422 | `get_trace_api_memory_trace__surface__get` |
| DELETE | `/api/memory/trace/{surface}/day/{day}` | memory / Clear Trace Day | path:surface*, path:day* | — | 200, 422 | `clear_trace_day_api_memory_trace__surface__day__day__delete` |
| GET | `/api/multi-user/admin/books` | multi-user / Admin Books | — | — | 200, 422 | `admin_books_api_multi_user_admin_books_get` |
| GET | `/api/multi-user/admin/resources` | multi-user / Admin Resources | — | — | 200, 422 | `admin_resources_api_multi_user_admin_resources_get` |
| POST | `/api/multi-user/admin/skills/install` | multi-user / Admin Install Skill | — | application/json | 200, 422 | `admin_install_skill_api_multi_user_admin_skills_install_post` |
| GET | `/api/multi-user/guardians` | multi-user / List Guardian Relationships | query:include_revoked | — | 200, 422 | `list_guardian_relationships_api_multi_user_guardians_get` |
| POST | `/api/multi-user/guardians` | multi-user / Authorize Guardian Relationship | — | application/json | 201, 422 | `authorize_guardian_relationship_api_multi_user_guardians_post` |
| DELETE | `/api/multi-user/guardians/{relationship_id}` | multi-user / Revoke Guardian Relationship | path:relationship_id* | — | 200, 422 | `revoke_guardian_relationship_api_multi_user_guardians__relationship_id__delete` |
| POST | `/api/multi-user/learners/{learner_user_id}/credentials/reset` | multi-user / Reset Learner Credentials | path:learner_user_id* | application/json | 200, 422 | `reset_learner_credentials_api_multi_user_learners__learner_user_id__credentials_reset_post` |
| GET | `/api/multi-user/learners/{learner_user_id}/guardian-report` | multi-user / Guardian Report | path:learner_user_id* | — | 200, 422 | `guardian_report_api_multi_user_learners__learner_user_id__guardian_report_get` |
| GET | `/api/multi-user/learners/{learner_user_id}/materials` | multi-user / Guardian Material Catalog | path:learner_user_id* | — | 200, 422 | `guardian_material_catalog_api_multi_user_learners__learner_user_id__materials_get` |
| PUT | `/api/multi-user/learners/{learner_user_id}/materials` | multi-user / Assign Guardian Materials | path:learner_user_id* | application/json | 200, 422 | `assign_guardian_materials_api_multi_user_learners__learner_user_id__materials_put` |
| GET | `/api/multi-user/learners/{learner_user_id}/restrictions` | multi-user / Get Guardian Restrictions | path:learner_user_id* | — | 200, 422 | `get_guardian_restrictions_api_multi_user_learners__learner_user_id__restrictions_get` |
| PUT | `/api/multi-user/learners/{learner_user_id}/restrictions` | multi-user / Put Guardian Restrictions | path:learner_user_id* | application/json | 200, 422 | `put_guardian_restrictions_api_multi_user_learners__learner_user_id__restrictions_put` |
| GET | `/api/multi-user/me/guardianships` | multi-user / My Guardianships | — | — | 200, 422 | `my_guardianships_api_multi_user_me_guardianships_get` |
| DELETE | `/api/multi-user/me/guardianships/{relationship_id}` | multi-user / Revoke My Guardianship | path:relationship_id* | — | 200, 422 | `revoke_my_guardianship_api_multi_user_me_guardianships__relationship_id__delete` |
| GET | `/api/multi-user/users` | multi-user / Multi User List Users | — | — | 200, 422 | `multi_user_list_users_api_multi_user_users_get` |
| GET | `/api/multi-user/users/{user_id}/book-permission` | multi-user / Get User Book Permission | path:user_id* | — | 200, 422 | `get_user_book_permission_api_multi_user_users__user_id__book_permission_get` |
| PUT | `/api/multi-user/users/{user_id}/book-permission` | multi-user / Put User Book Permission | path:user_id* | application/json | 200, 422 | `put_user_book_permission_api_multi_user_users__user_id__book_permission_put` |
| GET | `/api/multi-user/users/{user_id}/grants` | multi-user / Get User Grants | path:user_id* | — | 200, 422 | `get_user_grants_api_multi_user_users__user_id__grants_get` |
| PUT | `/api/multi-user/users/{user_id}/grants` | multi-user / Put User Grants | path:user_id* | application/json | 200, 422 | `put_user_grants_api_multi_user_users__user_id__grants_put` |
| GET | `/api/notebooks` | notebooks / List Notebooks | — | — | 200, 422 | `list_notebooks_api_notebooks_get` |
| POST | `/api/notebooks` | notebooks / Create Notebook | — | application/json | 200, 422 | `create_notebook_api_notebooks_post` |
| POST | `/api/notebooks/actions/add-record` | notebooks / Add Record | — | application/json | 200, 422 | `add_record_api_notebooks_actions_add_record_post` |
| POST | `/api/notebooks/actions/add-record-with-summary` | notebooks / Add Record With Summary | — | application/json | 200, 422 | `add_record_with_summary_api_notebooks_actions_add_record_with_summary_post` |
| GET | `/api/notebooks/health` | notebooks / Health Check | — | — | 200, 422 | `health_check_api_notebooks_health_get` |
| GET | `/api/notebooks/statistics` | notebooks / Get Statistics | — | — | 200, 422 | `get_statistics_api_notebooks_statistics_get` |
| DELETE | `/api/notebooks/{notebook_id}` | notebooks / Delete Notebook | path:notebook_id* | — | 200, 422 | `delete_notebook_api_notebooks__notebook_id__delete` |
| GET | `/api/notebooks/{notebook_id}` | notebooks / Get Notebook | path:notebook_id* | — | 200, 422 | `get_notebook_api_notebooks__notebook_id__get` |
| PUT | `/api/notebooks/{notebook_id}` | notebooks / Update Notebook | path:notebook_id* | application/json | 200, 422 | `update_notebook_api_notebooks__notebook_id__put` |
| GET | `/api/notebooks/{notebook_id}/export` | notebooks / Export Notebook | path:notebook_id* | — | 200, 422 | `export_notebook_api_notebooks__notebook_id__export_get` |
| DELETE | `/api/notebooks/{notebook_id}/records/{record_id}` | notebooks / Remove Record | path:notebook_id*, path:record_id* | — | 200, 422 | `remove_record_api_notebooks__notebook_id__records__record_id__delete` |
| PUT | `/api/notebooks/{notebook_id}/records/{record_id}` | notebooks / Update Record | path:notebook_id*, path:record_id* | application/json | 200, 422 | `update_record_api_notebooks__notebook_id__records__record_id__put` |
| POST | `/api/notebooks/{notebook_id}/records/{record_id}/actions/copy` | notebooks / Copy Record | path:notebook_id*, path:record_id* | application/json | 200, 422 | `copy_record_api_notebooks__notebook_id__records__record_id__actions_copy_post` |
| POST | `/api/notebooks/{notebook_id}/records/{record_id}/actions/move` | notebooks / Move Record | path:notebook_id*, path:record_id* | application/json | 200, 422 | `move_record_api_notebooks__notebook_id__records__record_id__actions_move_post` |
| GET | `/api/partner-groups` | partner-groups / List Partner Groups | — | — | 200, 422 | `list_partner_groups_api_partner_groups_get` |
| POST | `/api/partner-groups` | partner-groups / Create Partner Group | — | application/json | 200, 422 | `create_partner_group_api_partner_groups_post` |
| GET | `/api/partner-groups/discussion-modes` | partner-groups / List Discussion Modes | — | — | 200, 422 | `list_discussion_modes_api_partner_groups_discussion_modes_get` |
| GET | `/api/partner-groups/shared-memory-types` | partner-groups / List Shared Memory Types | — | — | 200, 422 | `list_shared_memory_types_api_partner_groups_shared_memory_types_get` |
| DELETE | `/api/partner-groups/{group_id}` | partner-groups / Delete Partner Group | path:group_id* | — | 200, 422 | `delete_partner_group_api_partner_groups__group_id__delete` |
| GET | `/api/partner-groups/{group_id}` | partner-groups / Get Partner Group | path:group_id* | — | 200, 422 | `get_partner_group_api_partner_groups__group_id__get` |
| PATCH | `/api/partner-groups/{group_id}` | partner-groups / Update Partner Group | path:group_id* | application/json | 200, 422 | `update_partner_group_api_partner_groups__group_id__patch` |
| GET | `/api/partner-groups/{group_id}/history` | partner-groups / Partner Group History | path:group_id*, query:session_key, query:limit | — | 200, 422 | `partner_group_history_api_partner_groups__group_id__history_get` |
| GET | `/api/partner-groups/{group_id}/invocations` | partner-groups / Partner Group Invocations | path:group_id*, query:session_key, query:limit | — | 200, 422 | `partner_group_invocations_api_partner_groups__group_id__invocations_get` |
| POST | `/api/partner-groups/{group_id}/invocations` | partner-groups / Create Partner Invocation | path:group_id* | application/json | 200, 422 | `create_partner_invocation_api_partner_groups__group_id__invocations_post` |
| POST | `/api/partner-groups/{group_id}/invocations/{invocation_id}/approve` | partner-groups / Approve Partner Invocation | path:group_id*, path:invocation_id* | application/json | 200, 422 | `approve_partner_invocation_api_partner_groups__group_id__invocations__invocation_id__approve_post` |
| POST | `/api/partner-groups/{group_id}/invocations/{invocation_id}/reject` | partner-groups / Reject Partner Invocation | path:group_id*, path:invocation_id* | application/json | 200, 422 | `reject_partner_invocation_api_partner_groups__group_id__invocations__invocation_id__reject_post` |
| POST | `/api/partner-groups/{group_id}/messages` | partner-groups / Send Partner Group Message | path:group_id* | application/json | 200, 422 | `send_partner_group_message_api_partner_groups__group_id__messages_post` |
| POST | `/api/partner-groups/{group_id}/rounds/{turn_id}/summary` | partner-groups / Summarize Partner Group Round | path:group_id*, path:turn_id* | application/json | 200, 422 | `summarize_partner_group_round_api_partner_groups__group_id__rounds__turn_id__summary_post` |
| GET | `/api/partner-groups/{group_id}/sessions` | partner-groups / List Partner Group Sessions | path:group_id* | — | 200, 422 | `list_partner_group_sessions_api_partner_groups__group_id__sessions_get` |
| POST | `/api/partner-groups/{group_id}/sessions` | partner-groups / Create Partner Group Session | path:group_id* | — | 201, 422 | `create_partner_group_session_api_partner_groups__group_id__sessions_post` |
| DELETE | `/api/partner-groups/{group_id}/sessions/{session_key}` | partner-groups / Delete Partner Group Session | path:group_id*, path:session_key* | — | 200, 422 | `delete_partner_group_session_api_partner_groups__group_id__sessions__session_key__delete` |
| POST | `/api/partner-groups/{group_id}/turns/{turn_id}/partners/{partner_id}/retry` | partner-groups / Retry Partner Group Seat | path:group_id*, path:turn_id*, path:partner_id* | application/json | 200, 422 | `retry_partner_group_seat_api_partner_groups__group_id__turns__turn_id__partners__partner_id__retry_post` |
| GET | `/api/partner-groups/{group_id}/whiteboard` | partner-groups / Partner Group Whiteboard | path:group_id*, query:limit | — | 200, 422 | `partner_group_whiteboard_api_partner_groups__group_id__whiteboard_get` |
| POST | `/api/partner-groups/{group_id}/whiteboard/pins` | partner-groups / Pin Partner Group Whiteboard | path:group_id* | application/json | 200, 422 | `pin_partner_group_whiteboard_api_partner_groups__group_id__whiteboard_pins_post` |
| DELETE | `/api/partner-groups/{group_id}/whiteboard/pins/{event_id}` | partner-groups / Unpin Partner Group Whiteboard | path:group_id*, path:event_id* | — | 200, 422 | `unpin_partner_group_whiteboard_api_partner_groups__group_id__whiteboard_pins__event_id__delete` |
| GET | `/api/partners` | partners / List Partners | — | — | 200, 422 | `list_partners_api_partners_get` |
| POST | `/api/partners` | partners / Create Partner | — | application/json | 200, 422 | `create_partner_api_partners_post` |
| GET | `/api/partners/channels/schema` | partners / List Channel Schemas | — | — | 200, 422 | `list_channel_schemas_api_partners_channels_schema_get` |
| GET | `/api/partners/commands/palette` | partners / Partner Command Palette | — | — | 200, 422 | `partner_command_palette_api_partners_commands_palette_get` |
| GET | `/api/partners/consultation-session` | partners / Get Partner Consultation Session | query:chat_session_id*, query:partner_name* | — | 200, 422 | `get_partner_consultation_session_api_partners_consultation_session_get` |
| GET | `/api/partners/drafts/{draft_id}` | partners / Get Partner Draft | path:draft_id* | — | 200, 422 | `get_partner_draft_api_partners_drafts__draft_id__get` |
| POST | `/api/partners/drafts/{draft_id}/confirm` | partners / Confirm Partner Draft | path:draft_id* | application/json | 200, 422 | `confirm_partner_draft_api_partners_drafts__draft_id__confirm_post` |
| GET | `/api/partners/recent` | partners / Recent Partners | query:limit | — | 200, 422 | `recent_partners_api_partners_recent_get` |
| GET | `/api/partners/soul-sources` | partners / Soul Sources | — | — | 200, 422 | `soul_sources_api_partners_soul_sources_get` |
| GET | `/api/partners/souls` | partners / List Souls | — | — | 200, 422 | `list_souls_api_partners_souls_get` |
| POST | `/api/partners/souls` | partners / Create Soul | — | application/json | 200, 422 | `create_soul_api_partners_souls_post` |
| DELETE | `/api/partners/souls/{soul_id}` | partners / Delete Soul | path:soul_id* | — | 200, 422 | `delete_soul_api_partners_souls__soul_id__delete` |
| GET | `/api/partners/souls/{soul_id}` | partners / Get Soul | path:soul_id* | — | 200, 422 | `get_soul_api_partners_souls__soul_id__get` |
| PUT | `/api/partners/souls/{soul_id}` | partners / Update Soul | path:soul_id* | application/json | 200, 422 | `update_soul_api_partners_souls__soul_id__put` |
| GET | `/api/partners/tool-options` | partners / Tool Options | — | — | 200, 422 | `tool_options_api_partners_tool_options_get` |
| DELETE | `/api/partners/{partner_id}` | partners / Destroy Partner | path:partner_id* | — | 200, 422 | `destroy_partner_api_partners__partner_id__delete` |
| GET | `/api/partners/{partner_id}` | partners / Get Partner | path:partner_id*, query:include_secrets | — | 200, 422 | `get_partner_api_partners__partner_id__get` |
| PATCH | `/api/partners/{partner_id}` | partners / Update Partner | path:partner_id* | application/json | 200, 422 | `update_partner_api_partners__partner_id__patch` |
| GET | `/api/partners/{partner_id}/assets` | partners / Get Partner Assets | path:partner_id* | — | 200, 422 | `get_partner_assets_api_partners__partner_id__assets_get` |
| POST | `/api/partners/{partner_id}/assets` | partners / Add Partner Assets | path:partner_id* | application/json | 200, 422 | `add_partner_assets_api_partners__partner_id__assets_post` |
| DELETE | `/api/partners/{partner_id}/assets/{asset_type}/{name}` | partners / Delete Partner Asset | path:partner_id*, path:asset_type*, path:name* | — | 200, 422 | `delete_partner_asset_api_partners__partner_id__assets__asset_type___name__delete` |
| POST | `/api/partners/{partner_id}/channel-onboarding/start` | partners / Start Partner Channel Onboarding | path:partner_id* | application/json | 200, 422 | `start_partner_channel_onboarding_api_partners__partner_id__channel_onboarding_start_post` |
| DELETE | `/api/partners/{partner_id}/channel-onboarding/{session_id}` | partners / Cancel Partner Channel Onboarding | path:partner_id*, path:session_id* | — | 200, 422 | `cancel_partner_channel_onboarding_api_partners__partner_id__channel_onboarding__session_id__delete` |
| GET | `/api/partners/{partner_id}/channel-onboarding/{session_id}` | partners / Get Partner Channel Onboarding | path:partner_id*, path:session_id* | — | 200, 422 | `get_partner_channel_onboarding_api_partners__partner_id__channel_onboarding__session_id__get` |
| POST | `/api/partners/{partner_id}/channel-onboarding/{session_id}/apply` | partners / Apply Partner Channel Onboarding | path:partner_id*, path:session_id* | — | 200, 422 | `apply_partner_channel_onboarding_api_partners__partner_id__channel_onboarding__session_id__apply_post` |
| POST | `/api/partners/{partner_id}/channels/reload` | partners / Reload Partner Channels | path:partner_id* | — | 200, 422 | `reload_partner_channels_api_partners__partner_id__channels_reload_post` |
| GET | `/api/partners/{partner_id}/channels/status` | partners / Get Partner Channel Status | path:partner_id* | — | 200, 422 | `get_partner_channel_status_api_partners__partner_id__channels_status_get` |
| POST | `/api/partners/{partner_id}/channels/weixin/qr` | partners / Start Weixin Qr | path:partner_id* | — | 200, 422 | `start_weixin_qr_api_partners__partner_id__channels_weixin_qr_post` |
| GET | `/api/partners/{partner_id}/channels/weixin/qr/{session_id}` | partners / Poll Weixin Qr | path:partner_id*, path:session_id* | — | 200, 422 | `poll_weixin_qr_api_partners__partner_id__channels_weixin_qr__session_id__get` |
| POST | `/api/partners/{partner_id}/chat` | partners / Partner Chat Http | path:partner_id* | application/json | 200, 422 | `partner_chat_http_api_partners__partner_id__chat_post` |
| POST | `/api/partners/{partner_id}/chat/execute-stream` | partners / Partner Chat Http Stream | path:partner_id* | application/json | 200, 422 | `partner_chat_http_stream_api_partners__partner_id__chat_execute_stream_post` |
| GET | `/api/partners/{partner_id}/history` | partners / Get Partner History | path:partner_id*, query:session_key, query:session_id, query:limit | — | 200, 422 | `get_partner_history_api_partners__partner_id__history_get` |
| GET | `/api/partners/{partner_id}/history/page` | partners / Get Partner History Page | path:partner_id*, query:session_key*, query:before, query:limit | — | 200, 422 | `get_partner_history_page_api_partners__partner_id__history_page_get` |
| GET | `/api/partners/{partner_id}/links` | partners / List Partner Links | path:partner_id* | — | 200, 422 | `list_partner_links_api_partners__partner_id__links_get` |
| POST | `/api/partners/{partner_id}/links/code` | partners / Create Partner Link Code | path:partner_id* | — | 200, 422 | `create_partner_link_code_api_partners__partner_id__links_code_post` |
| DELETE | `/api/partners/{partner_id}/links/{key}` | partners / Delete Partner Link | path:partner_id*, path:key* | — | 200, 422 | `delete_partner_link_api_partners__partner_id__links__key__delete` |
| GET | `/api/partners/{partner_id}/sessions` | partners / Get Partner Sessions | path:partner_id* | — | 200, 422 | `get_partner_sessions_api_partners__partner_id__sessions_get` |
| POST | `/api/partners/{partner_id}/sessions/archive` | partners / Archive Partner Session | path:partner_id* | application/json | 200, 422 | `archive_partner_session_api_partners__partner_id__sessions_archive_post` |
| POST | `/api/partners/{partner_id}/sessions/branch` | partners / Branch Partner Session | path:partner_id* | application/json | 200, 422 | `branch_partner_session_api_partners__partner_id__sessions_branch_post` |
| POST | `/api/partners/{partner_id}/sessions/delete` | partners / Delete Partner Session | path:partner_id* | application/json | 200, 422 | `delete_partner_session_api_partners__partner_id__sessions_delete_post` |
| POST | `/api/partners/{partner_id}/sessions/resume` | partners / Resume Partner Session | path:partner_id* | application/json | 200, 422 | `resume_partner_session_api_partners__partner_id__sessions_resume_post` |
| GET | `/api/partners/{partner_id}/soul` | partners / Get Partner Soul | path:partner_id* | — | 200, 422 | `get_partner_soul_api_partners__partner_id__soul_get` |
| PUT | `/api/partners/{partner_id}/soul` | partners / Put Partner Soul | path:partner_id* | application/json | 200, 422 | `put_partner_soul_api_partners__partner_id__soul_put` |
| POST | `/api/partners/{partner_id}/start` | partners / Start Partner | path:partner_id* | — | 200, 422 | `start_partner_api_partners__partner_id__start_post` |
| POST | `/api/partners/{partner_id}/stop` | partners / Stop Partner | path:partner_id* | — | 200, 422 | `stop_partner_api_partners__partner_id__stop_post` |
| GET | `/api/partners/{partner_id}/web-continuity` | partners / Get Partner Web Continuity | path:partner_id* | — | 200, 422 | `get_partner_web_continuity_api_partners__partner_id__web_continuity_get` |
| PUT | `/api/partners/{partner_id}/web-continuity` | partners / Put Partner Web Continuity | path:partner_id* | application/json | 200, 422 | `put_partner_web_continuity_api_partners__partner_id__web_continuity_put` |
| GET | `/api/partners/{partner_id}/workspaces` | partners / Get Partner Workspaces | path:partner_id* | — | 200, 422 | `get_partner_workspaces_api_partners__partner_id__workspaces_get` |
| GET | `/api/personas` | personas / List Personas | — | — | 200, 422 | `list_personas_api_personas_get` |
| POST | `/api/personas` | personas / Create Persona | — | application/json | 200, 422 | `create_persona_api_personas_post` |
| DELETE | `/api/personas/{name}` | personas / Delete Persona | path:name* | — | 200, 422 | `delete_persona_api_personas__name__delete` |
| GET | `/api/personas/{name}` | personas / Get Persona | path:name* | — | 200, 422 | `get_persona_api_personas__name__get` |
| PUT | `/api/personas/{name}` | personas / Update Persona | path:name* | application/json | 200, 422 | `update_persona_api_personas__name__put` |
| GET | `/api/question-notebook/categories` | question-notebook / List Categories | query:course_id | — | 200, 422 | `list_categories_api_question_notebook_categories_get` |
| POST | `/api/question-notebook/categories` | question-notebook / Create Category | — | application/json | 201, 422 | `create_category_api_question_notebook_categories_post` |
| DELETE | `/api/question-notebook/categories/{category_id}` | question-notebook / Delete Category | path:category_id* | — | 200, 422 | `delete_category_api_question_notebook_categories__category_id__delete` |
| PATCH | `/api/question-notebook/categories/{category_id}` | question-notebook / Rename Category | path:category_id* | application/json | 200, 422 | `rename_category_api_question_notebook_categories__category_id__patch` |
| GET | `/api/question-notebook/entries` | question-notebook / List Entries | query:category_id, query:mistakes_only, query:uncategorized, query:bookmarked, query:is_correct, query:course_id, query:source, query:material_id, query:section_id, query:assessment_type, query:result, query:mastery_path_id, query:knowledge_point_id, query:resolved, query:score_trend, query:search, query:sort, query:limit, query:offset | — | 200, 422 | `list_entries_api_question_notebook_entries_get` |
| POST | `/api/question-notebook/entries/categories/bulk` | question-notebook / Bulk Link Entries | — | application/json | 200, 422 | `bulk_link_entries_api_question_notebook_entries_categories_bulk_post` |
| GET | `/api/question-notebook/entries/lookup/by-question` | question-notebook / Lookup Entry | query:session_id, query:origin_type, query:origin_ref, query:question_id*, query:turn_id, query:missing_ok | — | 200, 422 | `lookup_entry_api_question_notebook_entries_lookup_by_question_get` |
| POST | `/api/question-notebook/entries/upsert` | question-notebook / Upsert Single Entry | — | application/json | 200, 422 | `upsert_single_entry_api_question_notebook_entries_upsert_post` |
| DELETE | `/api/question-notebook/entries/{entry_id}` | question-notebook / Delete Entry | path:entry_id* | — | 200, 422 | `delete_entry_api_question_notebook_entries__entry_id__delete` |
| GET | `/api/question-notebook/entries/{entry_id}` | question-notebook / Get Entry | path:entry_id* | — | 200, 422 | `get_entry_api_question_notebook_entries__entry_id__get` |
| PATCH | `/api/question-notebook/entries/{entry_id}` | question-notebook / Update Entry | path:entry_id* | application/json | 200, 422 | `update_entry_api_question_notebook_entries__entry_id__patch` |
| POST | `/api/question-notebook/entries/{entry_id}/categories` | question-notebook / Add Entry To Category | path:entry_id* | application/json | 200, 422 | `add_entry_to_category_api_question_notebook_entries__entry_id__categories_post` |
| DELETE | `/api/question-notebook/entries/{entry_id}/categories/{category_id}` | question-notebook / Remove Entry From Category | path:entry_id*, path:category_id* | — | 200, 422 | `remove_entry_from_category_api_question_notebook_entries__entry_id__categories__category_id__delete` |
| GET | `/api/question-notebook/materials` | question-notebook / List Question Bank Materials | query:course_id | — | 200, 422 | `list_question_bank_materials_api_question_notebook_materials_get` |
| GET | `/api/question-notebook/practice/analytics` | practice / Practice Analytics | query:timezone, query:days, query:course_id, query:all_workspaces | — | 200, 422 | `practice_analytics_api_question_notebook_practice_analytics_get` |
| POST | `/api/question-notebook/practice/import/commit` | practice / Import Commit | — | application/json | 200, 422 | `import_commit_api_question_notebook_practice_import_commit_post` |
| POST | `/api/question-notebook/practice/import/preview` | practice / Import Preview | — | multipart/form-data | 200, 422 | `import_preview_api_question_notebook_practice_import_preview_post` |
| GET | `/api/question-notebook/practice/import/template` | practice / Import Template | query:format | — | 200, 422 | `import_template_api_question_notebook_practice_import_template_get` |
| GET | `/api/question-notebook/practice/questions/{entry_id}` | practice / Practice Question | path:entry_id* | — | 200, 422 | `practice_question_api_question_notebook_practice_questions__entry_id__get` |
| POST | `/api/question-notebook/practice/questions/{entry_id}/check` | practice / Check | path:entry_id* | application/json | 200, 422 | `check_api_question_notebook_practice_questions__entry_id__check_post` |
| POST | `/api/question-notebook/practice/questions/{entry_id}/review` | practice / Review | path:entry_id* | application/json | 200, 422 | `review_api_question_notebook_practice_questions__entry_id__review_post` |
| GET | `/api/question-notebook/practice/queue` | practice / Queue | query:timezone, query:course_id, query:category_id, query:limit, query:all_workspaces | — | 200, 422 | `queue_api_question_notebook_practice_queue_get` |
| GET | `/api/question-notebook/practice/summary` | practice / Summary | query:timezone, query:course_id, query:all_workspaces | — | 200, 422 | `summary_api_question_notebook_practice_summary_get` |
| GET | `/api/question-notebook/stats` | question-notebook / Question Bank Stats | query:course_id | — | 200, 422 | `question_bank_stats_api_question_notebook_stats_get` |
| GET | `/api/reading/epub-pairings` | reading / Epub Pairings | — | — | 200, 422 | `epub_pairings_api_reading_epub_pairings_get` |
| POST | `/api/reading/epub-pairings` | reading / Create Epub Pairing | — | application/json | 200, 422 | `create_epub_pairing_api_reading_epub_pairings_post` |
| DELETE | `/api/reading/epub-pairings/{pairing_id}` | reading / Remove Epub Pairing | path:pairing_id* | — | 200, 422 | `remove_epub_pairing_api_reading_epub_pairings__pairing_id__delete` |
| GET | `/api/reading/extensions` | reading-extensions / List Extensions | — | — | 200, 422 | `list_extensions_api_reading_extensions_get` |
| POST | `/api/reading/library/duplicate-check` | reading / Duplicate Check | — | application/json | 200, 422 | `duplicate_check_api_reading_library_duplicate_check_post` |
| POST | `/api/reading/library/import-urls` | reading / Import Urls | — | application/json | 202, 422 | `import_urls_api_reading_library_import_urls_post` |
| GET | `/api/reading/library/materials` | reading / List Library Materials | query:search, query:status, query:filter | — | 200, 422 | `list_library_materials_api_reading_library_materials_get` |
| GET | `/api/reading/materials` | reading / List Materials | — | — | 200, 422 | `list_materials_api_reading_materials_get` |
| POST | `/api/reading/materials` | reading / Upload Material | query:reuse | multipart/form-data | 200, 422 | `upload_material_api_reading_materials_post` |
| DELETE | `/api/reading/materials/{material_id}` | reading / Delete Material | path:material_id* | — | 200, 422 | `delete_material_api_reading_materials__material_id__delete` |
| GET | `/api/reading/materials/{material_id}` | reading / Get Material | path:material_id* | — | 200, 422 | `get_material_api_reading_materials__material_id__get` |
| GET | `/api/reading/materials/{material_id}/annotations` | reading / List Annotations | path:material_id* | — | 200, 422 | `list_annotations_api_reading_materials__material_id__annotations_get` |
| PUT | `/api/reading/materials/{material_id}/annotations` | reading / Save Annotation | path:material_id* | application/json | 200, 422 | `save_annotation_api_reading_materials__material_id__annotations_put` |
| DELETE | `/api/reading/materials/{material_id}/annotations/{annotation_id}` | reading / Delete Annotation | path:material_id*, path:annotation_id* | — | 200, 422 | `delete_annotation_api_reading_materials__material_id__annotations__annotation_id__delete` |
| GET | `/api/reading/materials/{material_id}/assets/{asset_name}` | reading / Get Snapshot Asset | path:material_id*, path:asset_name* | — | 200, 422 | `get_snapshot_asset_api_reading_materials__material_id__assets__asset_name__get` |
| GET | `/api/reading/materials/{material_id}/bookmarks` | reading / List Bookmarks | path:material_id* | — | 200, 422 | `list_bookmarks_api_reading_materials__material_id__bookmarks_get` |
| POST | `/api/reading/materials/{material_id}/bookmarks` | reading / Add Bookmark | path:material_id* | application/json | 200, 422 | `add_bookmark_api_reading_materials__material_id__bookmarks_post` |
| DELETE | `/api/reading/materials/{material_id}/bookmarks/{bookmark_id}` | reading / Delete Bookmark | path:material_id*, path:bookmark_id* | — | 200, 422 | `delete_bookmark_api_reading_materials__material_id__bookmarks__bookmark_id__delete` |
| GET | `/api/reading/materials/{material_id}/epub-pairing-candidates` | reading / Epub Pairing Candidates | path:material_id* | — | 200, 422 | `epub_pairing_candidates_api_reading_materials__material_id__epub_pairing_candidates_get` |
| GET | `/api/reading/materials/{material_id}/export` | reading / Export | path:material_id*, query:fmt | — | 200, 422 | `export_api_reading_materials__material_id__export_get` |
| POST | `/api/reading/materials/{material_id}/extensions/quiz/answers` | reading-extensions / Submit Quiz Answers | path:material_id* | application/json | 200, 422 | `submit_quiz_answers_api_reading_materials__material_id__extensions_quiz_answers_post` |
| POST | `/api/reading/materials/{material_id}/extensions/{extension_id}/actions/{action}` | reading-extensions / Run Extension Action | path:material_id*, path:extension_id*, path:action* | application/json | 200, 422 | `run_extension_action_api_reading_materials__material_id__extensions__extension_id__actions__action__post` |
| GET | `/api/reading/materials/{material_id}/media` | reading / List Material Media | path:material_id* | — | 200, 422 | `list_material_media_api_reading_materials__material_id__media_get` |
| GET | `/api/reading/materials/{material_id}/media/{name}` | reading / Get Material Media | path:material_id*, path:name* | — | 200, 422 | `get_material_media_api_reading_materials__material_id__media__name__get` |
| GET | `/api/reading/materials/{material_id}/position` | reading / Get Position | path:material_id* | — | 200, 422 | `get_position_api_reading_materials__material_id__position_get` |
| PUT | `/api/reading/materials/{material_id}/position` | reading / Save Position | path:material_id* | application/json | 200, 422 | `save_position_api_reading_materials__material_id__position_put` |
| GET | `/api/reading/materials/{material_id}/raw` | reading / Get Raw | path:material_id* | — | 200, 422 | `get_raw_api_reading_materials__material_id__raw_get` |
| GET | `/api/reading/materials/{material_id}/render` | reading / Get Render | path:material_id* | — | 200, 422 | `get_render_api_reading_materials__material_id__render_get` |
| POST | `/api/reading/materials/{material_id}/retry` | reading / Retry Import | path:material_id* | — | 202, 422 | `retry_import_api_reading_materials__material_id__retry_post` |
| GET | `/api/reading/materials/{material_id}/revisions` | reading / List Material Revisions | path:material_id* | — | 200, 422 | `list_material_revisions_api_reading_materials__material_id__revisions_get` |
| GET | `/api/reading/materials/{material_id}/revisions/{revision}/units/{locator}` | reading / Get Revision Unit | path:material_id*, path:revision*, path:locator* | — | 200, 422 | `get_revision_unit_api_reading_materials__material_id__revisions__revision__units__locator__get` |
| GET | `/api/reading/materials/{material_id}/transcript` | reading / Get Transcript | path:material_id* | — | 200, 422 | `get_transcript_api_reading_materials__material_id__transcript_get` |
| GET | `/api/reading/materials/{material_id}/units/{locator}` | reading / Get Unit | path:material_id*, path:locator* | — | 200, 422 | `get_unit_api_reading_materials__material_id__units__locator__get` |
| GET | `/api/reading/supported-formats` | reading / Supported Formats | — | — | 200, 422 | `supported_formats_api_reading_supported_formats_get` |
| GET | `/api/reading/workspaces` | reading / List Workspaces | query:search | — | 200, 422 | `list_workspaces_api_reading_workspaces_get` |
| POST | `/api/reading/workspaces` | reading / Create Workspace | — | application/json | 201, 422 | `create_workspace_api_reading_workspaces_post` |
| GET | `/api/reading/workspaces/index` | reading / List Workspace Index | — | — | 200, 422 | `list_workspace_index_api_reading_workspaces_index_get` |
| DELETE | `/api/reading/workspaces/{workspace_id}` | reading / Delete Workspace | path:workspace_id* | — | 200, 422 | `delete_workspace_api_reading_workspaces__workspace_id__delete` |
| GET | `/api/reading/workspaces/{workspace_id}` | reading / Get Workspace | path:workspace_id* | — | 200, 422 | `get_workspace_api_reading_workspaces__workspace_id__get` |
| PATCH | `/api/reading/workspaces/{workspace_id}` | reading / Update Workspace | path:workspace_id* | application/json | 200, 422 | `update_workspace_api_reading_workspaces__workspace_id__patch` |
| GET | `/api/reading/workspaces/{workspace_id}/ask-hint` | reading / Get Workspace Ask Hint | path:workspace_id*, query:session_id, query:locator, query:selection | — | 200, 422 | `get_workspace_ask_hint_api_reading_workspaces__workspace_id__ask_hint_get` |
| POST | `/api/reading/workspaces/{workspace_id}/materials` | reading / Add Workspace Material | path:workspace_id* | application/json | 200, 422 | `add_workspace_material_api_reading_workspaces__workspace_id__materials_post` |
| PUT | `/api/reading/workspaces/{workspace_id}/materials/order` | reading / Reorder Workspace Materials | path:workspace_id* | application/json | 200, 422 | `reorder_workspace_materials_api_reading_workspaces__workspace_id__materials_order_put` |
| DELETE | `/api/reading/workspaces/{workspace_id}/materials/{material_id}` | reading / Remove Workspace Material | path:workspace_id*, path:material_id* | — | 200, 422 | `remove_workspace_material_api_reading_workspaces__workspace_id__materials__material_id__delete` |
| PUT | `/api/reading/workspaces/{workspace_id}/materials/{material_id}/active` | reading / Activate Workspace Material | path:workspace_id*, path:material_id* | — | 200, 422 | `activate_workspace_material_api_reading_workspaces__workspace_id__materials__material_id__active_put` |
| POST | `/api/reading/workspaces/{workspace_id}/notebook` | reading / Capture Reading To Notebook | path:workspace_id* | application/json | 200, 422 | `capture_reading_to_notebook_api_reading_workspaces__workspace_id__notebook_post` |
| POST | `/api/reading/workspaces/{workspace_id}/notes/organize` | reading / Organize Reading Notes | path:workspace_id* | application/json | 200, 422 | `organize_reading_notes_api_reading_workspaces__workspace_id__notes_organize_post` |
| GET | `/api/reading/workspaces/{workspace_id}/sessions` | reading / List Reading Sessions | path:workspace_id* | — | 200, 422 | `list_reading_sessions_api_reading_workspaces__workspace_id__sessions_get` |
| POST | `/api/reading/workspaces/{workspace_id}/sessions` | reading / Create Reading Session | path:workspace_id* | application/json | 201, 422 | `create_reading_session_api_reading_workspaces__workspace_id__sessions_post` |
| DELETE | `/api/reading/workspaces/{workspace_id}/sessions/{session_id}` | reading / Delete Reading Session | path:workspace_id*, path:session_id* | — | 200, 422 | `delete_reading_session_api_reading_workspaces__workspace_id__sessions__session_id__delete` |
| PATCH | `/api/reading/workspaces/{workspace_id}/sessions/{session_id}` | reading / Rename Reading Session | path:workspace_id*, path:session_id* | application/json | 200, 422 | `rename_reading_session_api_reading_workspaces__workspace_id__sessions__session_id__patch` |
| POST | `/api/reading/workspaces/{workspace_id}/sessions/{session_id}/links` | reading / Link Reading Session | path:workspace_id*, path:session_id* | application/json | 200, 422 | `link_reading_session_api_reading_workspaces__workspace_id__sessions__session_id__links_post` |
| DELETE | `/api/reading/workspaces/{workspace_id}/sessions/{session_id}/links/{target_session_id}` | reading / Unlink Reading Session | path:workspace_id*, path:session_id*, path:target_session_id* | — | 200, 422 | `unlink_reading_session_api_reading_workspaces__workspace_id__sessions__session_id__links__target_session_id__delete` |
| GET | `/api/sessions` | sessions / List Sessions | query:limit, query:offset, query:workspace_id, query:all_workspaces | — | 200, 422 | `list_sessions_api_sessions_get` |
| GET | `/api/sessions/recycle-bin` | sessions / List Recycle Bin | query:limit, query:offset | — | 200, 422 | `list_recycle_bin_api_sessions_recycle_bin_get` |
| GET | `/api/sessions/search` | sessions / Search Sessions | query:q*, query:limit, query:offset, query:all_workspaces | — | 200, 422 | `search_sessions_api_sessions_search_get` |
| DELETE | `/api/sessions/{session_id}` | sessions / Delete Session | path:session_id* | — | 200, 422 | `delete_session_api_sessions__session_id__delete` |
| GET | `/api/sessions/{session_id}` | sessions / Get Session | path:session_id* | — | 200, 422 | `get_session_api_sessions__session_id__get` |
| PATCH | `/api/sessions/{session_id}` | sessions / Rename Session | path:session_id* | application/json | 200, 422 | `rename_session_api_sessions__session_id__patch` |
| GET | `/api/sessions/{session_id}/ask-hint` | sessions / Get Session Ask Hint | path:session_id* | — | 200, 422 | `get_session_ask_hint_api_sessions__session_id__ask_hint_get` |
| PUT | `/api/sessions/{session_id}/branch-selection` | sessions / Update Branch Selection | path:session_id* | application/json | 200, 422 | `update_branch_selection_api_sessions__session_id__branch_selection_put` |
| DELETE | `/api/sessions/{session_id}/messages/{message_id}` | sessions / Delete Turn By Message | path:session_id*, path:message_id* | — | 200, 422 | `delete_turn_by_message_api_sessions__session_id__messages__message_id__delete` |
| GET | `/api/sessions/{session_id}/messages/{message_id}/events` | sessions / Get Message Events | path:session_id*, path:message_id*, query:after_seq, query:limit | — | 200, 422 | `get_message_events_api_sessions__session_id__messages__message_id__events_get` |
| PATCH | `/api/sessions/{session_id}/organization` | sessions / Update Session Organization | path:session_id* | application/json | 200, 422 | `update_session_organization_api_sessions__session_id__organization_patch` |
| DELETE | `/api/sessions/{session_id}/purge` | sessions / Purge Session | path:session_id* | — | 200, 422 | `purge_session_api_sessions__session_id__purge_delete` |
| POST | `/api/sessions/{session_id}/quiz-results` | sessions / Record Quiz Results | path:session_id* | application/json | 200, 422 | `record_quiz_results_api_sessions__session_id__quiz_results_post` |
| PATCH | `/api/sessions/{session_id}/reply-language` | sessions / Update Session Reply Language | path:session_id* | application/json | 200, 422 | `update_session_reply_language_api_sessions__session_id__reply_language_patch` |
| POST | `/api/sessions/{session_id}/restore` | sessions / Restore Session | path:session_id* | — | 200, 422 | `restore_session_api_sessions__session_id__restore_post` |
| GET | `/api/settings` | settings / Get Settings | — | — | 200, 422 | `get_settings_api_settings_get` |
| POST | `/api/settings/apply` | settings / Apply Catalog | — | application/json | 200, 422 | `apply_catalog_api_settings_apply_post` |
| POST | `/api/settings/apply/provider` | settings / Apply Provider Edit | — | application/json | 200, 422 | `apply_provider_edit_api_settings_apply_provider_post` |