class Payment:
    def __init__(self, payment_id: str, ride, amount: float, method: str):
        self._payment_id = payment_id
        self._ride = ride
        self._amount = amount
        self._method = method
        self._is_completed = False

    @property
    def payment_id(self):
        return self._payment_id

    @property
    def amount(self):
        return self._amount

    @property
    def method(self):
        return self._method

    @property
    def is_completed(self):
        return self._is_completed

    def complete_payment(self):
        self._is_completed = True

    def __str__(self):
        status = "Completed" if self._is_completed else "Pending"
        return f"Payment(id={self._payment_id}, amount={self._amount}, status={status})"
