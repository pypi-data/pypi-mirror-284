"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1620 import DegreesMinutesSeconds
    from ._1621 import EnumUnit
    from ._1622 import InverseUnit
    from ._1623 import MeasurementBase
    from ._1624 import MeasurementSettings
    from ._1625 import MeasurementSystem
    from ._1626 import SafetyFactorUnit
    from ._1627 import TimeUnit
    from ._1628 import Unit
    from ._1629 import UnitGradient
else:
    import_structure = {
        "_1620": ["DegreesMinutesSeconds"],
        "_1621": ["EnumUnit"],
        "_1622": ["InverseUnit"],
        "_1623": ["MeasurementBase"],
        "_1624": ["MeasurementSettings"],
        "_1625": ["MeasurementSystem"],
        "_1626": ["SafetyFactorUnit"],
        "_1627": ["TimeUnit"],
        "_1628": ["Unit"],
        "_1629": ["UnitGradient"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DegreesMinutesSeconds",
    "EnumUnit",
    "InverseUnit",
    "MeasurementBase",
    "MeasurementSettings",
    "MeasurementSystem",
    "SafetyFactorUnit",
    "TimeUnit",
    "Unit",
    "UnitGradient",
)
