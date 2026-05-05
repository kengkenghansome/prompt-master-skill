---
name: prompt-master-skill
description: 根据用户提供的创意、主题或任务，自动生成适用于视频生成、图片生成或文本生成的高质量结构化 Prompt。适用于 AI 视频、AI 图片、文本写作、报告、文案、PPT 内容、邮件、脚本等场景。
---

# Prompt Master Skill

## Overview

This skill helps the agent transform a user's rough idea, topic, material, or task into a structured, high-quality prompt.

It supports three major prompt types:

1. Video generation prompts
2. Image generation prompts
3. Text generation prompts

The core principle is:

- Video prompt = director thinking
- Image prompt = photographer / visual designer thinking
- Text prompt = professional executor thinking

The final prompt should be clear, structured, reusable, and directly usable in AI tools.

---

## When to use

Use this skill when the user asks to:

- 生成提示词
- 优化提示词
- 扩写 Prompt
- 制作 Prompt 模板
- 把创意变成视频生成提示词
- 把图片想法变成图片生成提示词
- 把写作任务变成文本生成提示词
- 设计 prompt skill
- 生成适合 AI 视频、AI 图片、AI 写作工具使用的结构化提示词

Examples:

- “帮我把这个想法扩写成视频生成 Prompt”
- “给我一个图片生成强化 Prompt”
- “我想让 AI 帮我写管理层日报，Prompt 怎么写？”
- “基于这个主题生成可直接复制的 Prompt”
- “把我的需求改成专业 Prompt”

---

## Core workflow

When using this skill, follow this workflow:

1. Identify the user's raw input.
2. Determine the task type:
   - video generation
   - image generation
   - text generation
   - mixed / uncertain
3. Select the corresponding prompt framework.
4. Expand the user's rough idea into a structured prompt.
5. Add professional details:
   - for video: camera, motion, timing, rhythm, continuity
   - for image: subject, scene, composition, lighting, texture, negative prompt
   - for text: role, background, task, audience, structure, tone, constraints
6. Add quality standards and limitations.
7. Output a final copy-ready prompt.
8. If useful, provide structure breakdown and optional optimization suggestions.

---

## Reference files

Use the following references when needed:

- Video prompt framework:
  `{baseDir}/references/video-prompt-framework.md`

- Image prompt framework:
  `{baseDir}/references/image-prompt-framework.md`

- Text prompt framework:
  `{baseDir}/references/text-prompt-framework.md`

- Output template:
  `{baseDir}/assets/prompt-output-template.md`

If the task is simple, do not over-read all references. Only load the relevant reference file.

---

## Optional script

A helper script is available at:

`{baseDir}/scripts/prompt_builder.py`

Use it only when a structured prompt needs to be generated from command-line input or when batch processing multiple prompt requests.

Do not use the script if normal reasoning is enough.

---

## Task type detection rules

### Video generation

Classify as video generation if the user mentions:

- 视频
- 短视频
- 分镜
- 镜头
- 运镜
- 电影感
- Sora
- Runway
- Kling
- Pika
- Veo
- 生成视频
- 多少秒视频

Video prompt focus:

- film style
- subject
- scene
- plot / action
- camera language
- motion
- rhythm
- atmosphere
- visual details
- negative prompt

---

### Image generation

Classify as image generation if the user mentions:

- 图片
- 海报
- 照片
- 插画
- 视觉图
- Midjourney
- Stable Diffusion
- DALL·E
- 生成图
- 摄影
- 构图
- 光线
- 质感

Image prompt focus:

- subject
- scene
- action / relationship
- composition
- lighting
- mood
- style / medium
- texture
- camera parameters
- negative prompt

---

### Text generation

Classify as text generation if the user mentions:

- 文案
- 报告
- 总结
- 邮件
- 脚本
- PPT
- 文章
- 笔记
- 翻译
- 分析
- 方案
- 说明
- 提纲
- 写作

Text prompt focus:

- role
- background
- task objective
- audience
- content scope
- output structure
- tone
- constraints
- quality standards

---

## General prompt formula

Use this universal formula when the task type is unclear:

目标 + 角色 + 背景 + 受众 + 内容 + 结构 + 风格 + 限制 + 标准

In English:

Goal + Role + Background + Audience + Content + Structure + Style + Constraints + Quality Standards

---

## Output format

Unless the user asks otherwise, output in this format:

### 1. 优化后的最终 Prompt

Provide a complete, copy-ready prompt.

### 2. 结构拆解

Explain what each part of the prompt controls.

### 3. 可继续优化方向

Tell the user what extra information can improve the result.

If the user says “只要最终 Prompt”, only output the final prompt.

If the user says “要模板”, output a reusable template with placeholders.

If the user says “要一比一直译”, do not rewrite meaning; translate directly.

---

## Video prompt generation rules

When generating a video prompt, use director thinking.

Required structure:

1. 影片风格
2. 主体设定
3. 场景设定
4. 情节动作
5. 镜头语言
6. 节奏控制
7. 氛围情绪
8. 细节强化
9. 负面提示词

Quality requirements:

- The video should not feel like static images stitched together.
- The action must be clear.
- The camera movement must be explicit.
- The timeline should fit the requested duration.
- The visual continuity should be maintained.
- Avoid vague adjective stacking.

---

## Image prompt generation rules

When generating an image prompt, use photographer and visual designer thinking.

Required structure:

1. 主体
2. 场景
3. 动作 / 关系
4. 构图
5. 光线
6. 情绪
7. 风格 / 媒介
8. 质感细节
9. 镜头参数
10. 负面提示词

Quality requirements:

- The subject must be clear.
- The composition must be controllable.
- The lighting should match the mood.
- The style should be unified.
- Texture and details should be specific.
- Negative prompts should reduce common AI image errors.

---

## Text prompt generation rules

When generating a text prompt, use professional executor thinking.

Required structure:

1. 角色身份
2. 背景信息
3. 任务目标
4. 目标受众
5. 内容要求
6. 输出结构
7. 风格语气
8. 限制条件
9. 质量标准

Quality requirements:

- The prompt should tell the AI who it is acting as.
- The task should be specific.
- The audience should be clear.
- The output structure should be defined.
- The style and tone should be controlled.
- The restrictions should prevent hallucination or unsuitable output.

---

## Safety and accuracy rules

For factual, financial, legal, medical, policy, news, or data-related prompts:

- Do not invent facts.
- Do not invent sources.
- Ask the model to state uncertainty when information is insufficient.
- Require citations or source verification when needed.
- Require the model to distinguish between facts, assumptions, and suggestions.

For image or video prompts:

- Avoid generating unsafe, illegal, or harmful content.
- Avoid prompts involving impersonation, explicit sexual content, or harmful deception.
- If the user asks for realistic document fraud, fake evidence, or deceptive images, refuse and redirect to safe alternatives.

---

## Prompt quality checklist

Before final output, check:

- Is the task type clear?
- Is the role defined?
- Is the target audience defined?
- Is the output structure clear?
- Are style and tone controlled?
- Are constraints included?
- Are quality standards included?
- Is the final prompt directly copyable?
- Is the prompt too vague?
- Is the prompt overloaded with meaningless adjectives?

A strong prompt is not necessarily long. It is clear, structured, bounded, and usable.
