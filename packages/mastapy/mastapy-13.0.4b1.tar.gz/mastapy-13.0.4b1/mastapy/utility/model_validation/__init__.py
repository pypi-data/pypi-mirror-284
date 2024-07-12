"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1809 import Fix
    from ._1810 import Severity
    from ._1811 import Status
    from ._1812 import StatusItem
    from ._1813 import StatusItemSeverity
else:
    import_structure = {
        "_1809": ["Fix"],
        "_1810": ["Severity"],
        "_1811": ["Status"],
        "_1812": ["StatusItem"],
        "_1813": ["StatusItemSeverity"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Fix",
    "Severity",
    "Status",
    "StatusItem",
    "StatusItemSeverity",
)
