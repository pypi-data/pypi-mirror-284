from typing import overload
import ghidra.dbg.target
import ghidra.util.task
import java.lang
import java.util.concurrent


class SymbolRecorder(object):




    def __init__(self, __a0: ghidra.debug.api.model.TraceRecorder): ...



    @overload
    def captureSymbols(self, __a0: ghidra.dbg.target.TargetModule, __a1: ghidra.util.task.TaskMonitor) -> java.util.concurrent.CompletableFuture: ...

    @overload
    def captureSymbols(self, __a0: ghidra.dbg.target.TargetSymbolNamespace, __a1: ghidra.util.task.TaskMonitor) -> java.util.concurrent.CompletableFuture: ...

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

