"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2632 import ActiveFESubstructureSelection
    from ._2633 import ActiveFESubstructureSelectionGroup
    from ._2634 import ActiveShaftDesignSelection
    from ._2635 import ActiveShaftDesignSelectionGroup
    from ._2636 import BearingDetailConfiguration
    from ._2637 import BearingDetailSelection
    from ._2638 import PartDetailConfiguration
    from ._2639 import PartDetailSelection
else:
    import_structure = {
        "_2632": ["ActiveFESubstructureSelection"],
        "_2633": ["ActiveFESubstructureSelectionGroup"],
        "_2634": ["ActiveShaftDesignSelection"],
        "_2635": ["ActiveShaftDesignSelectionGroup"],
        "_2636": ["BearingDetailConfiguration"],
        "_2637": ["BearingDetailSelection"],
        "_2638": ["PartDetailConfiguration"],
        "_2639": ["PartDetailSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveFESubstructureSelection",
    "ActiveFESubstructureSelectionGroup",
    "ActiveShaftDesignSelection",
    "ActiveShaftDesignSelectionGroup",
    "BearingDetailConfiguration",
    "BearingDetailSelection",
    "PartDetailConfiguration",
    "PartDetailSelection",
)
