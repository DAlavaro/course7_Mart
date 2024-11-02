# Generated by Django 5.1 on 2024-11-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('lessons', '0002_lesson_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ManyToManyField(blank=True, related_name='lessons', to='courses.course', verbose_name='Course'),
        ),
    ]