# app/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_avatar(file, model)->str:
    return f'avatars/{model.pk}/{file}'


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    city = models.CharField(max_length=100, verbose_name='City')
    avatar = models.ImageField(upload_to=upload_avatar, null=True, blank=True, verbose_name='Avatar')
    role = models.CharField(max_length=20, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='Role')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email