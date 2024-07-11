from typing import overload
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.trace.model
import ghidra.trace.model.bookmark
import java.lang
import java.util


class TraceBookmarkSpace(ghidra.trace.model.bookmark.TraceBookmarkOperations, object):








    @overload
    def addBookmark(self, __a0: ghidra.trace.model.Lifespan, __a1: ghidra.program.model.address.Address, __a2: ghidra.trace.model.bookmark.TraceBookmarkType, __a3: unicode, __a4: unicode) -> ghidra.trace.model.bookmark.TraceBookmark: ...

    @overload
    def addBookmark(self, __a0: ghidra.trace.model.Lifespan, __a1: ghidra.program.model.lang.Register, __a2: ghidra.trace.model.bookmark.TraceBookmarkType, __a3: unicode, __a4: unicode) -> ghidra.trace.model.bookmark.TraceBookmark: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    def getAllBookmarks(self) -> java.util.Collection: ...

    def getBookmarksAt(self, __a0: long, __a1: ghidra.program.model.address.Address) -> java.lang.Iterable: ...

    @overload
    def getBookmarksEnclosed(self, __a0: ghidra.trace.model.Lifespan, __a1: ghidra.program.model.address.AddressRange) -> java.lang.Iterable: ...

    @overload
    def getBookmarksEnclosed(self, __a0: ghidra.trace.model.Lifespan, __a1: ghidra.program.model.lang.Register) -> java.lang.Iterable: ...

    @overload
    def getBookmarksIntersecting(self, __a0: ghidra.trace.model.Lifespan, __a1: ghidra.program.model.address.AddressRange) -> java.lang.Iterable: ...

    @overload
    def getBookmarksIntersecting(self, __a0: ghidra.trace.model.Lifespan, __a1: ghidra.program.model.lang.Register) -> java.lang.Iterable: ...

    def getCategoriesForType(self, __a0: ghidra.trace.model.bookmark.TraceBookmarkType) -> java.util.Set: ...

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

    @property
    def addressSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def allBookmarks(self) -> java.util.Collection: ...