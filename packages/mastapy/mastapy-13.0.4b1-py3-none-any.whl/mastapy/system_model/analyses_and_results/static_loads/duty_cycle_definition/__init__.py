"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7010 import AdditionalForcesObtainedFrom
    from ._7011 import BoostPressureLoadCaseInputOptions
    from ._7012 import DesignStateOptions
    from ._7013 import DestinationDesignState
    from ._7014 import ForceInputOptions
    from ._7015 import GearRatioInputOptions
    from ._7016 import LoadCaseNameOptions
    from ._7017 import MomentInputOptions
    from ._7018 import MultiTimeSeriesDataInputFileOptions
    from ._7019 import PointLoadInputOptions
    from ._7020 import PowerLoadInputOptions
    from ._7021 import RampOrSteadyStateInputOptions
    from ._7022 import SpeedInputOptions
    from ._7023 import TimeSeriesImporter
    from ._7024 import TimeStepInputOptions
    from ._7025 import TorqueInputOptions
    from ._7026 import TorqueValuesObtainedFrom
else:
    import_structure = {
        "_7010": ["AdditionalForcesObtainedFrom"],
        "_7011": ["BoostPressureLoadCaseInputOptions"],
        "_7012": ["DesignStateOptions"],
        "_7013": ["DestinationDesignState"],
        "_7014": ["ForceInputOptions"],
        "_7015": ["GearRatioInputOptions"],
        "_7016": ["LoadCaseNameOptions"],
        "_7017": ["MomentInputOptions"],
        "_7018": ["MultiTimeSeriesDataInputFileOptions"],
        "_7019": ["PointLoadInputOptions"],
        "_7020": ["PowerLoadInputOptions"],
        "_7021": ["RampOrSteadyStateInputOptions"],
        "_7022": ["SpeedInputOptions"],
        "_7023": ["TimeSeriesImporter"],
        "_7024": ["TimeStepInputOptions"],
        "_7025": ["TorqueInputOptions"],
        "_7026": ["TorqueValuesObtainedFrom"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdditionalForcesObtainedFrom",
    "BoostPressureLoadCaseInputOptions",
    "DesignStateOptions",
    "DestinationDesignState",
    "ForceInputOptions",
    "GearRatioInputOptions",
    "LoadCaseNameOptions",
    "MomentInputOptions",
    "MultiTimeSeriesDataInputFileOptions",
    "PointLoadInputOptions",
    "PowerLoadInputOptions",
    "RampOrSteadyStateInputOptions",
    "SpeedInputOptions",
    "TimeSeriesImporter",
    "TimeStepInputOptions",
    "TorqueInputOptions",
    "TorqueValuesObtainedFrom",
)
