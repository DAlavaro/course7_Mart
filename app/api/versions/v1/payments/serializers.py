# app/api/versions/v1/payments/serializers.py
from app.payments.models import Payment
from rest_framework import serializers


class PaymentListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    paid_item = serializers.SerializerMethodField()
    formatted_date_pay = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    def get_paid_item(self, obj):
        # Возвращаем название курса или урока в зависимости от оплаченного объекта
        if obj.course:
            return obj.course.name
        elif obj.lesson:
            return obj.lesson.name
        return None

    def get_formatted_date_pay(self, obj):
        # Форматируем дату как "день, месяц, год, время"
        return obj.date_pay.strftime("%d %B %Y %H:%M:%S")

    class Meta:
        model = Payment
        fields = ['user', 'formatted_date_pay', 'paid_item', 'amount', 'payment_method']
