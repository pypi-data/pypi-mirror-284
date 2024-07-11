from typing import overload
import ghidra.dbg.target
import java.lang


class RecorderBreakpointLocationResolver(object):




    def __init__(self, __a0: ghidra.app.plugin.core.debug.service.model.DefaultTraceRecorder, __a1: ghidra.dbg.target.TargetBreakpointLocation): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def updateBreakpoint(self, __a0: ghidra.dbg.target.TargetObject, __a1: ghidra.dbg.target.TargetBreakpointLocation) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

