"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1396 import ElectricMachineHarmonicLoadDataBase
    from ._1397 import ForceDisplayOption
    from ._1398 import HarmonicLoadDataBase
    from ._1399 import HarmonicLoadDataControlExcitationOptionBase
    from ._1400 import HarmonicLoadDataType
    from ._1401 import SpeedDependentHarmonicLoadData
    from ._1402 import StatorToothInterpolator
    from ._1403 import StatorToothLoadInterpolator
    from ._1404 import StatorToothMomentInterpolator
else:
    import_structure = {
        "_1396": ["ElectricMachineHarmonicLoadDataBase"],
        "_1397": ["ForceDisplayOption"],
        "_1398": ["HarmonicLoadDataBase"],
        "_1399": ["HarmonicLoadDataControlExcitationOptionBase"],
        "_1400": ["HarmonicLoadDataType"],
        "_1401": ["SpeedDependentHarmonicLoadData"],
        "_1402": ["StatorToothInterpolator"],
        "_1403": ["StatorToothLoadInterpolator"],
        "_1404": ["StatorToothMomentInterpolator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElectricMachineHarmonicLoadDataBase",
    "ForceDisplayOption",
    "HarmonicLoadDataBase",
    "HarmonicLoadDataControlExcitationOptionBase",
    "HarmonicLoadDataType",
    "SpeedDependentHarmonicLoadData",
    "StatorToothInterpolator",
    "StatorToothLoadInterpolator",
    "StatorToothMomentInterpolator",
)
