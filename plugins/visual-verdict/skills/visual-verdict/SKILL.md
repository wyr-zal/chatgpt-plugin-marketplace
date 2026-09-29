---
name: visual-verdict
description: "视觉 QA — 对比生成截图与参考图，输出结构化 JSON 评分（90+ 通过），驱动迭代修改"
argument-hint: "<reference_image> <generated_screenshot> [category_hint]"
---

<Purpose>
对比生成的 UI 截图与参考图片，返回结构化 JSON verdict，驱动下一轮代码修改。
</Purpose>

<Use_When>
- 任务有视觉还原要求（布局、间距、字体、组件样式）
- 有当前生成截图和至少一张参考图
- 需要确定性的 pass/fail 判断
</Use_When>

<Inputs>
- `reference_images[]`: 一张或多张参考图片路径
- `generated_screenshot`: 当前产出截图
- 可选 `category_hint`: 如 dashboard, sns-feed, landing-page
</Inputs>

<Steps>

## Step 1: 读取图片

用 Read 工具读取参考图和生成截图（Claude Code 支持读取图片文件）。

## Step 2: 逐维度对比

对比以下维度：
- **Layout**: 整体布局结构是否一致
- **Spacing**: 间距、padding、margin 是否匹配
- **Typography**: 字体、字号、字重、行高
- **Colors**: 配色方案是否一致
- **Components**: 组件样式是否匹配
- **Hierarchy**: 视觉层级是否正确

## Step 3: 输出 JSON Verdict

必须只返回以下格式的 JSON：

```json
{
  "score": 0,
  "verdict": "revise",
  "category_match": false,
  "differences": ["具体视觉差异1", "具体视觉差异2"],
  "suggestions": ["可执行的修改建议1", "可执行的修改建议2"],
  "reasoning": "1-2 句总结"
}
```

字段规则：
- `score`: 0-100 整数
- `verdict`: `pass`（90+）、`revise`（60-89）、`fail`（<60）
- `category_match`: 是否符合目标 UI 类型
- `differences[]`: 具体视觉差异
- `suggestions[]`: 与差异对应的修改建议
- `reasoning`: 简短总结

## Step 4: 迭代规则

- 通过阈值: **90 分以上**
- score < 90 时，继续修改代码并重新运行 /visual-verdict
- 每次迭代只修 priority_fixes 中的问题

</Steps>

Task: {{ARGUMENTS}}