from django.db import models
from app.users.models import CustomUser


def upload_image(file, model) -> str:
    return f'lessons/{model.pk}/{file}'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name='Image')
    video = models.URLField(verbose_name='Video', null=True, blank=True)
    course = models.ManyToManyField('courses.Course', related_name='lessons', verbose_name='Course', blank=True)
    owners = models.ManyToManyField(CustomUser, related_name='owned_lessons', verbose_name='Owners', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
