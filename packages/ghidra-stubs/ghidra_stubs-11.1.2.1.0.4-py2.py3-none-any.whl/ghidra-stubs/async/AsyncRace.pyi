from typing import overload
import ghidra.async
import java.lang
import java.util.concurrent


class AsyncRace(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def include(self, __a0: java.util.concurrent.CompletableFuture) -> ghidra.async.AsyncRace: ...

    def next(self) -> java.util.concurrent.CompletableFuture: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

