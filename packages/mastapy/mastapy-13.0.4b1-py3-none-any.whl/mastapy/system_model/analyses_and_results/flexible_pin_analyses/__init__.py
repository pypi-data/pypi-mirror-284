"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6289 import CombinationAnalysis
    from ._6290 import FlexiblePinAnalysis
    from ._6291 import FlexiblePinAnalysisConceptLevel
    from ._6292 import FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
    from ._6293 import FlexiblePinAnalysisGearAndBearingRating
    from ._6294 import FlexiblePinAnalysisManufactureLevel
    from ._6295 import FlexiblePinAnalysisOptions
    from ._6296 import FlexiblePinAnalysisStopStartAnalysis
    from ._6297 import WindTurbineCertificationReport
else:
    import_structure = {
        "_6289": ["CombinationAnalysis"],
        "_6290": ["FlexiblePinAnalysis"],
        "_6291": ["FlexiblePinAnalysisConceptLevel"],
        "_6292": ["FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass"],
        "_6293": ["FlexiblePinAnalysisGearAndBearingRating"],
        "_6294": ["FlexiblePinAnalysisManufactureLevel"],
        "_6295": ["FlexiblePinAnalysisOptions"],
        "_6296": ["FlexiblePinAnalysisStopStartAnalysis"],
        "_6297": ["WindTurbineCertificationReport"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CombinationAnalysis",
    "FlexiblePinAnalysis",
    "FlexiblePinAnalysisConceptLevel",
    "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
    "FlexiblePinAnalysisGearAndBearingRating",
    "FlexiblePinAnalysisManufactureLevel",
    "FlexiblePinAnalysisOptions",
    "FlexiblePinAnalysisStopStartAnalysis",
    "WindTurbineCertificationReport",
)
