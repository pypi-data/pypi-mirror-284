from typing import overload
import ghidra.debug.api.model
import ghidra.framework.plugintool
import ghidra.program.model.lang
import ghidra.trace.model
import java.lang


class DebuggerTargetTraceMapper(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getTraceCompilerSpec(self) -> ghidra.program.model.lang.CompilerSpec: ...

    def getTraceLanguage(self) -> ghidra.program.model.lang.Language: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def startRecording(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.trace.model.Trace) -> ghidra.debug.api.model.TraceRecorder: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def traceCompilerSpec(self) -> ghidra.program.model.lang.CompilerSpec: ...

    @property
    def traceLanguage(self) -> ghidra.program.model.lang.Language: ...