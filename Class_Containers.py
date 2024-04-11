from __future__ import annotations
import Descriptor_UNUM
import Descriptor_ARRAY
import Decos_HELPER
from typing import Callable, Any, Iterator, List

class ListContainer:
    data: Descriptor_ARRAY.LimitedTypeListDescriptor     = Descriptor_ARRAY.LimitedTypeListDescriptor(object)
    def __init__(self, initialDataType: type = object) -> None:
        self.data = initialDataType
        self._dataType = initialDataType
    
    
    @property
    def datatype(self):
        if len(self.data) == 0: return self._dataType
        else: return self.data[0].__class__
        
    @datatype.setter
    def property(self): self._dataType = self.data[0].__class__
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}[{self.datatype}]: {self.data}>"
    
    def append(self, other: ListContainer._dataType) -> None:
        if isinstance(other, self.data[0].__class__):
            self.data.append(other)
        else: raise TypeError("Not a matching type")
    
    def __iter__(self) -> Iterator[ListContainer._datatype]: return iter(self.data)
    
    def sort(self, key: Callable[[Any], None] = None) -> None:
        self.data.sort(key=key)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.data
    
    @Decos_HELPER.checkPositiveIntegerArgs
    def __getitem__(self, index: int = None) -> ListContainer._datatype:
        return self.data[index]

    def __len__(self): return len(self.data)


class Array(ListContainer):
    length: Descriptor_UNUM.UINT = Descriptor_UNUM.UINT()
    data: Descriptor_ARRAY.LimitedTypeLengthDescriptor = Descriptor_ARRAY.LimitedTypeLengthDescriptor()
    def __init__(self, initialDataType: type = object, length: int= 32) -> None:
        super().__init__(initialDataType)
        self.data   = initialDataType
        self.length = length

    def append(self, other: ListContainer._dataType) -> None:
        if len(self) < self.length: return super().append(other)
        else: raise AttributeError(f"{self.__class__.__name__}: tried exceeding the limited length ({self.length}) of the contained by appending <{other}: {other.__class__.__name__}")