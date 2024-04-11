import typing
from Descriptor_UNUM import UINT as UNUM_Descriptors_UINT

class LimitedTypeListDescriptor(object):
    def __init__(self, dataType: type= object):
        self.dataType = dataType
        
    def __get__(self, instance, owner) -> typing.List[object]:
        if instance is None: return self
        if "_data" not in instance.__dict__: instance._data = []
        return instance._data
    
    def __set__(self, instance, value) -> None:
        if isinstance(value, type):
            self.dataType = value
            instance._data = [value(ob) for ob in instance.data]
            instance._dataType = value
            
        elif isinstance(value, self.dataType):
            if "_data" not in instance.__dict__: instance._data = []
            instance._data.append(value)
        
        else:
            try:    raise ValueError(f"{instance.__name__}: Only {self.dataType} are allowed in the list, you passed: <{value}, {value.__class__.__name__}>")
            except: raise ValueError(f"{instance.__class__.__name__}: Only {self.dataType} are allowed in the list, you passed: <{value}, {value.__class__.__name__}>")
        
    def __delete__(self, instance) -> None:
        if "_data" in instance.__dict__: instance._data = []



class LimitedTypeLengthDescriptor(LimitedTypeListDescriptor):
    length:UNUM_Descriptors_UINT = UNUM_Descriptors_UINT()
    def __init__(self, dataType: type = object, length: int = 32):
        super().__init__(dataType)
        self.length = length
    
    def __set__(self, instance, value) -> None:
        if len(instance.data) == self.length and not isinstance(value, type):
            raise MemoryError(f"{instance.__class__.__name__}: attempting to add a value (count = {self.length+1}) to a fixed length list (maximum = {self.length} {self.dataType.__name__} values)")
        return super().__set__(instance, value)