# 具身智能项目主页 · 刘轩

中文项目主页，围绕 OpenArmX 真机系统、仿真与数据平台、SO-101 策略实验及演示结果组织内容。原初版保留在 `/tmp/homepage-v1/`（临时备份）。

## 查看

直接用浏览器打开 `index.html`，或运行：

```bash
cd /home/wxn/desktop/personal-homepage
python3 serve.py
```

访问 http://127.0.0.1:8080 。此预览服务支持 HTTP Range 分段读取，可拖动视频进度条。页面无需构建、无外部字体或运行时依赖，支持手机布局。

## 修改入口

- `index.html`：项目概览、作者信息与校徽、三个项目章节（真机系统、仿真平台、SO-101 策略实验）与笔记。
- `styles.css`：统一深色背景、高对比度文字、视频卡片及手机布局。
- `serve.py`：支持视频跳转播放的本地静态预览服务。
- `main.js`：按视口和用户操作预加载视频；首段真机演示提前缓冲，其他视频按需加载；播放新视频时暂停并取消其他视频的后台下载。
- `assets/media/`：页面使用 7 段经过流式播放优化的 H.264 MP4，保持原分辨率、帧率和时长；展示视频使用已发表纯音乐，SmolVLA 与 π0.5 仿真演示共用配乐，含淡入淡出，替换原现场声音；部分长数据录像取节选。
- `video-optimization.json`：记录视频编码、音频、faststart 容器和优化前后文件大小。
- `assets/posters/`：对应视频封面；视频点击后加载。
- `assets/images/`：场景重建、实机与仿真对照、PPO 曲线。
- `media-sources.json`：视频原始文件与节选记录。
- `CONTENT_SOURCES.md`：内容与校徽来源，方便后续维护。

发布地址：https://liu135718.github.io/ 。本地修改需推送并完成 GitHub Pages 部署后才会在线生效。页面以项目为主体，照片与校徽作为作者信息，页脚不再展示简历入口。

## 当前讲述顺序

1. OpenArmX 真机系统：工作台现场 → RTC 对照 → 数据、推理与执行工作。
2. OpenArmX 仿真平台：场景搭建 → 虚实对齐 → VR 示范采集 → SmolVLA / π0.5 策略验证。
3. SO-101 策略实验：成功演示 → 基线比较 → IQL / 采样器 / PPO 实验。
4. 支撑内容：源码笔记与早期 ROS 抓取实践。

摆杆演示已从页面移除，原始学习项目与媒体文件保留。

配乐为 Kevin MacLeod 已发表的轻音乐作品，采用 CC BY 4.0 授权。音乐原文件位于 `assets/music/licensed/`，曲目、来源、授权和处理记录见 `music-credits.json`。署名统一放在 `music-credits.html`，通过主页页脚的“音乐鸣谢”访问，视频旁不显示曲名或作者。配乐直接嵌入视频，已做响度调整与淡入淡出。旧合成配乐和 `make_music.py` 已停用。
