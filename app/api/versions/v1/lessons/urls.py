# app/api/versions/v1/lessons/urls.py
from django.urls import path
from .views import LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonRetrieveAPIView, LessonDestroyAPIView

urlpatterns = [
    path('', LessonListAPIView.as_view(), name='list_view'),
    path('create/', LessonCreateAPIView.as_view(), name='create_view'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update_view'),
    path('retrieve/<int:pk>/', LessonRetrieveAPIView.as_view(), name='retrieve_view'),
    path('delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='destroy_view'),
]