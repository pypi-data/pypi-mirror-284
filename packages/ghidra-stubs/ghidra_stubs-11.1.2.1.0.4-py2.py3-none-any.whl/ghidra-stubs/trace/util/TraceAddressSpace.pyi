from typing import overload
import ghidra.program.model.address
import ghidra.trace.model.thread
import java.lang


class TraceAddressSpace(object):








    def equals(self, __a0: object) -> bool: ...

    def getAddressSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    def getClass(self) -> java.lang.Class: ...

    def getFrameLevel(self) -> int: ...

    def getThread(self) -> ghidra.trace.model.thread.TraceThread: ...

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

    @property
    def addressSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def frameLevel(self) -> int: ...

    @property
    def thread(self) -> ghidra.trace.model.thread.TraceThread: ...