# 练习 08：复盘任务卡

这不是新知识，而是把前面的动作拆成短任务。每天开始写代码前可以任选 3 到 5 张卡练 10 分钟。

## 卡 1：模式恢复

目标：任何时候都能回到普通模式。

1. 打开 `lessons/01_modes.txt`。
2. 按 `i` 输入几个字。
3. 按 `jk` 回普通模式。
4. 按 `u` 撤销。
5. 按 `<C-r>` 重做。
6. 按 `:e!` 丢弃未保存修改。

合格标准：你不再因为“不知道怎么退出输入状态”而卡住。

## 卡 2：无鼠标移动

目标：不用鼠标定位到一个词。

1. 打开 `lessons/02_movement.txt`。
2. 用 `/target` 搜索。
3. 用 `n` / `N` 跳结果。
4. 用 `0` / `$` 在行首行尾移动。
5. 用 `gg` / `G` 在文件头尾移动。

合格标准：你可以不用鼠标找到目标文字。

## 卡 3：改一个字符串

目标：用文本对象替代鼠标选择。

1. 打开 `lessons/03_editing_practice.py`。
2. 把光标放进 `"Neovim"`。
3. 按 `ci"`。
4. 输入你的名字。
5. 按 `jk`。
6. 按 `<leader>w`。
7. 按 `<leader>rr` 运行。

合格标准：你理解 `ci"` 是“修改双引号里面”。

## 卡 4：改一个变量名的一处

目标：练 `ciw`。

1. 打开 `lessons/03_editing_practice.py`。
2. 把光标放在 `message` 上。
3. 按 `ciw`。
4. 输入 `text`。
5. 按 `jk`。
6. 按 `u` 撤销。

合格标准：你能快速修改一个单词。

## 卡 5：当前文件搜索替换

目标：掌握当前文件内的搜索和替换。

1. 打开 `lessons/04_search_replace.txt`。
2. 输入 `/apple`。
3. 用 `n` / `N` 跳转。
4. 执行 `:%s/apple/invoice/gc`。
5. 每次确认时只按 `y` 或 `n`。
6. 按 `u` 撤销。

合格标准：你知道替换前应该先搜索确认范围。

## 卡 6：全项目搜索

目标：替代 VSCode `Ctrl-Shift-F`。

1. 按 `<leader>fg`。
2. 搜索 `format_invoice`。
3. 用 `<C-j>` / `<C-k>` 切换结果。
4. 按 Enter 打开一个结果。
5. 按 `Ctrl-o` 回到上一个位置。

合格标准：你可以通过内容找到文件。

## 卡 7：LSP 代码理解

目标：替代 VSCode Go to Definition / Hover / Find References。

1. 打开 `lessons/05_lsp_completion.py`。
2. 光标放到 `Product`，按 `<leader>lh`（或 `K`）。
3. 光标放到 `format_receipt` 的调用处，按 `<leader>ld`（或 `gd`）。
4. 按 `<leader>lb`（或 `Ctrl-o`）返回。
5. 光标放到 `calculate_total`，按 `<leader>lr`（或 `gr`）。

合格标准：你会用 LSP 读代码。

## 卡 8：补全和参数提示

目标：替代 VSCode IntelliSense。

1. 打开 `lessons/05_lsp_completion.py`。
2. 在 `main()` 里新建一行。
3. 输入 `product.`。
4. 按 `<C-l>`（或 `<C-Space>`）。
5. 选择 `name`、`price` 或 `quantity`。
6. 输入 `format_receipt(`，观察参数提示。
7. 如果没有提示，按 `<leader>ls`。

合格标准：你能主动触发补全和参数提示。

## 卡 9：运行当前文件

目标：替代 VSCode Run Python File。

1. 打开 `lessons/06_run_test_debug.py`。
2. 按 `<leader>rr`。
3. 看底部终端输出。
4. 按 `Esc` 或 `jk` 从终端回普通模式。

