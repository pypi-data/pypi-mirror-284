from typing import List
from typing import overload
import db
import ghidra.feature.vt.api.db
import ghidra.feature.vt.api.main
import java.lang
import java.util


class VTMatchTableDBAdapter(object):





    class ColumnDescription(java.lang.Enum):
        ASSOCIATION_COL: ghidra.feature.vt.api.db.VTMatchTableDBAdapter.ColumnDescription
        CONFIDENCE_SCORE_COL: ghidra.feature.vt.api.db.VTMatchTableDBAdapter.ColumnDescription
        DESTINATION_LENGTH_COL: ghidra.feature.vt.api.db.VTMatchTableDBAdapter.ColumnDescription
        LENGTH_TYPE: ghidra.feature.vt.api.db.VTMatchTableDBAdapter.ColumnDescription
        MATCH_SET_COL: ghidra.feature.vt.api.db.VTMatchTableDBAdapter.ColumnDescription
        SIMILARITY_SCORE_COL: ghidra.feature.vt.api.db.VTMatchTableDBAdapter.ColumnDescription
        SOURCE_LENGTH_COL: ghidra.feature.vt.api.db.VTMatchTableDBAdapter.ColumnDescription
        TAG_KEY_COL: ghidra.feature.vt.api.db.VTMatchTableDBAdapter.ColumnDescription







        def column(self) -> int: ...

        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def describeConstable(self) -> java.util.Optional: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getColumnField(self) -> db.Field: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.feature.vt.api.db.VTMatchTableDBAdapter.ColumnDescription: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.feature.vt.api.db.VTMatchTableDBAdapter.ColumnDescription]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def columnField(self) -> db.Field: ...

    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRecords(self) -> db.RecordIterator: ...

    def hashCode(self) -> int: ...

    def insertMatchRecord(self, __a0: ghidra.feature.vt.api.main.VTMatchInfo, __a1: ghidra.feature.vt.api.db.VTMatchSetDB, __a2: ghidra.feature.vt.api.db.VTAssociationDB, __a3: ghidra.feature.vt.api.db.VTMatchTagDB) -> db.DBRecord: ...

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
    def records(self) -> db.RecordIterator: ...