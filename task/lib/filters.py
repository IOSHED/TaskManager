from datetime import date
from typing import List

from accounts.models import CustomUser
from task.models import Task


def get_task_today(user: CustomUser) -> List[Task]:
    return Task.objects.filter(user=user, send_notify_at__date=date.today())
