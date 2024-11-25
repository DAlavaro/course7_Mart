from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import LessonBaseSerializer, Lesson
from .permissions import IsModeratorOrOwner
from ..users.models import UserRoles


class LessonBaseAPIView:
    queryset = Lesson.objects.all()
    serializer_class = LessonBaseSerializer
    permission_classes = [IsAuthenticated, IsModeratorOrOwner]


class LessonListAPIView(LessonBaseAPIView, generics.ListAPIView):
    """
    Модераторы и владельцы могут видеть список уроков.
    """
    pass


class LessonCreateAPIView(LessonBaseAPIView, generics.CreateAPIView):
    """
    Только участники с ролью MEMBER могут создавать свои уроки.
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveAPIView(LessonBaseAPIView, generics.RetrieveAPIView):
    """
    Модераторы и владельцы могут видеть детали урока.
    """
    pass


class LessonUpdateAPIView(LessonBaseAPIView, generics.UpdateAPIView):
    """
    Модераторы могут редактировать любые уроки, владельцы только свои.
    """
    pass


class LessonDestroyAPIView(LessonBaseAPIView, generics.DestroyAPIView):
    """
    Только владельцы могут удалять свои уроки.
    """
    def has_permission(self, request, view):
        # Модераторы не могут удалять
        if request.user.role == UserRoles.MODERATOR:
            return False
        return super().has_permission(request, view)
