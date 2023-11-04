from celery import shared_task

from lms.services.subsribtions import send_course_updates


@shared_task
def task_send_updates(course_id: int, url: str) -> None:
    """Функция для отправки писем об обновлениях курса"""

    send_course_updates(course_id, url)

