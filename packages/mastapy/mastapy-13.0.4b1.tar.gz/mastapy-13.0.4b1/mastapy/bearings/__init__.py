"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1889 import BearingCatalog
    from ._1890 import BasicDynamicLoadRatingCalculationMethod
    from ._1891 import BasicStaticLoadRatingCalculationMethod
    from ._1892 import BearingCageMaterial
    from ._1893 import BearingDampingMatrixOption
    from ._1894 import BearingLoadCaseResultsForPST
    from ._1895 import BearingLoadCaseResultsLightweight
    from ._1896 import BearingMeasurementType
    from ._1897 import BearingModel
    from ._1898 import BearingRow
    from ._1899 import BearingSettings
    from ._1900 import BearingSettingsDatabase
    from ._1901 import BearingSettingsItem
    from ._1902 import BearingStiffnessMatrixOption
    from ._1903 import ExponentAndReductionFactorsInISO16281Calculation
    from ._1904 import FluidFilmTemperatureOptions
    from ._1905 import HybridSteelAll
    from ._1906 import JournalBearingType
    from ._1907 import JournalOilFeedType
    from ._1908 import MountingPointSurfaceFinishes
    from ._1909 import OuterRingMounting
    from ._1910 import RatingLife
    from ._1911 import RollerBearingProfileTypes
    from ._1912 import RollingBearingArrangement
    from ._1913 import RollingBearingDatabase
    from ._1914 import RollingBearingKey
    from ._1915 import RollingBearingRaceType
    from ._1916 import RollingBearingType
    from ._1917 import RotationalDirections
    from ._1918 import SealLocation
    from ._1919 import SKFSettings
    from ._1920 import TiltingPadTypes
else:
    import_structure = {
        "_1889": ["BearingCatalog"],
        "_1890": ["BasicDynamicLoadRatingCalculationMethod"],
        "_1891": ["BasicStaticLoadRatingCalculationMethod"],
        "_1892": ["BearingCageMaterial"],
        "_1893": ["BearingDampingMatrixOption"],
        "_1894": ["BearingLoadCaseResultsForPST"],
        "_1895": ["BearingLoadCaseResultsLightweight"],
        "_1896": ["BearingMeasurementType"],
        "_1897": ["BearingModel"],
        "_1898": ["BearingRow"],
        "_1899": ["BearingSettings"],
        "_1900": ["BearingSettingsDatabase"],
        "_1901": ["BearingSettingsItem"],
        "_1902": ["BearingStiffnessMatrixOption"],
        "_1903": ["ExponentAndReductionFactorsInISO16281Calculation"],
        "_1904": ["FluidFilmTemperatureOptions"],
        "_1905": ["HybridSteelAll"],
        "_1906": ["JournalBearingType"],
        "_1907": ["JournalOilFeedType"],
        "_1908": ["MountingPointSurfaceFinishes"],
        "_1909": ["OuterRingMounting"],
        "_1910": ["RatingLife"],
        "_1911": ["RollerBearingProfileTypes"],
        "_1912": ["RollingBearingArrangement"],
        "_1913": ["RollingBearingDatabase"],
        "_1914": ["RollingBearingKey"],
        "_1915": ["RollingBearingRaceType"],
        "_1916": ["RollingBearingType"],
        "_1917": ["RotationalDirections"],
        "_1918": ["SealLocation"],
        "_1919": ["SKFSettings"],
        "_1920": ["TiltingPadTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingCatalog",
    "BasicDynamicLoadRatingCalculationMethod",
    "BasicStaticLoadRatingCalculationMethod",
    "BearingCageMaterial",
    "BearingDampingMatrixOption",
    "BearingLoadCaseResultsForPST",
    "BearingLoadCaseResultsLightweight",
    "BearingMeasurementType",
    "BearingModel",
    "BearingRow",
    "BearingSettings",
    "BearingSettingsDatabase",
    "BearingSettingsItem",
    "BearingStiffnessMatrixOption",
    "ExponentAndReductionFactorsInISO16281Calculation",
    "FluidFilmTemperatureOptions",
    "HybridSteelAll",
    "JournalBearingType",
    "JournalOilFeedType",
    "MountingPointSurfaceFinishes",
    "OuterRingMounting",
    "RatingLife",
    "RollerBearingProfileTypes",
    "RollingBearingArrangement",
    "RollingBearingDatabase",
    "RollingBearingKey",
    "RollingBearingRaceType",
    "RollingBearingType",
    "RotationalDirections",
    "SealLocation",
    "SKFSettings",
    "TiltingPadTypes",
)
