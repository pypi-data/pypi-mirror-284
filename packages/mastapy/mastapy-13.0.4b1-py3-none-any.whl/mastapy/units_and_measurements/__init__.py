"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7581 import MeasurementType
    from ._7582 import MeasurementTypeExtensions
else:
    import_structure = {
        "_7581": ["MeasurementType"],
        "_7582": ["MeasurementTypeExtensions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "MeasurementType",
    "MeasurementTypeExtensions",
)
