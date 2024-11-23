from django.core.management.base import BaseCommand
from django.utils import timezone
from app.users.models import CustomUser, UserRoles
from app.courses.models import Course
from app.lessons.models import Lesson
from app.payments.models import Payment


class Command(BaseCommand):
    help = 'Add new users, payments, courses, and lessons to the database'

    def handle(self, *args, **kwargs):
        # Создание пользователей
        self.stdout.write(self.style.SUCCESS('Creating users...'))

        moderator, created = CustomUser.objects.get_or_create(
            email='moderator@example.com',
            defaults={
                'role': UserRoles.MODERATOR,
                'password': CustomUser.objects.make_random_password(),
            },
        )
        if created:
            moderator.set_password('123')
            moderator.save()

        user1, created = CustomUser.objects.get_or_create(
            email='user1@example.com',
            defaults={
                'role': UserRoles.MEMBER,
                'password': CustomUser.objects.make_random_password(),
            },
        )
        if created:
            user1.set_password('123')
            user1.save()

        user2, created = CustomUser.objects.get_or_create(
            email='user2@example.com',
            defaults={
                'role': UserRoles.MEMBER,
                'password': CustomUser.objects.make_random_password(),
            },
        )
        if created:
            user2.set_password('123')
            user2.save()

        self.stdout.write(self.style.SUCCESS('Users created successfully!'))

        # Получение курсов и уроков
        self.stdout.write(self.style.SUCCESS('Retrieving existing courses and lessons...'))

        course1 = Course.objects.filter(name='Course 1').first()
        course2 = Course.objects.filter(name='Course 2').first()

        lesson1 = Lesson.objects.filter(name='Lesson 1').first()
        lesson2 = Lesson.objects.filter(name='Lesson 2').first()

        # Создание платежей
        self.stdout.write(self.style.SUCCESS('Creating new payments...'))

        if user1 and course1:
            Payment.objects.create(
                user=user1,
                amount=100.00,
                course=course1,
                payment_method='cash',
            )

        if user2 and lesson2:
            Payment.objects.create(
                user=user2,
                amount=150.00,
                lesson=lesson2,
                payment_method='transfer',
            )

        self.stdout.write(self.style.SUCCESS('New payments added successfully!'))

