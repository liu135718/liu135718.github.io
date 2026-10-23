# 内容与素材依据

## 项目范围

按桌面实际工作归纳项目，第三方框架源码、虚拟环境、SDK 与重复备份不单列为原创项目。

| 页面内容 | 桌面来源 | 表述边界 |
| --- | --- | --- |
| 真机 RTC 对照 | 微信视频2026-10-22_180134_767.mp4 | 模型与训练条件取视频内字幕，不据此宣称成功率提升 |
| π0.5 真机长程任务 | 微信视频2026-10-22_180141_575.mp4 | 用户于 2026-10-22 确认：π0.5 经 LoRA 微调 20 轮后的执行结果 |
| 办公室重建与仿真 | office_reconstruction/README_重建说明.md、office_sim/README.md | 照片近似重建，不声称精确数字孪生 |
| SmolVLA / π0.5 | office_sim/SMOLVLA_ROLLOUT.md、PI05_ROLLOUT.md 与 reports 下实际录像 | 模型闭环运行，任务成功率尚未系统评估 |
| VR 与数据采集 | office_sim/VR_SIM.md、VR_DATASET.md、datasets/lerobot/banana_vr_002 | 画面是数据集机身相机，非头显操作录像 |
| SO-101 实验 | so101-lab/docs/workflow/reproduction_local_zh.md、outputs/reproduction/ | 页面表述为策略实验；素材来自本机新录制 ACT 成功回合，底层项目来源仍见本文件记录，不使用上游演示或成功率作为个人结果 |
| PPO 学习 | sb3-learning-lab/README.md、runs/ppo_baseline_seed0 | 行为视频仅展示一个初始条件；不外推多 seed 结论 |
| 虚实画面对齐 | office_sim/STATE_RGB_REPLAY.md、reports/openarmx_n_replay_verified | 图像对照与姿态重放，不声称标定已完全准确 |
| OpenArmX 系统链路 | OpenArmX_采集训练云端推理全流程.md、openarmx-lerobot/lerobot/examples/README_openarmx_pi05.md、openarmx_ws | 描述接口适配与部署实践，不将整个上游仓库作为独立原创成果 |
| 模型与 RL 源码学习 | my-help/*.md、sb3-learning-lab/阶段*学习详解.md | 学习与实现分析，不等同于提出算法 |
| 半自动抓取 | semi_auto_match_26/scripts/grasp.py、teleop.py | 依据已有代码描述练习内容，未补造实测结果 |

## 校徽

来自学校官网的校名组合标识，裁出左侧校徽，按透明度生成单色显示版本。页面只显示校徽与专业，不使用横向校名字标。

- 清华大学：https://www.tsinghua.edu.cn/image/logo180.png （裁切左侧 58×58，紫色显示）
- 哈尔滨工业大学（深圳）：https://www.hitsz.edu.cn/_upload/tpl/00/0d/13/template13/images/logo.png （裁切左侧 78×67，蓝色显示）

原始素材保留为 `assets/schools/*-source.png`。学历依据用户提供的简历。

## 视频处理

原始视频未修改。网页副本使用 H.264 / yuv420p，七段视频配以已发表纯音乐，SmolVLA 与 π0.5 仿真演示共用曲目，音轨为 AAC。换配乐时直接复制视频流，保留画面与时长；音乐响度目标为 -23 LUFS，淡入 0.8 秒、淡出 1.5 秒。两段真机现场音轨已替换。SO-101 使用首个成功回合（250 帧，30 FPS，约 8.33 秒）。具体映射见 `media-sources.json`。

## 2026-10-22 视频更新

原 ACT 网页节选来自只保存失败回合的评测视频，已替换为新运行 `homepage_act_selection_20261022` 的成功回合。对应模型 `outputs/act_easy_s42/best`、任务 `figure_shape_placement_easy`；成功由环境任务判据记录，并核对了视频动作。该片段仅展示一个成功案例，不代表总体成功率。

本地预览改用 `python3 serve.py`，支持 HTTP 206 / Range，以便前后跳转视频。

## 项目叙事调整

将 OpenArmX 真机系统、OpenArmX 仿真平台与 SO-101 策略实验作为三个项目章节。平台内部按场景 → 对齐 → 采集 → 策略验证排列；这是讲述顺序，不暗示各策略已完成严格 sim-to-real 成功率验证。Pendulum 演示从主页移除，学习文件保留。

## 历史：2026-10-23 恢复原声（后续已替换）

`real-rtc.mp4` 与 `real-arm.mp4` 从对应原片直接复用 AAC 音轨，视频流保持不变。网页媒体地址加入版本参数，避免沿用旧的无声缓存。其余在用仿真视频的原文件均无音轨。

## 历史：2026-10-23 统一配乐（已停用）

所有页面中展示的视频（OpenArmX 真机、RTC 对照、办公室漫游、VR 数据、SmolVLA、π0.5、SO-101 ACT 成功回合）统一换成 `assets/music/robot-demo-theme.mp3` 原创轻音乐，播放器仍可单独调整音量或静音。编码后均包含 AAC 音轨；原仿真录像没有现场原声，真机两段原声替换为配乐。


## 当前配乐：不同的已发表作品

曲目均为 Kevin MacLeod（incompetech.com）的作品；其中 SmolVLA 与 π0.5 仿真演示共用 Montauk Point，其余各段使用不同曲目，按官方曲目页的 CC BY 4.0 授权使用。署名及来源统一置于页脚链接的 `music-credits.html`，视频旁不显示音乐信息。完整来源、下载地址、文件校验值与截取起点见 `music-credits.json`。全部做了节选、响度调整及淡入淡出。

| 视频 | 曲目 | 官方来源 |
| --- | --- | --- |
| π0.5 真机长程任务 | Inspired | [官方曲目页](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1600022) |
| SmolVLA 真机 RTC 对照 | Easy Lemon | [官方曲目页](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1200076) |
| 办公室仿真场景漫游 | Dream Culture | [官方曲目页](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1300046) |
| VR 示范数据 | Life of Riley | [官方曲目页](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1400054) |
| SmolVLA 仿真运行 | Montauk Point | [官方曲目页](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1400013) |
| π0.5 仿真运行 | Montauk Point（与 SmolVLA 仿真演示相同） | [官方曲目页](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1400013) |
| SO-101 ACT 成功回合 | Carefree | [官方曲目页](https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1400037) |


主页 π0.5 演示改用 `office_sim/reports/my_pi05_127s/episode_000_observer.mp4` 的完整约 20.8 秒观察视角片段，保留原始画面并加配乐；与 SmolVLA 仿真视频均使用 Montauk Point。该次 rollout 在键盘中断时保存，片段按其呈现作演示，不标注为成功结果。
