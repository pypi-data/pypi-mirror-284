"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2591 import BeltCreationOptions
    from ._2592 import CycloidalAssemblyCreationOptions
    from ._2593 import CylindricalGearLinearTrainCreationOptions
    from ._2594 import PlanetCarrierCreationOptions
    from ._2595 import ShaftCreationOptions
else:
    import_structure = {
        "_2591": ["BeltCreationOptions"],
        "_2592": ["CycloidalAssemblyCreationOptions"],
        "_2593": ["CylindricalGearLinearTrainCreationOptions"],
        "_2594": ["PlanetCarrierCreationOptions"],
        "_2595": ["ShaftCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltCreationOptions",
    "CycloidalAssemblyCreationOptions",
    "CylindricalGearLinearTrainCreationOptions",
    "PlanetCarrierCreationOptions",
    "ShaftCreationOptions",
)
