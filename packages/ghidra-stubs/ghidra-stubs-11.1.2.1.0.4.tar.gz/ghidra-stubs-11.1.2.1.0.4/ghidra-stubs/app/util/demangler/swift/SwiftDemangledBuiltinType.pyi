from typing import List
from typing import overload
import ghidra.app.util.demangler.swift
import java.lang
import java.util


class SwiftDemangledBuiltinType(java.lang.Enum):
    Int1: ghidra.app.util.demangler.swift.SwiftDemangledBuiltinType
    RawPointer: ghidra.app.util.demangler.swift.SwiftDemangledBuiltinType
    Unsupported: ghidra.app.util.demangler.swift.SwiftDemangledBuiltinType
    Word: ghidra.app.util.demangler.swift.SwiftDemangledBuiltinType







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
    def valueOf(__a0: unicode) -> ghidra.app.util.demangler.swift.SwiftDemangledBuiltinType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.demangler.swift.SwiftDemangledBuiltinType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

