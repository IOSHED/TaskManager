from task.lib.calendar.interface import GetData


class Weather(GetData):
    def __init__(self, degrees: float, wind_speed: float, humidity: float) -> None:
        self.degrees = round(degrees)
        self.wind_speed = round(wind_speed, 1)
        self.humidity = humidity

    def get(self) -> 'Weather':
        return self
