# FPGA 音乐游戏框架计划

## 当前仓库概览
- `verilog/`：MuseDash 的 FPGA RTL（顶层 `MuseDash.v`，ROM、按键去抖、判定/计分、数码管与 LCD 驱动等）。
- `chart/`：C++ 工具，读取 `input_example.txt`（首行 `bpm=xxx`，后续 `(pos,type,line)`），生成 `verilog/ROM.v` 并修改 `MuseDash.v` 的 `div_cnt`；附带示例可执行文件 `main`。
- `testbench/`：计分与判定的简单 Verilog testbench。
- `quartus/`：Quartus 工程（`MuseDash.qsf`），生成目录在 `.gitignore` 中已忽略。
- `HLS/`：若干 HLS 示例及 Windows `hls.exe`。
- `doc/`、`Figure/`、`video/`：文档、图示和演示视频。

## 想要的框架能力
- 接收外部谱面文件，做语法/语义校验，转换成 FPGA 可用的 ROM/初始化数据。
- 提供前端界面（Web/Electron/Qt 均可）：选谱面→查看解析结果→校验→一键生成并触发编译/烧录。
- 自动化 Quartus CLI 完成编译与烧录（如 `quartus_sh --flow compile MuseDash` + `quartus_pgm`，指定线缆/设备）。
- RTL 保持通用：谱面只通过外部数据文件注入，BPM 除数参数化，每张谱面无需改 RTL。
- 可选工具：快速仿真波形、分数/LED/LCD 预览、示例模板谱面。

## 落地步骤
1) 仓库整理：把生成物（`ROM.v`、带 BPM 的顶层）分离到 `generated/` 或使用模板，避免手改；新增 `charts/` 目录存放输入与输出。
2) 谱面规范：文档化格式（首行 bpm + `(position,type,line)`；type 如 tap/hold_start/hold_mid/...；位置范围、轨道 ID），定义语义校验（顺序、hold 成对、越界检查）。
3) 谱面工具重写：用跨平台脚本（Python/Node）完成 (a) 解析+校验，(b) 生成 ROM 初始化文件（`.v` 或 `.mif`），(c) 输出 BPM 配置供 RTL/生成包引用。避免直接改 `MuseDash.v`，改为参数/包含文件方式。
4) RTL 调整：`ROM` 用外部内存初始化（`$readmemb`/`$readmemh`），`div_cnt` 暴露为顶层参数由脚本注入；若扩按键需考虑轨道扩展。
5) 前端：做一个文件选择+时间线预览+校验结果的页面，按钮执行 (a) 生成资源，(b) 运行 Quartus 编译，(c) 烧录。后端用服务或 CLI 调用脚本。
6) 编译/烧录自动化：提供 PowerShell/Bash 脚本，调用 Quartus（`quartus_sh --flow compile quartus/MuseDash`），检查日志并调用 `quartus_pgm -c <cable> -m JTAG -o "p;output_files/MuseDash.sof"`。
7) 测试：为解析/校验加单元测试；准备小型仿真（ModelSim/iverilog）加载示例谱面，检查队列/判定输出；可选记录 VCD。
8) 体验补充：展示最近构建状态、目标板选择、进度日志；谱面非法或未识别编程器时给出清晰错误。
9) 文档：在 `README` 写快速上手，包含谱面格式、UI/CLI 使用方法、Quartus/烧录排错。

## 可选扩展
- 前端按 BPM/position 对齐音频预览，播放伴奏对拍检查。
- 支持多种按键/玩法（更多轨道、hold/slide），RTL 与谱面格式参数化。
- 通过 UART/USB 采集游戏轨迹，做榜单/成绩导出。
- 加 CI 钩子，至少在新谱面上跑解析测试和 RTL lint/仿真。*** End Patch ***!
