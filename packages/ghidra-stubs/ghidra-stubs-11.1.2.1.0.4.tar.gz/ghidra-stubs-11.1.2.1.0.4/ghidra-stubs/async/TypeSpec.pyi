from typing import overload
import ghidra.async
import java.lang
import java.util.concurrent


class TypeSpec(object):
    BOOLEAN: ghidra.async.TypeSpec
    BYTE: ghidra.async.TypeSpec
    BYTE_ARRAY: ghidra.async.TypeSpec
    CHAR: ghidra.async.TypeSpec
    INT: ghidra.async.TypeSpec
    LONG: ghidra.async.TypeSpec
    OBJECT: ghidra.async.TypeSpec
    RAW: ghidra.async.TypeSpec
    SHORT: ghidra.async.TypeSpec
    STRING: ghidra.async.TypeSpec
    VOID: ghidra.async.TypeSpec




    class FuncArity1(object):








        def equals(self, __a0: object) -> bool: ...

        def func(self, __a0: object) -> object: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class FuncArity2(object):








        def equals(self, __a0: object) -> bool: ...

        def func(self, __a0: object, __a1: object) -> object: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class FuncArity3(object):








        def equals(self, __a0: object) -> bool: ...

        def func(self, __a0: object, __a1: object, __a2: object) -> object: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class FuncArity4(object):








        def equals(self, __a0: object) -> bool: ...

        def func(self, __a0: object, __a1: object, __a2: object, __a3: object) -> object: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class FuncArity0(object):








        def equals(self, __a0: object) -> bool: ...

        def func(self) -> object: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    @staticmethod
    def auto() -> ghidra.async.TypeSpec: ...

    @staticmethod
    def cls(__a0: java.lang.Class) -> ghidra.async.TypeSpec: ...

    @overload
    def col(self) -> ghidra.async.TypeSpec: ...

    @overload
    def col(self, __a0: java.lang.Class) -> ghidra.async.TypeSpec: ...

    def equals(self, __a0: object) -> bool: ...

    def ext(self) -> ghidra.async.TypeSpec: ...

    @staticmethod
    def from(__a0: java.util.concurrent.Future) -> ghidra.async.TypeSpec: ...

    @overload
    @staticmethod
    def future(__a0: ghidra.async.TypeSpec.FuncArity0) -> ghidra.async.TypeSpec: ...

    @overload
    @staticmethod
    def future(__a0: ghidra.async.TypeSpec.FuncArity1) -> ghidra.async.TypeSpec: ...

    @overload
    @staticmethod
    def future(__a0: ghidra.async.TypeSpec.FuncArity2) -> ghidra.async.TypeSpec: ...

    @overload
    @staticmethod
    def future(__a0: ghidra.async.TypeSpec.FuncArity3) -> ghidra.async.TypeSpec: ...

    @overload
    @staticmethod
    def future(__a0: ghidra.async.TypeSpec.FuncArity4) -> ghidra.async.TypeSpec: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def list(self) -> ghidra.async.TypeSpec: ...

    @staticmethod
    def map(__a0: java.lang.Class, __a1: java.lang.Class) -> ghidra.async.TypeSpec: ...

    @overload
    def mappedBy(self, __a0: ghidra.async.TypeSpec) -> ghidra.async.TypeSpec: ...

    @overload
    def mappedBy(self, __a0: java.lang.Class) -> ghidra.async.TypeSpec: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def obj(__a0: object) -> ghidra.async.TypeSpec: ...

    @staticmethod
    def pair(__a0: ghidra.async.TypeSpec, __a1: ghidra.async.TypeSpec) -> ghidra.async.TypeSpec: ...

    def set(self) -> ghidra.async.TypeSpec: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

