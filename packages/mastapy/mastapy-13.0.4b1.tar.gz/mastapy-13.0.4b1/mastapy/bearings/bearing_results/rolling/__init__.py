"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1986 import BallBearingAnalysisMethod
    from ._1987 import BallBearingContactCalculation
    from ._1988 import BallBearingRaceContactGeometry
    from ._1989 import DIN7322010Results
    from ._1990 import ForceAtLaminaGroupReportable
    from ._1991 import ForceAtLaminaReportable
    from ._1992 import FrictionModelForGyroscopicMoment
    from ._1993 import InternalClearance
    from ._1994 import ISO14179Settings
    from ._1995 import ISO14179SettingsDatabase
    from ._1996 import ISO14179SettingsPerBearingType
    from ._1997 import ISO153122018Results
    from ._1998 import ISOTR1417912001Results
    from ._1999 import ISOTR141792001Results
    from ._2000 import ISOTR1417922001Results
    from ._2001 import LoadedAbstractSphericalRollerBearingStripLoadResults
    from ._2002 import LoadedAngularContactBallBearingElement
    from ._2003 import LoadedAngularContactBallBearingResults
    from ._2004 import LoadedAngularContactBallBearingRow
    from ._2005 import LoadedAngularContactThrustBallBearingElement
    from ._2006 import LoadedAngularContactThrustBallBearingResults
    from ._2007 import LoadedAngularContactThrustBallBearingRow
    from ._2008 import LoadedAsymmetricSphericalRollerBearingElement
    from ._2009 import LoadedAsymmetricSphericalRollerBearingResults
    from ._2010 import LoadedAsymmetricSphericalRollerBearingRow
    from ._2011 import LoadedAsymmetricSphericalRollerBearingStripLoadResults
    from ._2012 import LoadedAxialThrustCylindricalRollerBearingDutyCycle
    from ._2013 import LoadedAxialThrustCylindricalRollerBearingElement
    from ._2014 import LoadedAxialThrustCylindricalRollerBearingResults
    from ._2015 import LoadedAxialThrustCylindricalRollerBearingRow
    from ._2016 import LoadedAxialThrustNeedleRollerBearingElement
    from ._2017 import LoadedAxialThrustNeedleRollerBearingResults
    from ._2018 import LoadedAxialThrustNeedleRollerBearingRow
    from ._2019 import LoadedBallBearingDutyCycle
    from ._2020 import LoadedBallBearingElement
    from ._2021 import LoadedBallBearingRaceResults
    from ._2022 import LoadedBallBearingResults
    from ._2023 import LoadedBallBearingRow
    from ._2024 import LoadedCrossedRollerBearingElement
    from ._2025 import LoadedCrossedRollerBearingResults
    from ._2026 import LoadedCrossedRollerBearingRow
    from ._2027 import LoadedCylindricalRollerBearingDutyCycle
    from ._2028 import LoadedCylindricalRollerBearingElement
    from ._2029 import LoadedCylindricalRollerBearingResults
    from ._2030 import LoadedCylindricalRollerBearingRow
    from ._2031 import LoadedDeepGrooveBallBearingElement
    from ._2032 import LoadedDeepGrooveBallBearingResults
    from ._2033 import LoadedDeepGrooveBallBearingRow
    from ._2034 import LoadedElement
    from ._2035 import LoadedFourPointContactBallBearingElement
    from ._2036 import LoadedFourPointContactBallBearingRaceResults
    from ._2037 import LoadedFourPointContactBallBearingResults
    from ._2038 import LoadedFourPointContactBallBearingRow
    from ._2039 import LoadedMultiPointContactBallBearingElement
    from ._2040 import LoadedNeedleRollerBearingElement
    from ._2041 import LoadedNeedleRollerBearingResults
    from ._2042 import LoadedNeedleRollerBearingRow
    from ._2043 import LoadedNonBarrelRollerBearingDutyCycle
    from ._2044 import LoadedNonBarrelRollerBearingResults
    from ._2045 import LoadedNonBarrelRollerBearingRow
    from ._2046 import LoadedNonBarrelRollerBearingStripLoadResults
    from ._2047 import LoadedNonBarrelRollerElement
    from ._2048 import LoadedRollerBearingElement
    from ._2049 import LoadedRollerBearingResults
    from ._2050 import LoadedRollerBearingRow
    from ._2051 import LoadedRollerStripLoadResults
    from ._2052 import LoadedRollingBearingRaceResults
    from ._2053 import LoadedRollingBearingResults
    from ._2054 import LoadedRollingBearingRow
    from ._2055 import LoadedSelfAligningBallBearingElement
    from ._2056 import LoadedSelfAligningBallBearingResults
    from ._2057 import LoadedSelfAligningBallBearingRow
    from ._2058 import LoadedSphericalRadialRollerBearingElement
    from ._2059 import LoadedSphericalRollerBearingElement
    from ._2060 import LoadedSphericalRollerRadialBearingResults
    from ._2061 import LoadedSphericalRollerRadialBearingRow
    from ._2062 import LoadedSphericalRollerRadialBearingStripLoadResults
    from ._2063 import LoadedSphericalRollerThrustBearingResults
    from ._2064 import LoadedSphericalRollerThrustBearingRow
    from ._2065 import LoadedSphericalThrustRollerBearingElement
    from ._2066 import LoadedTaperRollerBearingDutyCycle
    from ._2067 import LoadedTaperRollerBearingElement
    from ._2068 import LoadedTaperRollerBearingResults
    from ._2069 import LoadedTaperRollerBearingRow
    from ._2070 import LoadedThreePointContactBallBearingElement
    from ._2071 import LoadedThreePointContactBallBearingResults
    from ._2072 import LoadedThreePointContactBallBearingRow
    from ._2073 import LoadedThrustBallBearingElement
    from ._2074 import LoadedThrustBallBearingResults
    from ._2075 import LoadedThrustBallBearingRow
    from ._2076 import LoadedToroidalRollerBearingElement
    from ._2077 import LoadedToroidalRollerBearingResults
    from ._2078 import LoadedToroidalRollerBearingRow
    from ._2079 import LoadedToroidalRollerBearingStripLoadResults
    from ._2080 import MaximumStaticContactStress
    from ._2081 import MaximumStaticContactStressDutyCycle
    from ._2082 import MaximumStaticContactStressResultsAbstract
    from ._2083 import MaxStripLoadStressObject
    from ._2084 import PermissibleContinuousAxialLoadResults
    from ._2085 import PowerRatingF1EstimationMethod
    from ._2086 import PreloadFactorLookupTable
    from ._2087 import ResultsAtRollerOffset
    from ._2088 import RingForceAndDisplacement
    from ._2089 import RollerAnalysisMethod
    from ._2090 import RollingBearingFrictionCoefficients
    from ._2091 import RollingBearingSpeedResults
    from ._2092 import SMTRibStressResults
    from ._2093 import StressAtPosition
    from ._2094 import ThreePointContactInternalClearance
    from ._2095 import TrackTruncationSafetyFactorResults
