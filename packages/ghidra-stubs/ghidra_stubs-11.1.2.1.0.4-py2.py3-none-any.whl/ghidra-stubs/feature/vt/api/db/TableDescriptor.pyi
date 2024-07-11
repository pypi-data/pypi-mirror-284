from typing import List
from typing import overload
import db
import java.lang


class TableDescriptor(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumnFields(self) -> List[db.Field]: ...

    def getColumnNames(self) -> List[unicode]: ...

    def getIndexedColumns(self) -> List[int]: ...

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
    def columnFields(self) -> List[db.Field]: ...

    @property
    def columnNames(self) -> List[unicode]: ...

    @property
    def indexedColumns(self) -> List[int]: ...