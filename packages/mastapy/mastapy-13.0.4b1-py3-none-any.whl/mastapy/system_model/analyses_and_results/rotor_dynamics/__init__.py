"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4047 import RotorDynamicsDrawStyle
    from ._4048 import ShaftComplexShape
    from ._4049 import ShaftForcedComplexShape
    from ._4050 import ShaftModalComplexShape
    from ._4051 import ShaftModalComplexShapeAtSpeeds
    from ._4052 import ShaftModalComplexShapeAtStiffness
else:
    import_structure = {
        "_4047": ["RotorDynamicsDrawStyle"],
        "_4048": ["ShaftComplexShape"],
        "_4049": ["ShaftForcedComplexShape"],
        "_4050": ["ShaftModalComplexShape"],
        "_4051": ["ShaftModalComplexShapeAtSpeeds"],
        "_4052": ["ShaftModalComplexShapeAtStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "RotorDynamicsDrawStyle",
    "ShaftComplexShape",
    "ShaftForcedComplexShape",
    "ShaftModalComplexShape",
    "ShaftModalComplexShapeAtSpeeds",
    "ShaftModalComplexShapeAtStiffness",
)
