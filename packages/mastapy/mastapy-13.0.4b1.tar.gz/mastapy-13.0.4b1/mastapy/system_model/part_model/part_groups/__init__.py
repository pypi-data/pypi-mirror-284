"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2506 import ConcentricOrParallelPartGroup
    from ._2507 import ConcentricPartGroup
    from ._2508 import ConcentricPartGroupParallelToThis
    from ._2509 import DesignMeasurements
    from ._2510 import ParallelPartGroup
    from ._2511 import ParallelPartGroupSelection
    from ._2512 import PartGroup
else:
    import_structure = {
        "_2506": ["ConcentricOrParallelPartGroup"],
        "_2507": ["ConcentricPartGroup"],
        "_2508": ["ConcentricPartGroupParallelToThis"],
        "_2509": ["DesignMeasurements"],
        "_2510": ["ParallelPartGroup"],
        "_2511": ["ParallelPartGroupSelection"],
        "_2512": ["PartGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConcentricOrParallelPartGroup",
    "ConcentricPartGroup",
    "ConcentricPartGroupParallelToThis",
    "DesignMeasurements",
    "ParallelPartGroup",
    "ParallelPartGroupSelection",
    "PartGroup",
)
