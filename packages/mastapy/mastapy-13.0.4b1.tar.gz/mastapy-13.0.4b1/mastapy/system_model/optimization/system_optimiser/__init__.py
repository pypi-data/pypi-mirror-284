"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2257 import DesignStateTargetRatio
    from ._2258 import PlanetGearOptions
    from ._2259 import SystemOptimiser
    from ._2260 import SystemOptimiserDetails
    from ._2261 import ToothNumberFinder
else:
    import_structure = {
        "_2257": ["DesignStateTargetRatio"],
        "_2258": ["PlanetGearOptions"],
        "_2259": ["SystemOptimiser"],
        "_2260": ["SystemOptimiserDetails"],
        "_2261": ["ToothNumberFinder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignStateTargetRatio",
    "PlanetGearOptions",
    "SystemOptimiser",
    "SystemOptimiserDetails",
    "ToothNumberFinder",
)
