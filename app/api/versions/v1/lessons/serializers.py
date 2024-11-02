# app/api/versions/v1/lessons/serializers.py
from rest_framework import serializers
from app.lessons.models import Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'