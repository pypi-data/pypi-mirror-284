"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1407 import CustomSplineHalfDesign
    from ._1408 import CustomSplineJointDesign
    from ._1409 import DetailedSplineJointSettings
    from ._1410 import DIN5480SplineHalfDesign
    from ._1411 import DIN5480SplineJointDesign
    from ._1412 import DudleyEffectiveLengthApproximationOption
    from ._1413 import FitTypes
    from ._1414 import GBT3478SplineHalfDesign
    from ._1415 import GBT3478SplineJointDesign
    from ._1416 import HeatTreatmentTypes
    from ._1417 import ISO4156SplineHalfDesign
    from ._1418 import ISO4156SplineJointDesign
    from ._1419 import JISB1603SplineJointDesign
    from ._1420 import ManufacturingTypes
    from ._1421 import Modules
    from ._1422 import PressureAngleTypes
    from ._1423 import RootTypes
    from ._1424 import SAEFatigueLifeFactorTypes
    from ._1425 import SAESplineHalfDesign
    from ._1426 import SAESplineJointDesign
    from ._1427 import SAETorqueCycles
    from ._1428 import SplineDesignTypes
    from ._1429 import FinishingMethods
    from ._1430 import SplineFitClassType
    from ._1431 import SplineFixtureTypes
    from ._1432 import SplineHalfDesign
    from ._1433 import SplineJointDesign
    from ._1434 import SplineMaterial
    from ._1435 import SplineRatingTypes
    from ._1436 import SplineToleranceClassTypes
    from ._1437 import StandardSplineHalfDesign
    from ._1438 import StandardSplineJointDesign
else:
    import_structure = {
        "_1407": ["CustomSplineHalfDesign"],
        "_1408": ["CustomSplineJointDesign"],
        "_1409": ["DetailedSplineJointSettings"],
        "_1410": ["DIN5480SplineHalfDesign"],
        "_1411": ["DIN5480SplineJointDesign"],
        "_1412": ["DudleyEffectiveLengthApproximationOption"],
        "_1413": ["FitTypes"],
        "_1414": ["GBT3478SplineHalfDesign"],
        "_1415": ["GBT3478SplineJointDesign"],
        "_1416": ["HeatTreatmentTypes"],
        "_1417": ["ISO4156SplineHalfDesign"],
        "_1418": ["ISO4156SplineJointDesign"],
        "_1419": ["JISB1603SplineJointDesign"],
        "_1420": ["ManufacturingTypes"],
        "_1421": ["Modules"],
        "_1422": ["PressureAngleTypes"],
        "_1423": ["RootTypes"],
        "_1424": ["SAEFatigueLifeFactorTypes"],
        "_1425": ["SAESplineHalfDesign"],
        "_1426": ["SAESplineJointDesign"],
        "_1427": ["SAETorqueCycles"],
        "_1428": ["SplineDesignTypes"],
        "_1429": ["FinishingMethods"],
        "_1430": ["SplineFitClassType"],
        "_1431": ["SplineFixtureTypes"],
        "_1432": ["SplineHalfDesign"],
        "_1433": ["SplineJointDesign"],
        "_1434": ["SplineMaterial"],
        "_1435": ["SplineRatingTypes"],
        "_1436": ["SplineToleranceClassTypes"],
        "_1437": ["StandardSplineHalfDesign"],
        "_1438": ["StandardSplineJointDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CustomSplineHalfDesign",
    "CustomSplineJointDesign",
    "DetailedSplineJointSettings",
    "DIN5480SplineHalfDesign",
    "DIN5480SplineJointDesign",
    "DudleyEffectiveLengthApproximationOption",
    "FitTypes",
    "GBT3478SplineHalfDesign",
    "GBT3478SplineJointDesign",
    "HeatTreatmentTypes",
    "ISO4156SplineHalfDesign",
    "ISO4156SplineJointDesign",
    "JISB1603SplineJointDesign",
    "ManufacturingTypes",
    "Modules",
    "PressureAngleTypes",
    "RootTypes",
    "SAEFatigueLifeFactorTypes",
    "SAESplineHalfDesign",
    "SAESplineJointDesign",
    "SAETorqueCycles",
    "SplineDesignTypes",
    "FinishingMethods",
    "SplineFitClassType",
    "SplineFixtureTypes",
    "SplineHalfDesign",
    "SplineJointDesign",
    "SplineMaterial",
    "SplineRatingTypes",
    "SplineToleranceClassTypes",
    "StandardSplineHalfDesign",
    "StandardSplineJointDesign",
)
