from loan.tests.mixin import LoanPaymentCalculatorTestsMixin
from loan.serializers import LoanPaymentCalculatorSerializer
from loan.services import LoanPaymentCalculatorService


class LoanPaymentCalculatorServiceTestCase(LoanPaymentCalculatorTestsMixin):
    service = None

    def setUp(self) -> None:
        self.service = LoanPaymentCalculatorService()
        super().setUp()

    def test_calculate_loan_payment_with_valid_input(self):
        serializer = LoanPaymentCalculatorSerializer(data=self.data)
        serializer.is_valid()
        result = self.service.calculate(serializer.validated_data)

        self.assertEqual(result['monthly payment'], 668.35)
        self.assertEqual(result['total interest'], 202.0)
        self.assertEqual(result['total payment'], 80202.0)

    def test_calculate_loan_payment_with_valid_interest_percentage(self):
        self.data.update({'interest': '5%'})

        serializer = LoanPaymentCalculatorSerializer(data=self.data)
        serializer.is_valid()
        result = self.service.calculate(serializer.validated_data)

        self.assertEqual(result['monthly payment'], 668.35)
        self.assertEqual(result['total interest'], 202.0)
        self.assertEqual(result['total payment'], 80202.0)

    def test_calculate_loan_payment_with_invalid_interest_digit(self):
        self.data.update({'interest': '55'})

        serializer = LoanPaymentCalculatorSerializer(data=self.data)
        serializer.is_valid()
        self.assertEqual(serializer.is_valid(), False)

    def test_calculate_loan_payment_with_invalid_interest_percentage(self):
        self.data.update({'interest': '555%'})

        serializer = LoanPaymentCalculatorSerializer(data=self.data)
        serializer.is_valid()
        self.assertEqual(serializer.is_valid(), False)

    def test_calculate_loan_payment_with_invalid_amount(self):
        self.data.update({'amount': 'er34324'})

        serializer = LoanPaymentCalculatorSerializer(data=self.data)
        serializer.is_valid()
        self.assertEqual(serializer.is_valid(), False)

    def test_calculate_loan_payment_with_invalid_down_payment(self):
        self.data.update({'down_payment': 'er34324'})

        serializer = LoanPaymentCalculatorSerializer(data=self.data)
        serializer.is_valid()
        self.assertEqual(serializer.is_valid(), False)

    def test_calculate_loan_payment_with_invalid_term(self):
        self.data.update({'term': '12.4'})

        serializer = LoanPaymentCalculatorSerializer(data=self.data)
        serializer.is_valid()
        self.assertEqual(serializer.is_valid(), False)
