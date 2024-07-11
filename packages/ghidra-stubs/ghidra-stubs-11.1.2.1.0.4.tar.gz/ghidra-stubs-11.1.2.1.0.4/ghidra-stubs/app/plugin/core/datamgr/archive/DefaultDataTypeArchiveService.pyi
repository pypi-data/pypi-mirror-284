from typing import List
from typing import overload
import generic.jar
import ghidra.app.plugin.core.datamgr.archive
import ghidra.app.services
import ghidra.framework.model
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.io
import java.lang


class DefaultDataTypeArchiveService(object, ghidra.app.services.DataTypeArchiveService):




    def __init__(self): ...



    def closeArchive(self, __a0: ghidra.program.model.data.DataTypeManager) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBuiltInDataTypesManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeManagers(self) -> List[ghidra.program.model.data.DataTypeManager]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openArchive(self, __a0: ghidra.program.model.listing.DataTypeArchive) -> ghidra.app.plugin.core.datamgr.archive.Archive: ...

    @overload
    def openArchive(self, __a0: generic.jar.ResourceFile, __a1: bool) -> ghidra.program.model.data.DataTypeManager: ...

    @overload
    def openArchive(self, __a0: java.io.File, __a1: bool) -> ghidra.app.plugin.core.datamgr.archive.Archive: ...

    @overload
    def openArchive(self, __a0: ghidra.framework.model.DomainFile, __a1: ghidra.util.task.TaskMonitor) -> ghidra.program.model.data.DataTypeManager: ...

    def openDataTypeArchive(self, __a0: unicode) -> ghidra.program.model.data.DataTypeManager: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def builtInDataTypesManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    @property
    def dataTypeManagers(self) -> List[ghidra.program.model.data.DataTypeManager]: ...