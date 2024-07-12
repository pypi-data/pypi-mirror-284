"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1222 import ConicalGearFEModel
    from ._1223 import ConicalMeshFEModel
    from ._1224 import ConicalSetFEModel
    from ._1225 import FlankDataSource
else:
    import_structure = {
        "_1222": ["ConicalGearFEModel"],
        "_1223": ["ConicalMeshFEModel"],
        "_1224": ["ConicalSetFEModel"],
        "_1225": ["FlankDataSource"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearFEModel",
    "ConicalMeshFEModel",
    "ConicalSetFEModel",
    "FlankDataSource",
)
