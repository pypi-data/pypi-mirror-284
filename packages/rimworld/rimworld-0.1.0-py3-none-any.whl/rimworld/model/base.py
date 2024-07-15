from typing import Generic, Protocol, Sequence, TypeAlias

from lxml import etree


class SerializationError(Exception):
    ...


class DeserializationError(Exception):
    ...


Serializer: TypeAlias = 'XmlTypeSerializer|XmlNestedSerializer'


class XmlSerializer:
    def __init__(self, serializers: Sequence['Serializer']) -> None:
        self._serializers = serializers

    def serialize(self, value, node: etree._Element):
        type_ = type(value)
        for serializer in self._serializers:
            if serializer.check_type(type_):
                match serializer:
                    case XmlTypeSerializer():
                        serializer.serialize(value, node)
                    case XmlNestedSerializer():
                        serializer.serialize(self, value, node)
                return
        raise SerializationError(f"Don't know how to serialize {type_}")

    def deserialize(self, type_, node: etree._Element):
        for serializer in self._serializers:
            if serializer.check_type(type_):
                match serializer:
                    case XmlTypeSerializer():
                        serializer.deserialize(node)
                    case XmlNestedSerializer():
                        serializer.deserialize(self, node)
        raise DeserializationError(f"Don't know how to deserialize {type_}")


class XmlTypeSerializer[T](Protocol):
    def check_type(self, type_) -> bool:
        ...

    def serialize(self, value: T, node: etree._Element):
        ...

    def deserialize(self, node: etree._Element) -> T:
        ...
    

class XmlNestedSerializer[T](Protocol):
    def check_type(self, type_) -> bool:
        ...

    def serialize(self, serializer: XmlSerializer, value: T, node: etree._Element):
        ...

    def deserialize(self, serializer: XmlSerializer, node: etree._Element) -> T:
        ...
