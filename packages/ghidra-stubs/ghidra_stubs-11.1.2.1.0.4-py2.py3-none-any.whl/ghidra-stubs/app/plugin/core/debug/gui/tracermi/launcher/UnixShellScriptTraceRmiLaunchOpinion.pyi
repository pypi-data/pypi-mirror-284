from typing import overload
import ghidra.app.plugin.core.debug.gui.tracermi.launcher
import ghidra.framework.options
import ghidra.program.model.listing
import java.lang
import java.util


class UnixShellScriptTraceRmiLaunchOpinion(ghidra.app.plugin.core.debug.gui.tracermi.launcher.AbstractTraceRmiLaunchOpinion):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOffers(self, __a0: ghidra.app.plugin.core.debug.gui.tracermi.launcher.TraceRmiLauncherServicePlugin, __a1: ghidra.program.model.listing.Program) -> java.util.Collection: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def registerOptions(self, __a0: ghidra.framework.options.Options) -> None: ...

    def requiresRefresh(self, __a0: unicode) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

