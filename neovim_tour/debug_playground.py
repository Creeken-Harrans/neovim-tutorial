from neovim_tour.calculator import Invoice, add, apply_discount, format_invoice


def build_invoice(customer: str, prices: list[float], discount_rate: float) -> Invoice:
    subtotal = 0.0
    for price in prices:
        subtotal = add(subtotal, price)

    discounted_total = apply_discount(subtotal, discount_rate)
    return Invoice(customer=customer, subtotal=discounted_total)


def main() -> None:
    prices = [20.0, 22.0, 8.0]
    invoice = build_invoice("Debug Student", prices, 0.1)
    print(format_invoice(invoice))


if __name__ == "__main__":
    main()
