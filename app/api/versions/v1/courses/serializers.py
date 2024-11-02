# app/api/versions/v1/courses/serializers.py
from rest_framework import serializers
from app.courses.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'