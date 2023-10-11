from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='list'),
    path('users/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    ]

