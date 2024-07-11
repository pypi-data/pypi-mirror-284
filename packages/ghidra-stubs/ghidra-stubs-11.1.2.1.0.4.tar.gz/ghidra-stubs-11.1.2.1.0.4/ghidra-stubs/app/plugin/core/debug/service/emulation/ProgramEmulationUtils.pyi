from typing import List
from typing import overload
import ghidra.dbg.target.schema
import ghidra.dbg.util
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.trace.model
import ghidra.trace.model.thread
import ghidra.trace.model.time
import java.lang
import java.util


class ProgramEmulationUtils(object):
    BLOCK_NAME_STACK: unicode = u'STACK'
    EMULATION_STARTED_AT: unicode = u'Emulation started at '
    EMU_CTX: ghidra.dbg.target.schema.SchemaContext
    EMU_CTX_XML: unicode = u"<context>\n    <schema name='EmuSession' elementResync='NEVER' attributeResync='NEVER'>\n        <interface name='Process' />\n        <interface name='Aggregate' />\n        <attribute name='Breakpoints' schema='BreakpointContainer' />\n        <attribute name='Memory' schema='RegionContainer' />\n        <attribute name='Modules' schema='ModuleContainer' />\n        <attribute name='Threads' schema='ThreadContainer' />\n    </schema>\n    <schema name='BreakpointContainer' canonical='yes' elementResync='NEVER'\n            attributeResync='NEVER'>\n        <interface name='BreakpointSpecContainer' />\n        <interface name='BreakpointLocationContainer' />\n        <element schema='Breakpoint' />\n    </schema>\n    <schema name='Breakpoint' elementResync='NEVER' attributeResync='NEVER'>\n        <interface name='BreakpointSpec' />\n        <interface name='BreakpointLocation' />\n    </schema>\n    <schema name='RegionContainer' canonical='yes' elementResync='NEVER'\n            attributeResync='NEVER'>\n        <element schema='Region' />\n    </schema>\n    <schema name='Region' elementResync='NEVER' attributeResync='NEVER'>\n        <interface name='MemoryRegion' />\n    </schema>\n    <schema name='ModuleContainer' canonical='yes' elementResync='NEVER'\n            attributeResync='NEVER'>\n        <element schema='Module' />\n    </schema>\n    <schema name='Module' elementResync='NEVER' attributeResync='NEVER'>\n        <interface name='Module' />\n        <attribute name='Sections' schema='SectionContainer' />\n    </schema>\n    <schema name='SectionContainer' canonical='yes' elementResync='NEVER'\n            attributeResync='NEVER'>\n        <element schema='Section' />\n    </schema>\n    <schema name='Section' elementResync='NEVER' attributeResync='NEVER'>\n        <interface name='Section' />\n    </schema>\n    <schema name='ThreadContainer' canonical='yes' elementResync='NEVER'\n            attributeResync='NEVER'>\n        <element schema='Thread' />\n    </schema>\n    <schema name='Thread' elementResync='NEVER' attributeResync='NEVER'>\n        <interface name='Thread' />\n        <interface name='Activatable' />\n        <interface name='Aggregate' />\n        <attribute name='Registers' schema='RegisterContainer' />\n    </schema>\n    <schema name='RegisterContainer' canonical='yes' elementResync='NEVER'\n            attributeResync='NEVER'>\n        <interface name='RegisterContainer' />\n        <element schema='Register' />\n    </schema>\n    <schema name='Register' elementResync='NEVER' attributeResync='NEVER'>\n        <interface name='Register' />\n    </schema>\n</context>\n"
    EMU_SESSION_SCHEMA: ghidra.dbg.target.schema.TargetObjectSchema







    @staticmethod
    def allocateStack(__a0: ghidra.trace.model.Trace, __a1: long, __a2: ghidra.trace.model.thread.TraceThread, __a3: ghidra.program.model.listing.Program, __a4: long) -> ghidra.program.model.address.AddressRange: ...

    @staticmethod
    def allocateStackCustom(__a0: ghidra.trace.model.Trace, __a1: long, __a2: ghidra.trace.model.thread.TraceThread, __a3: ghidra.program.model.listing.Program) -> ghidra.program.model.address.AddressRange: ...

    @staticmethod
    def computePattern(__a0: ghidra.dbg.target.schema.TargetObjectSchema, __a1: ghidra.trace.model.Trace, __a2: java.lang.Class) -> ghidra.dbg.util.PathPattern: ...

    @staticmethod
    def computePatternRegion(__a0: ghidra.trace.model.Trace) -> ghidra.dbg.util.PathPattern: ...

    @staticmethod
    def computePatternThread(__a0: ghidra.trace.model.Trace) -> ghidra.dbg.util.PathPattern: ...

    @staticmethod
    def doLaunchEmulationThread(__a0: ghidra.trace.model.Trace, __a1: long, __a2: ghidra.program.model.listing.Program, __a3: ghidra.program.model.address.Address, __a4: ghidra.program.model.address.Address) -> ghidra.trace.model.thread.TraceThread: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getModuleName(__a0: ghidra.program.model.listing.Program) -> unicode: ...

    @staticmethod
    def getRegionFlags(__a0: ghidra.program.model.mem.MemoryBlock) -> java.util.Set: ...

    @staticmethod
    def getTraceName(__a0: ghidra.program.model.listing.Program) -> unicode: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def initializeRegisters(__a0: ghidra.trace.model.Trace, __a1: long, __a2: ghidra.trace.model.thread.TraceThread, __a3: ghidra.program.model.listing.Program, __a4: ghidra.program.model.address.Address, __a5: ghidra.program.model.address.Address, __a6: ghidra.program.model.address.AddressRange) -> None: ...

    @staticmethod
    def isEmulatedProgram(__a0: ghidra.trace.model.Trace) -> bool: ...

    @staticmethod
    def launchEmulationThread(__a0: ghidra.trace.model.Trace, __a1: long, __a2: ghidra.program.model.listing.Program, __a3: ghidra.program.model.address.Address, __a4: ghidra.program.model.address.Address) -> ghidra.trace.model.thread.TraceThread: ...

    @staticmethod
    def launchEmulationTrace(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: object) -> ghidra.trace.model.Trace: ...

    @staticmethod
    def loadExecutable(__a0: ghidra.trace.model.time.TraceSnapshot, __a1: ghidra.program.model.listing.Program, __a2: List[object]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def spawnThread(__a0: ghidra.trace.model.Trace, __a1: long) -> ghidra.trace.model.thread.TraceThread: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

