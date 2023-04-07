import abc
import typing

T = typing.TypeVar('T')

class IStorage(abc.ABC, typing.Generic[T]):
    '''
    Storage interface - factory
    '''
    @abc.abstractmethod
    def add(self, item: T): ...

    @abc.abstractmethod
    def remove(self, item: T): ...

    @abc.abstractmethod
    def get_all(self) -> typing.Sequence[T]: ...
