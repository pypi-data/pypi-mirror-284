from typing import overload
import ghidra.app.plugin.core.debug.service.model.launch
import ghidra.app.services
import ghidra.framework.plugintool
import ghidra.program.model.listing
import java.lang
import java.util


class DbgDebuggerProgramLaunchOpinion(ghidra.app.plugin.core.debug.service.model.launch.AbstractDebuggerProgramLaunchOpinion):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOffers(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.framework.plugintool.PluginTool, __a2: ghidra.app.services.DebuggerModelService) -> java.util.Collection: ...

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

