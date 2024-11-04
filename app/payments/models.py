# app/payments/models.py
from django.contrib.auth import get_user_model
from django.db import models


class Payment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT, verbose_name='User')
    date_pay = models.DateTimeField(auto_now_add=True, verbose_name='Create at')
    course = models.ForeignKey('courses.Course', on_delete=models.RESTRICT, null=True, blank=True,
                               verbose_name='Paid Course')
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.RESTRICT, null=True, blank=True,
                               verbose_name='Paid Lesson')
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Amount')
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('transfer', 'Transfer')
    ]
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, verbose_name='Payment Method')

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.date_pay}"

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'