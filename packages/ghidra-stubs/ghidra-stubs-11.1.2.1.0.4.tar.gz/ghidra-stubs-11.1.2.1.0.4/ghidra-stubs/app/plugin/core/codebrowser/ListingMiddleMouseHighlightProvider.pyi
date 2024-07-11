from typing import List
from typing import overload
import docking.widgets.fieldpanel.support
import ghidra.app.services
import ghidra.app.util
import ghidra.app.util.viewer.field
import ghidra.framework.options
import ghidra.program.util
import java.awt.event
import java.lang


class ListingMiddleMouseHighlightProvider(object, ghidra.app.services.ButtonPressedListener, ghidra.framework.options.OptionsChangeListener, ghidra.app.util.ListingHighlightProvider):
    NO_HIGHLIGHTS: List[docking.widgets.fieldpanel.support.Highlight]



    def __init__(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: java.awt.Component): ...



    def buttonPressed(self, __a0: ghidra.program.util.ProgramLocation, __a1: docking.widgets.fieldpanel.support.FieldLocation, __a2: ghidra.app.util.viewer.field.ListingField, __a3: java.awt.event.MouseEvent) -> None: ...

    def createHighlights(self, __a0: unicode, __a1: ghidra.app.util.viewer.field.ListingField, __a2: int) -> List[docking.widgets.fieldpanel.support.Highlight]: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, __a0: ghidra.framework.options.ToolOptions, __a1: unicode, __a2: object, __a3: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

