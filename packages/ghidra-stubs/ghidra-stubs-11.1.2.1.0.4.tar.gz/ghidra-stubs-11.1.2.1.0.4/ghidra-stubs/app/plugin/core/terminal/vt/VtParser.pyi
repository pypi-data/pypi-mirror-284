from typing import overload
import java.lang
import java.nio


class VtParser(object):




    def __init__(self, __a0: ghidra.app.plugin.core.terminal.vt.VtHandler): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def process(self, __a0: java.nio.ByteBuffer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

