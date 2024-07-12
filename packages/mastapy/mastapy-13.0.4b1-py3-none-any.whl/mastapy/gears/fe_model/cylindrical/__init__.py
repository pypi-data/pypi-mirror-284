"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1219 import CylindricalGearFEModel
    from ._1220 import CylindricalGearMeshFEModel
    from ._1221 import CylindricalGearSetFEModel
else:
    import_structure = {
        "_1219": ["CylindricalGearFEModel"],
        "_1220": ["CylindricalGearMeshFEModel"],
        "_1221": ["CylindricalGearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearFEModel",
    "CylindricalGearMeshFEModel",
    "CylindricalGearSetFEModel",
)
