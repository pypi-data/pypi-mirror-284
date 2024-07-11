from typing import overload
import ghidra.features.bsim.query.description
import ghidra.features.bsim.query.protocol
import ghidra.xml
import java.io
import java.lang


class ExeSpecifier(object, java.lang.Comparable):
    arch: unicode
    execompname: unicode
    exemd5: unicode
    exename: unicode



    def __init__(self): ...



    @overload
    def compareTo(self, __a0: ghidra.features.bsim.query.protocol.ExeSpecifier) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExeNameWithMD5(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, __a0: ghidra.xml.XmlPullParser) -> None: ...

    def saveXml(self, __a0: java.io.Writer) -> None: ...

    def toString(self) -> unicode: ...

    def transfer(self, __a0: ghidra.features.bsim.query.description.ExecutableRecord) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def exeNameWithMD5(self) -> unicode: ...