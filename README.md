# Neovim Python Tour Project

这是配套 `../README.md` 的 Python 练习项目，用来体验当前 Neovim 配置里和 Python 开发有关的工作流。

建议从这里打开：

```bash
cd /home/Creeken/Paper/neovim/tutorial-project
nvim .
```

推荐练习顺序：

1. 用 `<leader>ff` 打开 `neovim_tour/cli.py`。
2. 用 `<leader>fg` 搜索 `TODO`、`Invoice` 或 `format_invoice`。
3. 在 `neovim_tour/calculator.py` 里体验补全、注释、搜索、替换。
4. 在 `tests/test_calculator.py` 里体验跳转定义、查找引用和运行测试。
5. 修改任意文件后观察左侧 Git 标记。
6. 在终端里运行 `python -m neovim_tour.cli` 和 `pytest`。
