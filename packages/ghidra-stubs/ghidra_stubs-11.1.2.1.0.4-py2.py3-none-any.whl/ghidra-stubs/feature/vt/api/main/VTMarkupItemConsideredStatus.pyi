from typing import List
from typing import overload
import ghidra.feature.vt.api.main
import java.lang
import java.util


class VTMarkupItemConsideredStatus(java.lang.Enum):
    IGNORE_DONT_CARE: ghidra.feature.vt.api.main.VTMarkupItemConsideredStatus
    IGNORE_DONT_KNOW: ghidra.feature.vt.api.main.VTMarkupItemConsideredStatus
    REJECT: ghidra.feature.vt.api.main.VTMarkupItemConsideredStatus
    UNCONSIDERED: ghidra.feature.vt.api.main.VTMarkupItemConsideredStatus







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def describeConstable(self) -> java.util.Optional: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getMarkupItemStatus(self) -> ghidra.feature.vt.api.main.VTMarkupItemStatus: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.feature.vt.api.main.VTMarkupItemConsideredStatus: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.feature.vt.api.main.VTMarkupItemConsideredStatus]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def markupItemStatus(self) -> ghidra.feature.vt.api.main.VTMarkupItemStatus: ...