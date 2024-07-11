from typing import overload
import ghidra.program.model.data.ISF
import java.lang


class IsfComponent(ghidra.program.model.data.ISF.AbstractIsfObject):
    comment: unicode
    field_name: unicode
    length: int
    location: unicode
    name: unicode
    noFieldName: bool
    offset: int
    ordinal: int
    settings: List[object]
    type: ghidra.program.model.data.ISF.IsfObject



    def __init__(self, __a0: ghidra.program.model.data.DataTypeComponent, __a1: ghidra.program.model.data.ISF.IsfObject): ...



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

