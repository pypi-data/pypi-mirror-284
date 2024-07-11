from typing import overload
import ghidra.async
import java.lang


class AsyncSequenceHandlerForRunner(ghidra.async.AsyncHandlerCanExit, object):








    def equals(self, __a0: object) -> bool: ...

    @overload
    def exit(self) -> None: ...

    @overload
    def exit(self, __a0: java.lang.Throwable) -> None: ...

    @overload
    def exit(self, __a0: object) -> None: ...

    @overload
    def exit(self, __a0: object, __a1: java.lang.Throwable) -> java.lang.Void: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def next(self, __a0: java.lang.Void, __a1: java.lang.Throwable) -> java.lang.Void: ...

    def nextIgnore(self, __a0: object, __a1: java.lang.Throwable) -> java.lang.Void: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

