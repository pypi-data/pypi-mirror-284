from typing import List
from typing import overload
import java.lang
import java.lang.annotation


class TraceObjectInfo(java.lang.annotation.Annotation, object):








    def annotationType(self) -> java.lang.Class: ...

    def equals(self, __a0: object) -> bool: ...

    def fixedKeys(self) -> List[unicode]: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def shortName(self) -> unicode: ...

    def targetIf(self) -> java.lang.Class: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

