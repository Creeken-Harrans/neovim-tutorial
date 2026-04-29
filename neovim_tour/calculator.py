from dataclasses import dataclass


@dataclass
class Invoice:
    customer: str
    subtotal: float
    discount_rate: float = 0.0

    @property
    def total(self) -> float:
        return apply_discount(self.subtotal, self.discount_rate)


def add(left: float, right: float) -> float:
    return left + right


def apply_discount(amount: float, discount_rate: float) -> float:
    if not 0 <= discount_rate <= 1:
        raise ValueError("discount_rate must be between 0 and 1")
    return amount * (1 - discount_rate)


def format_invoice(invoice: Invoice) -> str:
    return f"{invoice.customer}: ${invoice.total:.2f}"

