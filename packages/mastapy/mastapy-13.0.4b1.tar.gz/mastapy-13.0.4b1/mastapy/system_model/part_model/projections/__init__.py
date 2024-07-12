"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2504 import SpecifiedConcentricPartGroupDrawingOrder
    from ._2505 import SpecifiedParallelPartGroupDrawingOrder
else:
    import_structure = {
        "_2504": ["SpecifiedConcentricPartGroupDrawingOrder"],
        "_2505": ["SpecifiedParallelPartGroupDrawingOrder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpecifiedConcentricPartGroupDrawingOrder",
    "SpecifiedParallelPartGroupDrawingOrder",
)
