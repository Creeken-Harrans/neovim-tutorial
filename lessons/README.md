# Neovim 零基础练习目录

建议按顺序练，不要跳着背命令。

| 文件 | 练什么 |
| --- | --- |
| `01_modes.txt` | 普通模式、插入模式（i/a/I/A/o/O/s/S/C/cc/r/x/~）、保存、退出、撤销 |
| `02_movement.txt` | hjkl、w/b/e、0/^/$、f/t/F/T、;/，、{/}、%、gg/G、Ctrl-d/u/f/b、/搜索、*/#、*g;*/g,、Ctrl-o/Ctrl-i |
| `03_editing_practice.py` | 操作符+范围语法、文本对象 ci"/ci(/ci{/di"/da"、. 重复修改、dd/yy/p、视觉模式 V/v/Ctrl-v、J 合并、~ 大小写、gU/gu、Ctrl-a/Ctrl-x、= 自动缩进、**寄存器** "a-z、**宏** q/@、**标记** m/` |
| `04_search_replace.txt` | /搜索、?向上搜索、n/N、*/#、:%s/.../gc 替换、范围替换、全项目搜索 fg、全项目替换 fr、正则、:g 全局命令 |
| `05_lsp_completion.py` | Pyright LSP、hover、跳转定义、查找引用、参数提示、补全、重命名、诊断、格式化 |
| `06_run_test_debug.py` | 运行 Python、断点 db、启动调试 dc、方向键单步 ↓→←↑、观察变量 |
| `07_daily_workflow.md` | 完整日常流程：导航→编辑→运行→测试→debug→Git→窗口管理→buffer管理→标记→宏 |
| `08_practice_cards.md` | 15 张复盘任务卡，涵盖全部基础用法，适合每天重复练 |

打开方式：

```bash
cd /home/Creeken/Paper/neovim/tutorial-project
nvim .
```

然后用 `<leader>ff` 搜索文件名，例如 `01_modes`。（`<leader>` = 空格键）

推荐节奏：

1. 第一次学习时按 01 到 08 顺序做。
2. 完成 01-04 后你已经能独立编辑任何文本文件。
3. 完成 05-06 后你能在 Neovim 里做完整 Python 开发。
4. 之后每天用 `08_practice_cards.md` 任选几张卡复习。
5. 真正写 Python 项目前，至少确认自己会 `<leader>ff`、`i`、`jk`、`<leader>w`、`<leader>ld`、`<leader>rr`、`<leader>rt`。
