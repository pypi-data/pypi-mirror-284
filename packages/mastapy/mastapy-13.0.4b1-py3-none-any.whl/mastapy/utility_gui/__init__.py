"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1867 import ColumnInputOptions
    from ._1868 import DataInputFileOptions
    from ._1869 import DataLoggerItem
    from ._1870 import DataLoggerWithCharts
    from ._1871 import ScalingDrawStyle
else:
    import_structure = {
        "_1867": ["ColumnInputOptions"],
        "_1868": ["DataInputFileOptions"],
        "_1869": ["DataLoggerItem"],
        "_1870": ["DataLoggerWithCharts"],
        "_1871": ["ScalingDrawStyle"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ColumnInputOptions",
    "DataInputFileOptions",
    "DataLoggerItem",
    "DataLoggerWithCharts",
    "ScalingDrawStyle",
)
