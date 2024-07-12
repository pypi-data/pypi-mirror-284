"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2150 import BearingDesign
    from ._2151 import DetailedBearing
    from ._2152 import DummyRollingBearing
    from ._2153 import LinearBearing
    from ._2154 import NonLinearBearing
else:
    import_structure = {
        "_2150": ["BearingDesign"],
        "_2151": ["DetailedBearing"],
        "_2152": ["DummyRollingBearing"],
        "_2153": ["LinearBearing"],
        "_2154": ["NonLinearBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingDesign",
    "DetailedBearing",
    "DummyRollingBearing",
    "LinearBearing",
    "NonLinearBearing",
)
