from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from app.users.models import CustomUser, UserRoles
from app.courses.models import Course
from app.lessons.models import Lesson
from app.payments.models import Payment


class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        # Очистка существующих данных
        self.stdout.write(self.style.WARNING('Очищаем базу данных...'))
        Payment.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()
        CustomUser.objects.all().delete()

        # Создание пользователей
        self.stdout.write(self.style.SUCCESS('Создаем пользователей...'))

        moderator = CustomUser.objects.create(
            email='moderator@example.com',
            phone='1111111111',
            city='CityModerator',
            role=UserRoles.MODERATOR
        )
        moderator.set_password('123')
        moderator.save()

        # Добавляем пользователя в группу Moderators
        moderator_group = Group.objects.get(name='Moderators')
        moderator.groups.add(moderator_group)
        self.stdout.write(self.style.SUCCESS('Пользователь moderator добавлен в группу Moderators'))

        user1 = CustomUser.objects.create(
            email='user1@example.com',
            phone='1234567890',
            city='City1',
            role=UserRoles.MEMBER
        )
        user1.set_password('123')
        user1.save()

        user2 = CustomUser.objects.create(
            email='user2@example.com',
            phone='0987654321',
            city='City2',
            role=UserRoles.MEMBER
        )
        user2.set_password('123')
        user2.save()

        self.stdout.write(self.style.SUCCESS('Создание пользователей успешно завершено!'))

        # Создание курсов
        self.stdout.write(self.style.SUCCESS('Создаём курсы...'))
        course1 = Course.objects.create(name='Course 1', description='Description for Course 1')
        course1.owners.add(user1)

        course2 = Course.objects.create(name='Course 2', description='Description for Course 2')
        course2.owners.add(user2)

        # Создание уроков
        self.stdout.write(self.style.SUCCESS('Создаём уроки...'))
        lesson1 = Lesson.objects.create(name='Lesson 1', description='Description for Lesson 1')
        lesson1.owners.add(user1)
        lesson1.course.add(course1)

        lesson2 = Lesson.objects.create(name='Lesson 2', description='Description for Lesson 2')
        lesson2.owners.add(user1, user2)  # Пример нескольких владельцев
        lesson2.course.add(course1, course2)

        self.stdout.write(self.style.SUCCESS('Уроки и курсы успешно созданы!'))

        # Создание платежей
        self.stdout.write(self.style.SUCCESS('Создаём платежи...'))
        Payment.objects.create(user=user1, amount=100.00, course=course1, payment_method='cash')
        Payment.objects.create(user=user2, amount=150.00, lesson=lesson2, payment_method='transfer')

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена'))
