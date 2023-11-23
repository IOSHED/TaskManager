from django.db import models

from accounts.models import CustomUser


class Task(models.Model):

    name = models.TextField(max_length=255)
    description = models.TextField(max_length=510, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    send_notify_at = models.DateTimeField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    complete_at = models.DateField(null=True, blank=True)

    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'Task {self.name}'
