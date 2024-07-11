from typing import List
from typing import overload
import ghidra.app.util.pdb.pdbapplicator
import java.lang
import java.util


class ObjectOrientedClassLayout(java.lang.Enum):
    BASIC_SIMPLE_COMPLEX: ghidra.app.util.pdb.pdbapplicator.ObjectOrientedClassLayout
    COMPLEX: ghidra.app.util.pdb.pdbapplicator.ObjectOrientedClassLayout
    MEMBERS_ONLY: ghidra.app.util.pdb.pdbapplicator.ObjectOrientedClassLayout
    SIMPLE_COMPLEX: ghidra.app.util.pdb.pdbapplicator.ObjectOrientedClassLayout







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def describeConstable(self) -> java.util.Optional: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.pdb.pdbapplicator.ObjectOrientedClassLayout: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.pdb.pdbapplicator.ObjectOrientedClassLayout]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

