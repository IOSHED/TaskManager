from django.db import models


class Task(models.Model):

    name = models.TextField(max_length=255, null=True)
    description = models.TextField(max_length=510, null=True)

    send_notify_at = models.DateTimeField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    complete_at = models.DateField(null=True)

    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'Task {self.name}'
