"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1441 import AGMA6123SplineHalfRating
    from ._1442 import AGMA6123SplineJointRating
    from ._1443 import DIN5466SplineHalfRating
    from ._1444 import DIN5466SplineRating
    from ._1445 import GBT17855SplineHalfRating
    from ._1446 import GBT17855SplineJointRating
    from ._1447 import SAESplineHalfRating
    from ._1448 import SAESplineJointRating
    from ._1449 import SplineHalfRating
    from ._1450 import SplineJointRating
else:
    import_structure = {
        "_1441": ["AGMA6123SplineHalfRating"],
        "_1442": ["AGMA6123SplineJointRating"],
        "_1443": ["DIN5466SplineHalfRating"],
        "_1444": ["DIN5466SplineRating"],
        "_1445": ["GBT17855SplineHalfRating"],
        "_1446": ["GBT17855SplineJointRating"],
        "_1447": ["SAESplineHalfRating"],
        "_1448": ["SAESplineJointRating"],
        "_1449": ["SplineHalfRating"],
        "_1450": ["SplineJointRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA6123SplineHalfRating",
    "AGMA6123SplineJointRating",
    "DIN5466SplineHalfRating",
    "DIN5466SplineRating",
    "GBT17855SplineHalfRating",
    "GBT17855SplineJointRating",
    "SAESplineHalfRating",
    "SAESplineJointRating",
    "SplineHalfRating",
    "SplineJointRating",
)
