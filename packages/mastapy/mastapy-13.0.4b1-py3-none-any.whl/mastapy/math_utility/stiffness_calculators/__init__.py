"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1555 import IndividualContactPosition
    from ._1556 import SurfaceToSurfaceContact
else:
    import_structure = {
        "_1555": ["IndividualContactPosition"],
        "_1556": ["SurfaceToSurfaceContact"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "IndividualContactPosition",
    "SurfaceToSurfaceContact",
)
