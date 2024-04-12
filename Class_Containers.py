from __future__ import annotations
import Descriptor_UNUM
import Descriptor_ARRAY
import Decos_HELPER
import typing
from numbers import Number

import Typing_HELPER

# proc dedim z takove kraviny, jako je typing.Generic?
# protoze to zpusobi binding toho Typing_HELPER.GENERICINSTANCE
# ergo mene mypy chyb
# https://stackoverflow.com/questions/73848672/binding-a-mypy-type-variable-for-a-type-alias-in-the-type-annotation-of-an-assig
# 
class ListContainer(typing.Iterable, typing.Generic[Typing_HELPER.GENERICINSTANCE]):
    data: typing.List[Typing_HELPER.GENERICINSTANCE] = Descriptor_ARRAY.LimitedTypeListDescriptor(Typing_HELPER.GENERICINSTANCE)
    
    def __init__(self, initialDataType: Typing_HELPER.GENERICINSTANCE) -> None:
        self.data = initialDataType
        self._dataType:type = initialDataType
    
    
    @property
    def datatype(self) -> Typing_HELPER.GENERICTYPE:
        if len(self.data) == 0: return self._dataType
        else: return type(self.data[0])
        
    @datatype.setter
    def property(self) -> None: self._dataType = self.data[0].__class__
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}[{self.datatype}]: {self.data}>"
    
    def append(self, other: Typing_HELPER.GENERICTYPE) -> None:
        if isinstance(other, self.data[0].__class__):
            self.data.append(other)
        else: raise TypeError("Not a matching type")
        
    def __len__(self) -> int: return len(self.data)
    
    def __iter__(self) -> typing.Iterator[Typing_HELPER.GENERICTYPE]:
        #proc neiteruji primo sebe? no protoze mam jinak nekonecnou smycku.
        return iter(self.data)
    
    def __next__(self) -> Typing_HELPER.GENERICTYPE:
        try: return next(self.data)
        except: raise StopIteration
        
    #pouzil jsem: typing.Callable[[bool], None] = None)
    #ale krici to, ze chce: "Callable[[Never], SupportsDunderLT[Any] | SupportsDunderGT[Any]]
    def sort(self, keyUser: Typing_HELPER.SORTINGKEY = None) -> None:
        self.data.sort(key=keyUser)
    
    def __call__(self, *args: typing.Any, **kwds: typing.Any) -> typing.Iterator[Typing_HELPER.GENERICTYPE]:
        return self.__iter__()
    
    
    @Decos_HELPER.checkPositiveIntegerArgs
    def __getitem__(self, index: int) -> Typing_HELPER.GENERICINSTANCE:
        value = self.data[index]
        return value


class Array(ListContainer):
    length: Descriptor_UNUM.UINT = Descriptor_UNUM.UINT()
    data: typing.List[Typing_HELPER.GENERICINSTANCE] = Descriptor_ARRAY.LimitedTypeLengthDescriptor(Typing_HELPER.GENERICINSTANCE)
    
    def __init__(self, initialDataType: Typing_HELPER.GENERICINSTANCE, length: int= 32) -> None:
        super().__init__(initialDataType)
        #self.data: Descriptor_ARRAY.LimitedTypeLengthDescriptor[Typing_HELPER.GENERICINSTANCE]    = initialDataType
        self.length:int = length

    def append(self, other: Typing_HELPER.GENERICINSTANCE) -> None:
        if len(self) < self.length: return super().append(other)
        else: raise AttributeError(f"{self.__class__.__name__}: tried exceeding the limited length ({self.length}) of the contained by appending <{other}: {other.__class__.__name__}") 