# api/versions/v1/courses/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CourseSerializer, Course
from ..users.permissions import IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]

    def get_permissions(self):
        """
        Переопределяем права доступа для отдельных методов.
        """
        if self.action in ['create', 'destroy']:
            # Создание и удаление курсов запрещено для модераторов
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'update', 'partial_update']:
            # Просмотр и редактирование курсов разрешено для модераторов
            self.permission_classes = [IsAuthenticated, IsModerator]
        return super().get_permissions()
