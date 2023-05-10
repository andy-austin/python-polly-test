import json
from typing import Type, Union
from django.core.management.base import BaseCommand

from loan.services import LoanPaymentCalculatorService


class LoanPaymentCalculatorCommand(BaseCommand):
    help = 'Calculates loan payment'

    def _get_option_field_value(self, options: dict, field: str, label: str, parse: Type[Union[str, float, int]]):
        value = options.get(field, None)
        while not value:
            try:
                raw_value = input(f'{label}: ')

                if field == 'interest':
                    is_percentage = raw_value.endswith('%')

                    if is_percentage:
                        assert float(raw_value[:-1]) <= 100
                        value = float(raw_value[:-1])
                    else:
                        assert len(raw_value) == 1
                        value = float(raw_value)
                else:
                    value = parse(raw_value)

            except ValueError:
                self.stdout.write(self.style.ERROR(f'Please enter a valid {label.lower()}'))
            except AssertionError:
                self.stdout.write(self.style.ERROR(f'{label} must be a percentage or a digit'))
        return value

    def handle(self, *args, **options):
        amount = self._get_option_field_value(options, 'amount', 'Loan amount', float)
        interest = self._get_option_field_value(options, 'interest', 'Interest rate', str)
        down_payment = self._get_option_field_value(options, 'down-payment', 'Down payment amount', float)
        term = self._get_option_field_value(options, 'term', 'Loan term', int)

        data = dict(
            amount=amount,
            interest=str(interest),
            down_payment=down_payment,
            term=term
        )

        results = LoanPaymentCalculatorService().calculate(data)
        self.stdout.write(json.dumps(results))


Command = LoanPaymentCalculatorCommand
