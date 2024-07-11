from typing import List
from typing import overload
import ghidra.app.util.bin.format.pdb2.pdbreader
import java.lang


class C13FileChecksums(ghidra.app.util.bin.format.pdb2.pdbreader.C13Section):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFileChecksums(self) -> List[object]: ...

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

    @property
    def fileChecksums(self) -> List[object]: ...