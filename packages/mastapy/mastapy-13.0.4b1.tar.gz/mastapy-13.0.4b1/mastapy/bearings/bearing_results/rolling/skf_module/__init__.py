"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2096 import AdjustedSpeed
    from ._2097 import AdjustmentFactors
    from ._2098 import BearingLoads
    from ._2099 import BearingRatingLife
    from ._2100 import DynamicAxialLoadCarryingCapacity
    from ._2101 import Frequencies
    from ._2102 import FrequencyOfOverRolling
    from ._2103 import Friction
    from ._2104 import FrictionalMoment
    from ._2105 import FrictionSources
    from ._2106 import Grease
    from ._2107 import GreaseLifeAndRelubricationInterval
    from ._2108 import GreaseQuantity
    from ._2109 import InitialFill
    from ._2110 import LifeModel
    from ._2111 import MinimumLoad
    from ._2112 import OperatingViscosity
    from ._2113 import PermissibleAxialLoad
    from ._2114 import RotationalFrequency
    from ._2115 import SKFAuthentication
    from ._2116 import SKFCalculationResult
    from ._2117 import SKFCredentials
    from ._2118 import SKFModuleResults
    from ._2119 import StaticSafetyFactors
    from ._2120 import Viscosities
else:
    import_structure = {
        "_2096": ["AdjustedSpeed"],
        "_2097": ["AdjustmentFactors"],
        "_2098": ["BearingLoads"],
        "_2099": ["BearingRatingLife"],
        "_2100": ["DynamicAxialLoadCarryingCapacity"],
        "_2101": ["Frequencies"],
        "_2102": ["FrequencyOfOverRolling"],
        "_2103": ["Friction"],
        "_2104": ["FrictionalMoment"],
        "_2105": ["FrictionSources"],
        "_2106": ["Grease"],
        "_2107": ["GreaseLifeAndRelubricationInterval"],
        "_2108": ["GreaseQuantity"],
        "_2109": ["InitialFill"],
        "_2110": ["LifeModel"],
        "_2111": ["MinimumLoad"],
        "_2112": ["OperatingViscosity"],
        "_2113": ["PermissibleAxialLoad"],
        "_2114": ["RotationalFrequency"],
        "_2115": ["SKFAuthentication"],
        "_2116": ["SKFCalculationResult"],
        "_2117": ["SKFCredentials"],
        "_2118": ["SKFModuleResults"],
        "_2119": ["StaticSafetyFactors"],
        "_2120": ["Viscosities"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdjustedSpeed",
    "AdjustmentFactors",
    "BearingLoads",
    "BearingRatingLife",
    "DynamicAxialLoadCarryingCapacity",
    "Frequencies",
    "FrequencyOfOverRolling",
    "Friction",
    "FrictionalMoment",
    "FrictionSources",
    "Grease",
    "GreaseLifeAndRelubricationInterval",
    "GreaseQuantity",
    "InitialFill",
    "LifeModel",
    "MinimumLoad",
    "OperatingViscosity",
    "PermissibleAxialLoad",
    "RotationalFrequency",
    "SKFAuthentication",
    "SKFCalculationResult",
    "SKFCredentials",
    "SKFModuleResults",
    "StaticSafetyFactors",
    "Viscosities",
)
