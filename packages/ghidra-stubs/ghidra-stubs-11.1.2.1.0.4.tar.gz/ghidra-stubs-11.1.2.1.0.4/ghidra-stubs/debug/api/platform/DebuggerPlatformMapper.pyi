from typing import overload
import ghidra.debug.api.platform
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.trace.model.target
import ghidra.trace.model.thread
import ghidra.util.task
import java.lang


class DebuggerPlatformMapper(object):








    def addToTrace(self, __a0: long) -> None: ...

    def canInterpret(self, __a0: ghidra.trace.model.target.TraceObject, __a1: long) -> bool: ...

    def disassemble(self, __a0: ghidra.trace.model.thread.TraceThread, __a1: ghidra.trace.model.target.TraceObject, __a2: ghidra.program.model.address.Address, __a3: ghidra.program.model.address.AddressSetView, __a4: long, __a5: ghidra.util.task.TaskMonitor) -> ghidra.debug.api.platform.DisassemblyResult: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompilerSpec(self, __a0: ghidra.trace.model.target.TraceObject) -> ghidra.program.model.lang.CompilerSpec: ...

    def getLangauge(self, __a0: ghidra.trace.model.target.TraceObject) -> ghidra.program.model.lang.Language: ...

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

