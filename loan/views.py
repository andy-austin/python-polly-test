import logging
from rest_framework import exceptions, generics, permissions, parsers
from rest_framework.request import Request
from rest_framework.response import Response

from loan.serializers import LoanPaymentCalculatorSerializer
from loan.services import LoanPaymentCalculatorService


class LoanPaymentCalculatorView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanPaymentCalculatorSerializer
    parser_classes = [parsers.JSONParser]

    @classmethod
    def post(cls, request: Request, *args, **kwargs):
        try:
            serializer = LoanPaymentCalculatorSerializer(data=request.data)

            if serializer.is_valid():
                results = LoanPaymentCalculatorService().calculate(serializer.validated_data)
                return Response(results)
            return Response(serializer.errors)
        except Exception as exception:
            logging.getLogger(__name__).error(exception)
            raise exceptions.APIException('Unknown error')
