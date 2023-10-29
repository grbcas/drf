from django_filters import rest_framework as filters
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from lms.models import Course, Lesson, Payment, Subscription
from lms.permissions import IsModerator, IsOwnerOrModerator, IsOwner
from lms.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer
from lms.services.payments import create_payment, retrieve_payment


class LmsPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page size'
    max_page_size = 10


class CourseViewSet(viewsets.ModelViewSet):
    """ Viewset for Course """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LmsPageNumberPagination

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
    permission_classes = [IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    pagination_class = LmsPageNumberPagination
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
    permission_classes = [IsAdminUser | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser | IsOwner]


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class SubscribeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated & IsOwnerOrModerator]

    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('course', 'lesson', 'payment_method')
    ordering_fields = ('date',)

    def perform_create(self, serializer):
        payment_id = create_payment(self.request.data['amount'])
        print(payment_id)
        serializer.is_valid()
        serializer.save(stripe_id=payment_id)


class PaymentRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_update(self, serializer):
        obj = self.get_object()
        print(obj)
        print(obj.stripe_id)
        payment_id = obj.stripe_id
        get_payment_response = retrieve_payment(payment_id)
        print(payment_id, get_payment_response)
        if get_payment_response:
            serializer.save(status=1)
