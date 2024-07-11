from typing import List
from typing import overload
import java.lang
import java.util


class ShellUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def generateEnvBlock(__a0: java.util.Map) -> unicode: ...

    @staticmethod
    def generateLine(__a0: List[object]) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parseArgs(__a0: unicode) -> List[object]: ...

    @overload
    @staticmethod
    def removePath(__a0: unicode) -> unicode: ...

    @overload
    @staticmethod
    def removePath(__a0: List[object]) -> List[object]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

