from typing import overload
import ghidra.dbg.target
import ghidra.trace.model.stack
import ghidra.trace.model.thread
import java.lang


class ManagedStackRecorder(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSuccessorFrameLevel(self, __a0: ghidra.dbg.target.TargetObject) -> int: ...

    def getTargetStackFrame(self, __a0: int) -> ghidra.dbg.target.TargetStackFrame: ...

    def getTraceStackFrame(self, __a0: ghidra.trace.model.thread.TraceThread, __a1: int) -> ghidra.trace.model.stack.TraceStackFrame: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def offerStackFrame(self, __a0: ghidra.dbg.target.TargetStackFrame) -> None: ...

    def recordStack(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

