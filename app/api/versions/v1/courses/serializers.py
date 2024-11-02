# app/api/versions/v1/courses/serializers.py
from rest_framework import serializers

from app.api.versions.v1.lessons.serializers import LessonSerializer
from app.courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_lessons(self, obj):
        return LessonSerializer(obj.lessons.all(), many=True).data

    class Meta:
        model = Course
        fields = '__all__'