from typing import List
from typing import overload
import ghidra.file.formats.android.art.image_root
import java.lang
import java.util


class ImageRoot_Q(java.lang.Enum):
    kAppImageClassLoader: ghidra.file.formats.android.art.image_root.ImageRoot_Q
    kBootImageLiveObjects: ghidra.file.formats.android.art.image_root.ImageRoot_Q
    kClassRoots: ghidra.file.formats.android.art.image_root.ImageRoot_Q
    kDexCaches: ghidra.file.formats.android.art.image_root.ImageRoot_Q
    kImageRootsMax: ghidra.file.formats.android.art.image_root.ImageRoot_Q
    kNoClassDefFoundError: ghidra.file.formats.android.art.image_root.ImageRoot_Q
    kOomeWhenHandlingStackOverflow: ghidra.file.formats.android.art.image_root.ImageRoot_Q
    kOomeWhenThrowingException: ghidra.file.formats.android.art.image_root.ImageRoot_Q
    kOomeWhenThrowingOome: ghidra.file.formats.android.art.image_root.ImageRoot_Q
    kSpecialRoots: ghidra.file.formats.android.art.image_root.ImageRoot_Q







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def describeConstable(self) -> java.util.Optional: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.file.formats.android.art.image_root.ImageRoot_Q: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.file.formats.android.art.image_root.ImageRoot_Q]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

