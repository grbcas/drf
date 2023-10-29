from django.urls import path

from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter

from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, SubscribeDestroyAPIView, PaymentRetrieveUpdateAPIView, PaymentListCreateAPIView
from lms.views import SubscribeCreateAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', viewset=CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('payments/', PaymentListCreateAPIView.as_view(), name='list'),
    # path('payments/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateAPIView.as_view(), name='payment_retrieve'),

    path('subscription/', SubscribeCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/<int:pk>/', SubscribeDestroyAPIView.as_view(), name='subscription_delete'),

] + router.urls
