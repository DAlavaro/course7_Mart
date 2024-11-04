# app/payments/management/commands/add_payments.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from app.users.models import CustomUser
from app.courses.models import Course
from app.lessons.models import Lesson
from app.payments.models import Payment


class Command(BaseCommand):
    help = 'Add new payments to the database without deleting existing data'

    def handle(self, *args, **kwargs):
        # Retrieving existing users, courses, and lessons
        self.stdout.write(self.style.SUCCESS('Retrieving existing users, courses, and lessons...'))

        user1 = CustomUser.objects.filter(email='user1@example.com').first()
        user2 = CustomUser.objects.filter(email='user2@example.com').first()

        course1 = Course.objects.filter(name='Course 1').first()
        course2 = Course.objects.filter(name='Course 2').first()

        lesson1 = Lesson.objects.filter(name='Lesson 1').first()
        lesson2 = Lesson.objects.filter(name='Lesson 2').first()

        # Creating payments with specific dates
        self.stdout.write(self.style.SUCCESS('Creating new payments...'))

        Payment.objects.create(
            user=user1,
            amount=100.00,
            course=course1,
            payment_method='cash',
        )

        Payment.objects.create(
            user=user2,
            amount=150.00,
            lesson=lesson2,
            payment_method='transfer',
        )

        self.stdout.write(self.style.SUCCESS('New payments added successfully!'))
