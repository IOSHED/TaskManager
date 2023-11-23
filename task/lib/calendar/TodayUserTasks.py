from accounts.models import CustomUser
from task.lib.calendar.interface import GetData
from task.lib.filters import get_task_today


class TodayUserTasks(GetData):
    def __init__(self, user: CustomUser) -> None:
        self.tasks = get_task_today(user)[:3]

    def get(self) -> 'TodayUserTasks':
        return self

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < len(self.tasks):
            result = self.tasks[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration
