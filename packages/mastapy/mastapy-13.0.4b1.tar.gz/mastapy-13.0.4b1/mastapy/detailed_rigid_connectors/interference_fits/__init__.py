"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1461 import AssemblyMethods
    from ._1462 import CalculationMethods
    from ._1463 import InterferenceFitDesign
    from ._1464 import InterferenceFitHalfDesign
    from ._1465 import StressRegions
    from ._1466 import Table4JointInterfaceTypes
else:
    import_structure = {
        "_1461": ["AssemblyMethods"],
        "_1462": ["CalculationMethods"],
        "_1463": ["InterferenceFitDesign"],
        "_1464": ["InterferenceFitHalfDesign"],
        "_1465": ["StressRegions"],
        "_1466": ["Table4JointInterfaceTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AssemblyMethods",
    "CalculationMethods",
    "InterferenceFitDesign",
    "InterferenceFitHalfDesign",
    "StressRegions",
    "Table4JointInterfaceTypes",
)