合格标准：你知道运行结果在哪里看，也知道怎么从终端回到编辑器。

## 卡 10：断点调试

目标：替代 VSCode Run and Debug。

1. 打开 `lessons/06_run_test_debug.py`。
2. 光标放到 `total += score`。
3. 按 `<leader>db`。
4. 按 `<leader>dc`。
5. 选择 `Launch current file`。
6. 用 `↓` 单步（调试中方向键自动切换为调试控制）。
7. 用 `<leader>dt` 停止。

合格标准：你能设置断点、启动调试、单步和停止。

## 卡 11：测试

目标：替代 VSCode Testing。

1. 打开 `tests/test_calculator.py`。
2. 光标放到任意 `test_...` 函数里。
3. 按 `<leader>tn`。
4. 按 `<leader>to` 查看输出。
5. 按 `<leader>rt` 跑全部测试。

合格标准：你知道怎么跑单个测试和全部测试。

## 卡 12：Problems 和诊断

目标：替代 VSCode Problems。

1. 打开 `diagnostics_playground.py`。
2. 取消最后一行 `print(unknown_value)` 的注释。
3. 保存。
4. 按 `<leader>le` 看当前行诊断。
5. 按 `<leader>xx` 打开 Problems。
6. 练习后重新注释那一行。

合格标准：你知道错误提示来自 Pyright，也知道在哪里看。

## 卡 13：Git hunk

目标：替代 VSCode Source Control 的一部分。

1. 修改任意一行并保存。
2. 观察左侧 `+` 或 `~`。
3. 按 `<leader>ghp` 预览当前 hunk。
4. 如果只是练习，按 `u` 撤销。

合格标准：你能看懂左侧 Git 标记。

## 卡 14：窗口和分屏

目标：VSCode Split Editor。

1. 按 `<leader>ff` 打开 `neovim_tour/calculator.py`。
2. 按 `<leader>sv` 右侧开一个分屏。
3. 在新窗口按 `<leader>ff` 打开 `tests/test_calculator.py`。
4. 用 `<C-w>h` / `<C-w>l` 在左右窗口间移动。
5. 按 `<leader>sx` 关闭不需要的窗口。

合格标准：你能分屏对照代码和测试。

## 卡 15：寄存器

目标：理解 Vim 有多个剪贴板。

1. 在任意行按 `"ayy` 复制到寄存器 a。
2. 跳到文件末尾，按 `"ap` 粘贴。
3. 在另一行按 `"bdd` 剪切到寄存器 b。
4. 跳到别处按 `"bp` 粘贴。

合格标准：你知道不同寄存器可以存不同内容。

## 卡 16：宏

目标：录制并重放重复操作。

1. 在 `lessons/03_editing_practice.py` 找到 line_0 到 line_4 那几行。
2. 光标放到 line_0，按 `qa` 开始录制。
3. 给这行加引号（I + " + Esc + A + ", + Esc + j + q）。
4. 按 `4@a` 对下面 4 行重放。
5. 按 `u` 撤销。

合格标准：你能录制简单宏并重放。

## 卡 17：标记

目标：给重要位置打书签。

1. 在 `calculator.py` 里任意位置按 `ma`。
2. 跳到文件末尾（G）。
3. 按 `` `a `` 回来。
4. 按 `''` 回到文件末尾。

合格标准：你能设置标记并跳回来。

## 卡 18：完整小循环

目标：串起一次真实开发。

1. `<leader>ff` 找文件。
2. `<leader>lh`（或 `K`）/ `<leader>ld`（或 `gd`）理解代码。
3. `ciw` 或 `ci"` 修改。
4. `<leader>w` 保存。
5. `<leader>lf` 格式化。
6. `<leader>rr` 运行。
7. `<leader>rt` 测试。
8. `<leader>xx` 看 Problems。
9. `<leader>gg` 看 Git 状态。

合格标准：你能不用鼠标完成一次小改动。
