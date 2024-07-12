"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2575 import BoostPressureInputOptions
    from ._2576 import InputPowerInputOptions
    from ._2577 import PressureRatioInputOptions
    from ._2578 import RotorSetDataInputFileOptions
    from ._2579 import RotorSetMeasuredPoint
    from ._2580 import RotorSpeedInputOptions
    from ._2581 import SuperchargerMap
    from ._2582 import SuperchargerMaps
    from ._2583 import SuperchargerRotorSet
    from ._2584 import SuperchargerRotorSetDatabase
    from ._2585 import YVariableForImportedData
else:
    import_structure = {
        "_2575": ["BoostPressureInputOptions"],
        "_2576": ["InputPowerInputOptions"],
        "_2577": ["PressureRatioInputOptions"],
        "_2578": ["RotorSetDataInputFileOptions"],
        "_2579": ["RotorSetMeasuredPoint"],
        "_2580": ["RotorSpeedInputOptions"],
        "_2581": ["SuperchargerMap"],
        "_2582": ["SuperchargerMaps"],
        "_2583": ["SuperchargerRotorSet"],
        "_2584": ["SuperchargerRotorSetDatabase"],
        "_2585": ["YVariableForImportedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BoostPressureInputOptions",
    "InputPowerInputOptions",
    "PressureRatioInputOptions",
    "RotorSetDataInputFileOptions",
    "RotorSetMeasuredPoint",
    "RotorSpeedInputOptions",
    "SuperchargerMap",
    "SuperchargerMaps",
    "SuperchargerRotorSet",
    "SuperchargerRotorSetDatabase",
    "YVariableForImportedData",
)
