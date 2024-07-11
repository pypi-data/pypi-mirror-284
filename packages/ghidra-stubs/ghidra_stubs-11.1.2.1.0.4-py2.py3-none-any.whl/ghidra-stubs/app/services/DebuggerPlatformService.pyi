from typing import overload
import ghidra.debug.api.platform
import ghidra.trace.model
import ghidra.trace.model.target
import java.lang


class DebuggerPlatformService(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentMapperFor(self, __a0: ghidra.trace.model.Trace) -> ghidra.debug.api.platform.DebuggerPlatformMapper: ...

    def getMapper(self, __a0: ghidra.trace.model.Trace, __a1: ghidra.trace.model.target.TraceObject, __a2: long) -> ghidra.debug.api.platform.DebuggerPlatformMapper: ...

    def getNewMapper(self, __a0: ghidra.trace.model.Trace, __a1: ghidra.trace.model.target.TraceObject, __a2: long) -> ghidra.debug.api.platform.DebuggerPlatformMapper: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCurrentMapperFor(self, __a0: ghidra.trace.model.Trace, __a1: ghidra.debug.api.platform.DebuggerPlatformMapper, __a2: long) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

