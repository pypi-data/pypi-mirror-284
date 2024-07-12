"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2246 import ConicalGearOptimisationStrategy
    from ._2247 import ConicalGearOptimizationStep
    from ._2248 import ConicalGearOptimizationStrategyDatabase
    from ._2249 import CylindricalGearOptimisationStrategy
    from ._2250 import CylindricalGearOptimizationStep
    from ._2251 import MeasuredAndFactorViewModel
    from ._2252 import MicroGeometryOptimisationTarget
    from ._2253 import OptimizationStep
    from ._2254 import OptimizationStrategy
    from ._2255 import OptimizationStrategyBase
    from ._2256 import OptimizationStrategyDatabase
else:
    import_structure = {
        "_2246": ["ConicalGearOptimisationStrategy"],
        "_2247": ["ConicalGearOptimizationStep"],
        "_2248": ["ConicalGearOptimizationStrategyDatabase"],
        "_2249": ["CylindricalGearOptimisationStrategy"],
        "_2250": ["CylindricalGearOptimizationStep"],
        "_2251": ["MeasuredAndFactorViewModel"],
        "_2252": ["MicroGeometryOptimisationTarget"],
        "_2253": ["OptimizationStep"],
        "_2254": ["OptimizationStrategy"],
        "_2255": ["OptimizationStrategyBase"],
        "_2256": ["OptimizationStrategyDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearOptimisationStrategy",
    "ConicalGearOptimizationStep",
    "ConicalGearOptimizationStrategyDatabase",
    "CylindricalGearOptimisationStrategy",
    "CylindricalGearOptimizationStep",
    "MeasuredAndFactorViewModel",
    "MicroGeometryOptimisationTarget",
    "OptimizationStep",
    "OptimizationStrategy",
    "OptimizationStrategyBase",
    "OptimizationStrategyDatabase",
)
