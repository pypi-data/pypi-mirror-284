"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2588 import CycloidalAssembly
    from ._2589 import CycloidalDisc
    from ._2590 import RingPins
else:
    import_structure = {
        "_2588": ["CycloidalAssembly"],
        "_2589": ["CycloidalDisc"],
        "_2590": ["RingPins"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalAssembly",
    "CycloidalDisc",
    "RingPins",
)
