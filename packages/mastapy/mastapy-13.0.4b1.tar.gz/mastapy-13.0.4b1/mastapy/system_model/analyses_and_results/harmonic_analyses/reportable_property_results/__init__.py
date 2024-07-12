"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5875 import AbstractSingleWhineAnalysisResultsPropertyAccessor
    from ._5876 import DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic
    from ._5877 import DataPointForResponseOfANodeAtAFrequencyToAHarmonic
    from ._5878 import FEPartHarmonicAnalysisResultsPropertyAccessor
    from ._5879 import FEPartSingleWhineAnalysisResultsPropertyAccessor
    from ._5880 import HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
    from ._5881 import HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic
    from ._5882 import HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic
    from ._5883 import HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
    from ._5884 import HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic
    from ._5885 import HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
    from ._5886 import HarmonicAnalysisResultsPropertyAccessor
    from ._5887 import ResultsForMultipleOrders
    from ._5888 import ResultsForMultipleOrdersForFESurface
    from ._5889 import ResultsForMultipleOrdersForGroups
    from ._5890 import ResultsForOrder
    from ._5891 import ResultsForOrderIncludingGroups
    from ._5892 import ResultsForOrderIncludingNodes
    from ._5893 import ResultsForOrderIncludingSurfaces
    from ._5894 import ResultsForResponseOfAComponentOrSurfaceInAHarmonic
    from ._5895 import ResultsForResponseOfANodeOnAHarmonic
    from ._5896 import ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic
    from ._5897 import RootAssemblyHarmonicAnalysisResultsPropertyAccessor
    from ._5898 import RootAssemblySingleWhineAnalysisResultsPropertyAccessor
    from ._5899 import SingleWhineAnalysisResultsPropertyAccessor
else:
    import_structure = {
        "_5875": ["AbstractSingleWhineAnalysisResultsPropertyAccessor"],
        "_5876": ["DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic"],
        "_5877": ["DataPointForResponseOfANodeAtAFrequencyToAHarmonic"],
        "_5878": ["FEPartHarmonicAnalysisResultsPropertyAccessor"],
        "_5879": ["FEPartSingleWhineAnalysisResultsPropertyAccessor"],
        "_5880": ["HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic"],
        "_5881": ["HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic"],
        "_5882": ["HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic"],
        "_5883": ["HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic"],
        "_5884": ["HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic"],
        "_5885": ["HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic"],
        "_5886": ["HarmonicAnalysisResultsPropertyAccessor"],
        "_5887": ["ResultsForMultipleOrders"],
        "_5888": ["ResultsForMultipleOrdersForFESurface"],
        "_5889": ["ResultsForMultipleOrdersForGroups"],
        "_5890": ["ResultsForOrder"],
        "_5891": ["ResultsForOrderIncludingGroups"],
        "_5892": ["ResultsForOrderIncludingNodes"],
        "_5893": ["ResultsForOrderIncludingSurfaces"],
        "_5894": ["ResultsForResponseOfAComponentOrSurfaceInAHarmonic"],
        "_5895": ["ResultsForResponseOfANodeOnAHarmonic"],
        "_5896": ["ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic"],
        "_5897": ["RootAssemblyHarmonicAnalysisResultsPropertyAccessor"],
        "_5898": ["RootAssemblySingleWhineAnalysisResultsPropertyAccessor"],
        "_5899": ["SingleWhineAnalysisResultsPropertyAccessor"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractSingleWhineAnalysisResultsPropertyAccessor",
    "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
    "DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
    "FEPartHarmonicAnalysisResultsPropertyAccessor",
    "FEPartSingleWhineAnalysisResultsPropertyAccessor",
    "HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
    "HarmonicAnalysisResultsPropertyAccessor",
    "ResultsForMultipleOrders",
    "ResultsForMultipleOrdersForFESurface",
    "ResultsForMultipleOrdersForGroups",
    "ResultsForOrder",
    "ResultsForOrderIncludingGroups",
    "ResultsForOrderIncludingNodes",
    "ResultsForOrderIncludingSurfaces",
    "ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
    "ResultsForResponseOfANodeOnAHarmonic",
    "ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic",
    "RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
    "RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
    "SingleWhineAnalysisResultsPropertyAccessor",
)
