# Neovim Python Tour Project

这是配套 `../README.md` 的 Python 练习项目，用来体验当前 Neovim 配置里和 Python 开发有关的工作流。

建议从这里打开：

```bash
cd /home/Creeken/Paper/neovim/tutorial-project
nvim .
```

> **注意**：本文的 `<leader>` 是空格键（Space）。例如 `<leader>ff` = 按空格，再按 `f`，再按 `f`。按空格等一下，which-key 会弹出提示。

## 这个项目用来练什么

| 文件 | 练习目标 |
| --- | --- |
| `lessons/README.md` | 零基础练习目录，包含完整学习路线 |
| `lessons/01_modes.txt` | 所有插入模式入口、小修改、撤销重做 |
| `lessons/02_movement.txt` | 方向键替代、单词移动、行内跳转 f/t、段落、括号、搜索 */#、跳转列表 |
| `lessons/03_editing_practice.py` | 操作符语法、文本对象、. 重复、视觉模式 V/v/Ctrl-v、J 合并、大小写、数字增减、寄存器、宏、标记 |
| `lessons/04_search_replace.txt` | 搜索 /?、替换 :%s/.../gc、全项目搜索 fg/fr、正则、:g 全局命令 |
| `lessons/05_lsp_completion.py` | Pyright LSP、补全、参数提示、重命名、诊断 |
| `lessons/06_run_test_debug.py` | 运行当前 Python 文件、断点、调试单步 ↓→←↑、观察变量 |
| `lessons/07_daily_workflow.md` | 导航、编辑、窗口管理、buffer管理、运行、测试、debug、Git、标记、宏 |
| `lessons/08_practice_cards.md` | 18 张复盘任务卡，覆盖全部基础用法 |
| `neovim_tour/calculator.py` | Python 编辑、4 空格缩进、补全、跳转定义、格式化 |
| `neovim_tour/cli.py` | 运行当前文件、运行 Python 模块、跟踪函数调用 |
| `neovim_tour/debug_playground.py` | 断点、单步执行、查看变量、调试 Python 程序 |
| `tests/test_calculator.py` | pytest、测试面板、调试单个测试 |
| `diagnostics_playground.py` | Pyright 诊断和 Problems 面板 |
| `search_notes.md` | 全项目搜索和 TODO 搜索 |

## 推荐练习顺序

如果你是零基础，按这个顺序：

1. 用 `<leader>ff` 打开 `lessons/README.md`。
2. 依次完成 `01_modes.txt` 到 `04_search_replace.txt`，先学会模式、移动、编辑、搜索。
3. 完成 `05_lsp_completion.py`，学习补全、跳转、参数提示、诊断。
4. 完成 `06_run_test_debug.py`，学习运行当前文件和断点调试。
5. 完成 `07_daily_workflow.md`，把导航、编辑、运行、测试、debug、Git 串起来。
6. 用 `08_practice_cards.md` 做复盘。

如果你已经会一点 Vim，可以直接做 Python tour：

1. 用 `<leader>ff` 打开 `neovim_tour/cli.py`。
2. 用 `<leader>fg` 搜索 `TODO`、`Invoice` 或 `format_invoice`。
3. 用 `<leader>fr` 打开全项目替换界面，只预览不执行替换。
4. 在 `neovim_tour/calculator.py` 里体验补全、注释、搜索、替换。
5. 按 `<leader>rr` 运行当前 Python 文件。
6. 按 `<leader>rm` 以 Python module 方式运行当前文件。
7. 按 `<leader>rt` 运行全部 pytest。
8. 在 `tests/test_calculator.py` 里用 `<leader>tn` 运行光标附近测试。
9. 在 `neovim_tour/debug_playground.py` 里用 `<leader>db` 设置断点，再用 `<leader>dc` 启动调试。
10. 修改任意文件后观察左侧 Git 标记，再用 `<leader>gg` 打开 Git 状态。

## 常用命令

| 目标 | Neovim 快捷键 | 终端等价命令 |
| --- | --- | --- |
| 运行当前 Python 文件 | `<leader>rr` | `PYTHONPATH=$PWD python path/to/file.py` |
| 按 Python module 运行当前文件 | `<leader>rm` | `PYTHONPATH=$PWD python -m neovim_tour.cli` |
| 运行全部测试 | `<leader>rt` | `pytest -q` |
| 运行当前测试文件 | `<leader>rT` | `pytest -q tests/test_calculator.py` |
| 全项目搜索替换 | `<leader>fr` | `rg` + 手动替换 |
| 打开测试面板 | `<leader>ts` | 无，属于 Neovim UI |
| 运行光标附近测试 | `<leader>tn` | `pytest tests/test_calculator.py::test_name` |
| 调试光标附近测试 | `<leader>td` | `pytest --pdb ...` |
| 格式化当前文件 | `<leader>lf` | `black file.py` |
| 查看 Problems | `<leader>xx` | `pyright` |
| 启动断点调试 | `<leader>dc` | `python -m debugpy ...` |

`<leader>rr`、`<leader>rm`、`<leader>rt` 和 `<leader>rT` 会自动把当前项目根目录加入 `PYTHONPATH`。这样从包内部文件运行代码时，`from neovim_tour...` 这类导入也能正常工作。

## 调试练习

打开：

```text
neovim_tour/debug_playground.py
```

建议先把断点放在这两行之一：

```python
subtotal = add(subtotal, price)
discounted_total = apply_discount(subtotal, discount_rate)
```

然后按：

```text
<leader>db
<leader>dc
```

如果出现配置选择，选 `Launch current file`。调试界面打开后，可以用：

| 快捷键 | 作用 |
| --- | --- |
| `↓` | step over，执行当前行（仅调试中） |
| `→` | step into，进入函数（仅调试中） |
| `←` | step out，跳出当前函数（仅调试中） |
| `↑` | restart frame（仅调试中） |
| `<leader>dc` | continue，继续到下一个断点 |
| `<leader>dr` | 打开 debug REPL |
| `<leader>dt` | 停止调试 |
| `<leader>du` | 打开或关闭调试 UI |

调试时建议观察：

| 变量 | 你应该看到什么 |
| --- | --- |
| `prices` | `[20.0, 22.0, 8.0]` |
| `price` | 循环里当前处理的单个价格 |
| `subtotal` | 每次循环累加后的金额 |
| `discounted_total` | 打折后的总价 |
| `invoice` | `Invoice(customer="Debug Student", subtotal=45.0, discount_rate=0.0)` |

如果你想调试测试，打开 `tests/test_calculator.py`，把光标放进某个 `test_...` 函数，按 `<leader>td`。
