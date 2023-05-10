class LoanPaymentCalculatorService:
    amount = None
    interest = None
    down_payment = None
    term = None

    def calculate(self, validated_data: dict) -> dict:
        self.amount = float(validated_data.get('amount'))
        self.interest = float(validated_data.get('interest').replace('%', '')) / 100
        self.down_payment = float(validated_data.get('down_payment'))
        self.term = int(validated_data.get('term'))

        monthly_interest_rate = self.interest / (12 * 100)
        total_months = self.term * 12

        return {
            "monthly payment": self._monthly_payment(monthly_interest_rate, total_months),
            "total interest": self._total_interest(monthly_interest_rate, total_months),
            "total payment": self._total_payment(monthly_interest_rate, total_months)
        }

    def _monthly_payment(self, monthly_interest_rate: float, total_months: float):
        principal = self.amount - self.down_payment
        total_payment_amount = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_months
        discount_factor = ((1 + monthly_interest_rate) ** total_months) - 1
        return round(total_payment_amount / discount_factor, 2)

    def _total_interest(self, monthly_interest_rate: float, total_months: float):
        monthly_payment = self._monthly_payment(monthly_interest_rate, total_months)
        total_interest = (monthly_payment * total_months) - (self.amount - self.down_payment)
        return round(total_interest, 2)

    def _total_payment(self, monthly_interest_rate: float, total_months: float):
        monthly_payment = self._monthly_payment(monthly_interest_rate, total_months)
        return round(monthly_payment * total_months, 2)
