"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1405 import DetailedRigidConnectorDesign
    from ._1406 import DetailedRigidConnectorHalfDesign
else:
    import_structure = {
        "_1405": ["DetailedRigidConnectorDesign"],
        "_1406": ["DetailedRigidConnectorHalfDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DetailedRigidConnectorDesign",
    "DetailedRigidConnectorHalfDesign",
)
