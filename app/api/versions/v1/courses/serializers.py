# app/api/versions/v1/courses/serializers.py
from rest_framework import serializers
from app.courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons.all().count()

    class Meta:
        model = Course
        fields = '__all__'