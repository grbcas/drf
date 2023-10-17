from django_filters import rest_framework as filters
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from lms.models import Course, Lesson, Payment
from lms.permissions import IsModerator, IsOwnerOrModerator, IsOwner
from lms.serializers import CourseSerializer, LessonSerializer, PaymentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['update', 'partial_update', 'list', 'retrieve']:
            permission_classes = [IsAuthenticated & IsOwnerOrModerator]
            # permission_classes = [IsOwner]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUser]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & IsOwnerOrModerator]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & IsOwnerOrModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated & IsOwnerOrModerator]

    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('course', 'lesson', 'payment_method')
    ordering_fields = ('date',)
