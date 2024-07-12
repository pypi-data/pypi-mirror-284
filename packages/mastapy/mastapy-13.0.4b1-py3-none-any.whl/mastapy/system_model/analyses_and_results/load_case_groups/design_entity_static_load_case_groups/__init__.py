"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5693 import AbstractAssemblyStaticLoadCaseGroup
    from ._5694 import ComponentStaticLoadCaseGroup
    from ._5695 import ConnectionStaticLoadCaseGroup
    from ._5696 import DesignEntityStaticLoadCaseGroup
    from ._5697 import GearSetStaticLoadCaseGroup
    from ._5698 import PartStaticLoadCaseGroup
else:
    import_structure = {
        "_5693": ["AbstractAssemblyStaticLoadCaseGroup"],
        "_5694": ["ComponentStaticLoadCaseGroup"],
        "_5695": ["ConnectionStaticLoadCaseGroup"],
        "_5696": ["DesignEntityStaticLoadCaseGroup"],
        "_5697": ["GearSetStaticLoadCaseGroup"],
        "_5698": ["PartStaticLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStaticLoadCaseGroup",
    "ComponentStaticLoadCaseGroup",
    "ConnectionStaticLoadCaseGroup",
    "DesignEntityStaticLoadCaseGroup",
    "GearSetStaticLoadCaseGroup",
    "PartStaticLoadCaseGroup",
)
