"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1815 import GearMeshForTE
    from ._1816 import GearOrderForTE
    from ._1817 import GearPositions
    from ._1818 import HarmonicOrderForTE
    from ._1819 import LabelOnlyOrder
    from ._1820 import OrderForTE
    from ._1821 import OrderSelector
    from ._1822 import OrderWithRadius
    from ._1823 import RollingBearingOrder
    from ._1824 import ShaftOrderForTE
    from ._1825 import UserDefinedOrderForTE
else:
    import_structure = {
        "_1815": ["GearMeshForTE"],
        "_1816": ["GearOrderForTE"],
        "_1817": ["GearPositions"],
        "_1818": ["HarmonicOrderForTE"],
        "_1819": ["LabelOnlyOrder"],
        "_1820": ["OrderForTE"],
        "_1821": ["OrderSelector"],
        "_1822": ["OrderWithRadius"],
        "_1823": ["RollingBearingOrder"],
        "_1824": ["ShaftOrderForTE"],
        "_1825": ["UserDefinedOrderForTE"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMeshForTE",
    "GearOrderForTE",
    "GearPositions",
    "HarmonicOrderForTE",
    "LabelOnlyOrder",
    "OrderForTE",
    "OrderSelector",
    "OrderWithRadius",
    "RollingBearingOrder",
    "ShaftOrderForTE",
    "UserDefinedOrderForTE",
)
