"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1226 import CylindricalGearLTCAContactChartDataAsTextFile
    from ._1227 import CylindricalGearLTCAContactCharts
    from ._1228 import CylindricalGearWorstLTCAContactChartDataAsTextFile
    from ._1229 import CylindricalGearWorstLTCAContactCharts
    from ._1230 import GearLTCAContactChartDataAsTextFile
    from ._1231 import GearLTCAContactCharts
    from ._1232 import PointsWithWorstResults
else:
    import_structure = {
        "_1226": ["CylindricalGearLTCAContactChartDataAsTextFile"],
        "_1227": ["CylindricalGearLTCAContactCharts"],
        "_1228": ["CylindricalGearWorstLTCAContactChartDataAsTextFile"],
        "_1229": ["CylindricalGearWorstLTCAContactCharts"],
        "_1230": ["GearLTCAContactChartDataAsTextFile"],
        "_1231": ["GearLTCAContactCharts"],
        "_1232": ["PointsWithWorstResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearLTCAContactChartDataAsTextFile",
    "CylindricalGearLTCAContactCharts",
    "CylindricalGearWorstLTCAContactChartDataAsTextFile",
    "CylindricalGearWorstLTCAContactCharts",
    "GearLTCAContactChartDataAsTextFile",
    "GearLTCAContactCharts",
    "PointsWithWorstResults",
)
