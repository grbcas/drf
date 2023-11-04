import datetime
from datetime import timedelta
from django.utils import timezone

from users.models import User


def block_inactive_users():
    """ block all inactive users for more than one month """

    activity_period = timezone.now() - timedelta(days=1)
    users = User.objects.filter(last_login__lt=activity_period)
    regular_users = users.exclude(is_staff=True).exclude(is_superuser=True)

    regular_users.update(is_active=False)
