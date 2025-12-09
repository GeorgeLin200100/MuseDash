# Chart 后端（Python 优先）

本目录已重构为 Python 主流程，旧的 C++ 流程仅保留参考。

## 目录说明
- `chart_engine.py`：Python 单文件骨架，负责读取通用谱面 TXT（兼容 Cthugha 等格式）、随机谱面生成、输出 `ROM.v`，并更新顶层 BPM。
- `samples/`：示例谱面 TXT，用于测试加载与生成逻辑。
- `outputs/`：生成的 HDL 产物存放处（如 `ROM.v`）。
- `legacy_cpp/`：原始 C++ 流程，保留不动作为参考。

## 后续工作
1) 在 `chart_engine.py` 中实现通用谱面解析（事件与节奏结构）。
2) 在同文件实现随机谱面生成与普通文件加载两种模式。
3) 在同文件实现将谱面模型转为 `ROM.v`。
4) 在同文件实现 FPGA 顶层文件的 BPM 更新。
5) 在同文件内完成 CLI：随机模式与普通模式均可一键输出 `ROM.v` 并更新 BPM。
