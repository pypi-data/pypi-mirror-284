"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1757 import ScriptingSetup
    from ._1758 import UserDefinedPropertyKey
    from ._1759 import UserSpecifiedData
else:
    import_structure = {
        "_1757": ["ScriptingSetup"],
        "_1758": ["UserDefinedPropertyKey"],
        "_1759": ["UserSpecifiedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ScriptingSetup",
    "UserDefinedPropertyKey",
    "UserSpecifiedData",
)
