#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
prompt_builder.py

A simple local helper script for generating structured prompt templates
for video, image, and text generation tasks.

Usage examples:

python prompt_builder.py --type video --idea "一个机器人在未来城市雨夜中独自行走" --duration 8
python prompt_builder.py --type image --idea "高级感护肤品海报"
python prompt_builder.py --type text --idea "写一份管理层日报"
"""

import argparse
from textwrap import dedent


def build_video_prompt(idea: str, duration: str = "10") -> str:
    return dedent(f"""
    请基于，生成一份适用于秒短视频的结构化视频生成 Prompt。

    请按照以下结构输出：

    影片风格：
    整体视觉风格、参考类型、影像质感。

    主体设定：
    主要人物、物体、角色或产品的外观、状态、特征。

    场景设定：
    时间、地点、环境、背景元素、空间氛围。

    情节动作：
    视频中发生什么，动作如何开始、推进和结束。

    镜头语言：
    景别、机位、镜头运动、推拉摇移、跟拍、特写、转场方式。

    节奏控制：
    开头、中段、结尾的节奏变化，适合 {duration} 秒短视频。

    氛围情绪：
    整体情绪、色彩倾向、音乐感、声音感。

    细节强化：
    材质、光影、天气、人物表情、环境动态、产品细节。

    负面提示词：
    不要出现的画面、风格、错误元素或不合理动作。

    要求：
    - 画面要有连续性
    - 动作要明确
    - 镜头要有变化
    - 不要像静态图片拼接
    - 适合直接复制到视频生成模型中使用
    """).strip()


def build_image_prompt(idea: str) -> str:
    return dedent(f"""
    请基于，生成一份适用于 AI 图片生成的强化 Prompt。

    请按照以下结构输出：

    主体：
    画面中的核心人物、产品、物体、动物或角色。

    场景：
    地点、时间、背景、环境元素。

    动作 / 关系：
    主体正在做什么，与其他元素有什么关系。

    构图：
    近景、中景、远景、俯拍、仰拍、对称构图、三分法、中心构图等。

    光线：
    自然光、柔光、逆光、电影光、霓虹光、伦勃朗光、棚拍光等。

    情绪：
    温暖、孤独、高级、清冷、梦幻、紧张、治愈等。

    风格 / 媒介：
    写实摄影、电影海报、商业摄影、油画、3D 渲染、插画、赛博朋克等。

    质感细节：
    皮肤、布料、金属、玻璃、塑料、空气感、颗粒感、景深、反光等。

    镜头参数：
    焦段、光圈、景深、画幅比例、清晰度，可选。

    负面提示词：
    畸形手指、模糊脸部、多余肢体、乱码文字、低清晰度、过度锐化等。

    要求：
    - 主体清晰
    - 画面重点明确
    - 风格统一
    - 细节具体但不要堆砌
    - 适合直接复制到图片生成模型中使用
    """).strip()


def build_text_prompt(idea: str) -> str:
    return dedent(f"""
    请你以【专业执行者】的身份，基于以下背景信息，完成。

    背景信息：
    【请补充任务背景、已有材料、上下文或参考信息】

    任务目标：
    【说明希望文本达到什么效果】

    目标受众：
    【说明写给谁看】

    内容要求：
    1. 必须包含【必要信息】
    2. 重点突出【重点内容】
    3. 简化【复杂内容】
    4. 避免【不适合内容】

    输出结构：
    请按照以下格式输出：
    1. 标题
    2. 核心结论
    3. 正文内容
    4. 重点摘要
    5. 后续建议 / 可选补充

    风格语气：
    【正式 / 商务 / 口语 / 深刻 / 简洁 / 管理层汇报 / 小红书风格 / 技术文档风格】

    限制条件：
    - 字数控制在【XX】字以内
    - 不要编造数据
    - 不要过度解释
    - 不要使用【XX】表达
    - 语言要适合【具体场景】

    质量标准：
    - 逻辑清晰
    - 重点突出
    - 可直接复制使用
    - 符合目标受众阅读习惯
    """).strip()


def main():
    parser = argparse.ArgumentParser(
        description="Generate structured prompt templates for video, image, or text generation."
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["video", "image", "text"],
        help="Prompt type: video, image, or text."
    )

    parser.add_argument(
        "--idea",
        required=True,
        help="The raw idea, topic, or task."
    )

    parser.add_argument(
        "--duration",
        default="10",
        help="Video duration in seconds. Only used for video prompts."
    )

    args = parser.parse_args()

    if args.type == "video":
        output = build_video_prompt(args.idea, args.duration)
    elif args.type == "image":
        output = build_image_prompt(args.idea)
    else:
        output = build_text_prompt(args.idea)

    print(output)


if __name__ == "__main__":
    main()