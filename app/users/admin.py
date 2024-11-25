# app/users/admin.py
from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active')
    ordering = ('email',)
