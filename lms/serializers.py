from rest_framework import serializers

from lms.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'course']


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.SerializerMethodField()

    lessons = LessonSerializer(many=True, required=False)

    @staticmethod
    def get_lesson_count(obj):
        return Lesson.objects.filter(course=obj.pk).count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'img_preview', 'description', 'lesson_count', 'lessons']


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
