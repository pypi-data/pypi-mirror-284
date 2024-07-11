from typing import List
from typing import overload
import docking.widgets.fieldpanel.support
import ghidra.app.util
import ghidra.app.util.viewer.field
import java.lang


class ListingDiffHighlightProvider(object, ghidra.app.util.ListingHighlightProvider):
    NO_HIGHLIGHTS: List[docking.widgets.fieldpanel.support.Highlight]



    def __init__(self, listingDiff: ghidra.program.util.ListingDiff, isListing1: bool, comparisonOptions: ghidra.app.util.viewer.listingpanel.ListingCodeComparisonOptions):
        """
        Constructor for this highlight provider.
        @param listingDiff the ListingDiff to use to determine where there are differences that 
         need highlighting.
        @param isListing1 true means that these are the highlights for the first listing.
         false means the highlights are for the second listing.
        @param comparisonOptions the tool options that indicate the current 
         background colors for the Listing code comparison panel.
        """
        ...



    def createHighlights(self, text: unicode, field: ghidra.app.util.viewer.field.ListingField, cursorTextOffset: int) -> List[docking.widgets.fieldpanel.support.Highlight]: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isListing1(self) -> bool:
        """
        Determines if this highlight provider is for the first listing of the ListingDiff.
        @return true if this provider's highlights are for the first listing. false if the
         highlights are for the second listing.
        """
        ...

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
    def listing1(self) -> bool: ...