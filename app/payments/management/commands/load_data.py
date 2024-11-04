from django.core.management.base import BaseCommand
from app.users.models import CustomUser
from app.courses.models import Course
from app.lessons.models import Lesson
from app.payments.models import Payment
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        # Clearing existing data
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        Payment.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()
        CustomUser.objects.all().delete()

        # Creating courses
        self.stdout.write(self.style.SUCCESS('Creating courses...'))
        course1 = Course.objects.create(name='Course 1', description='Description for Course 1')
        course2 = Course.objects.create(name='Course 2', description='Description for Course 2')

        # Creating lessons
        self.stdout.write(self.style.SUCCESS('Creating lessons...'))
        lesson1 = Lesson.objects.create(name='Lesson 1', description='Description for Lesson 1')
        lesson2 = Lesson.objects.create(name='Lesson 2', description='Description for Lesson 2')

        # Linking lessons to courses
        course1.lessons.add(lesson1)
        course1.lessons.add(lesson2)
        course2.lessons.add(lesson2)

        # Creating users
        self.stdout.write(self.style.SUCCESS('Creating users...'))
        user1 = CustomUser(email='user1@example.com', phone='1234567890', city='City1')
        user1.set_password('password123')
        user1.save()

        user2 = CustomUser(email='user2@example.com', phone='0987654321', city='City2')
        user2.set_password('password456')
        user2.save()

        # Creating payments
        self.stdout.write(self.style.SUCCESS('Creating payments...'))
        Payment.objects.create(user=user1, amount=100.00, course=course1, payment_method='cash')
        Payment.objects.create(user=user2, amount=150.00, lesson=lesson2, payment_method='transfer')

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
