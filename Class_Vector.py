from __future__ import annotations
from Funcs_HELPER import ArrayMath
from Funcs_HELPER import typing, functoolsCache, getAttributeValues
from itertools import chain
import Descriptor_UNUM
import Decos_HELPER


class positiveFloatVector(object):
    """
    A vector-type point object accepting only positive float values, non-positive float values will cause an exception to occur.
    Uses descriptors for attributes and the attribute count is fixed (workaround without slots).

    Args:
        object (_type_): base Python object

    Raises:
        AttributeError: raised if an attempt for dynamic attribute creation is made

    Returns:
        _type_: returns self
    """
    #__slots__:typing.Tuple[str]= "x", "y", "z", vyresit do budoucna
    x: Descriptor_UNUM.UFLOAT = Descriptor_UNUM.UFLOAT()
    y: Descriptor_UNUM.UFLOAT = Descriptor_UNUM.UFLOAT()
    z: Descriptor_UNUM.UFLOAT = Descriptor_UNUM.UFLOAT()
    
    @classmethod
    @functoolsCache
    def __attributes(cls) -> typing.Iterator[str]:
        """This "property" is used to check against when trying to dynamically assign a new attribute, which is forbidden.
        Cached so the call is not repeated constantly when there is an attribute check for exception handling.

        Returns:
            typing.Iterator[str]: the attributes of the class/instance (non-underscore are found, single-underscore values are created)
        """
        keys:   typing.Generator[str, None, None]  =   [val for val in (filtrval for filtrval in filter(lambda key: "__" not in key, cls.__dict__))]
        _keys:  typing.Generator[str, None, None] =   (f"_{val}" for val in keys)
        return list(chain(*zip(keys, _keys)))
 
    def __init__(self, x: float= None, y: float= None, z: float= None) -> None:
        """Instance initializer called after instantiation (but before attribute creation by __setattr__ or descriptor.__set__)

        Args:
            x (float, optional): positive x-value float. Defaults to None.
            y (float, optional): positive y-value float. Defaults to None.
            z (float, optional): positive z-value float. Defaults to None.
        """
        self.x: Descriptor_UNUM.UFLOAT = x
        self.y: Descriptor_UNUM.UFLOAT = y
        self.z: Descriptor_UNUM.UFLOAT = z
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: [{self.x:.6F}, {self.y:.6F}, {self.z:.6F}] @ {hex(id(self))}>"
    
    def __str__(self) -> str:
        return f"<{self.__class__.__name__}: [{self.x:.6F}, {self.y:.6F}, {self.z:.6F}]>"
    
    def __setattr__(self, name: str, value: typing.Any) -> None:
        if name in self.__class__.__attributes():
            super(self.__class__, self).__setattr__(name, value)
        else: raise AttributeError(f"{self.__class__.__name__}: cannot add another attribute <{name}>!")
    
    @HelperDecos.checkSameType
    def __add__(self, other: typing.Self) -> typing.Self:
        attrs = [ArrayMath.sum((a,b)) for a,b in zip(*getAttributeValues(self, other))]
        return self.__class__(*attrs)

    @HelperDecos.checkSameType
    def __sub__(self, other: typing.Self) -> typing.Self:
        attrs = [ArrayMath.sub((a,b)) for a,b in zip(*getAttributeValues(self, other))]
        return self.__class__(*attrs)

    @HelperDecos.checkSameType
    def __mul__(self, other: typing.Self) -> typing.Self:
        attrs = [ArrayMath.sum((a*b)) for a,b in zip(*getAttributeValues(self, other))]
        return self.__class__(*attrs)

    @HelperDecos.checkSameType
    def __div__(self, other: typing.Self) -> typing.Self:
        attrs = [ArrayMath.sub((a/b)) for a,b in zip(*getAttributeValues(self, other))]
        return self.__class__(*attrs)

    @property
    def coordinates(self) -> typing.Tuple[float, float, float]:
        return (self.x, self.y, self.z)
        
    @property
    def mag(self) -> float: return sum((a**2 for a in self.coordinates))**0.5
