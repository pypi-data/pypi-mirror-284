from typing import List
from typing import overload
import ghidra.pcode.emu
import ghidra.trace.model.time.schedule
import java.lang
import java.util


class Stepper(object):





    class Enum(java.lang.Enum, ghidra.trace.model.time.schedule.Stepper):
        INSTRUCTION: ghidra.trace.model.time.schedule.Stepper.Enum
        PCODE: ghidra.trace.model.time.schedule.Stepper.Enum







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def describeConstable(self) -> java.util.Optional: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        @staticmethod
        def instruction() -> ghidra.trace.model.time.schedule.Stepper: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        @staticmethod
        def pcode() -> ghidra.trace.model.time.schedule.Stepper: ...

        def skip(self, __a0: ghidra.pcode.emu.PcodeThread) -> None: ...

        def tick(self, __a0: ghidra.pcode.emu.PcodeThread) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.trace.model.time.schedule.Stepper.Enum: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.trace.model.time.schedule.Stepper.Enum]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def instruction() -> ghidra.trace.model.time.schedule.Stepper: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def pcode() -> ghidra.trace.model.time.schedule.Stepper: ...

    def skip(self, __a0: ghidra.pcode.emu.PcodeThread) -> None: ...

    def tick(self, __a0: ghidra.pcode.emu.PcodeThread) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

