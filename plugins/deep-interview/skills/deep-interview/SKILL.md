---
name: deep-interview
description: "苏格拉底式深度需求访谈 — 用量化歧义度评分把模糊想法压成可执行规格，在动手写代码之前先把需求问透"
argument-hint: "[--quick|--standard|--deep] <想法或模糊描述>"
---

<Purpose>
Deep Interview 是一个意图优先的苏格拉底式澄清循环，在规划或实现之前运行。它通过逐个追问，把模糊想法转化为可执行的规格文档：追问用户为什么要做这个改动、范围该到哪里、什么不该做、哪些决定可以由 AI 自主做。
</Purpose>

<Use_When>
- 请求范围大、描述模糊、缺少验收标准
- 用户说"别假设""多问我""把问题问清楚""深度访谈"
- 担心需求不清导致后续实现跑偏
- 需要先生成需求规格再进入实现
</Use_When>

<Do_Not_Use_When>
- 请求已有明确文件、符号目标和验收标准
- 用户明确说跳过访谈直接执行
- 只是轻量 brainstorm
- 已有完整 PRD 或计划文档
</Do_Not_Use_When>

<Depth_Profiles>
- **Quick (`--quick`)**: 快速澄清; 目标歧义度 `<= 0.30`; 最多 5 轮
- **Standard (默认)**: 完整需求访谈; 目标歧义度 `<= 0.20`; 最多 12 轮
- **Deep (`--deep`)**: 高严格度探索; 目标歧义度 `<= 0.15`; 最多 20 轮

未指定时使用 **Standard**。
</Depth_Profiles>

<Execution_Policy>
- 一轮只问一个问题，绝不批量提问
- 先问意图和边界，再问实现细节
- 每轮瞄准最弱的清晰度维度
- 对每个回答做压力测试：追问证据/例子、隐含假设、权衡边界、或从症状追到本质
- 当前线索还模糊时继续深挖，不要为覆盖面而浅尝辄止
- 代码库事实先自己用工具查，不要反问用户能查到的信息
- 每轮重新计算歧义度并透明展示
- 歧义高于阈值时不交给执行，除非用户明确接受风险
- Non-goals 和 Decision Boundaries 未明确前不结束，即使数值已达标
</Execution_Policy>

<Steps>

## Phase 0: 预检上下文

1. 解析 `{{ARGUMENTS}}`，提取深度档位和任务描述。
2. 用 Glob/Grep/Read 工具扫描当前项目，判断 **brownfield**（已有代码库）还是 **greenfield**。
3. 创建上下文快照，记录：任务陈述、期望结果、意图假设、已知事实、约束、未知项、可能的代码触点。
4. 将快照写入项目 `docs/interviews/{slug}-context.md`。

## Phase 1: 初始化

1. 确定深度档位（quick/standard/deep）和对应阈值、轮次上限。
2. 如果是 brownfield，先用 Read/Grep 收集相关代码上下文。
3. 初始化状态：
   - 当前歧义度: 1.0 (100%)
   - 各维度得分: 全部 0.0
   - 已用挑战模式: 无
4. 向用户宣布访谈开始，展示档位、阈值和当前歧义度。

## Phase 2: 苏格拉底式访谈循环

重复直到歧义度 <= 阈值且门槛条件满足，或用户退出，或达到轮次上限。

### 2a) 生成下一个问题
基于已有 Q&A、当前维度得分、代码上下文，瞄准最弱维度。

阶段优先级：
- **Stage 1 — 意图优先**: Intent, Outcome, Scope, Non-goals, Decision Boundaries
- **Stage 2 — 可行性**: Constraints, Success Criteria
- **Stage 3 — 代码库对齐**: Context Clarity (仅 brownfield)

压力阶梯（每个回答后）：
1. 追问具体例子、反例或证据
2. 探查隐含假设或依赖
3. 逼出边界或权衡：什么明确不做、推迟或拒绝？
4. 如果回答仍停留在症状层，重新框定到本质/根因

### 2b) 提问
使用 AskUserQuestion 工具，格式：

```
第 {n} 轮 | 目标维度: {weakest_dimension} | 歧义度: {score}%

{问题}
```

### 2c) 计算歧义度
对每个维度在 [0.0, 1.0] 范围评分。

Greenfield 公式:
`歧义度 = 1 - (intent×0.30 + outcome×0.25 + scope×0.20 + constraints×0.15 + success×0.10)`

Brownfield 公式:
`歧义度 = 1 - (intent×0.25 + outcome×0.20 + scope×0.20 + constraints×0.15 + success×0.10 + context×0.10)`

就绪门槛（即使数值达标也必须满足）：
- Non-goals 已明确
- Decision Boundaries 已明确
- 至少做过一次压力追问

### 2d) 展示进度
显示各维度得分表、就绪门槛状态、下一轮聚焦维度。

### 2e) 轮次控制
- 第 4 轮起允许用户提前退出（带风险警告）
- 档位中点时给出软提醒
- 达到轮次上限时强制结束并标注残余风险

## Phase 3: 挑战模式

每种模式最多使用一次：
- **Contrarian**（第 2 轮+）: 挑战核心假设
- **Simplifier**（第 4 轮+）: 压缩到最小可行范围
- **Ontologist**（第 5 轮+ 且歧义 > 0.25）: 追问本质，避免停留在症状层

歧义度连续 3 轮停滞（±0.05）时强制触发 Ontologist。

## Phase 4: 结晶化产物

当阈值达标（或用户退出/达到上限）：

1. 将访谈摘要写入 `docs/interviews/{slug}-transcript.md`
2. 将执行规格写入 `docs/interviews/{slug}-spec.md`

规格内容：
- 元数据（档位、轮次、最终歧义度、项目类型）
- 各维度清晰度评分表
- Intent（为什么要做）
- Desired Outcome（期望结果）
- In-Scope（范围内）
- Out-of-Scope / Non-goals（非目标）
- Decision Boundaries（AI 可自主决定 vs 必须回问的边界）
- Constraints（约束）
- 可测试的验收标准
- 暴露的假设及其解决状态
- 压力追问发现（哪个回答被深挖了，改变了什么）
- Brownfield 证据 vs 推断说明
- 完整或精简的访谈记录

## Phase 5: 执行桥接

访谈完成后，展示后续选项：

1. **进入计划模式（推荐）** — 用 EnterPlanMode 基于规格做架构规划
2. **直接执行** — 如果规格已足够清晰，直接开始实现
3. **继续深挖** — 重新进入访谈循环解决剩余模糊点

如果访谈是提前退出或带风险结束的，必须在交接时明确标注残余风险。

**重要：deep-interview 是需求模式，绝不在此模式内直接实现代码。**

</Steps>

<Escalation_And_Stop>
- 用户说停止/取消/中止 → 保存当前状态并停止
- 歧义度连续 3 轮停滞 → 强制 Ontologist 模式
- 达到轮次上限 → 带残余风险警告结束
- 所有维度 >= 0.9 → 允许提前结晶化
</Escalation_And_Stop>

<Final_Checklist>
- [ ] 上下文快照已创建
- [ ] 每轮都展示了歧义度
- [ ] 遵循了先意图后实现细节的顺序
- [ ] 至少做过一次显式假设追问
- [ ] 至少做过一次持续追问把之前的回答压得更实
- [ ] 挑战模式在适当时机触发
- [ ] 已生成访谈摘要和执行规格文档
- [ ] 已提供后续执行选项
- [ ] 在此模式内没有直接动手实现
</Final_Checklist>

Task: {{ARGUMENTS}}