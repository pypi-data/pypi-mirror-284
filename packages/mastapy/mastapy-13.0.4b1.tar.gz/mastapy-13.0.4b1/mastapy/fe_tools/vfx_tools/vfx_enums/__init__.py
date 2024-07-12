"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1257 import ProSolveMpcType
    from ._1258 import ProSolveSolverType
else:
    import_structure = {
        "_1257": ["ProSolveMpcType"],
        "_1258": ["ProSolveSolverType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProSolveMpcType",
    "ProSolveSolverType",
)
