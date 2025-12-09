"""
Python 谱面后端单文件骨架。
职责涵盖：通用谱面读取、随机谱面生成、ROM 输出、顶层 BPM 更新，以及 CLI 编排。
"""


def load_chart(path):
    """
    TODO:
    - 解析通用 TXT 谱面（兼容 Cthugha 等格式）
    - 归一化时间轴与事件列表，形成统一谱面模型
    """
    raise NotImplementedError("谱面读取尚未实现。")


def generate_random(seed, bpm, length_seconds):
    """
    TODO:
    - 基于 seed 构造可复现的伪随机谱面
    - 输出与 ROM 生成兼容的谱面模型
    """
    raise NotImplementedError("随机谱面生成尚未实现。")


def build_rom(chart_model, output_path):
    """
    TODO:
    - 将谱面模型映射为 ROM 地址/数据
    - 生成 Verilog `ROM.v` 写入 output_path
    """
    raise NotImplementedError("ROM 生成尚未实现。")


def update_top_bpm(top_file_path, bpm_value):
    """
    TODO:
    - 定位 HDL 顶层（如 MuseDash.v）中的 BPM 定义
    - 安全替换为新 BPM，并可选生成备份
    """
    raise NotImplementedError("BPM 更新尚未实现。")


def main():
    """
    TODO:
    - 解析 CLI 参数：模式（random/file）、输入路径/seed、BPM/时长、输出目录等
    - 串联：load_chart 或 generate_random -> build_rom -> update_top_bpm
    """
    raise NotImplementedError("CLI 尚未实现。")


if __name__ == "__main__":
    main()
