from typing import List
from typing import overload
import ghidra.dbg.target
import ghidra.debug.api.model
import ghidra.program.model.lang
import java.lang
import java.util


class DefaultGdbDebuggerMappingOpinion(object, ghidra.debug.api.model.DebuggerMappingOpinion):
    EXTERNAL_TOOL: unicode = u'gnu'
    HIGHEST_CONFIDENCE_FIRST: java.util.Comparator
    PREFERRED_CSPEC_ID: ghidra.program.model.lang.CompilerSpecID



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getCompilerSpecsForGnu(__a0: unicode, __a1: ghidra.program.model.lang.Endian) -> List[object]: ...

    @staticmethod
    def getEndian(__a0: ghidra.dbg.target.TargetEnvironment) -> ghidra.program.model.lang.Endian: ...

    def getOffers(self, __a0: ghidra.dbg.target.TargetObject, __a1: bool) -> java.util.Set: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isGdb(__a0: ghidra.dbg.target.TargetEnvironment) -> bool: ...

    @staticmethod
    def isLinux(__a0: ghidra.dbg.target.TargetEnvironment) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def offersForEnv(self, __a0: ghidra.dbg.target.TargetEnvironment, __a1: ghidra.dbg.target.TargetObject, __a2: bool) -> java.util.Set: ...

    @staticmethod
    def queryOpinions(__a0: ghidra.dbg.target.TargetObject, __a1: bool) -> List[object]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

