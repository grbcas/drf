from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserListAPIView, UserRetrieveAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='list'),
    path('users/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    path('users/detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]

