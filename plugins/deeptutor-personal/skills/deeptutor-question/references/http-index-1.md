# HTTP 接口索引 1/3

来源：官方 v1.6.12，提交 `ef2d9e5c3c99fd073742c5aadc2bb9584b1e503b`。由同目录 `openapi.json` 提取，未使用本地定制代码。

[调用指南](README.md) · [索引 1](http-index-1.md) · [索引 2](http-index-2.md) · [索引 3](http-index-3.md)

本表是导航，不是权限清单。参数的类型、默认值、约束、枚举和响应结构请按 operationId 在 OpenAPI 中查阅。必填参数标 `*`；公共 Authorization/Cookie 参数省略。

响应列仅为官方 schema 已声明的 HTTP 状态码，未覆盖全部运行时错误。部分 SSE/文件接口在 schema 中仍显示 JSON，实际行为见调用指南。

| 方法 | 精确路径 | 分组 / 官方摘要 | 参数位置与名称 | 请求体媒体类型 | 声明状态码 | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/` |  / Root | — | — | 200 | `root__get` |
| GET | `/api/agent-config/agents` | agent-config / Get Agent Config | — | — | 200, 422 | `get_agent_config_api_agent_config_agents_get` |
| GET | `/api/agent-config/agents/{agent_type}` | agent-config / Get Single Agent Config | path:agent_type* | — | 200, 422 | `get_single_agent_config_api_agent_config_agents__agent_type__get` |
| GET | `/api/auth/avatar/{user_id}` | auth / Get Avatar Image | path:user_id* | — | 200, 422 | `get_avatar_image_api_auth_avatar__user_id__get` |
| POST | `/api/auth/device-login` | auth / Device Login | — | application/json | 200, 422 | `device_login_api_auth_device_login_post` |
| POST | `/api/auth/device/heartbeat` | auth / Device Heartbeat | — | — | 200, 422 | `device_heartbeat_api_auth_device_heartbeat_post` |
| GET | `/api/auth/devices` | auth / List Devices | query:user_id, query:include_revoked | — | 200, 422 | `list_devices_api_auth_devices_get` |
| POST | `/api/auth/devices` | auth / Issue Device | — | application/json | 201, 422 | `issue_device_api_auth_devices_post` |
| DELETE | `/api/auth/devices/{device_credential_id}` | auth / Revoke Device | path:device_credential_id* | — | 200, 422 | `revoke_device_api_auth_devices__device_credential_id__delete` |
| GET | `/api/auth/is_first_user` | auth / Check Is First User | — | — | 200 | `check_is_first_user_api_auth_is_first_user_get` |
| POST | `/api/auth/login` | auth / Login | — | application/json | 200, 422 | `login_api_auth_login_post` |
| POST | `/api/auth/logout` | auth / Logout | — | — | 200 | `logout_api_auth_logout_post` |
| GET | `/api/auth/openai-codex/callback` | auth / Receive Codex Oauth Callback | query:code, query:state, query:error | — | 200, 422 | `receive_codex_oauth_callback_api_auth_openai_codex_callback_get` |
| GET | `/api/auth/profile` | auth / Get Profile | — | — | 200, 422 | `get_profile_api_auth_profile_get` |
| PUT | `/api/auth/profile` | auth / Update Profile | — | application/json | 200, 422 | `update_profile_api_auth_profile_put` |
| DELETE | `/api/auth/profile/avatar` | auth / Remove Avatar | — | — | 200, 422 | `remove_avatar_api_auth_profile_avatar_delete` |
| PUT | `/api/auth/profile/avatar` | auth / Upload Avatar | — | multipart/form-data | 200, 422 | `upload_avatar_api_auth_profile_avatar_put` |
| GET | `/api/auth/profile/learner-profile` | auth / Get Current Learner Profile | — | — | 200, 422 | `get_current_learner_profile_api_auth_profile_learner_profile_get` |
| PUT | `/api/auth/profile/learner-profile` | auth / Put Current Learner Profile | — | application/json | 200, 422 | `put_current_learner_profile_api_auth_profile_learner_profile_put` |
| POST | `/api/auth/register` | auth / Register | — | application/json | 201, 422 | `register_api_auth_register_post` |
| POST | `/api/auth/session-handoff` | auth / Create Session Handoff | — | application/json | 200, 422 | `create_session_handoff_api_auth_session_handoff_post` |
| POST | `/api/auth/session-handoff/complete` | auth / Complete Session Handoff | — | application/json | 200, 422 | `complete_session_handoff_api_auth_session_handoff_complete_post` |
| POST | `/api/auth/session-handoff/exchange` | auth / Exchange Session Handoff | — | application/json | 200, 422 | `exchange_session_handoff_api_auth_session_handoff_exchange_post` |
| GET | `/api/auth/status` | auth / Auth Status | — | — | 200, 422 | `auth_status_api_auth_status_get` |
| GET | `/api/auth/users` | auth / Get Users | — | — | 200, 422 | `get_users_api_auth_users_get` |
| POST | `/api/auth/users` | auth / Admin Create User | — | application/json | 201, 422 | `admin_create_user_api_auth_users_post` |
| POST | `/api/auth/users/batch-delete` | auth / Batch Remove Users | — | application/json | 200, 422 | `batch_remove_users_api_auth_users_batch_delete_post` |
| POST | `/api/auth/users/import` | auth / Admin Import Users | — | multipart/form-data | 200, 422 | `admin_import_users_api_auth_users_import_post` |
| DELETE | `/api/auth/users/{username}` | auth / Remove User | path:username* | — | 200, 422 | `remove_user_api_auth_users__username__delete` |
| GET | `/api/auth/users/{username}/learner-profile` | auth / Get Learner Profile | path:username* | — | 200, 422 | `get_learner_profile_api_auth_users__username__learner_profile_get` |
| PUT | `/api/auth/users/{username}/learner-profile` | auth / Put Learner Profile | path:username* | application/json | 200, 422 | `put_learner_profile_api_auth_users__username__learner_profile_put` |
| PUT | `/api/auth/users/{username}/role` | auth / Update User Role | path:username* | application/json | 200, 422 | `update_user_role_api_auth_users__username__role_put` |
| GET | `/api/books` | books / List Books | — | — | 200, 422 | `list_books_api_books_get` |
| POST | `/api/books` | books / Create Book | — | application/json | 200, 422 | `create_book_api_books_post` |
| GET | `/api/books/block-types` | books / Block Types | — | — | 200, 422 | `block_types_api_books_block_types_get` |
| POST | `/api/books/change-block-type` | books / Change Block Type | — | application/json | 200, 422 | `change_block_type_api_books_change_block_type_post` |
| POST | `/api/books/compile-page` | books / Compile Page | — | application/json | 200, 422 | `compile_page_api_books_compile_page_post` |
| POST | `/api/books/confirm-proposal` | books / Confirm Proposal | — | application/json | 200, 422 | `confirm_proposal_api_books_confirm_proposal_post` |
| POST | `/api/books/confirm-spine` | books / Confirm Spine | — | application/json | 200, 422 | `confirm_spine_api_books_confirm_spine_post` |
| POST | `/api/books/deep-dive` | books / Deep Dive | — | application/json | 200, 422 | `deep_dive_api_books_deep_dive_post` |
| POST | `/api/books/delete-block` | books / Delete Block | — | application/json | 200, 422 | `delete_block_api_books_delete_block_post` |
| GET | `/api/books/estimate-basis` | books / Estimate Basis | query:depth | — | 200, 422 | `estimate_basis_api_books_estimate_basis_get` |
| GET | `/api/books/health` | books / Health Check | — | — | 200, 422 | `health_check_api_books_health_get` |
| POST | `/api/books/insert-block` | books / Insert Block | — | application/json | 200, 422 | `insert_block_api_books_insert_block_post` |
| POST | `/api/books/move-block` | books / Move Block | — | application/json | 200, 422 | `move_block_api_books_move_block_post` |
| POST | `/api/books/page-chat-session` | books / Set Page Chat Session | — | application/json | 200, 422 | `set_page_chat_session_api_books_page_chat_session_post` |
| POST | `/api/books/pause` | books / Pause Book | — | application/json | 200, 422 | `pause_book_api_books_pause_post` |
| POST | `/api/books/progress/bookmark` | books / Toggle Bookmark | — | application/json | 200, 422 | `toggle_bookmark_api_books_progress_bookmark_post` |
| POST | `/api/books/progress/visit` | books / Mark Visited | — | application/json | 200, 422 | `mark_visited_api_books_progress_visit_post` |
| POST | `/api/books/quiz-attempt` | books / Quiz Attempt | — | application/json | 200, 422 | `quiz_attempt_api_books_quiz_attempt_post` |
| POST | `/api/books/rebuild` | books / Rebuild Book | — | application/json | 200, 422 | `rebuild_book_api_books_rebuild_post` |
| POST | `/api/books/regenerate-block` | books / Regenerate Block | — | application/json | 200, 422 | `regenerate_block_api_books_regenerate_block_post` |
| POST | `/api/books/resume` | books / Resume Book | — | application/json | 200, 422 | `resume_book_api_books_resume_post` |
| POST | `/api/books/supplement` | books / Supplement | — | application/json | 200, 422 | `supplement_api_books_supplement_post` |
| POST | `/api/books/update-block` | books / Update Block | — | application/json | 200, 422 | `update_block_api_books_update_block_post` |
| DELETE | `/api/books/{book_id}` | books / Delete Book | path:book_id* | — | 200, 422 | `delete_book_api_books__book_id__delete` |
| GET | `/api/books/{book_id}` | books / Get Book | path:book_id*, query:include_blocks | — | 200, 422 | `get_book_api_books__book_id__get` |
| GET | `/api/books/{book_id}/export` | books / Export Book | path:book_id* | — | 200, 422 | `export_book_api_books__book_id__export_get` |
| GET | `/api/books/{book_id}/health` | books / Book Health | path:book_id* | — | 200, 422 | `book_health_api_books__book_id__health_get` |
| GET | `/api/books/{book_id}/learning-captures` | books / List Learning Captures | path:book_id*, query:status | — | 200, 422 | `list_learning_captures_api_books__book_id__learning_captures_get` |
| POST | `/api/books/{book_id}/learning-captures` | books / Create Learning Capture | path:book_id* | application/json | 200, 422 | `create_learning_capture_api_books__book_id__learning_captures_post` |
| PATCH | `/api/books/{book_id}/learning-captures/{capture_id}` | books / Update Learning Capture | path:book_id*, path:capture_id* | application/json | 200, 422 | `update_learning_capture_api_books__book_id__learning_captures__capture_id__patch` |
| GET | `/api/books/{book_id}/pages/{page_id}` | books / Get Page | path:book_id*, path:page_id* | — | 200, 422 | `get_page_api_books__book_id__pages__page_id__get` |
| POST | `/api/books/{book_id}/refresh-fingerprints` | books / Refresh Fingerprints | path:book_id*, query:force, query:expected_revision | — | 200, 422 | `refresh_fingerprints_api_books__book_id__refresh_fingerprints_post` |
| GET | `/api/books/{book_id}/spine` | books / Get Spine | path:book_id* | — | 200, 422 | `get_spine_api_books__book_id__spine_get` |
| GET | `/api/capabilities/registered` | capabilities / List Registered Capabilities | — | — | 200, 422 | `list_registered_capabilities_api_capabilities_registered_get` |
| GET | `/api/capabilities/settings` | capabilities / Get Capabilities Settings Endpoint | — | — | 200, 422 | `get_capabilities_settings_endpoint_api_capabilities_settings_get` |
| PUT | `/api/capabilities/settings` | capabilities / Put Capabilities Settings | — | application/json | 200, 422 | `put_capabilities_settings_api_capabilities_settings_put` |
| GET | `/api/courses` | courses / List Courses | — | — | 200, 422 | `list_courses_api_courses_get` |
| POST | `/api/courses` | courses / Create Course | — | application/json | 200, 422 | `create_course_api_courses_post` |
| GET | `/api/courses/resource-candidates` | courses / List Resource Candidates | — | — | 200, 422 | `list_resource_candidates_api_courses_resource_candidates_get` |
| DELETE | `/api/courses/{course_id}` | courses / Delete Course | path:course_id* | — | 200, 422 | `delete_course_api_courses__course_id__delete` |
| PATCH | `/api/courses/{course_id}` | courses / Update Course | path:course_id* | application/json | 200, 422 | `update_course_api_courses__course_id__patch` |
| POST | `/api/courses/{course_id}/resources` | courses / Attach Course Resource | path:course_id* | application/json | 200, 422 | `attach_course_resource_api_courses__course_id__resources_post` |
| DELETE | `/api/courses/{course_id}/resources/{resource_id}` | courses / Detach Course Resource | path:course_id*, path:resource_id* | — | 200, 422 | `detach_course_resource_api_courses__course_id__resources__resource_id__delete` |
| GET | `/api/courses/{course_id}/state` | courses / Get Course State | path:course_id* | — | 200, 422 | `get_course_state_api_courses__course_id__state_get` |
| PUT | `/api/courses/{course_id}/syllabus` | courses / Set Course Syllabus | path:course_id* | application/json | 200, 422 | `set_course_syllabus_api_courses__course_id__syllabus_put` |
| PATCH | `/api/courses/{course_id}/syllabus/{unit_id}` | courses / Update Syllabus Unit | path:course_id*, path:unit_id* | application/json | 200, 422 | `update_syllabus_unit_api_courses__course_id__syllabus__unit_id__patch` |
| GET | `/api/dashboard/learning-index` | dashboard / Get Learning Index | — | — | 200, 422 | `get_learning_index_api_dashboard_learning_index_get` |
| GET | `/api/dashboard/learning-library/{kind}` | dashboard / Get Learning Library | path:kind* | — | 200, 422 | `get_learning_library_api_dashboard_learning_library__kind__get` |
| GET | `/api/dashboard/recent` | dashboard / Get Recent Activities | query:limit, query:type | — | 200, 422 | `get_recent_activities_api_dashboard_recent_get` |
| GET | `/api/dashboard/source-library/{kind}` | dashboard / Get Source Library | path:kind* | — | 200, 422 | `get_source_library_api_dashboard_source_library__kind__get` |
| GET | `/api/dashboard/suggestions` | dashboard / Get Starter Suggestions | — | — | 200, 422 | `get_starter_suggestions_api_dashboard_suggestions_get` |
| POST | `/api/dashboard/suggestions/refresh` | dashboard / Refresh Starter Suggestions | — | — | 200, 422 | `refresh_starter_suggestions_api_dashboard_suggestions_refresh_post` |
| GET | `/api/dashboard/{entry_id}` | dashboard / Get Activity Entry | path:entry_id* | — | 200, 422 | `get_activity_entry_api_dashboard__entry_id__get` |
| GET | `/api/documents` | documents / List Documents | — | — | 200, 422 | `list_documents_api_documents_get` |
| POST | `/api/documents` | documents / Create Document | — | application/json | 200, 422 | `create_document_api_documents_post` |
| POST | `/api/documents/actions/automark` | documents / Auto Mark Text | — | application/json | 200, 422 | `auto_mark_text_api_documents_actions_automark_post` |
| POST | `/api/documents/actions/edit` | documents / Edit Text | — | application/json | 200, 422 | `edit_text_api_documents_actions_edit_post` |
| POST | `/api/documents/actions/edit-react` | documents / Edit Text React | — | application/json | 200, 422 | `edit_text_react_api_documents_actions_edit_react_post` |
| POST | `/api/documents/actions/edit-react/stream` | documents / Edit Text React Stream | — | application/json | 200, 422 | `edit_text_react_stream_api_documents_actions_edit_react_stream_post` |
| POST | `/api/documents/export/docx` | documents / Export Docx | — | application/json | 200, 422 | `export_docx_api_documents_export_docx_post` |
| GET | `/api/documents/history` | documents / Get History | — | — | 200, 422 | `get_history_api_documents_history_get` |
| GET | `/api/documents/history/{operation_id}` | documents / Get Operation | path:operation_id* | — | 200, 422 | `get_operation_api_documents_history__operation_id__get` |
| POST | `/api/documents/import/docx` | documents / Import Docx | — | multipart/form-data | 200, 422 | `import_docx_api_documents_import_docx_post` |
| GET | `/api/documents/tool-calls/{operation_id}` | documents / Get Tool Call | path:operation_id* | — | 200, 422 | `get_tool_call_api_documents_tool_calls__operation_id__get` |
| DELETE | `/api/documents/{doc_id}` | documents / Delete Document | path:doc_id* | — | 200, 422 | `delete_document_api_documents__doc_id__delete` |
| GET | `/api/documents/{doc_id}` | documents / Get Document | path:doc_id* | — | 200, 422 | `get_document_api_documents__doc_id__get` |
| PUT | `/api/documents/{doc_id}` | documents / Update Document | path:doc_id* | application/json | 200, 422 | `update_document_api_documents__doc_id__put` |
| GET | `/api/file-preview/pdf` | file-preview / Preview Office Source | query:source* | — | 200, 422 | `preview_office_source_api_file_preview_pdf_get` |
| POST | `/api/file-preview/pdf` | file-preview / Preview Office Upload | — | multipart/form-data | 200, 422 | `preview_office_upload_api_file_preview_pdf_post` |
| GET | `/api/imports/chat-history` | imports / List Imported Chat History | query:limit, query:offset | — | 200, 422 | `list_imported_chat_history_api_imports_chat_history_get` |
| POST | `/api/imports/chat-history` | imports / Import Chat History | — | application/json | 200, 422 | `import_chat_history_api_imports_chat_history_post` |
| GET | `/api/knowledge-bases` | knowledge-bases / List Knowledge Bases | — | — | 200, 422 | `list_knowledge_bases_api_knowledge_bases_get` |
| POST | `/api/knowledge-bases` | knowledge-bases / Create Knowledge Base | — | multipart/form-data | 200, 422 | `create_knowledge_base_api_knowledge_bases_post` |
| GET | `/api/knowledge-bases/configs` | knowledge-bases / Get All Kb Configs | — | — | 200, 422 | `get_all_kb_configs_api_knowledge_bases_configs_get` |
| POST | `/api/knowledge-bases/configs/sync` | knowledge-bases / Sync Configs From Metadata | — | — | 200, 422 | `sync_configs_from_metadata_api_knowledge_bases_configs_sync_post` |
| POST | `/api/knowledge-bases/connect-folder` | knowledge-bases / Connect Linked Folder Route | — | application/json | 200, 422 | `connect_linked_folder_route_api_knowledge_bases_connect_folder_post` |
| POST | `/api/knowledge-bases/connect-ima` | knowledge-bases / Connect Ima Route | — | application/json | 200, 422 | `connect_ima_route_api_knowledge_bases_connect_ima_post` |
| POST | `/api/knowledge-bases/connect-lightrag-server` | knowledge-bases / Connect Lightrag Server Route | — | application/json | 200, 422 | `connect_lightrag_server_route_api_knowledge_bases_connect_lightrag_server_post` |
| POST | `/api/knowledge-bases/connect-marginnote4` | knowledge-bases / Connect Marginnote4 | — | application/json | 200, 422 | `connect_marginnote4_api_knowledge_bases_connect_marginnote4_post` |
| POST | `/api/knowledge-bases/connect-obsidian` | knowledge-bases / Connect Obsidian Vault | — | application/json | 200, 422 | `connect_obsidian_vault_api_knowledge_bases_connect_obsidian_post` |
| POST | `/api/knowledge-bases/connect-weknora` | knowledge-bases / Connect Weknora Route | — | application/json | 200, 422 | `connect_weknora_route_api_knowledge_bases_connect_weknora_post` |
| GET | `/api/knowledge-bases/default` | knowledge-bases / Get Default Kb | — | — | 200, 422 | `get_default_kb_api_knowledge_bases_default_get` |
| PUT | `/api/knowledge-bases/default/{kb_name}` | knowledge-bases / Set Default Kb | path:kb_name* | — | 200, 422 | `set_default_kb_api_knowledge_bases_default__kb_name__put` |
| POST | `/api/knowledge-bases/delete` | knowledge-bases / Delete Knowledge Base By Name | — | application/json | 200, 422 | `delete_knowledge_base_by_name_api_knowledge_bases_delete_post` |
| GET | `/api/knowledge-bases/embedding-usage` | knowledge-bases / Get Embedding Usage | — | — | 200, 422 | `get_embedding_usage_api_knowledge_bases_embedding_usage_get` |
| GET | `/api/knowledge-bases/health` | knowledge-bases / Health Check | — | — | 200, 422 | `health_check_api_knowledge_bases_health_get` |
| POST | `/api/knowledge-bases/list-ima` | knowledge-bases / List Ima Route | — | application/json | 200, 422 | `list_ima_route_api_knowledge_bases_list_ima_post` |
| POST | `/api/knowledge-bases/probe-folder` | knowledge-bases / Probe Linked Folder Route | — | application/json | 200, 422 | `probe_linked_folder_route_api_knowledge_bases_probe_folder_post` |
| POST | `/api/knowledge-bases/probe-ima` | knowledge-bases / Probe Ima Route | — | application/json | 200, 422 | `probe_ima_route_api_knowledge_bases_probe_ima_post` |
| POST | `/api/knowledge-bases/probe-lightrag-server` | knowledge-bases / Probe Lightrag Server Route | — | application/json | 200, 422 | `probe_lightrag_server_route_api_knowledge_bases_probe_lightrag_server_post` |
| POST | `/api/knowledge-bases/probe-weknora` | knowledge-bases / Probe Weknora Route | — | application/json | 200, 422 | `probe_weknora_route_api_knowledge_bases_probe_weknora_post` |
| PUT | `/api/knowledge-bases/rag-pipelines/active-model` | knowledge-bases / Set Rag Active Model | — | application/json | 200, 422 | `set_rag_active_model_api_knowledge_bases_rag_pipelines_active_model_put` |
| GET | `/api/knowledge-bases/rag-pipelines/graphrag/config` | knowledge-bases / Get Graphrag Pipeline Config | — | — | 200, 422 | `get_graphrag_pipeline_config_api_knowledge_bases_rag_pipelines_graphrag_config_get` |
| PUT | `/api/knowledge-bases/rag-pipelines/graphrag/config` | knowledge-bases / Update Graphrag Pipeline Config | — | application/json | 200, 422 | `update_graphrag_pipeline_config_api_knowledge_bases_rag_pipelines_graphrag_config_put` |
| POST | `/api/knowledge-bases/rag-pipelines/graphrag/model-compatibility` | knowledge-bases / Test Graphrag Model Compatibility | — | application/json | 200, 422 | `test_graphrag_model_compatibility_api_knowledge_bases_rag_pipelines_graphrag_model_compatibility_post` |
| GET | `/api/knowledge-bases/rag-pipelines/ima/config` | knowledge-bases / Get Ima Pipeline Config | — | — | 200, 422 | `get_ima_pipeline_config_api_knowledge_bases_rag_pipelines_ima_config_get` |
| PUT | `/api/knowledge-bases/rag-pipelines/ima/config` | knowledge-bases / Update Ima Pipeline Config | — | application/json | 200, 422 | `update_ima_pipeline_config_api_knowledge_bases_rag_pipelines_ima_config_put` |
| GET | `/api/knowledge-bases/rag-pipelines/lightrag-server/config` | knowledge-bases / Get Lightrag Server Pipeline Config | — | — | 200, 422 | `get_lightrag_server_pipeline_config_api_knowledge_bases_rag_pipelines_lightrag_server_config_get` |
| PUT | `/api/knowledge-bases/rag-pipelines/lightrag-server/config` | knowledge-bases / Update Lightrag Server Pipeline Config | — | application/json | 200, 422 | `update_lightrag_server_pipeline_config_api_knowledge_bases_rag_pipelines_lightrag_server_config_put` |
| GET | `/api/knowledge-bases/rag-pipelines/lightrag/config` | knowledge-bases / Get Lightrag Pipeline Config | — | — | 200, 422 | `get_lightrag_pipeline_config_api_knowledge_bases_rag_pipelines_lightrag_config_get` |
| PUT | `/api/knowledge-bases/rag-pipelines/lightrag/config` | knowledge-bases / Update Lightrag Pipeline Config | — | application/json | 200, 422 | `update_lightrag_pipeline_config_api_knowledge_bases_rag_pipelines_lightrag_config_put` |
| GET | `/api/knowledge-bases/rag-pipelines/lightrag/model-options` | knowledge-bases / Get Lightrag Model Options | — | — | 200, 422 | `get_lightrag_model_options_api_knowledge_bases_rag_pipelines_lightrag_model_options_get` |
| GET | `/api/knowledge-bases/rag-pipelines/llamaindex/config` | knowledge-bases / Get Llamaindex Pipeline Config | — | — | 200, 422 | `get_llamaindex_pipeline_config_api_knowledge_bases_rag_pipelines_llamaindex_config_get` |
| PUT | `/api/knowledge-bases/rag-pipelines/llamaindex/config` | knowledge-bases / Update Llamaindex Pipeline Config | — | application/json | 200, 422 | `update_llamaindex_pipeline_config_api_knowledge_bases_rag_pipelines_llamaindex_config_put` |
| GET | `/api/knowledge-bases/rag-pipelines/model-options` | knowledge-bases / Get Rag Model Options | query:kinds | — | 200, 422 | `get_rag_model_options_api_knowledge_bases_rag_pipelines_model_options_get` |
| GET | `/api/knowledge-bases/rag-pipelines/pageindex/config` | knowledge-bases / Get Pageindex Pipeline Config | — | — | 200, 422 | `get_pageindex_pipeline_config_api_knowledge_bases_rag_pipelines_pageindex_config_get` |
| PUT | `/api/knowledge-bases/rag-pipelines/pageindex/config` | knowledge-bases / Update Pageindex Pipeline Config | — | application/json | 200, 422 | `update_pageindex_pipeline_config_api_knowledge_bases_rag_pipelines_pageindex_config_put` |
| GET | `/api/knowledge-bases/rag-pipelines/{provider}/preflight` | knowledge-bases / Get Rag Pipeline Preflight | path:provider* | — | 200, 422 | `get_rag_pipeline_preflight_api_knowledge_bases_rag_pipelines__provider__preflight_get` |
| GET | `/api/knowledge-bases/rag-providers` | knowledge-bases / Get Rag Providers | — | — | 200, 422 | `get_rag_providers_api_knowledge_bases_rag_providers_get` |
| PUT | `/api/knowledge-bases/rag-providers/{provider}/mode` | knowledge-bases / Set Rag Provider Mode | path:provider* | application/json | 200, 422 | `set_rag_provider_mode_api_knowledge_bases_rag_providers__provider__mode_put` |
| GET | `/api/knowledge-bases/supported-file-types` | knowledge-bases / Get Supported File Types | — | — | 200, 422 | `get_supported_file_types_api_knowledge_bases_supported_file_types_get` |
| GET | `/api/knowledge-bases/tasks/{task_id}/stream` | knowledge-bases / Stream Task Logs | path:task_id* | — | 200, 422 | `stream_task_logs_api_knowledge_bases_tasks__task_id__stream_get` |
| DELETE | `/api/knowledge-bases/{kb_name}` | knowledge-bases / Delete Knowledge Base | path:kb_name* | — | 200, 422 | `delete_knowledge_base_api_knowledge_bases__kb_name__delete` |
| GET | `/api/knowledge-bases/{kb_name}` | knowledge-bases / Get Knowledge Base Details | path:kb_name* | — | 200, 422 | `get_knowledge_base_details_api_knowledge_bases__kb_name__get` |
| GET | `/api/knowledge-bases/{kb_name}/config` | knowledge-bases / Get Kb Config | path:kb_name* | — | 200, 422 | `get_kb_config_api_knowledge_bases__kb_name__config_get` |
| PUT | `/api/knowledge-bases/{kb_name}/config` | knowledge-bases / Update Kb Config | path:kb_name* | application/json | 200, 422 | `update_kb_config_api_knowledge_bases__kb_name__config_put` |
| GET | `/api/knowledge-bases/{kb_name}/file-preview-text/{filename}` | knowledge-bases / Serve Kb Raw File Text Preview | path:kb_name*, path:filename* | — | 200, 422 | `serve_kb_raw_file_text_preview_api_knowledge_bases__kb_name__file_preview_text__filename__get` |
| GET | `/api/knowledge-bases/{kb_name}/files` | knowledge-bases / List Kb Raw Files | path:kb_name* | — | 200, 422 | `list_kb_raw_files_api_knowledge_bases__kb_name__files_get` |
| POST | `/api/knowledge-bases/{kb_name}/files/move` | knowledge-bases / Move Kb File | path:kb_name* | application/json | 200, 422 | `move_kb_file_api_knowledge_bases__kb_name__files_move_post` |
| DELETE | `/api/knowledge-bases/{kb_name}/files/{filename}` | knowledge-bases / Delete Kb File | path:kb_name*, path:filename* | — | 200, 422 | `delete_kb_file_api_knowledge_bases__kb_name__files__filename__delete` |
| GET | `/api/knowledge-bases/{kb_name}/files/{filename}` | knowledge-bases / Serve Kb Raw File | path:kb_name*, path:filename* | — | 200, 422 | `serve_kb_raw_file_api_knowledge_bases__kb_name__files__filename__get` |
| POST | `/api/knowledge-bases/{kb_name}/folders` | knowledge-bases / Create Kb Folder | path:kb_name* | application/json | 200, 422 | `create_kb_folder_api_knowledge_bases__kb_name__folders_post` |
| POST | `/api/knowledge-bases/{kb_name}/github-source` | knowledge-bases / Add Github Source | path:kb_name* | application/json | 200, 422 | `add_github_source_api_knowledge_bases__kb_name__github_source_post` |
| DELETE | `/api/knowledge-bases/{kb_name}/github-source/{source_id}` | knowledge-bases / Remove Github Source | path:kb_name*, path:source_id* | — | 200, 422 | `remove_github_source_api_knowledge_bases__kb_name__github_source__source_id__delete` |
| GET | `/api/knowledge-bases/{kb_name}/github-sources` | knowledge-bases / Get Github Sources | path:kb_name* | — | 200, 422 | `get_github_sources_api_knowledge_bases__kb_name__github_sources_get` |
| PUT | `/api/knowledge-bases/{kb_name}/indexing-policy` | knowledge-bases / Update Pending Indexing Policy | path:kb_name* | application/json | 200, 422 | `update_pending_indexing_policy_api_knowledge_bases__kb_name__indexing_policy_put` |
| POST | `/api/knowledge-bases/{kb_name}/link-folder` | knowledge-bases / Link Folder | path:kb_name* | application/json | 200, 422 | `link_folder_api_knowledge_bases__kb_name__link_folder_post` |
| GET | `/api/knowledge-bases/{kb_name}/linked-folders` | knowledge-bases / Get Linked Folders | path:kb_name* | — | 200, 422 | `get_linked_folders_api_knowledge_bases__kb_name__linked_folders_get` |
| DELETE | `/api/knowledge-bases/{kb_name}/linked-folders/{folder_id}` | knowledge-bases / Unlink Folder | path:kb_name*, path:folder_id* | — | 200, 422 | `unlink_folder_api_knowledge_bases__kb_name__linked_folders__folder_id__delete` |
| GET | `/api/knowledge-bases/{kb_name}/progress` | knowledge-bases / Get Progress | path:kb_name* | — | 200, 422 | `get_progress_api_knowledge_bases__kb_name__progress_get` |
| POST | `/api/knowledge-bases/{kb_name}/progress/clear` | knowledge-bases / Clear Progress | path:kb_name* | — | 200, 422 | `clear_progress_api_knowledge_bases__kb_name__progress_clear_post` |
| POST | `/api/knowledge-bases/{kb_name}/reindex` | knowledge-bases / Reindex Knowledge Base | path:kb_name* | application/x-www-form-urlencoded | 200, 422 | `reindex_knowledge_base_api_knowledge_bases__kb_name__reindex_post` |
| GET | `/api/knowledge-bases/{kb_name}/reindex-config` | knowledge-bases / Get Reindex Config | path:kb_name*, query:embedding_model | — | 200, 422 | `get_reindex_config_api_knowledge_bases__kb_name__reindex_config_get` |
| POST | `/api/knowledge-bases/{kb_name}/retry` | knowledge-bases / Retry Knowledge Base | path:kb_name* | — | 200, 422 | `retry_knowledge_base_api_knowledge_bases__kb_name__retry_post` |
| POST | `/api/knowledge-bases/{kb_name}/sync-folder/{folder_id}` | knowledge-bases / Sync Folder | path:kb_name*, path:folder_id* | — | 200, 422 | `sync_folder_api_knowledge_bases__kb_name__sync_folder__folder_id__post` |
| POST | `/api/knowledge-bases/{kb_name}/sync-github` | knowledge-bases / Sync Github Sources | path:kb_name* | — | 200, 422 | `sync_github_sources_api_knowledge_bases__kb_name__sync_github_post` |
| POST | `/api/knowledge-bases/{kb_name}/sync-web` | knowledge-bases / Sync Web Sources | path:kb_name* | — | 200, 422 | `sync_web_sources_api_knowledge_bases__kb_name__sync_web_post` |
| POST | `/api/knowledge-bases/{kb_name}/upload` | knowledge-bases / Upload Files | path:kb_name* | multipart/form-data | 200, 422 | `upload_files_api_knowledge_bases__kb_name__upload_post` |
| POST | `/api/knowledge-bases/{kb_name}/web-source` | knowledge-bases / Add Web Source | path:kb_name* | application/json | 200, 422 | `add_web_source_api_knowledge_bases__kb_name__web_source_post` |
| GET | `/api/knowledge-bases/{kb_name}/web-source-sync` | knowledge-bases / Get Web Source Sync Jobs | path:kb_name* | — | 200, 422 | `get_web_source_sync_jobs_api_knowledge_bases__kb_name__web_source_sync_get` |
| DELETE | `/api/knowledge-bases/{kb_name}/web-source/{source_id}` | knowledge-bases / Remove Web Source | path:kb_name*, path:source_id* | — | 200, 422 | `remove_web_source_api_knowledge_bases__kb_name__web_source__source_id__delete` |
| POST | `/api/knowledge-bases/{kb_name}/web-source/{source_id}/cancel` | knowledge-bases / Cancel Web Source Sync | path:kb_name*, path:source_id* | — | 200, 422 | `cancel_web_source_sync_api_knowledge_bases__kb_name__web_source__source_id__cancel_post` |
| POST | `/api/knowledge-bases/{kb_name}/web-source/{source_id}/retry` | knowledge-bases / Retry Web Source Sync | path:kb_name*, path:source_id* | — | 200, 422 | `retry_web_source_sync_api_knowledge_bases__kb_name__web_source__source_id__retry_post` |
| PUT | `/api/knowledge-bases/{kb_name}/web-source/{source_id}/schedule` | knowledge-bases / Update Web Source Schedule | path:kb_name*, path:source_id* | application/json | 200, 422 | `update_web_source_schedule_api_knowledge_bases__kb_name__web_source__source_id__schedule_put` |
| GET | `/api/knowledge-bases/{kb_name}/web-sources` | knowledge-bases / Get Web Sources | path:kb_name* | — | 200, 422 | `get_web_sources_api_knowledge_bases__kb_name__web_sources_get` |
| GET | `/api/marginnote4/devices` | marginnote4 / List Devices | — | — | 200, 422 | `list_devices_api_marginnote4_devices_get` |
| DELETE | `/api/marginnote4/devices/{device_id}` | marginnote4 / Revoke Device | path:device_id* | — | 200, 422 | `revoke_device_api_marginnote4_devices__device_id__delete` |
| POST | `/api/marginnote4/heartbeat` | marginnote4 / Heartbeat | — | — | 200, 422 | `heartbeat_api_marginnote4_heartbeat_post` |
| POST | `/api/marginnote4/pair` | marginnote4 / Pair Device | — | application/json | 200, 422 | `pair_device_api_marginnote4_pair_post` |
| GET | `/api/marginnote4/status` | marginnote4 / Status | — | — | 200, 422 | `status_api_marginnote4_status_get` |
| POST | `/api/marginnote4/sync` | marginnote4 / Sync Objects | — | application/json | 200, 422 | `sync_objects_api_marginnote4_sync_post` |
| GET | `/api/mastery-paths/progress` | mastery-path / List All Progress | — | — | 200, 422 | `list_all_progress_api_mastery_paths_progress_get` |
| DELETE | `/api/mastery-paths/progress/{book_id}` | mastery-path / Delete Progress | path:book_id* | — | 200, 422 | `delete_progress_api_mastery_paths_progress__book_id__delete` |
| GET | `/api/mastery-paths/progress/{book_id}` | mastery-path / Get Progress | path:book_id* | — | 200, 422 | `get_progress_api_mastery_paths_progress__book_id__get` |
| PATCH | `/api/mastery-paths/progress/{book_id}` | mastery-path / Rename Progress | path:book_id* | application/json | 200, 422 | `rename_progress_api_mastery_paths_progress__book_id__patch` |
| GET | `/api/mastery-paths/progress/{book_id}/board` | mastery-path / Get Progress Board | path:book_id* | — | 200, 422 | `get_progress_board_api_mastery_paths_progress__book_id__board_get` |
| GET | `/api/mastery-paths/progress/{book_id}/events` | mastery-path / Get Progress Events | path:book_id*, query:after_revision | — | 200, 422 | `get_progress_events_api_mastery_paths_progress__book_id__events_get` |
| POST | `/api/mastery-paths/progress/{book_id}/generate-from-notebook` | mastery-path / Generate From Notebook | path:book_id* | application/json | 200, 422 | `generate_from_notebook_api_mastery_paths_progress__book_id__generate_from_notebook_post` |
| POST | `/api/mastery-paths/progress/{book_id}/generate-from-reading` | mastery-path / Generate From Reading | path:book_id* | application/json | 200, 422 | `generate_from_reading_api_mastery_paths_progress__book_id__generate_from_reading_post` |
| POST | `/api/mastery-paths/progress/{book_id}/import-from-book` | mastery-path / Import From Book | path:book_id* | application/json | 200, 422 | `import_from_book_api_mastery_paths_progress__book_id__import_from_book_post` |
| POST | `/api/mastery-paths/progress/{book_id}/init-modules` | mastery-path / Init Modules | path:book_id* | application/json | 200, 422 | `init_modules_api_mastery_paths_progress__book_id__init_modules_post` |
| GET | `/api/mastery-paths/progress/{book_id}/map` | mastery-path / Get Progress Map | path:book_id* | — | 200, 422 | `get_progress_map_api_mastery_paths_progress__book_id__map_get` |
| GET | `/api/mastery-paths/progress/{book_id}/objectives/{kp_id}` | mastery-path / Get Objective Report | path:book_id*, path:kp_id* | — | 200, 422 | `get_objective_report_api_mastery_paths_progress__book_id__objectives__kp_id__get` |
| POST | `/api/mastery-paths/progress/{book_id}/redo` | mastery-path / Redo Progress | path:book_id* | — | 200, 422 | `redo_progress_api_mastery_paths_progress__book_id__redo_post` |
| GET | `/api/mastery-paths/progress/{book_id}/sessions` | mastery-path / Get Progress Sessions | path:book_id* | — | 200, 422 | `get_progress_sessions_api_mastery_paths_progress__book_id__sessions_get` |
| POST | `/api/mastery-paths/progress/{book_id}/skip-question` | mastery-path / Skip Pending Question | path:book_id* | — | 200, 422 | `skip_pending_question_api_mastery_paths_progress__book_id__skip_question_post` |
| GET | `/api/mastery-paths/reading/records` | mastery-path / List Reading Learning Records | — | — | 200, 422 | `list_reading_learning_records_api_mastery_paths_reading_records_get` |
| GET | `/api/mastery-paths/topics` | mastery-path / List Topics | — | — | 200, 422 | `list_topics_api_mastery_paths_topics_get` |
| POST | `/api/mastery-paths/topics` | mastery-path / Create Topic | — | application/json | 200, 422 | `create_topic_api_mastery_paths_topics_post` |
| POST | `/api/mastery-paths/topics/draft` | mastery-path / Generate Topic Route | — | application/json | 200, 422 | `generate_topic_route_api_mastery_paths_topics_draft_post` |
| GET | `/api/mastery-paths/topics/index` | mastery-path / List Topic Index | — | — | 200, 422 | `list_topic_index_api_mastery_paths_topics_index_get` |
| GET | `/api/mastery-paths/topics/{path_id}` | mastery-path / Get Topic | path:path_id* | — | 200, 422 | `get_topic_api_mastery_paths_topics__path_id__get` |
| GET | `/api/mastery-paths/topics/{path_id}/ask-hint` | mastery-path / Get Topic Ask Hint | path:path_id*, query:session_id | — | 200, 422 | `get_topic_ask_hint_api_mastery_paths_topics__path_id__ask_hint_get` |
| PUT | `/api/mastery-paths/topics/{path_id}/map` | mastery-path / Edit Topic Map | path:path_id* | application/json | 200, 422 | `edit_topic_map_api_mastery_paths_topics__path_id__map_put` |
| POST | `/api/mastery-paths/topics/{path_id}/objectives/{kp_id}/override` | mastery-path / Set Learner Override | path:path_id*, path:kp_id* | application/json | 200, 422 | `set_learner_override_api_mastery_paths_topics__path_id__objectives__kp_id__override_post` |
| GET | `/api/mastery-paths/topics/{path_id}/review-settings` | mastery-path / Get Review Settings | path:path_id* | — | 200, 422 | `get_review_settings_api_mastery_paths_topics__path_id__review_settings_get` |
| PUT | `/api/mastery-paths/topics/{path_id}/review-settings` | mastery-path / Update Review Settings | path:path_id* | application/json | 200, 422 | `update_review_settings_api_mastery_paths_topics__path_id__review_settings_put` |
| GET | `/api/mastery-paths/topics/{path_id}/sessions` | mastery-path / List Topic Sessions | path:path_id* | — | 200, 422 | `list_topic_sessions_api_mastery_paths_topics__path_id__sessions_get` |
| PUT | `/api/mastery-paths/topics/{path_id}/sessions/{session_id}/mode` | mastery-path / Set Session Mode | path:path_id*, path:session_id* | application/json | 200, 422 | `set_session_mode_api_mastery_paths_topics__path_id__sessions__session_id__mode_put` |
| GET | `/api/memory/backup` | memory / List Backups | — | — | 200, 422 | `list_backups_api_memory_backup_get` |
| GET | `/api/memory/doc/{layer}/{key}` | memory / Get Doc | path:layer*, path:key* | — | 200, 422 | `get_doc_api_memory_doc__layer___key__get` |
| PUT | `/api/memory/doc/{layer}/{key}` | memory / Put Doc | path:layer*, path:key* | application/json | 200, 422 | `put_doc_api_memory_doc__layer___key__put` |
| POST | `/api/memory/doc/{layer}/{key}/apply` | memory / Apply Doc Ops | path:layer*, path:key* | application/json | 200, 422 | `apply_doc_ops_api_memory_doc__layer___key__apply_post` |
| POST | `/api/memory/doc/{layer}/{key}/audit` | memory / Audit Doc | path:layer*, path:key* | application/json | 200, 422 | `audit_doc_api_memory_doc__layer___key__audit_post` |
| POST | `/api/memory/doc/{layer}/{key}/dedup` | memory / Dedup Doc | path:layer*, path:key* | application/json | 200, 422 | `dedup_doc_api_memory_doc__layer___key__dedup_post` |
| DELETE | `/api/memory/doc/{layer}/{key}/entry/{entry_id}` | memory / Delete Entry | path:layer*, path:key*, path:entry_id* | — | 200, 422 | `delete_entry_api_memory_doc__layer___key__entry__entry_id__delete` |
| GET | `/api/memory/doc/{layer}/{key}/lines` | memory / Get Doc Lines | path:layer*, path:key* | — | 200, 422 | `get_doc_lines_api_memory_doc__layer___key__lines_get` |
| POST | `/api/memory/doc/{layer}/{key}/reset` | memory / Reset Doc | path:layer*, path:key* | — | 200, 422 | `reset_doc_api_memory_doc__layer___key__reset_post` |