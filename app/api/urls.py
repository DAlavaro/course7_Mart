# app/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api.versions.v1.courses.views import CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
