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

虚实对齐图仅在顶部标注三列：真实采集 RGB、Isaac Sim 仿真画面和 50% 叠加对齐结果；图中不再显示相机英文名与中文视角标签。

主页的“Isaac Sim 房间全景（4K）”现使用 `assets/images/isaacsim-room-wide.jpg`。2026-10-23 重新启动 Isaac Sim，通过 `OfficeEnv(pose="tabletop")` 加载采集使用的 `office_sim/scenes/office_task.usda`，在房间内设置广角视角并直接保存 RTX 相机图像，分辨率 3840×2160。源图为 `office_sim/reports/homepage_room_actual_20261023/room_front.png`，拍摄参数见同目录 `capture.json`。这是当前场景重新运行的画面，不是历史采集过程中的某一帧，也不是录像截帧。此前 `reconstruction.jpg` 来自 Blender 的 `Final_Overview.png`，曾被误标为 Isaac Sim 全景，现已撤下该链接。

## 校徽

来自学校官网的校名组合标识，裁出左侧校徽，按透明度生成单色显示版本。页面只显示校徽与专业，不使用横向校名字标。

- 清华大学：https://www.tsinghua.edu.cn/image/logo180.png （裁切左侧 58×58，紫色显示）
- 哈尔滨工业大学（深圳）：https://www.hitsz.edu.cn/_upload/tpl/00/0d/13/template13/images/logo.png （裁切左侧 78×67，蓝色显示）

原始素材保留为 `assets/schools/*-source.png`。学历依据用户提供的简历。

## 视频处理

原始视频未修改，网页副本使用 H.264 / yuv420p，并统一采用 faststart 容器、约 2 秒关键帧间隔和较低峰值码率，以便 GitHub Pages 在普通网络下更快起播和拖动。七段视频配以已发表纯音乐，SmolVLA 与 π0.5 仿真演示共用曲目，音轨为 AAC；优化保留画面分辨率、帧率、时长和音乐内容。音乐响度目标为 -23 LUFS，淡入 0.8 秒、淡出 1.5 秒。两段真机现场音轨已替换。SO-101 使用首个成功回合（250 帧，30 FPS，约 8.33 秒）。具体映射见 `media-sources.json`，编码前后大小见 `video-optimization.json`。

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


对照图标注简化：基于 `office_sim/reports/openarmx_n_replay_verified/sample_000002/comparison.jpg` 重建，仅第 1–3 格显示列标题；已删除所有相机英文名与中文视角标签、各格中英副标题和底部重复说明。


## 2026-11-12 π0.5 仿真到真机对比

项目 02 的策略验证之后新增第 05 步“真机迁移”，卡片左侧为两个并排的竖屏视频，右侧为共用的三四行说明；手机上说明移至视频下方，视频仍保持左右顺序。训练数据设置及原片对应关系由用户确认：

| 位置 | 训练数据 | 原始视频 | 网页副本 |
| --- | --- | --- | --- |
| 左 | 50 条仿真示范，未加入真实示范训练 | `1eebe273096454571df314e5fdc6e738.mp4`（27.2 秒） | `assets/media/pi05-real-sim50.mp4` |
| 右 | 50 条仿真示范 + 5 条真实示范 | `ee7b631bd9d1b24fb93f607dde0e17d7.mp4`（约 35.83 秒） | `assets/media/pi05-real-sim50-real5.mp4` |

两段都是 π0.5 checkpoint 的 OpenArmX 真机部署录像。文案介绍数据设置及香蕉、抽屉交互的观察重点，不据单段录像宣称成功率提升，也不补充未提供的训练轮数、微调方式或数据混合比例。历史叙事中未完成严格 sim-to-real 成功率验证的说明仍适用。

原始文件保留在项目根目录。网页副本将 H.265 转为兼容浏览器的 H.264 / yuv420p，使用 CRF 25、60 帧关键帧上限和 MP4 faststart；保留 720×1280 分辨率、30 FPS、完整时长；原现场音轨已按用户要求替换为轻松愉快的 Carefree（Kevin MacLeod，CC BY 4.0）。封面取自各段第 2 秒画面，保存到 `assets/posters/`。播放器沿用原有按需加载和单视频播放逻辑。


### 两段真机对比的配乐

两段网页副本均从 `assets/music/licensed/Carefree.mp3` 的第 8 秒开始取完整视频时长的片段，完全去掉原现场音轨。配乐在淡入淡出前归一化至 -23 LUFS，淡入 0.8 秒、淡出 1.5 秒，编码为 AAC 双声道 64 kbps / 48 kHz；视频流直接复制，画面、帧率和时长不变。曲目、来源及 CC BY 4.0 署名已补到 `music-credits.json` 与页面页脚的“音乐鸣谢”。网页媒体地址更新版本参数，以便刷新后载入新配乐。

替换前的网页副本备份位于 `../personal-homepage-media-backups/before-music-20261112/`，根目录两段原片保留。


### 两段对比的表情标记

用户确认左侧片段效果不好、右侧片段效果较好。据此，在左侧视频画面右上角嵌入 😢 哭脸，右侧同位置嵌入 😊 笑脸，封面同步更新。表情使用本机 Noto Color Emoji 字体生成，源 PNG 保存在 `assets/overlays/`；标记为 136×136 像素，距右边与上边各 20 像素，附半透明深色底以保持可见。

表情直接编码进视频，全屏与下载后也可见；两段保持原分辨率、帧率、帧数和时长，Carefree 音轨直接复制并校验哈希一致。标记仅表达用户对这两段录像的定性评价，不表示系统评测的成功率。修改前的带配乐版本备份在 `../personal-homepage-media-backups/before-emotions-20261112/`。
