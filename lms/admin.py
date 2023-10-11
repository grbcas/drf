from django.contrib import admin

# Register your models here.
from lms.models import Course, Lesson, Payment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Payment)
