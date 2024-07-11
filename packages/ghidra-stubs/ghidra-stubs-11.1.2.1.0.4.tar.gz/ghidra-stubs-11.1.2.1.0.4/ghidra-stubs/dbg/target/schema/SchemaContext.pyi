from typing import overload
import ghidra.dbg.target.schema
import java.lang
import java.util


class SchemaContext(object):








    def equals(self, __a0: object) -> bool: ...

    def getAllSchemas(self) -> java.util.Set: ...

    def getClass(self) -> java.lang.Class: ...

    def getSchema(self, __a0: ghidra.dbg.target.schema.TargetObjectSchema.SchemaName) -> ghidra.dbg.target.schema.TargetObjectSchema: ...

    def getSchemaOrNull(self, __a0: ghidra.dbg.target.schema.TargetObjectSchema.SchemaName) -> ghidra.dbg.target.schema.TargetObjectSchema: ...

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
    def allSchemas(self) -> java.util.Set: ...