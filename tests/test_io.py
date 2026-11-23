# Miejsce na testy strumieni I/O (Część 4: capsys, monkeypatch)
import pytest
from smartorder.cli.receipt_printer import print_receipt, confirm_order_cli


def test_print_receipt_prints_header_items_and_total(capsys):
    items = [
        {"name": "Laptop", "price": 3500.0, "quantity": 1},
        {"name": "Myszka", "price": 150.0, "quantity": 2},
    ]
    total = 3800.0

    print_receipt(items, total)
    captured = capsys.readouterr()

    assert "=== PARAGON ===" in captured.out
    assert "Laptop" in captured.out
    assert "Myszka" in captured.out
    assert "3800.00" in captured.out


@pytest.mark.parametrize("user_input", ["Y", "y"])
def test_confirm_order_cli_returns_true_for_yes(monkeypatch, user_input):
    monkeypatch.setattr("builtins.input", lambda _prompt="": user_input)

    confirmed = confirm_order_cli()

    assert confirmed is True


@pytest.mark.parametrize("user_input", ["N", "n", "no", ""])
def test_confirm_order_cli_returns_false_for_other_inputs(monkeypatch, user_input):
    monkeypatch.setattr("builtins.input", lambda _prompt="": user_input)

    confirmed = confirm_order_cli()

    assert confirmed is False
