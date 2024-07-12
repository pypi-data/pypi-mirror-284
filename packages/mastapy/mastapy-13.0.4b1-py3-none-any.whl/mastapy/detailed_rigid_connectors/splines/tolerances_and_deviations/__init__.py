"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1439 import FitAndTolerance
    from ._1440 import SAESplineTolerances
else:
    import_structure = {
        "_1439": ["FitAndTolerance"],
        "_1440": ["SAESplineTolerances"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FitAndTolerance",
    "SAESplineTolerances",
)
