from io import StringIO
from unittest.mock import patch
from django.core.management import call_command

from loan.tests import LoanPaymentCalculatorTestsMixin


class LoanPaymentCalculatorCommandTestCase(LoanPaymentCalculatorTestsMixin):
    expected_output = '{"monthly payment": 668.35, "total interest": 202.0, "total payment": 80202.0}'

    @patch('builtins.input', side_effect=['100000', '5', '20000', '10'])
    def test_command_calculate_loan_payment_with_valid_input(self, mock_input):
        console = StringIO()
        call_command('loan-payment-calculator', stdout=console)
        result = console.getvalue().strip()
        self.assertEqual(result, self.expected_output)

    @patch('builtins.input', side_effect=['100000', '5%', '20000', '10'])
    def test_command_calculate_loan_payment_with_valid__interest_percentage(self, mock_input):
        console = StringIO()
        call_command('loan-payment-calculator', stdout=console)
        result = console.getvalue().strip()
        self.assertEqual(result, self.expected_output)
