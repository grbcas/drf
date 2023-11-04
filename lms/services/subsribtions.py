

from django.core.mail import send_mail

from config import settings
from lms.models import Subscription


def send_course_updates(course_id: int, url: str):
    subscriptions = Subscription.objects.filter(course=course_id).select_related('user', 'course')

    for subscription in subscriptions:
        send_mail(
            subject=f'Курс {subscription.course.name}',
            message=f'Обновления в курсе  ',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[subscription.user.email]
        )

    print(f'Рассылка {len(subscriptions)} писем)')
