from rest_framework.permissions import BasePermission, SAFE_METHODS
from app.users.models import UserRoles


class IsModeratorOrOwner(BasePermission):
    """
    Разрешение для модераторов (только просмотр и редактирование)
    и владельцев (просмотр и редактирование своих записей).
    """

    def has_permission(self, request, view):
        # Разрешить доступ только аутентифицированным пользователям
        if not request.user.is_authenticated:
            return False

        # Модераторы могут только читать и редактировать
        if request.user.role == UserRoles.MODERATOR:
            return request.method in SAFE_METHODS or request.method in ['PUT', 'PATCH']

        # Администратор имеет полный доступ
        if request.user.role == UserRoles.ADMIN:
            return True

        # Пользователи с ролью MEMBER проверяются на уровне объекта
        return request.user.role == UserRoles.MEMBER

    def has_object_permission(self, request, view, obj):
        # Только владелец может видеть и изменять объект
        if request.user.role == UserRoles.MEMBER:
            return obj.owner == request.user

        # Модераторы могут только читать и редактировать
        if request.user.role == UserRoles.MODERATOR:
            return request.method in SAFE_METHODS or request.method in ['PUT', 'PATCH']

        # Администратор имеет полный доступ
        if request.user.role == UserRoles.ADMIN:
            return True

        return False
