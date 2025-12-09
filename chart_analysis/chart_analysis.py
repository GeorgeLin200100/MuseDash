"""
谱面分析与可视化占位脚本。
职责：读取谱面 -> 计算统计 -> 生成图表/报告 -> 写出协议 JSON。
"""

from pathlib import Path
import json


def parse_chart(path):
    """
    TODO:
    - 复用 chart/chart_engine.py 的加载器，得到统一谱面模型
    """
    raise NotImplementedError("谱面解析尚未实现。")


def compute_metrics(chart_model):
    """
    TODO:
    - 计算密度曲线、音符类型数量/占比、BPM/节奏分布等
    - 返回结构化统计结果
    """
    raise NotImplementedError("统计计算尚未实现。")


def render_outputs(metrics, output_dir, chart_name):
    """
    TODO:
    - 根据 metrics 绘制图表（PNG/SVG），命名示例：
      * <曲目名>_note_count.png：音符类型计数/占比
      * <曲目名>_note_density.png：时间轴密度曲线
      * <曲目名>_bpm_curve.png：BPM/节奏分布
    - 导出 JSON/HTML 报告：
      * <曲目名>_summary.json：含总时长、BPM、音符计数、密度摘要等
    - 返回生成的文件名列表（相对 output_dir）
    """
    raise NotImplementedError("可视化与导出尚未实现。")


def write_protocol(entries, output_dir):
    """
    将分析产物列表写入协议 JSON。
    entries: 列表，元素形如
      {
        "name": "曲目名",
        "files": ["<曲目名>_note_count.png", ...],
        "summary": "<曲目名>_summary.json",
        "bpm": 170,
        "duration": "02:10",
        "folder": "charts/<曲目名>"
      }
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    protocol_path = output_dir / "protocol.json"
    payload = {
        "version": 1,
        "note": "占位协议示例；实际请生成真实图表和 summary。",
        "charts": entries,
    }
    protocol_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return protocol_path


def generate_dummy_protocol(chart_names, output_dir):
    """
    生成仅包含 *_dummy.png 的占位协议，供前端调试路径。
    chart_names: 可迭代的曲目名列表
    """
    entries = []
    for name in chart_names:
        entries.append(
            {
                "name": name,
                "files": [f"{name}_dummy.png"],
                "summary": f"{name}_summary.json",
                "bpm": None,
                "duration": None,
                "folder": f"charts/{name}",
            }
        )
    return write_protocol(entries, output_dir)


def main():
    """
    TODO:
    - 参数：谱面路径/目录、输出目录
    - 串联 parse_chart -> compute_metrics -> render_outputs -> write_protocol
    - 暂可调用 generate_dummy_protocol 输出占位协议
    """
    raise NotImplementedError("CLI 尚未实现。")


if __name__ == "__main__":
    main()
