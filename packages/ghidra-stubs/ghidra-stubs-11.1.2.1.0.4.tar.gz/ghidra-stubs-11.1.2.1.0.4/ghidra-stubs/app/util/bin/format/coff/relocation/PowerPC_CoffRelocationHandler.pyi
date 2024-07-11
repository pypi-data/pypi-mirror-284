from typing import overload
import ghidra.app.util.bin.format.coff
import ghidra.app.util.bin.format.coff.relocation
import ghidra.program.model.address
import ghidra.program.model.reloc
import java.lang


class PowerPC_CoffRelocationHandler(object, ghidra.app.util.bin.format.coff.relocation.CoffRelocationHandler):
    IMAGE_REL_PPC_ABSOLUTE: int = 0
    IMAGE_REL_PPC_ADDR14: int = 5
    IMAGE_REL_PPC_ADDR16: int = 4
    IMAGE_REL_PPC_ADDR24: int = 3
    IMAGE_REL_PPC_ADDR32: int = 2
    IMAGE_REL_PPC_ADDR32NB: int = 10
    IMAGE_REL_PPC_ADDR64: int = 1
    IMAGE_REL_PPC_GPREL: int = 21
    IMAGE_REL_PPC_PAIR: int = 18
    IMAGE_REL_PPC_REFHI: int = 16
    IMAGE_REL_PPC_REFLO: int = 17
    IMAGE_REL_PPC_REL14: int = 7
    IMAGE_REL_PPC_REL24: int = 6
    IMAGE_REL_PPC_SECREL: int = 11
    IMAGE_REL_PPC_SECREL16: int = 15
    IMAGE_REL_PPC_SECRELLO: int = 19
    IMAGE_REL_PPC_SECTION: int = 12
    IMAGE_REL_PPC_TOKEN: int = 22



    def __init__(self): ...



    def canRelocate(self, __a0: ghidra.app.util.bin.format.coff.CoffFileHeader) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def relocate(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.app.util.bin.format.coff.CoffRelocation, __a2: ghidra.app.util.bin.format.coff.relocation.CoffRelocationContext) -> ghidra.program.model.reloc.RelocationResult: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

