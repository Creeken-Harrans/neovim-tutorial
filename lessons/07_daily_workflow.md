# 练习 07：完整日常工作流

这一课把前面的能力串起来，模拟一次真实 Python 开发。

## 1. 打开项目

```bash
cd /home/Creeken/Paper/neovim/tutorial-project
nvim .
```

## 2. 找文件

按 `<leader>ff`，搜索：

```text
calculator
```

打开 `neovim_tour/calculator.py`。

## 3. 理解代码

按下面顺序体验：

| 目标 | 按键 |
| --- | --- |
| 查看说明 | `<leader>lh`（或 `K`） |
| 跳转定义 | `<leader>ld`（或 `gd`） |
| 返回上一个位置 | `<leader>lb`（或 `Ctrl-o`） |
| 前进到下一个位置 | `<leader>lB`（或 `Ctrl-i`） |
| 查找引用 | `<leader>lr`（或 `gr`） |
| 当前文件大纲 | `<leader>fo` |
| 全项目符号搜索 | `<leader>fS` |

## 4. 编辑代码

在 `calculator.py` 里练：

| 目标 | 按键 |
| --- | --- |
| 修改一个单词 | `ciw` |
| 修改引号内容 | `ci"` |
| 修改括号内容 | `ci(` 或 `ci{` |
| 删除一行 | `dd` |
| 复制一行 | `yy` |
| 粘贴到下一行 | `p` |
| 粘贴到上一行 | `P` |
| 重复上次修改 | `.` |
| 撤销 | `u` |
| 重做 | `Ctrl-r` |
| 合并下一行 | `J` |
| 注释当前行 | `gcc` |
| 注释多行 | `V` 选中后 `gc` |
| 格式化 | `<leader>lf`（保存时也会自动格式化） |

## 5. 窗口和分屏管理

边对照代码边写测试是常见需求。先掌握分屏：

| 目标 | 按键 |
| --- | --- |
| 垂直分屏（左右） | `<leader>sv` |
| 水平分屏（上下） | `<leader>sh` |
| 关闭当前分屏 | `<leader>sx` |
| 跳到左边窗口 | `Ctrl-w h`（或 `Ctrl-h`，如果用了 tmux-navigator） |
| 跳到右边窗口 | `Ctrl-w l`（或 `Ctrl-l`） |
| 跳到上方窗口 | `Ctrl-w k`（或 `Ctrl-k`） |
| 跳到下方窗口 | `Ctrl-w j`（或 `Ctrl-j`） |
| 等分所有窗口 | `Ctrl-w =` |
| 当前窗口最大化 | `Ctrl-w _` 再 `Ctrl-w \|` |

分屏实战练习：

1. 打开 `neovim_tour/calculator.py`。
2. 按 `<leader>sv` 在右侧开一个分屏。
3. 在新窗口按 `<leader>ff` 打开 `tests/test_calculator.py`。
4. 用 `Ctrl-w h` / `Ctrl-w l` 在左右窗口间移动。
5. 左边看实现，右边看测试。
6. 完成后按 `<leader>sx` 关闭右侧窗口。

## 6. Buffer 管理

| 目标 | 按键 |
| --- | --- |
| 下一个 buffer | `<leader>bn` |
| 上一个 buffer | `<leader>bp` |
| 关闭当前 buffer | `<leader>bd`（或 `:bd`） |
| 查看所有 buffer | `<leader>fb` |
| 按名称搜索 buffer | `<leader>fb` 后输入名字 |

## 7. 运行和测试

| 目标 | 按键 |
| --- | --- |
| 运行当前 Python 文件 | `<leader>rr` |
| 以 module 方式运行 | `<leader>rm` |
| 运行全部 pytest | `<leader>rt` |
| 运行当前测试文件 | `<leader>rT` |
| 打开测试面板 | `<leader>ts` |
| 运行光标附近测试 | `<leader>tn` |
| 调试光标附近测试 | `<leader>td` |
| 查看测试输出 | `<leader>to` |
| 打开测试输出面板 | `<leader>tO` |
| 停止测试 | `<leader>tx` |

## 8. 诊断和修复

打开 `diagnostics_playground.py`，取消最后一行注释并保存。

| 目标 | 按键 |
| --- | --- |
| 查看当前行诊断 | `<leader>le` |
| 打开 Problems 面板 | `<leader>xx` |
| 只看当前文件 Problems | `<leader>xX` |
| 跳到下一个诊断 | `]d` |
| 跳到上一个诊断 | `[d` |
| 把诊断放到 quickfix | `<leader>lq` |

练习后把那一行重新注释。

## 9. Debug

打开 `neovim_tour/debug_playground.py`。

基本流程：
1. 光标放到 `subtotal = add(subtotal, price)`。
2. 按 `<leader>db` 设置断点（左侧出现 `B`）。
3. 按 `<leader>dc` 启动调试，选择 `Launch current file`。
4. 程序停在断点处，DAP UI 自动打开。

