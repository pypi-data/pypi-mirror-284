"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1210 import AGMAGleasonConicalAccuracyGrades
    from ._1211 import AGMAGleasonConicalGearDesign
    from ._1212 import AGMAGleasonConicalGearMeshDesign
    from ._1213 import AGMAGleasonConicalGearSetDesign
    from ._1214 import AGMAGleasonConicalMeshedGearDesign
else:
    import_structure = {
        "_1210": ["AGMAGleasonConicalAccuracyGrades"],
        "_1211": ["AGMAGleasonConicalGearDesign"],
        "_1212": ["AGMAGleasonConicalGearMeshDesign"],
        "_1213": ["AGMAGleasonConicalGearSetDesign"],
        "_1214": ["AGMAGleasonConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalAccuracyGrades",
    "AGMAGleasonConicalGearDesign",
    "AGMAGleasonConicalGearMeshDesign",
    "AGMAGleasonConicalGearSetDesign",
    "AGMAGleasonConicalMeshedGearDesign",
)
