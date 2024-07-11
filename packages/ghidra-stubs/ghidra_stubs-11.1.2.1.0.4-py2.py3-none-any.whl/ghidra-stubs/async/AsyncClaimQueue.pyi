from typing import overload
import java.lang
import java.util.concurrent
import java.util.function


class AsyncClaimQueue(object):




    def __init__(self): ...



    @overload
    def claim(self) -> java.util.concurrent.CompletableFuture: ...

    @overload
    def claim(self, __a0: java.util.function.Predicate) -> java.util.concurrent.CompletableFuture: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def satisfy(self, __a0: object) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

