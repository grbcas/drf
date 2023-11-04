from celery import shared_task

from users.services import block_inactive_users


@shared_task
def user_block_task():
    block_inactive_users()
    print('block_inactive_users')
