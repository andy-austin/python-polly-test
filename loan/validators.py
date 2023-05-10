from rest_framework.exceptions import ValidationError


class InterestValidator:
    message = 'Interest rate must be a percentage or a digit.'

    def __call__(self, value):
        try:
            is_percentage = value.endswith('%')
            if is_percentage:
                assert float(value[:-1]) <= 100
            else:
                assert len(value) == 1
        except AssertionError:
            raise ValidationError(self.message)
