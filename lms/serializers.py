from rest_framework import serializers

from lms.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'course', 'user']


class CourseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    lesson_count = serializers.SerializerMethodField()

    lessons = LessonSerializer(many=True, required=False)

    @staticmethod
    def get_lesson_count(obj):
        return Lesson.objects.filter(course=obj.pk).count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'img_preview', 'description', 'lesson_count', 'lessons', 'user']


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
