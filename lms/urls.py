from django.urls import path

from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter

from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, PaymentListAPIView, SubscribeDestroyAPIView
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

    path('payments/', PaymentListAPIView.as_view(), name='list'),
    path('subscription/', SubscribeCreateAPIView.as_view(), name='create'),
    path('subscription/<int:pk>/', SubscribeDestroyAPIView.as_view(), name='delete'),

] + router.urls
