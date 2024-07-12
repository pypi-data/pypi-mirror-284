"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1101 import FinishStockSpecification
    from ._1102 import FinishStockType
    from ._1103 import NominalValueSpecification
    from ._1104 import NoValueSpecification
else:
    import_structure = {
        "_1101": ["FinishStockSpecification"],
        "_1102": ["FinishStockType"],
        "_1103": ["NominalValueSpecification"],
        "_1104": ["NoValueSpecification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FinishStockSpecification",
    "FinishStockType",
    "NominalValueSpecification",
    "NoValueSpecification",
)
