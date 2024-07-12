"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7556 import AnalysisCase
    from ._7557 import AbstractAnalysisOptions
    from ._7558 import CompoundAnalysisCase
    from ._7559 import ConnectionAnalysisCase
    from ._7560 import ConnectionCompoundAnalysis
    from ._7561 import ConnectionFEAnalysis
    from ._7562 import ConnectionStaticLoadAnalysisCase
    from ._7563 import ConnectionTimeSeriesLoadAnalysisCase
    from ._7564 import DesignEntityCompoundAnalysis
    from ._7565 import FEAnalysis
    from ._7566 import PartAnalysisCase
    from ._7567 import PartCompoundAnalysis
    from ._7568 import PartFEAnalysis
    from ._7569 import PartStaticLoadAnalysisCase
    from ._7570 import PartTimeSeriesLoadAnalysisCase
    from ._7571 import StaticLoadAnalysisCase
    from ._7572 import TimeSeriesLoadAnalysisCase
else:
    import_structure = {
        "_7556": ["AnalysisCase"],
        "_7557": ["AbstractAnalysisOptions"],
        "_7558": ["CompoundAnalysisCase"],
        "_7559": ["ConnectionAnalysisCase"],
        "_7560": ["ConnectionCompoundAnalysis"],
        "_7561": ["ConnectionFEAnalysis"],
        "_7562": ["ConnectionStaticLoadAnalysisCase"],
        "_7563": ["ConnectionTimeSeriesLoadAnalysisCase"],
        "_7564": ["DesignEntityCompoundAnalysis"],
        "_7565": ["FEAnalysis"],
        "_7566": ["PartAnalysisCase"],
        "_7567": ["PartCompoundAnalysis"],
        "_7568": ["PartFEAnalysis"],
        "_7569": ["PartStaticLoadAnalysisCase"],
        "_7570": ["PartTimeSeriesLoadAnalysisCase"],
        "_7571": ["StaticLoadAnalysisCase"],
        "_7572": ["TimeSeriesLoadAnalysisCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AnalysisCase",
    "AbstractAnalysisOptions",
    "CompoundAnalysisCase",
    "ConnectionAnalysisCase",
    "ConnectionCompoundAnalysis",
    "ConnectionFEAnalysis",
    "ConnectionStaticLoadAnalysisCase",
    "ConnectionTimeSeriesLoadAnalysisCase",
    "DesignEntityCompoundAnalysis",
    "FEAnalysis",
    "PartAnalysisCase",
    "PartCompoundAnalysis",
    "PartFEAnalysis",
    "PartStaticLoadAnalysisCase",
    "PartTimeSeriesLoadAnalysisCase",
    "StaticLoadAnalysisCase",
    "TimeSeriesLoadAnalysisCase",
)
