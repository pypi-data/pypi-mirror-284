from typing import overload
import ghidra.dbg.util
import ghidra.program.model.address
import ghidra.trace.database
import ghidra.trace.model.stack
import ghidra.trace.model.target
import ghidra.trace.model.thread
import java.io
import java.lang


class DBTraceStackManager(object, ghidra.trace.model.stack.TraceStackManager, ghidra.trace.database.DBTraceManager):




    def __init__(self, __a0: db.DBHandle, __a1: ghidra.framework.data.OpenMode, __a2: java.util.concurrent.locks.ReadWriteLock, __a3: ghidra.util.task.TaskMonitor, __a4: ghidra.trace.database.DBTrace, __a5: ghidra.trace.database.thread.DBTraceThreadManager, __a6: ghidra.trace.database.address.DBTraceOverlaySpaceAdapter): ...



    def dbError(self, __a0: java.io.IOException) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFramesIn(self, __a0: ghidra.program.model.address.AddressSetView) -> java.lang.Iterable: ...

    def getLatestStack(self, __a0: ghidra.trace.model.thread.TraceThread, __a1: long) -> ghidra.trace.model.stack.TraceStack: ...

    def getStack(self, __a0: ghidra.trace.model.thread.TraceThread, __a1: long, __a2: bool) -> ghidra.trace.model.stack.TraceStack: ...

    def hashCode(self) -> int: ...

    def invalidateCache(self, __a0: bool) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def single(__a0: ghidra.trace.model.target.TraceObject, __a1: java.lang.Class) -> ghidra.dbg.util.PathPredicates: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