调试中可用：

| 目标 | 按键 |
| --- | --- |
| 单步跳过（step over） | `↓` |
| 进入函数（step into） | `→` |
| 跳出函数（step out） | `←` |
| 重启栈帧 | `↑` |
| 继续到下一断点 | `<leader>dc` |
| 运行到光标位置 | `<leader>dC` |
| 设置条件断点 | `<leader>dB` |
| 设置 logpoint | `<leader>dL` |
| 暂停程序 | `<leader>dp` |
| 打开 Debug REPL | `<leader>dr` |
| 打开/关闭调试 UI | `<leader>du` |
| 停止调试 | `<leader>dt` |
| 重新运行上次调试 | `<leader>dl` |

## 10. 终端操作

| 目标 | 按键 |
| --- | --- |
| 打开/关闭底部终端 | `<leader>tt` |
| 打开浮动终端 | `<leader>tf` |
| 从终端回普通模式 | `Esc` 或 `jk` |
| 终端中切换到左边窗口 | `Ctrl-h` |
| 终端中切换到右边窗口 | `Ctrl-l` |

## 11. Git

修改任意文件并保存。

| 目标 | 按键 |
| --- | --- |
| 预览当前 hunk | `<leader>ghp` |
| stage 当前 hunk | `<leader>ghs` |
| reset 当前 hunk | `<leader>ghr` |
| undo stage hunk | `<leader>ghu` |
| 查看行 blame | `<leader>ghb` |
| 查看文件 diff | `<leader>ghd` |
| 打开 Git status | `<leader>gg` |
| Git commit | `<leader>gc` |
| Git push | `<leader>gp` |
| Git pull | `<leader>gP` |
| Git diff split | `<leader>gD` |
| Git blame | `<leader>gB` |
| 下一个 Git hunk | `]c` |
| 上一个 Git hunk | `[c` |

练习结束后，如果不保留改动，用 `u` 撤销或在 Git 面板不要 commit。

## 12. 标记和宏（进阶）

标记（marks）：在文件里打书签，方便快速跳回。

| 目标 | 按键 |
| --- | --- |
| 设置标记 a | `ma` |
| 跳回标记 a | `` `a `` |
| 跳到标记 a 所在行 | `'a` |
| 跳回上一次位置 | `''` 或 `` `` `` |
| 跳到上次修改位置 | `'.` |

宏（macros）：录制重复操作，一键重放。

| 目标 | 按键 |
| --- | --- |
| 开始录制到寄存器 a | `qa` |
| 停止录制 | `q` |
| 重放宏 a | `@a` |
| 重复上次宏 | `@@` |
| 重放宏 a 5 次 | `5@a` |

练习：在 `calculator.py` 里任意位置设标记 `ma`，跳到文件末尾，再按 `` `a `` 回来。

## 13. 搜索和替换

| 目标 | 按键 |
| --- | --- |
| 当前文件搜索 | `/关键词` |
| 向上搜索 | `?关键词` |
| 搜索光标所在单词 | `*`（向下）或 `#`（向上） |
| 全项目搜索 | `<leader>fg` |
| 当前文件替换 | `:%s/old/new/gc` |
| 只替换选中行 | `V` 选中后 `:s/old/new/g` |
| 全项目替换 | `<leader>fr` |
| 清除搜索高亮 | `<leader>nh` |
| 恢复上次 Telescope 搜索 | `<leader>fR` |

## 14. 日常检查

| 目标 | 命令 |
| --- | --- |
| 插件状态 | `:Lazy` |
| 工具管理 | `:Mason` |
| 健康检查 | `:checkhealth` |
| LSP 状态 | `:LspInfo` |
| 查看快捷键 | `<leader>fk` |
| 搜索命令 | `<leader>fc` |
| 查看帮助 | `<leader>fh` |

## 15. 完整循环总结

一次小改动的标准流程：

```text
nvim .
<leader>ff → 找文件
<leader>lh / <leader>ld → 理解代码
ciw / ci" → 修改
<leader>w → 保存（或 Ctrl-s）
<leader>lf → 格式化（保存时自动触发也行）
<leader>rr → 运行
<leader>rt → 测试
<leader>xx → 看 Problems
<leader>gg → Git 状态
```

一次完整 debug 流程：

```text
<leader>ff → 打开要调试的文件
光标放到目标行
<leader>db → 设断点
<leader>dc → 启动调试
↓ → 单步
变量在 DAP UI 的 Scopes 里观察
<leader>dr → 在 REPL 里试表达式
<leader>dt → 停止
```

---

这份配置的目标：你能在 Neovim 里完成 VSCode 日常 95% 的操作。剩下的 5% 是命令行 git、复杂 rebase、Docker、数据库——那些本就不该塞进编辑器里。
