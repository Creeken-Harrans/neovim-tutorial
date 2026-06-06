import pytest

from neovim_tour.calculator import Invoice, add, apply_discount, format_invoice


def test_add() -> None:
    assert add(20, 22) == 42


def test_apply_discount() -> None:
    assert apply_discount(100, 0.25) == 75


def test_apply_discount_rejects_invalid_rate() -> None:
    with pytest.raises(ValueError):
        apply_discount(100, 1.5)


def test_format_invoice() -> None:
    invoice = Invoice(customer="Neovim", subtotal=100, discount_rate=0.2)
    assert format_invoice(invoice) == "Neovim: $80.00"
