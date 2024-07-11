from typing import List
from typing import overload
import ghidra.bitpatterns.info
import java.lang
import java.util


class PatternMatchType(java.lang.Enum):
    CONTEXT_CONFLICT: ghidra.bitpatterns.info.PatternMatchType
    FP_DATA: ghidra.bitpatterns.info.PatternMatchType
    FP_MISALIGNED: ghidra.bitpatterns.info.PatternMatchType
    FP_WRONG_FLOW: ghidra.bitpatterns.info.PatternMatchType
    POSSIBLE_START_CODE: ghidra.bitpatterns.info.PatternMatchType
    POSSIBLE_START_UNDEFINED: ghidra.bitpatterns.info.PatternMatchType
    PRE_PATTERN_HIT: ghidra.bitpatterns.info.PatternMatchType
    TRUE_POSITIVE: ghidra.bitpatterns.info.PatternMatchType







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
    def valueOf(__a0: unicode) -> ghidra.bitpatterns.info.PatternMatchType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.bitpatterns.info.PatternMatchType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

