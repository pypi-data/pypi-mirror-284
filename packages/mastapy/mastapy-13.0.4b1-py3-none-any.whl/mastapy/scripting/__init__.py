"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7583 import ApiEnumForAttribute
    from ._7584 import ApiVersion
    from ._7585 import SMTBitmap
    from ._7587 import MastaPropertyAttribute
    from ._7588 import PythonCommand
    from ._7589 import ScriptingCommand
    from ._7590 import ScriptingExecutionCommand
    from ._7591 import ScriptingObjectCommand
    from ._7592 import ApiVersioning
else:
    import_structure = {
        "_7583": ["ApiEnumForAttribute"],
        "_7584": ["ApiVersion"],
        "_7585": ["SMTBitmap"],
        "_7587": ["MastaPropertyAttribute"],
        "_7588": ["PythonCommand"],
        "_7589": ["ScriptingCommand"],
        "_7590": ["ScriptingExecutionCommand"],
        "_7591": ["ScriptingObjectCommand"],
        "_7592": ["ApiVersioning"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ApiEnumForAttribute",
    "ApiVersion",
    "SMTBitmap",
    "MastaPropertyAttribute",
    "PythonCommand",
    "ScriptingCommand",
    "ScriptingExecutionCommand",
    "ScriptingObjectCommand",
    "ApiVersioning",
)
