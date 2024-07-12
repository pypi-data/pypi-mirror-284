"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2586 import GearMaterialExpertSystemMaterialDetails
    from ._2587 import GearMaterialExpertSystemMaterialOptions
else:
    import_structure = {
        "_2586": ["GearMaterialExpertSystemMaterialDetails"],
        "_2587": ["GearMaterialExpertSystemMaterialOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMaterialExpertSystemMaterialDetails",
    "GearMaterialExpertSystemMaterialOptions",
)
