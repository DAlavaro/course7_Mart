from django.db import models
from app.users.models import CustomUser


def upload_image(file, model) -> str:
    return f'courses/{model.pk}/{file}'


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name='Image')
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    owners = models.ManyToManyField(CustomUser, related_name='owned_courses', verbose_name='Owners', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
