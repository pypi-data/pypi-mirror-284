from typing import List
from typing import overload
import ghidra.dbg.target
import java.lang
import java.util


class ObjectElementRow(object):




    def __init__(self, __a0: ghidra.dbg.target.TargetObject, __a1: ghidra.app.plugin.core.debug.gui.objects.DebuggerObjectsProvider): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getKeys(self) -> List[object]: ...

    def getTargetObject(self) -> ghidra.dbg.target.TargetObject: ...

    def getValue(self) -> object: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAttributes(self, __a0: java.util.Map) -> None: ...

    def setCurrentKey(self, __a0: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def attributes(self) -> None: ...  # No getter available.

    @attributes.setter
    def attributes(self, value: java.util.Map) -> None: ...

    @property
    def currentKey(self) -> None: ...  # No getter available.

    @currentKey.setter
    def currentKey(self, value: unicode) -> None: ...

    @property
    def keys(self) -> List[object]: ...

    @property
    def targetObject(self) -> ghidra.dbg.target.TargetObject: ...

    @property
    def value(self) -> object: ...