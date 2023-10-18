from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser


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

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserUpdateAPIView(generics.UpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUserOrReadOnly]


class UserRetrieveAPIView(generics.RetrieveAPIView):

    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    # queryset = User.objects.values("email")

    def get_permissions(self):
        permission_classes = [IsUserOrReadOnly]
        return [permission() for permission in permission_classes]


