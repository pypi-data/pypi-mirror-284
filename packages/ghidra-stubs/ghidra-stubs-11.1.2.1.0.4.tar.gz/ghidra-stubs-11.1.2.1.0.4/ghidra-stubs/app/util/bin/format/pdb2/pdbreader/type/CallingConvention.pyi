from typing import List
from typing import overload
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import java.lang
import java.util


class CallingConvention(java.lang.Enum):
    ALPHACALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    AM33CALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    ARMCALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    CLRCALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    FAR_C: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    FAR_FAST: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    FAR_PASCAL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    FAR_STD: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    FAR_SYS: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    GENERIC: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    INLINE: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    M32RCALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    MIPSCALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    NEAR_C: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    NEAR_FAST: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    NEAR_PASCAL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    NEAR_STD: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    NEAR_SYS: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    NEAR_VECTOR: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    PPCCALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    RESERVED: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    SH5CALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    SHCALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    SKIPPED: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    THISCALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    TRICALL: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention
    UNKNOWN: ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def describeConstable(self) -> java.util.Optional: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getInfo(self) -> unicode: ...

    def getValue(self) -> int: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.type.CallingConvention]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def info(self) -> unicode: ...

    @property
    def value(self) -> int: ...