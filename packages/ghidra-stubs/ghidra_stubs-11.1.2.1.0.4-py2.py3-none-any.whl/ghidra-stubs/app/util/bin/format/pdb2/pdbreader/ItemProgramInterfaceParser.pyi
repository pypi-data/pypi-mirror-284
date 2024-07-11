from typing import overload
import ghidra.app.util.bin.format.pdb2.pdbreader
import java.lang


class ItemProgramInterfaceParser(ghidra.app.util.bin.format.pdb2.pdbreader.TypeProgramInterfaceParser):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def hackCheckNoNameForStream(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.NameTable) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb) -> ghidra.app.util.bin.format.pdb2.pdbreader.TypeProgramInterface: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

