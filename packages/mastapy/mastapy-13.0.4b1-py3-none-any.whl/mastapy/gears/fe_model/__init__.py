"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1215 import GearFEModel
    from ._1216 import GearMeshFEModel
    from ._1217 import GearMeshingElementOptions
    from ._1218 import GearSetFEModel
else:
    import_structure = {
        "_1215": ["GearFEModel"],
        "_1216": ["GearMeshFEModel"],
        "_1217": ["GearMeshingElementOptions"],
        "_1218": ["GearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearFEModel",
    "GearMeshFEModel",
    "GearMeshingElementOptions",
    "GearSetFEModel",
)
