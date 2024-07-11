from typing import overload
import ghidra.debug.api.model
import ghidra.program.model.address
import java.lang


class DefaultDebuggerMemoryMapper(object, ghidra.debug.api.model.DebuggerMemoryMapper):




    def __init__(self, __a0: ghidra.program.model.lang.Language, __a1: ghidra.dbg.DebuggerObjectModel): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def targetToTrace(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    @overload
    def targetToTrace(self, __a0: ghidra.program.model.address.AddressRange) -> ghidra.program.model.address.AddressRange: ...

    def targetToTraceTruncated(self, __a0: ghidra.program.model.address.AddressRange) -> ghidra.program.model.address.AddressRange: ...

    def toString(self) -> unicode: ...

    @overload
    def traceToTarget(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    @overload
    def traceToTarget(self, __a0: ghidra.program.model.address.AddressRange) -> ghidra.program.model.address.AddressRange: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

