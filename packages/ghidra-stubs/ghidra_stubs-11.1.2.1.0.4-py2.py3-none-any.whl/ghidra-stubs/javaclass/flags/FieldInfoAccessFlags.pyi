from typing import List
from typing import overload
import ghidra.javaclass.flags
import java.lang
import java.util


class FieldInfoAccessFlags(java.lang.Enum):
    ACC_ENUM: ghidra.javaclass.flags.FieldInfoAccessFlags
    ACC_FINAL: ghidra.javaclass.flags.FieldInfoAccessFlags
    ACC_PRIVATE: ghidra.javaclass.flags.FieldInfoAccessFlags
    ACC_PROTECTED: ghidra.javaclass.flags.FieldInfoAccessFlags
    ACC_PUBLIC: ghidra.javaclass.flags.FieldInfoAccessFlags
    ACC_STATIC: ghidra.javaclass.flags.FieldInfoAccessFlags
    ACC_SYNTHETIC: ghidra.javaclass.flags.FieldInfoAccessFlags
    ACC_TRANSIENT: ghidra.javaclass.flags.FieldInfoAccessFlags
    ACC_VOLATILE: ghidra.javaclass.flags.FieldInfoAccessFlags







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def describeConstable(self) -> java.util.Optional: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getValue(self) -> int: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.javaclass.flags.FieldInfoAccessFlags: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.javaclass.flags.FieldInfoAccessFlags]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def value(self) -> int: ...