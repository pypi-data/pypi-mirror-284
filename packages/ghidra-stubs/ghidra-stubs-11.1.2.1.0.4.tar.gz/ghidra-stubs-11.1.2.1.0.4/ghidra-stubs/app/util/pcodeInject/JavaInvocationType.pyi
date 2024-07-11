from typing import List
from typing import overload
import ghidra.app.util.pcodeInject
import java.lang
import java.util


class JavaInvocationType(java.lang.Enum):
    INVOKE_DYNAMIC: ghidra.app.util.pcodeInject.JavaInvocationType
    INVOKE_INTERFACE: ghidra.app.util.pcodeInject.JavaInvocationType
    INVOKE_SPECIAL: ghidra.app.util.pcodeInject.JavaInvocationType
    INVOKE_STATIC: ghidra.app.util.pcodeInject.JavaInvocationType
    INVOKE_VIRTUAL: ghidra.app.util.pcodeInject.JavaInvocationType







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
    def valueOf(__a0: unicode) -> ghidra.app.util.pcodeInject.JavaInvocationType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.pcodeInject.JavaInvocationType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

