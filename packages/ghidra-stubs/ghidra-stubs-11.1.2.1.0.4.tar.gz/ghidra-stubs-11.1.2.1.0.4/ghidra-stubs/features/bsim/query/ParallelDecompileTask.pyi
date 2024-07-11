from typing import overload
import java.lang
import java.util


class ParallelDecompileTask(object):




    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.util.task.TaskMonitor, __a2: ghidra.features.bsim.query.DecompileFunctionTask): ...



    def decompile(self, __a0: java.util.Iterator, __a1: int) -> None: ...

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

