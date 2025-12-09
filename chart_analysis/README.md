# 谱面可视化分析（外包模块）

目标：对谱面进行统计与可视化，产出密度、不同音符数量等图表。

建议职责：
- 解析输入谱面（复用 `chart/chart_engine.py` 的统一谱面模型）。
- 计算指标：总体密度、按时间分段的密度曲线、各音符类型数量/占比、BPM/节奏分布等。
- 导出结果：图表（PNG/SVG）、统计 JSON、可选 HTML 报告。
- 提供 CLI：输入谱面路径，输出统计图与报告文件。

输出协议（建议）：
- 输出目录：`chart_analysis/outputs/`
- 协议描述 JSON：`chart_analysis/outputs/protocol.json`，列出每个曲目的图表与数据文件路径。当前附带 `_dummy` 占位示例（纯占位，请替换为真实分析产物）。
- 基础占位（最低实现）：`<曲目名>_dummy.png`，供前端检测路径与加载逻辑。
- 完整命名建议（以谱面名为前缀，使用谱面文件夹名或 txt 主文件名）：
  - `<曲目名>_note_count.png`：各音符类型数量/占比柱状图
  - `<曲目名>_note_density.png`：时间轴密度曲线（可按秒/小节汇总）
  - `<曲目名>_bpm_curve.png`：BPM/节奏随时间分布（如有变速）
  - `<曲目名>_summary.json`：结构化统计（总时长、BPM、音符数量、密度分布摘要等）
- 前端可直接读取协议 JSON 获取文件清单，再去 `../chart_analysis/outputs/` 读取对应 PNG/JSON。

占位文件：
- `analyze.py`：入口脚本，调用解析/统计/绘图。
- `requirements.txt`：后续可加入 matplotlib/plotly 等依赖。

注意：本模块独立开发，不改动 Verilog/Quartus，仅消费谱面文本或统一谱面模型。
