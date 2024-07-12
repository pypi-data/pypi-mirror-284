"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2362 import ClutchConnection
    from ._2363 import ClutchSocket
    from ._2364 import ConceptCouplingConnection
    from ._2365 import ConceptCouplingSocket
    from ._2366 import CouplingConnection
    from ._2367 import CouplingSocket
    from ._2368 import PartToPartShearCouplingConnection
    from ._2369 import PartToPartShearCouplingSocket
    from ._2370 import SpringDamperConnection
    from ._2371 import SpringDamperSocket
    from ._2372 import TorqueConverterConnection
    from ._2373 import TorqueConverterPumpSocket
    from ._2374 import TorqueConverterTurbineSocket
else:
    import_structure = {
        "_2362": ["ClutchConnection"],
        "_2363": ["ClutchSocket"],
        "_2364": ["ConceptCouplingConnection"],
        "_2365": ["ConceptCouplingSocket"],
        "_2366": ["CouplingConnection"],
        "_2367": ["CouplingSocket"],
        "_2368": ["PartToPartShearCouplingConnection"],
        "_2369": ["PartToPartShearCouplingSocket"],
        "_2370": ["SpringDamperConnection"],
        "_2371": ["SpringDamperSocket"],
        "_2372": ["TorqueConverterConnection"],
        "_2373": ["TorqueConverterPumpSocket"],
        "_2374": ["TorqueConverterTurbineSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ClutchConnection",
    "ClutchSocket",
    "ConceptCouplingConnection",
    "ConceptCouplingSocket",
    "CouplingConnection",
    "CouplingSocket",
    "PartToPartShearCouplingConnection",
    "PartToPartShearCouplingSocket",
    "SpringDamperConnection",
    "SpringDamperSocket",
    "TorqueConverterConnection",
    "TorqueConverterPumpSocket",
    "TorqueConverterTurbineSocket",
)
