"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5544 import AbstractMeasuredDynamicResponseAtTime
    from ._5545 import DynamicForceResultAtTime
    from ._5546 import DynamicForceVector3DResult
    from ._5547 import DynamicTorqueResultAtTime
    from ._5548 import DynamicTorqueVector3DResult
else:
    import_structure = {
        "_5544": ["AbstractMeasuredDynamicResponseAtTime"],
        "_5545": ["DynamicForceResultAtTime"],
        "_5546": ["DynamicForceVector3DResult"],
        "_5547": ["DynamicTorqueResultAtTime"],
        "_5548": ["DynamicTorqueVector3DResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractMeasuredDynamicResponseAtTime",
    "DynamicForceResultAtTime",
    "DynamicForceVector3DResult",
    "DynamicTorqueResultAtTime",
    "DynamicTorqueVector3DResult",
)
