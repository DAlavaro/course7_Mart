# app/api/versions/v1/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .courses.views import CourseViewSet
from .users.views import UserViewSet
from config import settings
from .lessons.urls import urlpatterns as lesson_urls
from .payments.urls import urlpatterns as payment_urls


router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register(r'courses', CourseViewSet, basename='course')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', include(lesson_urls)),
    path('payments/', include(payment_urls)),
]