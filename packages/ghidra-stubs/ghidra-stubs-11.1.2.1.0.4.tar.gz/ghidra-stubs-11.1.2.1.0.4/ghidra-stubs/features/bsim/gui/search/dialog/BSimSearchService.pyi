from typing import overload
import ghidra.features.bsim.gui.search.dialog
import ghidra.features.bsim.query
import java.lang
import java.util


class BSimSearchService(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLastUsedSearchSettings(self) -> ghidra.features.bsim.gui.search.dialog.BSimSearchSettings: ...

    def getLastUsedServer(self) -> ghidra.features.bsim.query.BSimServerInfo: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def performOverview(self, __a0: ghidra.features.bsim.gui.search.dialog.BSimServerCache, __a1: ghidra.features.bsim.gui.search.dialog.BSimSearchSettings) -> None: ...

    def search(self, __a0: ghidra.features.bsim.gui.search.dialog.BSimServerCache, __a1: ghidra.features.bsim.gui.search.dialog.BSimSearchSettings, __a2: java.util.Set) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def lastUsedSearchSettings(self) -> ghidra.features.bsim.gui.search.dialog.BSimSearchSettings: ...

    @property
    def lastUsedServer(self) -> ghidra.features.bsim.query.BSimServerInfo: ...