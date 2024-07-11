from typing import overload
import ghidra.app.plugin.core.debug.disassemble
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.trace.model.guest
import ghidra.trace.model.thread
import ghidra.util.classfinder
import java.lang


class DisassemblyInject(ghidra.util.classfinder.ExtensionPoint, object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInfo(self) -> ghidra.app.plugin.core.debug.disassemble.DisassemblyInjectInfo: ...

    def getPriority(self) -> int: ...

    def hashCode(self) -> int: ...

    def isApplicable(self, __a0: ghidra.trace.model.guest.TracePlatform) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def post(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.trace.model.guest.TracePlatform, __a2: long, __a3: ghidra.program.model.address.AddressSetView) -> None: ...

    def pre(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.app.plugin.core.debug.disassemble.TraceDisassembleCommand, __a2: ghidra.trace.model.guest.TracePlatform, __a3: long, __a4: ghidra.trace.model.thread.TraceThread, __a5: ghidra.program.model.address.AddressSetView, __a6: ghidra.program.model.address.AddressSetView) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def info(self) -> ghidra.app.plugin.core.debug.disassemble.DisassemblyInjectInfo: ...

    @property
    def priority(self) -> int: ...