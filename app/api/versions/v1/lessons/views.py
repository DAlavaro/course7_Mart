# api/versions/v1/lessons/views.py
from rest_framework import generics

from .serializers import LessonSerializer, Lesson


class LessonBaseAPIView:
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListAPIView(LessonBaseAPIView, generics.ListAPIView):
    pass


class LessonCreateAPIView(LessonBaseAPIView, generics.CreateAPIView):
    pass


class LessonRetrieveAPIView(LessonBaseAPIView, generics.RetrieveAPIView):
    pass


class LessonUpdateAPIView(LessonBaseAPIView, generics.UpdateAPIView):
    pass


class LessonDestroyAPIView(LessonBaseAPIView, generics.DestroyAPIView):
    pass