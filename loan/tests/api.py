from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from loan.tests import LoanPaymentCalculatorTestsMixin


class LoanPaymentCalculatorAPITestCase(LoanPaymentCalculatorTestsMixin, APITestCase):
    path = reverse('loan-payment-calculator')

    def test_api_calculate_loan_payment_with_valid_input(self):
        response = self.client.post(self.path, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['monthly payment'], 668.35)
        self.assertEqual(response.data['total interest'], 202.0)
        self.assertEqual(response.data['total payment'], 80202.0)

    def test_api_calculate_loan_payment_with_valid_interest_percentage(self):
        self.data.update({'interest': '5%'})

        response = self.client.post(self.path, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['monthly payment'], 668.35)
        self.assertEqual(response.data['total interest'], 202.0)
        self.assertEqual(response.data['total payment'], 80202.0)

    def test_api_calculate_loan_payment_with_invalid_interest_digit(self):
        self.data.update({'interest': '55'})

        response = self.client.post(self.path, self.data, format='json')

        self.assertEqual(response.data['interest'][0].code, 'invalid')

    def test_api_calculate_loan_payment_with_invalid_interest_percentage(self):
        self.data.update({'interest': '555%'})

        response = self.client.post(self.path, self.data, format='json')

        self.assertEqual(response.data['interest'][0].code, 'invalid')

    def test_api_calculate_loan_payment_with_invalid_amount(self):
        self.data.update({'amount': 'er34324'})

        response = self.client.post(self.path, self.data, format='json')

        self.assertEqual(response.data['amount'][0].code, 'invalid')

    def test_api_calculate_loan_payment_with_invalid_down_payment(self):
        self.data.update({'down_payment': 'er34324'})

        response = self.client.post(self.path, self.data, format='json')

        self.assertEqual(response.data['down_payment'][0].code, 'invalid')

    def test_api_calculate_loan_payment_with_invalid_term(self):
        self.data.update({'term': '12.4'})

        response = self.client.post(self.path, self.data, format='json')

        self.assertEqual(response.data['term'][0].code, 'invalid')
