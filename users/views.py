from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from lms.permissions import IsOwnerOrModerator, IsOwner
from users.models import User
from users.permissions import IsUserOrReadOnly
from users.serializers import UserSerializer, UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = super().perform_create(serializer)

        if user is not None:
            password = self.request.data['password']
            user.set_password(password)
            user.save()
        return user


class UserListAPIView(generics.ListAPIView):

    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


# class UserUpdateAPIView(generics.UpdateAPIView):
#
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     permission_classes = [IsUserOrReadOnly]


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):

    queryset = User.objects.all()

    def get_serializer_class(self):
        if IsOwnerOrModerator():
            return UserSerializer
        else:
            return UserProfileSerializer
