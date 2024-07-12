"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1190 import ConicalGearBiasModification
    from ._1191 import ConicalGearFlankMicroGeometry
    from ._1192 import ConicalGearLeadModification
    from ._1193 import ConicalGearProfileModification
else:
    import_structure = {
        "_1190": ["ConicalGearBiasModification"],
        "_1191": ["ConicalGearFlankMicroGeometry"],
        "_1192": ["ConicalGearLeadModification"],
        "_1193": ["ConicalGearProfileModification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearBiasModification",
    "ConicalGearFlankMicroGeometry",
    "ConicalGearLeadModification",
    "ConicalGearProfileModification",
)
