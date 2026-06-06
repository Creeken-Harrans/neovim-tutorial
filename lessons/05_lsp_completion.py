"""练习 Pyright LSP、补全、参数提示和格式化。"""

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int


def calculate_total(product: Product, tax_rate: float) -> float:
    subtotal = product.price * product.quantity
    return subtotal * (1 + tax_rate)


def format_receipt(product: Product, tax_rate: float) -> str:
    total = calculate_total(product, tax_rate)
    return f"{product.name}: ${total:.2f}"


def main() -> None:
    product = Product(name="Notebook", price=12.5, quantity=3)
    print(format_receipt(product, 0.08))


if __name__ == "__main__":
    main()


# 练习 1：Hover
# 把光标放到 Product、calculate_total 或 format_receipt 上，按 <leader>lh（或 K）。
#
# 练习 2：跳转定义
# 把光标放到 main 里的 format_receipt 上，按 <leader>ld（或 gd）。
# 按 <leader>lb（或 Ctrl-o）可以跳回原来的位置。
#
# 练习 3：查找引用
# 把光标放到 calculate_total 的函数名上，按 <leader>lr（或 gr）。
#
# 练习 4：参数提示
# 在 main 里新开一行，输入 format_receipt(
# 参数提示会自动出现，也可以按 <leader>ls 手动打开。
#
# 练习 5：补全
# 在 main 里新开一行，输入 product.
# 然后按 <C-l>（或 <C-Space>），观察 name、price、quantity 候选。
#
# 练习 6：重命名
# 把光标放到 tax_rate 上，按 <leader>ln。
# 输入 rate，确认后观察同一个符号的引用是否一起变更。
# 练习后按 u 撤销。
#
# 练习 7：诊断
# 取消下面这一行注释，然后保存，观察 Pyright 报错。
# print(missing_value)
#
# 练习 8：格式化和运行
# 按 <leader>lf 格式化。
# 按 <leader>rr 运行当前文件。
