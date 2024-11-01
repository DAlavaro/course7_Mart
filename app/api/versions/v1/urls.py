# app/api/versions/v1/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.api.versions.v1.courses.views import CourseViewSet
from config import settings
from .lessons.urls import urlpatterns as lesson_urls


router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', include(lesson_urls)),
]