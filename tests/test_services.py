# Miejsce na testy dubletów testowych / Mocków (Część 5)
import pytest
from unittest.mock import MagicMock
from smartorder.services.payment import PaymentGateway, PaymentFailedException
from smartorder.services.notifier import NotificationService


def test_payment_gateway_charge_succeeds_with_mock():
    gateway = PaymentGateway()
    gateway.charge = MagicMock(return_value={"status": "ok", "tx_id": "TX-001"})

    result = gateway.charge(199.99, "PLN")

    assert result["status"] == "ok"
    gateway.charge.assert_called_once_with(199.99, "PLN")


def test_payment_gateway_charge_raises_payment_failed_exception():
    gateway = PaymentGateway()
    gateway.charge = MagicMock(side_effect=PaymentFailedException("Brak środków"))

    with pytest.raises(PaymentFailedException):
        gateway.charge(5000.0, "PLN")


def test_send_order_confirmation_calls_once_for_valid_email():
    notifier = NotificationService()
    notifier._send_email = MagicMock(return_value=True)

    result = notifier.send_order_confirmation("user@example.com", "ORD-123")

    assert result is True
    notifier._send_email.assert_called_once_with("user@example.com", "ORD-123")


def test_send_order_confirmation_invalid_email_raises_value_error():
    notifier = NotificationService()

    with pytest.raises(ValueError):
        notifier.send_order_confirmation("invalid-email.com", "ORD-123")
