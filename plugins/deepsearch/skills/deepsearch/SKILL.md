---
name: deepsearch
description: "深度代码搜索 — 三阶段搜索（广搜→深挖→综合），全面追踪概念在代码库中的使用"
argument-hint: "<搜索关键词或概念>"
---

<Purpose>
对代码库做彻底搜索，追踪指定查询、模式或概念的所有使用位置和关联关系。
</Purpose>

<Use_When>
- 需要全面了解某个概念在代码库中的使用
- 简单 Grep 不够，需要追踪调用链和依赖关系
- 不熟悉代码库，需要快速建立全局理解
</Use_When>

<Steps>

## Phase 1: 广泛搜索

- 用 Grep 搜索精确匹配
- 搜索相关术语和变体（驼峰、蛇形、缩写等）
- 用 Glob 检查常见目录（components, utils, services, hooks, api, models 等）

## Phase 2: 深入追踪

- 用 Read 读取所有命中文件
- 检查 import/export 关系
- 顺着调用链追踪：谁在导入它？它又依赖了什么？
- 检查配置文件中的引用

## Phase 3: 归纳总结

输出格式：

### Primary Locations
核心实现所在位置（带 file:line）

### Related Files
相关文件，包括依赖方和调用方

### Usage Patterns
该能力在代码库中的使用方式

### Key Insights
关键模式、约定以及容易踩坑的点

</Steps>

全面但简洁，所有引用都带具体文件路径和行号。

Task: {{ARGUMENTS}}