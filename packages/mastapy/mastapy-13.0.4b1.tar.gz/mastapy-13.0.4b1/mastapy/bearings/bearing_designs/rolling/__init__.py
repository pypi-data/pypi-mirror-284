"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2155 import AngularContactBallBearing
    from ._2156 import AngularContactThrustBallBearing
    from ._2157 import AsymmetricSphericalRollerBearing
    from ._2158 import AxialThrustCylindricalRollerBearing
    from ._2159 import AxialThrustNeedleRollerBearing
    from ._2160 import BallBearing
    from ._2161 import BallBearingShoulderDefinition
    from ._2162 import BarrelRollerBearing
    from ._2163 import BearingProtection
    from ._2164 import BearingProtectionDetailsModifier
    from ._2165 import BearingProtectionLevel
    from ._2166 import BearingTypeExtraInformation
    from ._2167 import CageBridgeShape
    from ._2168 import CrossedRollerBearing
    from ._2169 import CylindricalRollerBearing
    from ._2170 import DeepGrooveBallBearing
    from ._2171 import DiameterSeries
    from ._2172 import FatigueLoadLimitCalculationMethodEnum
    from ._2173 import FourPointContactAngleDefinition
    from ._2174 import FourPointContactBallBearing
    from ._2175 import GeometricConstants
    from ._2176 import GeometricConstantsForRollingFrictionalMoments
    from ._2177 import GeometricConstantsForSlidingFrictionalMoments
    from ._2178 import HeightSeries
    from ._2179 import MultiPointContactBallBearing
    from ._2180 import NeedleRollerBearing
    from ._2181 import NonBarrelRollerBearing
    from ._2182 import RollerBearing
    from ._2183 import RollerEndShape
    from ._2184 import RollerRibDetail
    from ._2185 import RollingBearing
    from ._2186 import SelfAligningBallBearing
    from ._2187 import SKFSealFrictionalMomentConstants
    from ._2188 import SleeveType
    from ._2189 import SphericalRollerBearing
    from ._2190 import SphericalRollerThrustBearing
    from ._2191 import TaperRollerBearing
    from ._2192 import ThreePointContactBallBearing
    from ._2193 import ThrustBallBearing
    from ._2194 import ToroidalRollerBearing
    from ._2195 import WidthSeries
else:
    import_structure = {
        "_2155": ["AngularContactBallBearing"],
        "_2156": ["AngularContactThrustBallBearing"],
        "_2157": ["AsymmetricSphericalRollerBearing"],
        "_2158": ["AxialThrustCylindricalRollerBearing"],
        "_2159": ["AxialThrustNeedleRollerBearing"],
        "_2160": ["BallBearing"],
        "_2161": ["BallBearingShoulderDefinition"],
        "_2162": ["BarrelRollerBearing"],
        "_2163": ["BearingProtection"],
        "_2164": ["BearingProtectionDetailsModifier"],
        "_2165": ["BearingProtectionLevel"],
        "_2166": ["BearingTypeExtraInformation"],
        "_2167": ["CageBridgeShape"],
        "_2168": ["CrossedRollerBearing"],
        "_2169": ["CylindricalRollerBearing"],
        "_2170": ["DeepGrooveBallBearing"],
        "_2171": ["DiameterSeries"],
        "_2172": ["FatigueLoadLimitCalculationMethodEnum"],
        "_2173": ["FourPointContactAngleDefinition"],
        "_2174": ["FourPointContactBallBearing"],
        "_2175": ["GeometricConstants"],
        "_2176": ["GeometricConstantsForRollingFrictionalMoments"],
        "_2177": ["GeometricConstantsForSlidingFrictionalMoments"],
        "_2178": ["HeightSeries"],
        "_2179": ["MultiPointContactBallBearing"],
        "_2180": ["NeedleRollerBearing"],
        "_2181": ["NonBarrelRollerBearing"],
        "_2182": ["RollerBearing"],
        "_2183": ["RollerEndShape"],
        "_2184": ["RollerRibDetail"],
        "_2185": ["RollingBearing"],
        "_2186": ["SelfAligningBallBearing"],
        "_2187": ["SKFSealFrictionalMomentConstants"],
        "_2188": ["SleeveType"],
        "_2189": ["SphericalRollerBearing"],
        "_2190": ["SphericalRollerThrustBearing"],
        "_2191": ["TaperRollerBearing"],
        "_2192": ["ThreePointContactBallBearing"],
        "_2193": ["ThrustBallBearing"],
        "_2194": ["ToroidalRollerBearing"],
        "_2195": ["WidthSeries"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AngularContactBallBearing",
    "AngularContactThrustBallBearing",
    "AsymmetricSphericalRollerBearing",
    "AxialThrustCylindricalRollerBearing",
    "AxialThrustNeedleRollerBearing",
    "BallBearing",
    "BallBearingShoulderDefinition",
    "BarrelRollerBearing",
    "BearingProtection",
    "BearingProtectionDetailsModifier",
    "BearingProtectionLevel",
    "BearingTypeExtraInformation",
    "CageBridgeShape",
    "CrossedRollerBearing",
    "CylindricalRollerBearing",
    "DeepGrooveBallBearing",
    "DiameterSeries",
    "FatigueLoadLimitCalculationMethodEnum",
    "FourPointContactAngleDefinition",
    "FourPointContactBallBearing",
    "GeometricConstants",
    "GeometricConstantsForRollingFrictionalMoments",
    "GeometricConstantsForSlidingFrictionalMoments",
    "HeightSeries",
    "MultiPointContactBallBearing",
    "NeedleRollerBearing",
    "NonBarrelRollerBearing",
    "RollerBearing",
    "RollerEndShape",
    "RollerRibDetail",
    "RollingBearing",
    "SelfAligningBallBearing",
    "SKFSealFrictionalMomentConstants",
    "SleeveType",
    "SphericalRollerBearing",
    "SphericalRollerThrustBearing",
    "TaperRollerBearing",
    "ThreePointContactBallBearing",
    "ThrustBallBearing",
    "ToroidalRollerBearing",
    "WidthSeries",
)
