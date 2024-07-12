"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1459 import KeywayHalfRating
    from ._1460 import KeywayRating
else:
    import_structure = {
        "_1459": ["KeywayHalfRating"],
        "_1460": ["KeywayRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeywayHalfRating",
    "KeywayRating",
)
