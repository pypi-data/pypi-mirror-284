from typing import overload
import ghidra.debug.api.tracemgr
import ghidra.program.model.address
import java.lang


class CachedBytePage(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getByte(self, __a0: ghidra.debug.api.tracemgr.DebuggerCoordinates, __a1: ghidra.program.model.address.Address) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def invalidate(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

