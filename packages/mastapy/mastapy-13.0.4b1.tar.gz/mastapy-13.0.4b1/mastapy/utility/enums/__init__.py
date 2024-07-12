"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1837 import BearingForceArrowOption
    from ._1838 import TableAndChartOptions
    from ._1839 import ThreeDViewContourOption
    from ._1840 import ThreeDViewContourOptionFirstSelection
    from ._1841 import ThreeDViewContourOptionSecondSelection
else:
    import_structure = {
        "_1837": ["BearingForceArrowOption"],
        "_1838": ["TableAndChartOptions"],
        "_1839": ["ThreeDViewContourOption"],
        "_1840": ["ThreeDViewContourOptionFirstSelection"],
        "_1841": ["ThreeDViewContourOptionSecondSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingForceArrowOption",
    "TableAndChartOptions",
    "ThreeDViewContourOption",
    "ThreeDViewContourOptionFirstSelection",
    "ThreeDViewContourOptionSecondSelection",
)
