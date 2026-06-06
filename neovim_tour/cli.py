from neovim_tour.calculator import Invoice, add, format_invoice


def main() -> None:
    invoice = Invoice(customer="Creeken", subtotal=add(20, 22), discount_rate=0.1)
    print(format_invoice(invoice))


if __name__ == "__main__":
    main()
