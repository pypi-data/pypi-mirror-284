from typing import List
from typing import overload
import java.lang
import javax.swing


class BSimValueEditor(object):
    FILTER_DELIMETER: unicode = u','
    INVALID_COLOR: java.awt.Color
    VALID_COLOR: java.awt.Color







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent: ...

    def getValues(self) -> List[object]: ...

    def hasValidValues(self) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setValues(self, __a0: List[object]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def component(self) -> javax.swing.JComponent: ...

    @property
    def values(self) -> List[object]: ...

    @values.setter
    def values(self, value: List[object]) -> None: ...