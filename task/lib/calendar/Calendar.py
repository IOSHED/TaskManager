from datetime import datetime

from task.lib.calendar.interface import GetData


class Calendar(GetData):
    def __init__(self) -> None:
        now = datetime.now()
        self.date = now.strftime("%d-%m-%y")
        self.short_date = now.strftime("%d %B")

    def get(self) -> 'Calendar':
        return self
