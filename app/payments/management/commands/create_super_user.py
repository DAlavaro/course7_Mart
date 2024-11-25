# app/payments/management/commands/create_super_user.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from app.users.models import CustomUser, UserRoles


class Command(BaseCommand):
    help = "Создаёт суперпользователя с предопределёнными данными и добавляет его в группу Admin"

    def handle(self, *args, **kwargs):
        email = 'admin@sky.pro'
        password = 'admin'

        # Проверяем, существует ли пользователь с таким email
        if CustomUser.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'Пользователь с email "{email}" уже существует.'))
            return

        # Проверяем, существует ли группа Admin
        admin_group, created = Group.objects.get_or_create(name='Admin')
        if created:
            self.stdout.write(self.style.SUCCESS('Группа Admin была создана.'))

        # Создаём суперпользователя
        user = CustomUser.objects.create(
            email=email,
            is_staff=True,
            is_superuser=True,
            role=UserRoles.ADMIN
        )
        user.set_password(password)
        user.save()

        # Добавляем суперпользователя в группу Admin
        user.groups.add(admin_group)

        self.stdout.write(
            self.style.SUCCESS(f'Суперпользователь "{email}" успешно создан, добавлен в группу "Admin" и имеет пароль "{password}".')
        )
