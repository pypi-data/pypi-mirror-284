from typing import overload
import ghidra.feature.vt.api
import java.lang


class NamespaceNeighborhood(ghidra.feature.vt.api.NeighborGenerator):




    def __init__(self, __a0: generic.lsh.vector.LSHVectorFactory, __a1: float, __a2: ghidra.feature.vt.api.FunctionNodeContainer, __a3: ghidra.feature.vt.api.FunctionNodeContainer): ...



    def equals(self, __a0: object) -> bool: ...

    def generate(self, __a0: ghidra.feature.vt.api.FunctionNode, __a1: ghidra.feature.vt.api.FunctionNode) -> ghidra.feature.vt.api.NeighborGenerator.NeighborhoodPair: ...

    def getClass(self) -> java.lang.Class: ...

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

