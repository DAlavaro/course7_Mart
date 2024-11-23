# api/versions/v1/courses/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CourseSerializer, Course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
