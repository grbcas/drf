from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.permissions import IsUser, ReadOnly
from users.serializers import UserSerializer


class UserListAPIView(generics.ListAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserUpdateAPIView(generics.UpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]





# class ExampleView(APIView):
#     permission_classes = [IsAuthenticated | ReadOnly]
#
#     def get(self, request, format=None):
#         content = {
#             'status': 'request was permitted'
#         }
#         return Response(content)

