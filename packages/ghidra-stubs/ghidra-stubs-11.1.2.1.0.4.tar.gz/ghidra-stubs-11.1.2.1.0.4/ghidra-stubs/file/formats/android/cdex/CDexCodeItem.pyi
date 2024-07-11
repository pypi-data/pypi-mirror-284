from typing import List
from typing import overload
import ghidra.file.formats.android.dex.format
import ghidra.program.model.data
import java.lang


class CDexCodeItem(ghidra.file.formats.android.dex.format.CodeItem):
    kBitPreHeaderInsSize: int = 1
    kBitPreHeaderInsnsSize: int = 4
    kBitPreHeaderOutsSize: int = 2
    kBitPreHeaderRegisterSize: int = 0
    kBitPreHeaderTriesSize: int = 3
    kFlagPreHeaderCombined: int = 31
    kFlagPreHeaderInsSize: int = 2
    kFlagPreHeaderInsnsSize: int = 16
    kFlagPreHeaderOutsSize: int = 4
    kFlagPreHeaderRegisterSize: int = 1
    kFlagPreHeaderTriesSize: int = 8
    kInsSizeShift: int = 8
    kInsnsSizeShift: int = 5
    kOutsSizeShift: int = 4
    kRegistersSizeShift: int = 12
    kTriesSizeSizeShift: int = 0



    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDebugInfo(self) -> ghidra.file.formats.android.dex.format.DebugInfoItem: ...

    def getDebugInfoOffset(self) -> int: ...

    def getHandlerList(self) -> ghidra.file.formats.android.dex.format.EncodedCatchHandlerList: ...

    def getIncomingSize(self) -> int: ...

    def getInstructionBytes(self) -> List[int]: ...

    def getInstructionSize(self) -> int: ...

    def getInstructions(self) -> List[int]: ...

    def getOutgoingSize(self) -> int: ...

    def getPadding(self) -> int: ...

    def getRegistersSize(self) -> int: ...

    def getTries(self) -> List[object]: ...

    def getTriesSize(self) -> int: ...

    @overload
    def hasPreHeader(self) -> bool: ...

    @overload
    def hasPreHeader(self, __a0: int) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

