from typing import Callable,List,Any
from Class_Vector import positiveFloatVector
from random import uniform
from math import floor as cmathFloor
import Decos_HELPER
from Class_Containers import Array

if __name__  == "__main__":
    @Decos_HELPER.timeFunc
    @Decos_HELPER.printFuncName
    def main():
        count: int      = 25
        minNum: float   = uniform(0.0, 100.0)
        maxNum: float   = uniform(0.0, 100.0)
        minNum, maxNum  = min(minNum, maxNum), max(minNum, maxNum)
        
        randFloatFuncGen: Callable[[float, float, float], Callable] = lambda a,b, precision: round(uniform(a,b), precision)
        randFloat: Callable[[None],float]           = lambda: randFloatFuncGen(minNum, maxNum, 6)
        niceZfill: Callable[[List[Any]], int]       = lambda arrayIpt: cmathFloor(len(arrayIpt)/10)
        niceIndex: Callable[[List[Any], int], str]  = lambda arrayIpt, index:  str(index+1).zfill(niceZfill(arrayIpt))
            
        nuArray = Array(positiveFloatVector, count)
        for _ in range(count//2): nuArray.data = positiveFloatVector(x= randFloat(), y=  randFloat(), z=  randFloat())
        for _ in range(count//2, count): nuArray.data = nuArray[_ - count//2] + nuArray[1 + _ - count//2 ]
        nuArray.sort(keyUser=lambda item: item.x)

        for _, ob in enumerate(nuArray):
            print(niceIndex(nuArray, _), ob)

        for ob in nuArray:
            
        for _, ob in enumerate(nuArray):
            print(niceIndex(nuArray, _), ob)
        
        
        #for _ in range(count): nuArray.append(positiveFloatVector(1.2, 3.4, 5.6))
    main()
