# app/api/versions/v1/payments/filter.py
from django_filters.rest_framework import FilterSet, filters
from app.payments.models import Payment

class PaymentFilter(FilterSet):
    paid_item_type = filters.CharFilter(method='filter_paid_item_type')
    payment_method = filters.ChoiceFilter(field_name='payment_method', choices=Payment.PAYMENT_METHOD_CHOICES)

    def filter_paid_item_type(self, queryset, name, value):
        if value == 'course':
            return queryset.filter(course__isnull=False, lesson__isnull=True)
        elif value == 'lesson':
            return queryset.filter(lesson__isnull=False, course__isnull=True)
        return queryset

    class Meta:
        model = Payment
        fields = ['paid_item_type', 'payment_method']
