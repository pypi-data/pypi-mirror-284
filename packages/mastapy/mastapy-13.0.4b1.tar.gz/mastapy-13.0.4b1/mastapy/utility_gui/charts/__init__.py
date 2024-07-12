"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1872 import BubbleChartDefinition
    from ._1873 import ConstantLine
    from ._1874 import CustomLineChart
    from ._1875 import CustomTableAndChart
    from ._1876 import LegacyChartMathChartDefinition
    from ._1877 import MatrixVisualisationDefinition
    from ._1878 import ModeConstantLine
    from ._1879 import NDChartDefinition
    from ._1880 import ParallelCoordinatesChartDefinition
    from ._1881 import PointsForSurface
    from ._1882 import ScatterChartDefinition
    from ._1883 import Series2D
    from ._1884 import SMTAxis
    from ._1885 import ThreeDChartDefinition
    from ._1886 import ThreeDVectorChartDefinition
    from ._1887 import TwoDChartDefinition
else:
    import_structure = {
        "_1872": ["BubbleChartDefinition"],
        "_1873": ["ConstantLine"],
        "_1874": ["CustomLineChart"],
        "_1875": ["CustomTableAndChart"],
        "_1876": ["LegacyChartMathChartDefinition"],
        "_1877": ["MatrixVisualisationDefinition"],
        "_1878": ["ModeConstantLine"],
        "_1879": ["NDChartDefinition"],
        "_1880": ["ParallelCoordinatesChartDefinition"],
        "_1881": ["PointsForSurface"],
        "_1882": ["ScatterChartDefinition"],
        "_1883": ["Series2D"],
        "_1884": ["SMTAxis"],
        "_1885": ["ThreeDChartDefinition"],
        "_1886": ["ThreeDVectorChartDefinition"],
        "_1887": ["TwoDChartDefinition"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BubbleChartDefinition",
    "ConstantLine",
    "CustomLineChart",
    "CustomTableAndChart",
    "LegacyChartMathChartDefinition",
    "MatrixVisualisationDefinition",
    "ModeConstantLine",
    "NDChartDefinition",
    "ParallelCoordinatesChartDefinition",
    "PointsForSurface",
    "ScatterChartDefinition",
    "Series2D",
    "SMTAxis",
    "ThreeDChartDefinition",
    "ThreeDVectorChartDefinition",
    "TwoDChartDefinition",
)
