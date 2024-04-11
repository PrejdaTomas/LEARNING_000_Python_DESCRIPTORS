from __future__ import annotations
from Funcs_HELPER import *


class UNUMBER(Number):
    """UNUMBER is a base object for all positive numbers which inherit its methods modified to the selected numeric-type _dataType"""
    _dataType:Number = Number
    
    def __set_name__(self, owner: typing.Type[UNUMBER], name:str) -> None:
        self.private_name = "_" + name
    
    def __get__(self, instance: UNUMBER, owner: typing.Type[UNUMBER]) -> UNUMBER:
        return getattr(instance, self.private_name)
    
    def __set__(self, instance: UNUMBER, value: Number) -> None:
        if not isinstance(value, self.__class__._dataType):
            if value < 0: 
                raise TypeError(f"{instance.__class__.__name__}: attempting to set {self.__class__.__name__} to a non-{self._dataType.__name__} value: <{value}: {value.__class__.__name__} >,  by the way, it is negative")
            else:
                raise TypeError(f"{instance.__class__.__name__}: attempting to set {self.__class__.__name__} to a non-{self._dataType.__name__} value: <{value}: {value.__class__.__name__} >")
            
        if value < 0:
            raise TypeError(f"{instance.__class__.__name__}: attempting to set {self.__class__.__name__} to a non-{self._dataType.__name__} value: {value}")
        setattr(instance, self.private_name, value)
    
    def __delete__(self, instance: UNUMBER) -> None:
        raise AttributeError(f"{instance.__class__.__name__}: attempting to delete the stored value {self.__class__.__name__}: {getattr(instance, self.private_name)}, which is not permitted")

    def __setattr__(self, name: str, value: typing.Any) -> None:
        if name == "_dataType":
            raise AttributeError(f"{self.__class__.__name__}: cannot change the _dataType after creation!")
        return super().__setattr__(name, value)

class UINT(UNUMBER):
    """UINT is a data-descriptor object used to specify positive integer valued attributes"""
    _dataType= int
    
class UFLOAT(UNUMBER):
    """UFLOAT is a data-descriptor object used to specify positive integer valued attributes"""
    _dataType = float