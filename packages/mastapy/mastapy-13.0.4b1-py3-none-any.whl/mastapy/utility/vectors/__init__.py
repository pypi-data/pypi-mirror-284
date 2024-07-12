"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1852 import PlaneVectorFieldData
    from ._1853 import PlaneScalarFieldData
else:
    import_structure = {
        "_1852": ["PlaneVectorFieldData"],
        "_1853": ["PlaneScalarFieldData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "PlaneVectorFieldData",
    "PlaneScalarFieldData",
)
