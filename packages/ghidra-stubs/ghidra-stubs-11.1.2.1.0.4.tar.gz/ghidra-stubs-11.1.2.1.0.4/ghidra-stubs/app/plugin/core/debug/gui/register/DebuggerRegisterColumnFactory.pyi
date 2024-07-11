from typing import overload
import docking.widgets.table
import ghidra.util.classfinder
import java.lang


class DebuggerRegisterColumnFactory(ghidra.util.classfinder.ExtensionPoint, object):








    def create(self) -> docking.widgets.table.DynamicTableColumn: ...

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