else:
    import_structure = {
        "_1986": ["BallBearingAnalysisMethod"],
        "_1987": ["BallBearingContactCalculation"],
        "_1988": ["BallBearingRaceContactGeometry"],
        "_1989": ["DIN7322010Results"],
        "_1990": ["ForceAtLaminaGroupReportable"],
        "_1991": ["ForceAtLaminaReportable"],
        "_1992": ["FrictionModelForGyroscopicMoment"],
        "_1993": ["InternalClearance"],
        "_1994": ["ISO14179Settings"],
        "_1995": ["ISO14179SettingsDatabase"],
        "_1996": ["ISO14179SettingsPerBearingType"],
        "_1997": ["ISO153122018Results"],
        "_1998": ["ISOTR1417912001Results"],
        "_1999": ["ISOTR141792001Results"],
        "_2000": ["ISOTR1417922001Results"],
        "_2001": ["LoadedAbstractSphericalRollerBearingStripLoadResults"],
        "_2002": ["LoadedAngularContactBallBearingElement"],
        "_2003": ["LoadedAngularContactBallBearingResults"],
        "_2004": ["LoadedAngularContactBallBearingRow"],
        "_2005": ["LoadedAngularContactThrustBallBearingElement"],
        "_2006": ["LoadedAngularContactThrustBallBearingResults"],
        "_2007": ["LoadedAngularContactThrustBallBearingRow"],
        "_2008": ["LoadedAsymmetricSphericalRollerBearingElement"],
        "_2009": ["LoadedAsymmetricSphericalRollerBearingResults"],
        "_2010": ["LoadedAsymmetricSphericalRollerBearingRow"],
        "_2011": ["LoadedAsymmetricSphericalRollerBearingStripLoadResults"],
        "_2012": ["LoadedAxialThrustCylindricalRollerBearingDutyCycle"],
        "_2013": ["LoadedAxialThrustCylindricalRollerBearingElement"],
        "_2014": ["LoadedAxialThrustCylindricalRollerBearingResults"],
        "_2015": ["LoadedAxialThrustCylindricalRollerBearingRow"],
        "_2016": ["LoadedAxialThrustNeedleRollerBearingElement"],
        "_2017": ["LoadedAxialThrustNeedleRollerBearingResults"],
        "_2018": ["LoadedAxialThrustNeedleRollerBearingRow"],
        "_2019": ["LoadedBallBearingDutyCycle"],
        "_2020": ["LoadedBallBearingElement"],
        "_2021": ["LoadedBallBearingRaceResults"],
        "_2022": ["LoadedBallBearingResults"],
        "_2023": ["LoadedBallBearingRow"],
        "_2024": ["LoadedCrossedRollerBearingElement"],
        "_2025": ["LoadedCrossedRollerBearingResults"],
        "_2026": ["LoadedCrossedRollerBearingRow"],
        "_2027": ["LoadedCylindricalRollerBearingDutyCycle"],
        "_2028": ["LoadedCylindricalRollerBearingElement"],
        "_2029": ["LoadedCylindricalRollerBearingResults"],
        "_2030": ["LoadedCylindricalRollerBearingRow"],
        "_2031": ["LoadedDeepGrooveBallBearingElement"],
        "_2032": ["LoadedDeepGrooveBallBearingResults"],
        "_2033": ["LoadedDeepGrooveBallBearingRow"],
        "_2034": ["LoadedElement"],
        "_2035": ["LoadedFourPointContactBallBearingElement"],
        "_2036": ["LoadedFourPointContactBallBearingRaceResults"],
        "_2037": ["LoadedFourPointContactBallBearingResults"],
        "_2038": ["LoadedFourPointContactBallBearingRow"],
        "_2039": ["LoadedMultiPointContactBallBearingElement"],
        "_2040": ["LoadedNeedleRollerBearingElement"],
        "_2041": ["LoadedNeedleRollerBearingResults"],
        "_2042": ["LoadedNeedleRollerBearingRow"],
        "_2043": ["LoadedNonBarrelRollerBearingDutyCycle"],
        "_2044": ["LoadedNonBarrelRollerBearingResults"],
        "_2045": ["LoadedNonBarrelRollerBearingRow"],
        "_2046": ["LoadedNonBarrelRollerBearingStripLoadResults"],
        "_2047": ["LoadedNonBarrelRollerElement"],
        "_2048": ["LoadedRollerBearingElement"],
        "_2049": ["LoadedRollerBearingResults"],
        "_2050": ["LoadedRollerBearingRow"],
        "_2051": ["LoadedRollerStripLoadResults"],
        "_2052": ["LoadedRollingBearingRaceResults"],
        "_2053": ["LoadedRollingBearingResults"],
        "_2054": ["LoadedRollingBearingRow"],
        "_2055": ["LoadedSelfAligningBallBearingElement"],
        "_2056": ["LoadedSelfAligningBallBearingResults"],
        "_2057": ["LoadedSelfAligningBallBearingRow"],
        "_2058": ["LoadedSphericalRadialRollerBearingElement"],
        "_2059": ["LoadedSphericalRollerBearingElement"],
        "_2060": ["LoadedSphericalRollerRadialBearingResults"],
        "_2061": ["LoadedSphericalRollerRadialBearingRow"],
        "_2062": ["LoadedSphericalRollerRadialBearingStripLoadResults"],
        "_2063": ["LoadedSphericalRollerThrustBearingResults"],
        "_2064": ["LoadedSphericalRollerThrustBearingRow"],
        "_2065": ["LoadedSphericalThrustRollerBearingElement"],
        "_2066": ["LoadedTaperRollerBearingDutyCycle"],
        "_2067": ["LoadedTaperRollerBearingElement"],
        "_2068": ["LoadedTaperRollerBearingResults"],
        "_2069": ["LoadedTaperRollerBearingRow"],
        "_2070": ["LoadedThreePointContactBallBearingElement"],
        "_2071": ["LoadedThreePointContactBallBearingResults"],
        "_2072": ["LoadedThreePointContactBallBearingRow"],
        "_2073": ["LoadedThrustBallBearingElement"],
        "_2074": ["LoadedThrustBallBearingResults"],
        "_2075": ["LoadedThrustBallBearingRow"],
        "_2076": ["LoadedToroidalRollerBearingElement"],
        "_2077": ["LoadedToroidalRollerBearingResults"],
        "_2078": ["LoadedToroidalRollerBearingRow"],
        "_2079": ["LoadedToroidalRollerBearingStripLoadResults"],
        "_2080": ["MaximumStaticContactStress"],
        "_2081": ["MaximumStaticContactStressDutyCycle"],
        "_2082": ["MaximumStaticContactStressResultsAbstract"],
        "_2083": ["MaxStripLoadStressObject"],
        "_2084": ["PermissibleContinuousAxialLoadResults"],
        "_2085": ["PowerRatingF1EstimationMethod"],
        "_2086": ["PreloadFactorLookupTable"],
        "_2087": ["ResultsAtRollerOffset"],
        "_2088": ["RingForceAndDisplacement"],
        "_2089": ["RollerAnalysisMethod"],
        "_2090": ["RollingBearingFrictionCoefficients"],
        "_2091": ["RollingBearingSpeedResults"],
        "_2092": ["SMTRibStressResults"],
        "_2093": ["StressAtPosition"],
        "_2094": ["ThreePointContactInternalClearance"],
        "_2095": ["TrackTruncationSafetyFactorResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallBearingAnalysisMethod",
    "BallBearingContactCalculation",
    "BallBearingRaceContactGeometry",
    "DIN7322010Results",
    "ForceAtLaminaGroupReportable",
    "ForceAtLaminaReportable",
    "FrictionModelForGyroscopicMoment",
    "InternalClearance",
    "ISO14179Settings",
    "ISO14179SettingsDatabase",
    "ISO14179SettingsPerBearingType",
    "ISO153122018Results",
    "ISOTR1417912001Results",
    "ISOTR141792001Results",
    "ISOTR1417922001Results",
    "LoadedAbstractSphericalRollerBearingStripLoadResults",
    "LoadedAngularContactBallBearingElement",
    "LoadedAngularContactBallBearingResults",
    "LoadedAngularContactBallBearingRow",
    "LoadedAngularContactThrustBallBearingElement",
    "LoadedAngularContactThrustBallBearingResults",
    "LoadedAngularContactThrustBallBearingRow",
    "LoadedAsymmetricSphericalRollerBearingElement",
    "LoadedAsymmetricSphericalRollerBearingResults",
    "LoadedAsymmetricSphericalRollerBearingRow",
    "LoadedAsymmetricSphericalRollerBearingStripLoadResults",
    "LoadedAxialThrustCylindricalRollerBearingDutyCycle",
    "LoadedAxialThrustCylindricalRollerBearingElement",
    "LoadedAxialThrustCylindricalRollerBearingResults",
    "LoadedAxialThrustCylindricalRollerBearingRow",
    "LoadedAxialThrustNeedleRollerBearingElement",
    "LoadedAxialThrustNeedleRollerBearingResults",
    "LoadedAxialThrustNeedleRollerBearingRow",
    "LoadedBallBearingDutyCycle",
    "LoadedBallBearingElement",
    "LoadedBallBearingRaceResults",
    "LoadedBallBearingResults",
    "LoadedBallBearingRow",
    "LoadedCrossedRollerBearingElement",
    "LoadedCrossedRollerBearingResults",
    "LoadedCrossedRollerBearingRow",
    "LoadedCylindricalRollerBearingDutyCycle",
    "LoadedCylindricalRollerBearingElement",
    "LoadedCylindricalRollerBearingResults",
    "LoadedCylindricalRollerBearingRow",
    "LoadedDeepGrooveBallBearingElement",
    "LoadedDeepGrooveBallBearingResults",
    "LoadedDeepGrooveBallBearingRow",
    "LoadedElement",
    "LoadedFourPointContactBallBearingElement",
    "LoadedFourPointContactBallBearingRaceResults",
    "LoadedFourPointContactBallBearingResults",
    "LoadedFourPointContactBallBearingRow",
    "LoadedMultiPointContactBallBearingElement",
    "LoadedNeedleRollerBearingElement",
    "LoadedNeedleRollerBearingResults",
    "LoadedNeedleRollerBearingRow",
    "LoadedNonBarrelRollerBearingDutyCycle",
    "LoadedNonBarrelRollerBearingResults",
    "LoadedNonBarrelRollerBearingRow",
    "LoadedNonBarrelRollerBearingStripLoadResults",
    "LoadedNonBarrelRollerElement",
    "LoadedRollerBearingElement",
    "LoadedRollerBearingResults",
    "LoadedRollerBearingRow",
    "LoadedRollerStripLoadResults",
    "LoadedRollingBearingRaceResults",
    "LoadedRollingBearingResults",
    "LoadedRollingBearingRow",
    "LoadedSelfAligningBallBearingElement",
    "LoadedSelfAligningBallBearingResults",
    "LoadedSelfAligningBallBearingRow",
    "LoadedSphericalRadialRollerBearingElement",
    "LoadedSphericalRollerBearingElement",
    "LoadedSphericalRollerRadialBearingResults",
    "LoadedSphericalRollerRadialBearingRow",
    "LoadedSphericalRollerRadialBearingStripLoadResults",
    "LoadedSphericalRollerThrustBearingResults",
    "LoadedSphericalRollerThrustBearingRow",
    "LoadedSphericalThrustRollerBearingElement",
    "LoadedTaperRollerBearingDutyCycle",
    "LoadedTaperRollerBearingElement",
    "LoadedTaperRollerBearingResults",
    "LoadedTaperRollerBearingRow",
    "LoadedThreePointContactBallBearingElement",
    "LoadedThreePointContactBallBearingResults",
    "LoadedThreePointContactBallBearingRow",
    "LoadedThrustBallBearingElement",
    "LoadedThrustBallBearingResults",
    "LoadedThrustBallBearingRow",
    "LoadedToroidalRollerBearingElement",
    "LoadedToroidalRollerBearingResults",
    "LoadedToroidalRollerBearingRow",
    "LoadedToroidalRollerBearingStripLoadResults",
    "MaximumStaticContactStress",
    "MaximumStaticContactStressDutyCycle",
    "MaximumStaticContactStressResultsAbstract",
    "MaxStripLoadStressObject",
    "PermissibleContinuousAxialLoadResults",
    "PowerRatingF1EstimationMethod",
    "PreloadFactorLookupTable",
    "ResultsAtRollerOffset",
    "RingForceAndDisplacement",
    "RollerAnalysisMethod",
    "RollingBearingFrictionCoefficients",
    "RollingBearingSpeedResults",
    "SMTRibStressResults",
    "StressAtPosition",
    "ThreePointContactInternalClearance",
    "TrackTruncationSafetyFactorResults",
)
