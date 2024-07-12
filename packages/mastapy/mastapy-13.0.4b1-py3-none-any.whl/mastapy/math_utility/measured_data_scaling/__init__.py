"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1587 import DataScalingOptions
    from ._1588 import DataScalingReferenceValues
    from ._1589 import DataScalingReferenceValuesBase
else:
    import_structure = {
        "_1587": ["DataScalingOptions"],
        "_1588": ["DataScalingReferenceValues"],
        "_1589": ["DataScalingReferenceValuesBase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DataScalingOptions",
    "DataScalingReferenceValues",
    "DataScalingReferenceValuesBase",
)
