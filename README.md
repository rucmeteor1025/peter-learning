# 🐻 Peter 学习空间

给 Peter（一年级 → 二年级）的私人学习小站，纯静态、无后端，托管于 GitHub Pages。

## 站点内容

| 入口 | 说明 |
|---|---|
| `index.html` | 门户首页（含连续打卡显示） |
| `static/app.html` | 每日练习 App：语文 / 英语 / 围棋，每天 10 题选择题，成绩存 localStorage |
| `data/` | 练习题库（`chinese.json` / `english.json` / `go.json`） |
| `graphs/` | 知识图谱（Three.js 3D 交互，自包含单文件）：暑假版 / 一年级下学期版 |

## 本地运行

```bash
cd ~/AI_invest/生活助理/Peter学习
python3 server.py          # http://localhost:8765
```

或用任意静态服务器打开本仓库根目录。

## 更新流程

业务源在 `~/AI_invest/生活助理/Peter学习/`（含 `build_summer_graph.py` 图谱构建脚本）。
改完源后同步到此部署仓库并推送：

```bash
cd ~/peter-learning
# 重新拷贝 index.html / static / data / graphs
git add -A && git commit -m "..." && git push
```

图谱重新生成：`python3 build_summer_graph.py`（输出到桌面 📁Peter教育，再拷入 `graphs/`）。

## 数据说明

- 进度、错题、打卡均存浏览器 localStorage（本机隐私，不传服务器）
- 语音朗读使用浏览器自带 TTS（Web Speech API），无需联网密钥
