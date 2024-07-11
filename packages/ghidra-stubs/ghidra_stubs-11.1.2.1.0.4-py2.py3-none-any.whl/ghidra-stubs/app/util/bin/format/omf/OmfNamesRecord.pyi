from typing import overload
import ghidra.app.util.bin
import ghidra.app.util.bin.format.omf
import java.lang
import java.util


class OmfNamesRecord(ghidra.app.util.bin.format.omf.OmfRecord):




    def __init__(self, reader: ghidra.app.util.bin.BinaryReader): ...



    def appendNames(self, __a0: java.util.ArrayList) -> None: ...

    def calcCheckSum(self, reader: ghidra.app.util.bin.BinaryReader) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRecordLength(self) -> int: ...

    @staticmethod
    def getRecordName(type: int) -> unicode:
        """
        Gets the name of the given record type
        @param type The record type
        @return The name of the given record type
        """
        ...

    def getRecordOffset(self) -> long: ...

    def getRecordType(self) -> int: ...

    def hasBigFields(self) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readCheckSumByte(self, reader: ghidra.app.util.bin.BinaryReader) -> None: ...

    @staticmethod
    def readIndex(reader: ghidra.app.util.bin.BinaryReader) -> int: ...

    @staticmethod
    def readInt1Or2(reader: ghidra.app.util.bin.BinaryReader, isBig: bool) -> int: ...

    @staticmethod
    def readInt2Or4(reader: ghidra.app.util.bin.BinaryReader, isBig: bool) -> int: ...

    @staticmethod
    def readRecord(reader: ghidra.app.util.bin.BinaryReader) -> ghidra.app.util.bin.format.omf.OmfRecord: ...

    def readRecordHeader(self, reader: ghidra.app.util.bin.BinaryReader) -> None: ...

    @staticmethod
    def readString(reader: ghidra.app.util.bin.BinaryReader) -> unicode:
        """
        Read the OMF string format: 1-byte length, followed by that many ascii characters
        @param reader A {@link BinaryReader} positioned at the start of the string
        @return the read OMF string
        @throws IOException if an IO-related error occurred
        """
        ...

    def toString(self) -> unicode: ...

    def validCheckSum(self, reader: ghidra.app.util.bin.BinaryReader) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

