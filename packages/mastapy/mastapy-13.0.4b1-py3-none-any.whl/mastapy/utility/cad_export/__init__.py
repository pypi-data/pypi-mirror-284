"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1850 import CADExportSettings
    from ._1851 import StockDrawings
else:
    import_structure = {
        "_1850": ["CADExportSettings"],
        "_1851": ["StockDrawings"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CADExportSettings",
    "StockDrawings",
)
