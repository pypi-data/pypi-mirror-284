from typing import List
from typing import overload
import ghidra.features.bsim.query.facade
import java.lang


class SFQueryResult(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDatabaseInfo(self) -> ghidra.features.bsim.query.facade.DatabaseInfo: ...

    def getQuery(self) -> ghidra.features.bsim.query.facade.SFQueryInfo: ...

    def getSimilarityResults(self) -> List[object]: ...

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
    def databaseInfo(self) -> ghidra.features.bsim.query.facade.DatabaseInfo: ...

    @property
    def query(self) -> ghidra.features.bsim.query.facade.SFQueryInfo: ...

    @property
    def similarityResults(self) -> List[object]: ...