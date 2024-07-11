from typing import overload
import ghidra.util.database.annotproc
import java.lang


class DBAnnotatedColumnValidator(ghidra.util.database.annotproc.AbstractDBAnnotationValidator):




    def __init__(self, __a0: ghidra.util.database.annotproc.ValidationContext, __a1: javax.lang.model.element.VariableElement): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def validate(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

