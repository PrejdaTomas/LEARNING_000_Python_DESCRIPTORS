from __future__ import annotations
import typing, operator
from numbers import Number
from functools import reduce as functoolsReduce, cache as functoolsCache

def printDecoratedLine(iptStr: str = None, start: bool = True) -> str:
    stars = len(iptStr)*"*"
    if start: print(iptStr), print(stars)
    else: print(stars), print(iptStr)
        
class ArrayMath(object):
    @staticmethod
    def mathFunc(operatorIpt: typing.Operator = None) -> typing.Callable[[Number, Number], Number]: return lambda a,b: operatorIpt(a,b)

    @staticmethod
    def sum(values1D: typing.Iterator = None) -> Number: return functoolsReduce(lambda a,b: ArrayMath.mathFunc(operator.add)(a,b), values1D)

    @staticmethod
    def sub(values1D: typing.Iterator = None) -> Number: return functoolsReduce(lambda a,b: ArrayMath.mathFunc(operator.sub)(a,b), values1D)

    @staticmethod
    def mul(values1D: typing.Iterator = None) -> Number: return functoolsReduce(lambda a,b: ArrayMath.mathFunc(operator.mul)(a,b), values1D)

    @staticmethod
    def div(values1D: typing.Iterator = None) -> Number: return functoolsReduce(lambda a,b: ArrayMath.mathFunc(operator.truediv)(a,b), values1D)



def getAttributeValues(*args: object) -> typing.Tuple[object, ...]:
    return tuple((vars(arg).values() for arg in args))

def numericZip(*args: typing.Iterator[Number]) -> typing.Iterator[typing.Tuple[float,...]]:
    for value in zip(*args):
        #yield value
        if all((isinstance(a, Number) for a in value)):
            yield value