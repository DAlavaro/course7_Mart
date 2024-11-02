# app/api/urls.py
from django.urls import path, include


app_name = 'api'

urlpatterns = [
    path('v1/', include('app.api.versions.v1.urls')),
]
