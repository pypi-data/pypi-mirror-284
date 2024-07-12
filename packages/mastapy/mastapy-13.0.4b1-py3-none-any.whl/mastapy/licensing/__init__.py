"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1506 import LicenceServer
    from ._7593 import LicenceServerDetails
    from ._7594 import ModuleDetails
    from ._7595 import ModuleLicenceStatus
else:
    import_structure = {
        "_1506": ["LicenceServer"],
        "_7593": ["LicenceServerDetails"],
        "_7594": ["ModuleDetails"],
        "_7595": ["ModuleLicenceStatus"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LicenceServer",
    "LicenceServerDetails",
    "ModuleDetails",
    "ModuleLicenceStatus",
)
