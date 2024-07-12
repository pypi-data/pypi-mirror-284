"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1149 import AGMA2000A88AccuracyGrader
    from ._1150 import AGMA20151A01AccuracyGrader
    from ._1151 import AGMA20151AccuracyGrades
    from ._1152 import AGMAISO13281B14AccuracyGrader
    from ._1153 import Customer102AGMA2000AccuracyGrader
    from ._1154 import CylindricalAccuracyGrader
    from ._1155 import CylindricalAccuracyGraderWithProfileFormAndSlope
    from ._1156 import CylindricalAccuracyGrades
    from ._1157 import CylindricalGearAccuracyTolerances
    from ._1158 import DIN3967SystemOfGearFits
    from ._1159 import ISO132811995AccuracyGrader
    from ._1160 import ISO132812013AccuracyGrader
    from ._1161 import ISO1328AccuracyGraderCommon
    from ._1162 import ISO1328AccuracyGrades
    from ._1163 import OverridableTolerance
else:
    import_structure = {
        "_1149": ["AGMA2000A88AccuracyGrader"],
        "_1150": ["AGMA20151A01AccuracyGrader"],
        "_1151": ["AGMA20151AccuracyGrades"],
        "_1152": ["AGMAISO13281B14AccuracyGrader"],
        "_1153": ["Customer102AGMA2000AccuracyGrader"],
        "_1154": ["CylindricalAccuracyGrader"],
        "_1155": ["CylindricalAccuracyGraderWithProfileFormAndSlope"],
        "_1156": ["CylindricalAccuracyGrades"],
        "_1157": ["CylindricalGearAccuracyTolerances"],
        "_1158": ["DIN3967SystemOfGearFits"],
        "_1159": ["ISO132811995AccuracyGrader"],
        "_1160": ["ISO132812013AccuracyGrader"],
        "_1161": ["ISO1328AccuracyGraderCommon"],
        "_1162": ["ISO1328AccuracyGrades"],
        "_1163": ["OverridableTolerance"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA2000A88AccuracyGrader",
    "AGMA20151A01AccuracyGrader",
    "AGMA20151AccuracyGrades",
    "AGMAISO13281B14AccuracyGrader",
    "Customer102AGMA2000AccuracyGrader",
    "CylindricalAccuracyGrader",
    "CylindricalAccuracyGraderWithProfileFormAndSlope",
    "CylindricalAccuracyGrades",
    "CylindricalGearAccuracyTolerances",
    "DIN3967SystemOfGearFits",
    "ISO132811995AccuracyGrader",
    "ISO132812013AccuracyGrader",
    "ISO1328AccuracyGraderCommon",
    "ISO1328AccuracyGrades",
    "OverridableTolerance",
)
