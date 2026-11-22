class NotificationService:
    def __init__(self, smtp_client=None):
        self.smtp_client = smtp_client

    def send_order_confirmation(self, user_email: str, order_id: str) -> bool:
        """
        Wysyła wiadomość e-mail z potwierdzeniem zamówienia.
        """
        if not user_email or "@" not in user_email:
            raise ValueError("Nieprawidłowy adres e-mail.")

        # Wywołanie zewnętrznej usługi (efekt uboczny)
        print(f"[EMAIL] Powiadomienie wysłane do {user_email} dla zamówienia {order_id}")
        return True
