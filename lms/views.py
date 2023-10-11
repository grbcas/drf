from rest_framework import viewsets

from lms.models import Course
from lms.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()     # AttributeError: type object 'Course' has no attribute 'objects'
