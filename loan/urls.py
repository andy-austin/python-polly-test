from django.urls import re_path

from loan import views

urlpatterns = [
    re_path('calc', views.LoanPaymentCalculatorView.as_view(), name='loan-payment-calculator')
]
