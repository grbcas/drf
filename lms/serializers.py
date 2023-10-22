from rest_framework import serializers

from lms.models import Course, Lesson, Payment, Subscription
from lms.validators import OnlyYoutubeUrl


class LessonSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    link_video = serializers.URLField(validators=[OnlyYoutubeUrl()])

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'course', 'user', 'link_video']


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, required=False)
    subscription = SubscriptionSerializer()

    @staticmethod
    def get_lesson_count(obj):
        return Lesson.objects.filter(course=obj.pk).count()

    @staticmethod
    def get_subscription(obj):
        return Subscription.objects.filter(course=obj.pk)

    class Meta:
        model = Course
        fields = ['id', 'name', 'img_preview', 'description', 'lesson_count', 'lessons', 'user', 'subscription']


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
