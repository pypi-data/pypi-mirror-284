from typing import List
from typing import overload
import ghidra.program.model.data
import ghidra.program.model.lang
import java.lang


class ProgramStructureProviderContext(object, ghidra.program.model.lang.DataTypeProviderContext):




    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.util.ProgramLocation): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.data.Structure, __a3: int): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeComponent(self, __a0: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def getDataTypeComponents(self, __a0: int, __a1: int) -> List[ghidra.program.model.data.DataTypeComponent]: ...

    def getUniqueName(self, __a0: unicode) -> unicode: ...

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

