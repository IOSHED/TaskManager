from abc import ABC, abstractmethod


class IParser(ABC):
    @abstractmethod
    def parse(self) -> 'IParser':
        ...


class GetData(ABC):
    @abstractmethod
    def get(self) -> 'GetData':
        ...
