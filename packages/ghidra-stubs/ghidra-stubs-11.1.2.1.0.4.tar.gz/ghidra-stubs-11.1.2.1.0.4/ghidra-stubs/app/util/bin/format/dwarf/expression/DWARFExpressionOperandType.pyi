from typing import List
from typing import overload
import ghidra.app.util.bin.format.dwarf.expression
import java.lang
import java.util


class DWARFExpressionOperandType(java.lang.Enum):
    ADDR: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    DWARF_INT: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    SIZED_BLOB: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    S_BYTE: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    S_INT: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    S_LEB128: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    S_LONG: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    S_SHORT: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    U_BYTE: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    U_INT: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    U_LEB128: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    U_LONG: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType
    U_SHORT: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType







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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def valueToString(__a0: long, __a1: ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType) -> unicode: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.dwarf.expression.DWARFExpressionOperandType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

