from enum import Enum, EnumMeta, auto
from typing import Any, Dict, Mapping, Type, TypeVar, TypedDict
from icecream import ic
from pydantic import BaseModel
from dataclasses import dataclass


class BloodType(Enum):
    A =  auto()
    B = auto()
    AB = auto()
    O = auto()


class PatientTypedDict(TypedDict):
    name: Any
    age: int
    blood_type: BloodType

@dataclass
class PatientDataclass:
    name: str
    age: int
    blood_type: BloodType

class PatientPydantic(BaseModel):
    name: str
    age: int
    blood_type: BloodType

_T = TypeVar('_T')


def match_template(src: Mapping[str,Any], template: Type[_T]) -> _T:
    annotations = template.__annotations__
    unpack: Dict[str,Any] = {}
    for src_key, type_hint in zip(src, annotations.values()):
        content = src[src_key]
        if isinstance(type_hint,EnumMeta):
            content = type_hint[content]
        unpack[src_key] = content
    return template(**unpack)

bruh = {
    "name": "Jacques",
    "age" : 12,
    "blood_type": BloodType.A
}


bruh2 = match_template(bruh,PatientDataclass)
ic(match_template(bruh,PatientTypedDict))
ic(match_template(bruh,PatientPydantic))
