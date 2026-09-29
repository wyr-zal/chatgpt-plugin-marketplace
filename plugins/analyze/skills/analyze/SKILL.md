---
name: analyze
description: "证据驱动调查分析 — 用假设排名和证伪方法做根因分析，适合 bug/架构/性能问题的深度诊断"
argument-hint: "<问题描述或观察到的现象>"
---

<Purpose>
证据驱动的调查分析。解决的不是"改哪里"，而是"为什么会这样"。适合根因分析、架构调查、性能解释等需要跨文件推理的任务。
</Purpose>

<Use_When>
- 问题带因果性质："为什么会这样""什么导致了这个"
- 需要比较多个竞争性解释
- 需要跨多个文件/模块推理
- 运行时 bug、性能异常、架构分析、依赖影响评估
</Use_When>

<Do_Not_Use_When>
- 用户要直接改代码 — 直接改
- 用户要完整计划 — 用 /plan
- 单文件就能回答的简单问题 — 直接回答
</Do_Not_Use_When>

<Core_Contract>
始终区分以下内容，不能混在一起：

1. **Observation** — 实际观察到了什么
2. **Hypotheses** — 竞争性解释（至少 2-3 个）
3. **Evidence For** — 支持各解释的证据
4. **Evidence Against / Gaps** — 反驳或缺失的证据
5. **Current Best Explanation** — 当前最可信的解释
6. **Critical Unknown** — 最关键的未知事实
7. **Discriminating Probe** — 最值得做的下一步
</Core_Contract>

<Evidence_Hierarchy>
证据按强弱排序：
1. 可控复现、直接实验
2. 一手材料（日志、指标、配置、git 历史、具体代码行）
3. 多个独立来源共同指向同一解释
4. 单一来源的代码路径推理
5. 弱间接线索（时间巧合、命名相似）
6. 纯直觉或类比
</Evidence_Hierarchy>

<Falsification>
必须主动证伪自己最看好的解释：
- 既找支持证据，也找反对证据
- 写清它的独特预测
- 写清什么观察结果会和它冲突
- 找出区分它与次优解释的最便宜实验
</Falsification>

<Steps>

## Step 1: 明确观察结果
精确描述观察到的现象，不加解释。

## Step 2: 收集上下文
用 Read/Grep/Glob 工具收集相关代码、配置、日志。

## Step 3: 生成假设
提出至少 2-3 个竞争性解释，默认分三个方向：
- 代码路径/实现问题
- 配置/环境/编排问题
- 测量口径/假设偏差问题

## Step 4: 收集证据并证伪
对每个假设：
- 收集支持证据（带 file:line）
- 收集反对证据
- 评估证据强度

## Step 5: 输出结构化分析

```
### Observed Result
[观察到的现象]

### Ranked Hypotheses
| Rank | Hypothesis | Confidence | Evidence Strength |
|------|------------|------------|-------------------|
| 1 | ... | High/Medium/Low | Strong/Moderate/Weak |

### Evidence Summary
- Hypothesis 1: ...
- Hypothesis 2: ...

### Evidence Against / Missing
- Hypothesis 1: ...

### Most Likely Explanation
[当前最佳解释，带 file:line 引用]

### Critical Unknown
[最关键的未知事实]

### Recommended Next Step
[最值得做的下一步]
```

</Steps>

Task: {{ARGUMENTS}}