from typing import overload
import ghidra.graph.viewer.popup
import java.lang
import javax.swing


class AttributedToolTipInfo(ghidra.graph.viewer.popup.ToolTipInfo):








    def createToolTipComponent(self) -> javax.swing.JComponent: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getToolTipText(self) -> unicode: ...

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
    def toolTipText(self) -> unicode: ...