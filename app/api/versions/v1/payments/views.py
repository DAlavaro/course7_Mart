# api/versions/v1/payments/views.py
from .filter import PaymentFilter
from .serializers import PaymentListSerializer, Payment
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class PaymentBaseAPIView:
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer


class PaymentListAPIView(PaymentBaseAPIView, generics.ListAPIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PaymentFilter  # Устанавливаем кастомный фильтр
    ordering_fields = ['date_pay']  # Поля, по которым можно сортировать
    ordering = ['-date_pay']  # Сортировка по умолчанию (по убыванию даты оплаты)
