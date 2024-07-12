"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1259 import ElementPropertyClass
    from ._1260 import MaterialPropertyClass
else:
    import_structure = {
        "_1259": ["ElementPropertyClass"],
        "_1260": ["MaterialPropertyClass"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElementPropertyClass",
    "MaterialPropertyClass",
)
