"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2121 import BallISO2812007Results
    from ._2122 import BallISOTS162812008Results
    from ._2123 import ISO2812007Results
    from ._2124 import ISO762006Results
    from ._2125 import ISOResults
    from ._2126 import ISOTS162812008Results
    from ._2127 import RollerISO2812007Results
    from ._2128 import RollerISOTS162812008Results
    from ._2129 import StressConcentrationMethod
else:
    import_structure = {
        "_2121": ["BallISO2812007Results"],
        "_2122": ["BallISOTS162812008Results"],
        "_2123": ["ISO2812007Results"],
        "_2124": ["ISO762006Results"],
        "_2125": ["ISOResults"],
        "_2126": ["ISOTS162812008Results"],
        "_2127": ["RollerISO2812007Results"],
        "_2128": ["RollerISOTS162812008Results"],
        "_2129": ["StressConcentrationMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallISO2812007Results",
    "BallISOTS162812008Results",
    "ISO2812007Results",
    "ISO762006Results",
    "ISOResults",
    "ISOTS162812008Results",
    "RollerISO2812007Results",
    "RollerISOTS162812008Results",
    "StressConcentrationMethod",
)
