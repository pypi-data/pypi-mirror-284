from typing import overload
import ghidra.app.util.bin
import ghidra.file.formats.ios.dmg
import java.lang


class UDIFHeader(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasGoodOffsets(self, __a0: ghidra.app.util.bin.ByteProvider) -> bool: ...

    def hashCode(self) -> int: ...

    def isValid(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def read(__a0: ghidra.app.util.bin.ByteProvider) -> ghidra.file.formats.ios.dmg.UDIFHeader: ...

    @overload
    @staticmethod
    def read(__a0: ghidra.app.util.bin.ByteProvider, __a1: long) -> ghidra.file.formats.ios.dmg.UDIFHeader: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def valid(self) -> bool: ...