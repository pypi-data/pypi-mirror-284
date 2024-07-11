from typing import overload
import com.sun.jdi
import java.lang


class JdiThreadInfo(object):




    def __init__(self): ...



    @staticmethod
    def addThread(__a0: com.sun.jdi.ThreadReference) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def invalidateAll() -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeThread(__a0: com.sun.jdi.ThreadReference) -> None: ...

    @staticmethod
    def setCurrentThread(__a0: com.sun.jdi.ThreadReference) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

