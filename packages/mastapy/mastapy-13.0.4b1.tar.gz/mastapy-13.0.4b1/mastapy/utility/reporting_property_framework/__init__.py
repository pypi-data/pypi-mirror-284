"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1806 import CellValuePosition
    from ._1807 import CustomChartType
else:
    import_structure = {
        "_1806": ["CellValuePosition"],
        "_1807": ["CustomChartType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CellValuePosition",
    "CustomChartType",
)
