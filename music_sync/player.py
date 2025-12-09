"""
音乐播放协同占位实现。
处理空格键触发播放，以及缺失音频时的节拍回退。
"""


def find_audio_for_chart(chart_path):
    """
    TODO:
    - 在 assets/ 或谱面同目录下查找同名音频
    - 支持常见扩展名（wav/mp3 等）
    """
    raise NotImplementedError("音频查找尚未实现。")


def play_audio_or_beat(audio_path):
    """
    TODO:
    - 若有音频文件则直接播放
    - 否则根据谱面 BPM 播放合成节拍/节拍器
    """
    raise NotImplementedError("播放逻辑尚未实现。")


def main():
    """
    TODO:
    - 最小 CLI：加载谱面，等待空格触发播放/暂停
    - 与谱面后端对接获取 BPM 以驱动节拍回退
    """
    raise NotImplementedError("音乐协同 CLI 尚未实现。")


if __name__ == "__main__":
    main()
