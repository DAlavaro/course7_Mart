# app/api/versions/v1/payments/urls.py
from django.urls import path
from .views import PaymentListAPIView

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='list_view'),
]