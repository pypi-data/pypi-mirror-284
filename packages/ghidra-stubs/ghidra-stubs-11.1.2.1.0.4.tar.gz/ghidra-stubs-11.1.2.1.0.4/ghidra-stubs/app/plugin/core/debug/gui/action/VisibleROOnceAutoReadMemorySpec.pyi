from typing import overload
import ghidra.app.plugin.core.debug.gui.action
import ghidra.debug.api.tracemgr
import ghidra.framework.plugintool
import ghidra.program.model.address
import java.lang
import java.util
import java.util.concurrent
import java.util.function
import javax.swing


class VisibleROOnceAutoReadMemorySpec(object, ghidra.app.plugin.core.debug.gui.action.AutoReadMemorySpec):
    CONFIG_NAME: unicode = u'1_READ_VIS_RO_ONCE'
    PRIVATE: ghidra.app.plugin.core.debug.gui.action.AutoReadMemorySpec.Private



    def __init__(self): ...



    @staticmethod
    def allSpecs() -> java.util.Map: ...

    def doRead(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: java.util.function.Function) -> java.util.concurrent.CompletableFuture: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fromConfigName(__a0: unicode) -> ghidra.app.plugin.core.debug.gui.action.AutoReadMemorySpec: ...

    def getClass(self) -> java.lang.Class: ...

    def getConfigName(self) -> unicode: ...

    def getMenuIcon(self) -> javax.swing.Icon: ...

    def getMenuName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readMemory(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.debug.api.tracemgr.DebuggerCoordinates, __a2: ghidra.program.model.address.AddressSetView) -> java.util.concurrent.CompletableFuture: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def configName(self) -> unicode: ...

    @property
    def menuIcon(self) -> javax.swing.Icon: ...

    @property
    def menuName(self) -> unicode: ...