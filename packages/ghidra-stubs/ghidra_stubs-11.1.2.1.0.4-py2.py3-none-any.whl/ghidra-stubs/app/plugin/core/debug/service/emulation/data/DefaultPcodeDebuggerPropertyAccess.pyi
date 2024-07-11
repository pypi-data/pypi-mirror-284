from typing import overload
import ghidra.pcode.exec.trace.data
import ghidra.program.model.address
import java.lang


class DefaultPcodeDebuggerPropertyAccess(ghidra.pcode.exec.trace.data.DefaultPcodeTracePropertyAccess):








    def clear(self, __a0: ghidra.program.model.address.AddressRange) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, __a0: ghidra.program.model.address.Address) -> object: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, __a0: ghidra.program.model.address.Address, __a1: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

