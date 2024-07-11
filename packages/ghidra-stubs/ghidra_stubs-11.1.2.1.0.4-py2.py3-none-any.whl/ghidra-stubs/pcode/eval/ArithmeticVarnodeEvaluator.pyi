from typing import overload
import ghidra.pcode.eval
import ghidra.pcode.exec
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang


class ArithmeticVarnodeEvaluator(ghidra.pcode.eval.AbstractVarnodeEvaluator):




    def __init__(self, __a0: ghidra.pcode.exec.PcodeArithmetic): ...



    @staticmethod
    def catenate(__a0: ghidra.pcode.exec.PcodeArithmetic, __a1: int, __a2: object, __a3: object, __a4: int) -> object: ...

    def equals(self, __a0: object) -> bool: ...

    def evaluateOp(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.pcode.PcodeOp) -> object: ...

    def evaluateStorage(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.listing.VariableStorage) -> object: ...

    def evaluateVarnode(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.pcode.Varnode) -> object: ...

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

