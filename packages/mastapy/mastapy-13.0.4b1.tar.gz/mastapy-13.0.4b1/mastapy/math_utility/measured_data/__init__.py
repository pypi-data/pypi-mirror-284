"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1583 import GriddedSurfaceAccessor
    from ._1584 import LookupTableBase
    from ._1585 import OnedimensionalFunctionLookupTable
    from ._1586 import TwodimensionalFunctionLookupTable
else:
    import_structure = {
        "_1583": ["GriddedSurfaceAccessor"],
        "_1584": ["LookupTableBase"],
        "_1585": ["OnedimensionalFunctionLookupTable"],
        "_1586": ["TwodimensionalFunctionLookupTable"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GriddedSurfaceAccessor",
    "LookupTableBase",
    "OnedimensionalFunctionLookupTable",
    "TwodimensionalFunctionLookupTable",
)
