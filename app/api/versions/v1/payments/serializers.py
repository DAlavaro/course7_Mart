# app/api/versions/v1/payments/serializers.py
from app.payments.models import Payment
from rest_framework import serializers


class PaymentListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    formatted_date_pay = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    def get_formatted_date_pay(self, obj):
        # Форматируем дату как "день, месяц, год, время"
        return obj.date_pay.strftime("%d %B %Y %H:%M:%S")

    class Meta:
        model = Payment
        fields = ['user', 'formatted_date_pay', 'course', 'lesson', 'amount', 'payment_method']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Убираем поле в зависимости от оплаченного элемента
        if instance.course:
            representation.pop('lesson', None)  # Убираем lesson, если оплачен курс
        elif instance.lesson:
            representation.pop('course', None)  # Убираем course, если оплачен урок

        return representation