from task.lib.calendar.interface import GetData
from task.lib.calendar.parsers import ParseDegrees, ParseWindSpeed, ParseHumidity


class Weather(GetData):
    def __init__(self) -> None:
        self.degrees = ParseDegrees().parse()
        self.wind_speed = ParseWindSpeed().parse()
        self.humidity = ParseHumidity().parse()

    def get(self) -> 'Weather':
        return self
