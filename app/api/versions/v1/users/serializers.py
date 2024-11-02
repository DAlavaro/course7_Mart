# app/api/versions/v1/users/serializers.py

from rest_framework import serializers

from app.users.models import CustomUser



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email', 'phone', 'city', 'avatar']
