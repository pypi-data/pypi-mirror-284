from lxml import etree
from .base import DeserializationError, XmlNestedSerializer, XmlSerializer, XmlTypeSerializer



class BoolSerializer(XmlTypeSerializer[bool]):
    def check_type(self, type_) -> bool:
        return type_ is bool

    def serialize(self, value: bool, node: etree._Element):
        node.text = 'true' if value else 'false'

    def deserialize(self, node: etree._Element) -> bool:
        match node.text:
            case 'true':
                return True
            case 'false':
                return False
            case _:
                raise DeserializationError('bool node can only be True or False')



class IntSerializer(XmlTypeSerializer[int]):
    def check_type(self, type_) -> bool:
        return type_ is int 

    def serialize(self, value: int, node: etree._Element):
        node.text = str(value)

    def deserialize(self, node: etree._Element) -> int:
        if node.text is None:
            raise DeserializationError('int node should have text')
        try:
            return int(node.text)
        except ValueError:
            raise DeserializationError('could not deserialize as int')


class StrSerializer(XmlTypeSerializer[str]):
    def check_type(self, type_) -> bool:
        return type_ is str

    def serialize(self, value: str, node: etree._Element):
        node.text = value

    def deserialize(self, node: etree._Element) -> str:
        if node.text is None:
            raise DeserializationError('str node should have text')
        return node.text


class ListSerializer[T](XmlNestedSerializer[list[T]]):
    def check_type(self, type_) -> bool:
        return issubclass(type_, list)

    def serialize(self, serializer: XmlSerializer, value: list[T], node: etree._Element):
        for v in value:
            n = etree.Element('li')
            serializer.serialize(v, n)
            node.append(n)
