# api/versions/v1/users/views.py
from rest_framework import viewsets

from .serializers import UserSerializer, CustomUser



class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    