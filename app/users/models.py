# app/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


def upload_avatar(file, model)->str:
    return f'avatars/{model.pk}/{file}'


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    city = models.CharField(max_length=100, verbose_name='City')
    avatar = models.ImageField(upload_to=upload_avatar, null=True, blank=True, verbose_name='Avatar')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email