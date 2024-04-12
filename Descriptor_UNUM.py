from __future__ import annotations
from Funcs_HELPER import *
import Typing_HELPER
from typing import Generic

#Generic se týká dědění ze tříd, nebo obecných interfaců
class UNUMBER(Generic[Typing_HELPER.NUMBER]):
    """UNUMBER is a base object for all positive numbers which inherit its methods modified to the selected numeric-type _dataType"""
    _dataType:type = type#Generic[Typing_HELPER.NUMBER]
    
    def __set_name__(self, owner: type, name:str) -> None:
        self.private_name = "_" + name
    
    def __get__(self, instance: typing.Self, owner: type) -> typing.Self:
        return getattr(instance, self.private_name)
    
    def __set__(self, instance: typing.Self, value: Typing_HELPER.NUMBER) -> None:
        if not isinstance(value, self.__class__._dataType):
            if value < 0.0: raise TypeError(f"{instance.__class__.__name__}: attempting to set {self.__class__.__name__} to a non-{self._dataType.__name__} value: <{value}: {value.__class__.__name__} >,  by the way, it is negative")
            else:           raise TypeError(f"{instance.__class__.__name__}: attempting to set {self.__class__.__name__} to a non-{self._dataType.__name__} value: <{value}: {value.__class__.__name__} >")
        else:
            if value < 0.0:
                raise TypeError(f"{instance.__class__.__name__}: attempting to set {self.__class__.__name__} to a non-{self._dataType.__name__} value: {value}")
            setattr(instance, self.private_name, value)
    
    def __delete__(self, instance: typing.Self) -> None:
        raise AttributeError(f"{instance.__class__.__name__}: attempting to delete the stored value {self.__class__.__name__}: {getattr(instance, self.private_name)}, which is not permitted")

    def __setattr__(self, name: str, value: typing.Any) -> None:
        if name == "_dataType":
            raise AttributeError(f"{self.__class__.__name__}: cannot change the _dataType after creation!")
        return super().__setattr__(name, value)

class UINT(UNUMBER):
    """UINT is a data-descriptor object used to specify positive integer valued attributes"""
    _dataType = int
    
class UFLOAT(UNUMBER):
    """UFLOAT is a data-descriptor object used to specify positive integer valued attributes"""
    _dataType = float