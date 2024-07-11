from typing import overload
import ghidra.app.util.bin
import ghidra.file.formats.ios.dmg
import ghidra.formats.gfilesystem
import ghidra.formats.gfilesystem.factory
import ghidra.util.task
import java.lang


class DmgClientFileSystemFactory(object, ghidra.formats.gfilesystem.factory.GFileSystemFactoryByteProvider, ghidra.formats.gfilesystem.factory.GFileSystemProbeByteProvider):




    def __init__(self): ...



    def create(self, __a0: ghidra.formats.gfilesystem.FSRLRoot, __a1: ghidra.app.util.bin.ByteProvider, __a2: ghidra.formats.gfilesystem.FileSystemService, __a3: ghidra.util.task.TaskMonitor) -> ghidra.file.formats.ios.dmg.DmgClientFileSystem: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def probe(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: ghidra.formats.gfilesystem.FileSystemService, __a2: ghidra.util.task.TaskMonitor) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

