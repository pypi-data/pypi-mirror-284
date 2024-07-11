from typing import overload
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class Token(object, ghidra.app.util.bin.StructConverter):
    ASCII: ghidra.program.model.data.DataType
    BYTE: ghidra.program.model.data.DataType
    DWORD: ghidra.program.model.data.DataType
    IBO32: ghidra.program.model.data.DataType
    IBO64: ghidra.program.model.data.DataType
    NAME: unicode = u'MINIDUMP_TOKEN'
    POINTER: ghidra.program.model.data.DataType
    QWORD: ghidra.program.model.data.DataType
    SLEB128: ghidra.program.model.data.SignedLeb128DataType
    STRING: ghidra.program.model.data.DataType
    ULEB128: ghidra.program.model.data.UnsignedLeb128DataType
    UTF16: ghidra.program.model.data.DataType
    UTF8: ghidra.program.model.data.DataType
    VOID: ghidra.program.model.data.DataType
    WORD: ghidra.program.model.data.DataType







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getTokenHandle(self) -> long: ...

    def getTokenId(self) -> int: ...

    def getTokenSize(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setTokenHandle(self, __a0: long) -> None: ...

    def setTokenId(self, __a0: int) -> None: ...

    def setTokenSize(self, __a0: int) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def tokenHandle(self) -> long: ...

    @tokenHandle.setter
    def tokenHandle(self, value: long) -> None: ...

    @property
    def tokenId(self) -> int: ...

    @tokenId.setter
    def tokenId(self, value: int) -> None: ...

    @property
    def tokenSize(self) -> int: ...

    @tokenSize.setter
    def tokenSize(self, value: int) -> None: ...