from typing import overload
import ghidra.dbg.target
import java.lang


class RecorderSimpleRegisterSet(object):




    def __init__(self, __a0: ghidra.debug.api.model.TraceRecorder): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def updateRegisters(self, __a0: ghidra.dbg.target.TargetRegisterBank, __a1: ghidra.dbg.target.TargetRegisterBank) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

