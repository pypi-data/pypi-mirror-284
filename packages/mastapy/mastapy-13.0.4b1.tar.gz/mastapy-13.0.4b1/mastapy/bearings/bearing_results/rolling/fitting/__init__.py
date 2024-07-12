"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2130 import InnerRingFittingThermalResults
    from ._2131 import InterferenceComponents
    from ._2132 import OuterRingFittingThermalResults
    from ._2133 import RingFittingThermalResults
else:
    import_structure = {
        "_2130": ["InnerRingFittingThermalResults"],
        "_2131": ["InterferenceComponents"],
        "_2132": ["OuterRingFittingThermalResults"],
        "_2133": ["RingFittingThermalResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "InnerRingFittingThermalResults",
    "InterferenceComponents",
    "OuterRingFittingThermalResults",
    "RingFittingThermalResults",
)
