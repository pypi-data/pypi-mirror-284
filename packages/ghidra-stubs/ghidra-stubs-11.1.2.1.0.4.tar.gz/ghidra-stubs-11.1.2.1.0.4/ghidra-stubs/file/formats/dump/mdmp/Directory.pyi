from typing import overload
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class Directory(object, ghidra.app.util.bin.StructConverter):
    ASCII: ghidra.program.model.data.DataType
    BYTE: ghidra.program.model.data.DataType
    DWORD: ghidra.program.model.data.DataType
    EXCEPTION_STREAM: int = 6
    HANDLE_LIST_STREAM: int = 12
    IBO32: ghidra.program.model.data.DataType
    IBO64: ghidra.program.model.data.DataType
    MEMORY64_LIST_STREAM: int = 9
    MEMORY_INFO_LIST_STREAM: int = 16
    MEMORY_LIST_STREAM: int = 5
    MISC_INFO_STREAM: int = 15
    MODULE_LIST_STREAM: int = 4
    NAME: unicode = u'MINIDUMP_DIRECTORY'
    POINTER: ghidra.program.model.data.DataType
    QWORD: ghidra.program.model.data.DataType
    SLEB128: ghidra.program.model.data.SignedLeb128DataType
    STRING: ghidra.program.model.data.DataType
    SYSTEM_INFO_STREAM: int = 7
    THREAD_EX_LIST_STREAM: int = 8
    THREAD_LIST_STREAM: int = 3
    TOKEN_LIST_STREAM: int = 19
    ULEB128: ghidra.program.model.data.UnsignedLeb128DataType
    UNLOADED_MODULE_LIST_STREAM: int = 14
    UTF16: ghidra.program.model.data.DataType
    UTF8: ghidra.program.model.data.DataType
    VOID: ghidra.program.model.data.DataType
    WORD: ghidra.program.model.data.DataType







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataSize(self) -> int: ...

    def getRVA(self) -> long: ...

    def getReadableName(self) -> unicode: ...

    def getStreamType(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDataSize(self, __a0: int) -> None: ...

    def setRVA(self, __a0: long) -> None: ...

    def setStreamType(self, __a0: int) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def RVA(self) -> long: ...

    @RVA.setter
    def RVA(self, value: long) -> None: ...

    @property
    def dataSize(self) -> int: ...

    @dataSize.setter
    def dataSize(self, value: int) -> None: ...

    @property
    def readableName(self) -> unicode: ...

    @property
    def streamType(self) -> int: ...

    @streamType.setter
    def streamType(self, value: int) -> None: ...