from typing import overload
import ghidra.app.util.bin
import ghidra.file.formats.dump.mdmp
import ghidra.program.model.data
import java.lang


class HandleOperationListStream(object, ghidra.app.util.bin.StructConverter):
    ASCII: ghidra.program.model.data.DataType
    BYTE: ghidra.program.model.data.DataType
    DWORD: ghidra.program.model.data.DataType
    IBO32: ghidra.program.model.data.DataType
    IBO64: ghidra.program.model.data.DataType
    NAME: unicode = u'MINIDUMP_HANDLE_OPERATIONS'
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

    def getHandle(self, __a0: int) -> ghidra.file.formats.dump.mdmp.Handle: ...

    def getNumberOfHandles(self) -> int: ...

    def getSizeOfDescriptor(self) -> int: ...

    def getSizeOfHeader(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setHandle(self, __a0: ghidra.file.formats.dump.mdmp.Handle, __a1: int) -> None: ...

    def setNumberOfHandles(self, __a0: int) -> None: ...

    def setSizeOfDescriptor(self, __a0: int) -> None: ...

    def setSizeOfHeader(self, __a0: int) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def numberOfHandles(self) -> int: ...

    @numberOfHandles.setter
    def numberOfHandles(self, value: int) -> None: ...

    @property
    def sizeOfDescriptor(self) -> int: ...

    @sizeOfDescriptor.setter
    def sizeOfDescriptor(self, value: int) -> None: ...

    @property
    def sizeOfHeader(self) -> int: ...

    @sizeOfHeader.setter
    def sizeOfHeader(self, value: int) -> None: ...