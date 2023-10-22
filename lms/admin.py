from django.contrib import admin

# Register your models here.
from lms.models import Course, Lesson, Payment, Subscription

# admin.site.register(Course)
# admin.site.register(Lesson)
admin.site.register(Payment)
admin.site.register(Subscription)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    model = Lesson
    list_display = ('pk', 'name', 'course', 'user')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('pk', 'name', 'user')
