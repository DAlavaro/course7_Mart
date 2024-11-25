# api/versions/v1/lessons/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import LessonBaseSerializer, Lesson
from ..users.permissions import IsModerator


class LessonBaseAPIView:
    queryset = Lesson.objects.all()
    serializer_class = LessonBaseSerializer


class LessonListAPIView(LessonBaseAPIView, generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsModerator]


class LessonCreateAPIView(LessonBaseAPIView, generics.CreateAPIView):
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(LessonBaseAPIView, generics.RetrieveAPIView):
   permission_classes = [IsAuthenticated, IsModerator]


class LessonUpdateAPIView(LessonBaseAPIView, generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsModerator]


class LessonDestroyAPIView(LessonBaseAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]