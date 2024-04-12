from numbers import Number
import typing
import operator

class SupportsDunderLT(typing.Protocol):
    def __lt__(self, __other: typing.Any) -> bool:
        pass
   
class SupportsDunderGT(typing.Protocol):
    def __gt__(self, __other: typing.Any) -> bool:
        pass
     
GENERICINSTANCE         = typing.TypeVar("GENERICINSTANCE", bound=typing.Any)
GENERICTYPE             = typing.Type[GENERICINSTANCE]
STRNUM                  = typing.TypeVar("STRNUM", bound=str|Number)
NUMBER                  = typing.TypeVar("NUMBER", int,float)
OPERATORTYPE            = typing.TypeVar("OPERATORTYPE", bound=typing.Callable)
_SORTINGKEY             = typing.Callable[[typing.Never], SupportsDunderLT | SupportsDunderGT]
SORTINGKEY              = typing.Optional[_SORTINGKEY]
