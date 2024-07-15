from enum import Enum
from typing import Annotated, Any, Literal
from pydantic import Field, PlainSerializer, PlainValidator, computed_field, field_serializer, field_validator, validator, BaseModel
from lxml import etree
import xmltodict


class Success(Enum):
    Always='Always'
    Never='Never'
    Invert='Invert'
    Normal='Normal'



MayRequire = Annotated[
        list, 
        PlainSerializer(lambda x: ','.join(x), return_type=str), 
        PlainValidator(lambda x: x.split(',')),
        ]

Stupid = Annotated[
        int,
        PlainValidator(lambda x: int(x)+1000),
        PlainSerializer(lambda x: 'kkk'+str(x), return_type=str), 
        ]


Value_ = Annotated[
        etree._Element,
        PlainValidator(lambda x: etree.fromstring(xmltodict.unparse(x).encode('utf-8'))),
        PlainSerializer(lambda x: xmltodict.parse(etree.tostring(x, encoding='utf-8').decode('utf-8')), return_type=dict),
        ]


class PatchOperationModel(BaseModel):
    Class: str = Field(alias='@Class')
    success: Success = Success.Normal
    may_require: MayRequire|None = Field(None, alias='@MayRequire')
    value: Value_|None = None
    stupid: Stupid = 0

class PatchOperationInsert(PatchOperationModel):
    class_: Literal['PatchOperationInsert'] = Field(alias='@Class')

class PatchOperationAdd(PatchOperationModel):
    class_: Literal['PatchOperationAdd'] = Field(alias='@Class')

class Patch(BaseModel):
    Operation: list[PatchOperationInsert|PatchOperationAdd]


class Root(BaseModel):
    Patch: Patch 



    
