"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1455 import KeyedJointDesign
    from ._1456 import KeyTypes
    from ._1457 import KeywayJointHalfDesign
    from ._1458 import NumberOfKeys
else:
    import_structure = {
        "_1455": ["KeyedJointDesign"],
        "_1456": ["KeyTypes"],
        "_1457": ["KeywayJointHalfDesign"],
        "_1458": ["NumberOfKeys"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeyedJointDesign",
    "KeyTypes",
    "KeywayJointHalfDesign",
    "NumberOfKeys",
)
