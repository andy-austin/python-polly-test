from rest_framework import serializers

from loan.validators import InterestValidator


class LoanPaymentCalculatorSerializer(serializers.Serializer):
    amount = serializers.FloatField(required=True)
    interest = serializers.CharField(required=True, validators=[InterestValidator()])
    down_payment = serializers.FloatField(required=True)
    term = serializers.IntegerField(required=True)
