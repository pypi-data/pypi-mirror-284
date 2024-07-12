"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1577 import AbstractForceAndDisplacementResults
    from ._1578 import ForceAndDisplacementResults
    from ._1579 import ForceResults
    from ._1580 import NodeResults
    from ._1581 import OverridableDisplacementBoundaryCondition
    from ._1582 import VectorWithLinearAndAngularComponents
else:
    import_structure = {
        "_1577": ["AbstractForceAndDisplacementResults"],
        "_1578": ["ForceAndDisplacementResults"],
        "_1579": ["ForceResults"],
        "_1580": ["NodeResults"],
        "_1581": ["OverridableDisplacementBoundaryCondition"],
        "_1582": ["VectorWithLinearAndAngularComponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractForceAndDisplacementResults",
    "ForceAndDisplacementResults",
    "ForceResults",
    "NodeResults",
    "OverridableDisplacementBoundaryCondition",
    "VectorWithLinearAndAngularComponents",
)
