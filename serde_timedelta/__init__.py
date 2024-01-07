from datetime import timedelta
from plum import dispatch
from typing import Type, Any
import isodate
import serde


class Serializer:
    @dispatch
    def serialize(self, value: timedelta) -> Any:
        return isodate.duration_isoformat(value)


class Deserializer:
    @dispatch
    def deserialize(self, cls: Type[timedelta], value: Any) -> timedelta:
        return isodate.parse_duration(value)


def init() -> None:
    """
    Initialize pyserde-timedelta extenstion.
    Be sure to call this function before declaring pyserde class.
    """
    serde.add_serializer(Serializer())
    serde.add_deserializer(Deserializer())
