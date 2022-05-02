from typing import Generic, TypeVar

from .resource import Resource

T = TypeVar('T', bound=Resource)

class Converter(Generic[T]):
    @staticmethod
    def to_payload(resource: T):
        raise NotImplementedError

    @staticmethod
    def to_resource(payload) -> T:
        raise NotImplementedError
