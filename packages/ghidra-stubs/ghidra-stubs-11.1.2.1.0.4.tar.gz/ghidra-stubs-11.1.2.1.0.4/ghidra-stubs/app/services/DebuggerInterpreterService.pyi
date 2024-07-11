from typing import overload
import ghidra.dbg.target
import ghidra.debug.api.interpreter
import java.lang


class DebuggerInterpreterService(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def showConsole(self, __a0: ghidra.dbg.target.TargetConsole) -> ghidra.debug.api.interpreter.DebuggerInterpreterConnection: ...

    @overload
    def showConsole(self, __a0: ghidra.dbg.target.TargetInterpreter) -> ghidra.debug.api.interpreter.DebuggerInterpreterConnection: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

