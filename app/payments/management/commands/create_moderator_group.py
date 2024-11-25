# app/users/management/сommands/create_moderator_group.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Создание групп Admin и Moderator с соответствующими правами'

    def handle(self, *args, **kwargs):
        # Удаляем старые группы, если они существуют
        Group.objects.filter(name='Admin').delete()
        Group.objects.filter(name='Moderators').delete()

        # Создаём группу Admin
        admin_group, created = Group.objects.get_or_create(name='Admin')
        self.stdout.write(self.style.SUCCESS('Создана группа Admin'))

        # Добавляем все права группе Admin
        all_permissions = Permission.objects.all()
        admin_group.permissions.set(all_permissions)
        self.stdout.write(self.style.SUCCESS('Добавлены все права группе Admin'))

        # Создаём группу Moderators
        moderator_group, created = Group.objects.get_or_create(name='Moderators')
        self.stdout.write(self.style.SUCCESS('Создана группа Moderators'))

        # Добавляем только права на просмотр и редактирование
        moderator_permissions = Permission.objects.filter(
            codename__in=['view_course', 'change_course', 'view_lesson', 'change_lesson']
        )
        moderator_group.permissions.set(moderator_permissions)
        self.stdout.write(self.style.SUCCESS('Добавлены права группе Moderators'))

        self.stdout.write(self.style.SUCCESS('Настройка групп завершена!'))
