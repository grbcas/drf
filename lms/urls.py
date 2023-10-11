from django.urls import path

from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter

from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, PaymentListAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', viewset=CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='create'),
    path('lessons/', LessonListAPIView.as_view(), name='list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='retrieve'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete'),

    path('payments/', PaymentListAPIView.as_view(), name='list'),
] + router.urls
