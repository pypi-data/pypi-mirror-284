"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1164 import CylindricalGearPairCreationOptions
    from ._1165 import GearSetCreationOptions
    from ._1166 import HypoidGearSetCreationOptions
    from ._1167 import SpiralBevelGearSetCreationOptions
else:
    import_structure = {
        "_1164": ["CylindricalGearPairCreationOptions"],
        "_1165": ["GearSetCreationOptions"],
        "_1166": ["HypoidGearSetCreationOptions"],
        "_1167": ["SpiralBevelGearSetCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearPairCreationOptions",
    "GearSetCreationOptions",
    "HypoidGearSetCreationOptions",
    "SpiralBevelGearSetCreationOptions",
)
