from typing import overload
import ghidra.program.model.data.ISF
import java.lang


class IsfProducer(object, ghidra.program.model.data.ISF.IsfObject):
    datetime: unicode
    name: unicode
    version: unicode



    def __init__(self, __a0: ghidra.program.model.listing.Program): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

