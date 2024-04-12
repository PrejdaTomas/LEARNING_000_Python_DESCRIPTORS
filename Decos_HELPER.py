from Funcs_HELPER import printDecoratedLine
from typing import Callable, Any
from datetime import datetime
from time import perf_counter as timePerfCounter

#simplified and substituted by checkSameType
#def checkSingleType(objectType: type) -> Callable:
#    def _executor(func: Callable) -> Callable:
#        def _inner(*args: Any, **kwargs: Any) -> Callable:
#            print(objectType, args)
#            for _index, arg in enumerate(args):
#                if not isinstance(arg, objectType):
#                    raise TypeError(f"{func.__name__}: attempting to pass a non-{objectType.__name__} argument [{_index}]: <{arg}: {arg.__class__.__name__}>")
#            return func(*args, **kwargs)
#        return _inner
#    return _executor

def checkSameType(func: Callable) -> Callable:
    def _inner(self, *args: Any, **kwargs: Any) -> Callable:
        for _index, arg in enumerate(args):
            if not isinstance(arg, type(self)):
                raise TypeError(f"{func.__name__}: attempting to pass a non-{type(self).__name__} argument [{_index}]: <{arg}: {arg.__class__.__name__}>")
        return func(self, *args, **kwargs)
    return _inner

def checkPositiveIntegerArgs(func: Callable) -> Callable:
    """Checks, if the passed function got only positive integers in the arguments, if yes, the function return value is returned"""
    def _inner(*args: Any, **kwargs: Any):
        for _ in range(1, len(args)):
            if not isinstance(args[_], int): raise TypeError(f"{func.__name__}: expects a positive integer, you passed <{args[_]}, {args[_].__class__.__name__}>")
            if args[_] < 0: raise ValueError(f"{func.__name__}: expects a positive integer, you passed <{args[_]}, {args[_].__class__.__name__}>")
        return func(*args, **kwargs)
    _inner.__name__ = func.__name__
    return _inner

def printFuncName(func: Callable) -> Callable:
    """Prints the paassed function name before and after execution and returns the function return value"""
    def _inner(*args: Any, **kwargs: Any) -> Callable:
        printDecoratedLine(f"[{datetime.now()}] Running: {func.__name__}", start=True)
        result =  func(*args, **kwargs)
        printDecoratedLine(f"[{datetime.now()}] Executed: {func.__name__}", start=False)
        return result
    
    _inner.__name__ = func.__name__
    return _inner

def timeFunc(func: Callable) -> Callable:
    """Times the passed function and retrusn the function return value"""
    def _inner(*args: Any, **kwargs: Any) -> Callable:
        start   = timePerfCounter()
        result  =  func(*args, **kwargs)
        print(f"Took: {timePerfCounter()-start} s to execute!\n")
        return result
    _inner.__name__ = func.__name__
    return _inner