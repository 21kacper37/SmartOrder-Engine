class PaymentFailedException(Exception):
    """Wyjątek rzucany w przypadku niepowodzenia transakcji płatniczej."""
    pass


class PaymentGateway:
    def charge(self, amount: float, card_token: str) -> dict:
        """
        Symulacja zewnętrznej bramki płatności (API).
        W rzeczywistym systemie wykonuje zapytanie HTTP do dostawcy płatności.
        """
        if amount <= 0:
            raise ValueError("Kwota obciążenia musi być większa od zera.")
        if not card_token:
            raise PaymentFailedException("Brak wymaganego tokenu karty płatniczej.")

        # Symulacja pomyślnej odpowiedzi z serwera płatności
        return {
            "status": "SUCCESS",
            "transaction_id": "tx_9988776655",
            "amount": amount
        }
