from typing import overload
import generic.lsh.vector
import ghidra.features.bsim.query
import ghidra.features.bsim.query.description
import ghidra.features.bsim.query.protocol
import ghidra.xml
import java.io
import java.lang


class QueryNearest(ghidra.features.bsim.query.protocol.BSimQuery):
    DEFAULT_MAX_MATCHES: int = 100
    DEFAULT_SIGNIFICANCE_THRESHOLD: float = 0.0
    DEFAULT_SIMILARITY_THRESHOLD: float = 0.7
    bsimFilter: ghidra.features.bsim.query.protocol.BSimFilter
    fillinCategories: bool
    manage: ghidra.features.bsim.query.description.DescriptionManager
    max: int
    nearresponse: ghidra.features.bsim.query.protocol.ResponseNearest
    signifthresh: float
    thresh: float
    vectormax: int



    def __init__(self): ...



    def buildResponseTemplate(self) -> None: ...

    def clearResponse(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, __a0: ghidra.features.bsim.query.FunctionDatabase) -> ghidra.features.bsim.query.protocol.QueryResponseRecord: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescriptionManager(self) -> ghidra.features.bsim.query.description.DescriptionManager: ...

    def getLocalStagingCopy(self) -> ghidra.features.bsim.query.protocol.BSimQuery: ...

    def getName(self) -> unicode: ...

    def getResponse(self) -> ghidra.features.bsim.query.protocol.QueryResponseRecord: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreQuery(__a0: ghidra.xml.XmlPullParser, __a1: generic.lsh.vector.LSHVectorFactory) -> ghidra.features.bsim.query.protocol.BSimQuery: ...

    def restoreXml(self, __a0: ghidra.xml.XmlPullParser, __a1: generic.lsh.vector.LSHVectorFactory) -> None: ...

    def saveXml(self, __a0: java.io.Writer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def descriptionManager(self) -> ghidra.features.bsim.query.description.DescriptionManager: ...

    @property
    def localStagingCopy(self) -> ghidra.features.bsim.query.protocol.QueryNearest: ...