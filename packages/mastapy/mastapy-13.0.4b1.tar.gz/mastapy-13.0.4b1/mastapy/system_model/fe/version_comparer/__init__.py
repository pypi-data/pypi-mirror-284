"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2432 import DesignResults
    from ._2433 import FESubstructureResults
    from ._2434 import FESubstructureVersionComparer
    from ._2435 import LoadCaseResults
    from ._2436 import LoadCasesToRun
    from ._2437 import NodeComparisonResult
else:
    import_structure = {
        "_2432": ["DesignResults"],
        "_2433": ["FESubstructureResults"],
        "_2434": ["FESubstructureVersionComparer"],
        "_2435": ["LoadCaseResults"],
        "_2436": ["LoadCasesToRun"],
        "_2437": ["NodeComparisonResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignResults",
    "FESubstructureResults",
    "FESubstructureVersionComparer",
    "LoadCaseResults",
    "LoadCasesToRun",
    "NodeComparisonResult",
)
