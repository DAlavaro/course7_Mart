# api/versions/v1/lessons/permissions.py
from rest_framework.permissions import BasePermission
from app.users.models import UserRoles


class IsModerator(BasePermission):


    class IsModerator(BasePermission):
        """
            Разрешение для модераторов: только просмотр и редактирование
        """
        message = 'Недостаточно прав для выполнения этого действия.'
        def has_permission(self, request, view):
            return request.user.groups.filter(name='Moderators').exists()
