
from task.lib.calendar.interface import IParser


class ParseDegrees(IParser):
    def parse(self) -> 'ParseDegrees':
        ...


class ParseWindSpeed(IParser):
    def parse(self) -> 'ParseWindSpeed':
        ...


class ParseHumidity(IParser):
    def parse(self) -> 'ParseHumidity':
        ...
