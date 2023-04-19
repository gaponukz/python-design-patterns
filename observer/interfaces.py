import abc
import typing

T = typing.TypeVar('T')

class ISubscriber(abc.ABC):
    @abc.abstractmethod
    def update(self, message: str): ...

    @abc.abstractmethod
    def __eq__(self, other: object): ...

class IPublisher(abc.ABC, typing.Generic[T]):
    @abc.abstractmethod
    def add_subscriber(self, subscriber: T): ...
    
    @abc.abstractmethod
    def remove_subscriber(self, subscriber): ...
    
    @abc.abstractmethod
    def notify_subscribers(self, message: str): ...
