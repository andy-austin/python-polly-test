from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase


class LoanPaymentCalculatorTestsMixin(TestCase):
    data = None

    def setUp(self) -> None:
        self.data = dict(
            amount=100000,
            interest='5',
            down_payment=20000,
            term=10
        )

    def _post_teardown(self) -> None:
        try:
            super()._post_teardown()
        except ImproperlyConfigured:
            # to avoid error with databases configuration
            pass
