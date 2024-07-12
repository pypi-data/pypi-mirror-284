"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2201 import AxialFeedJournalBearing
    from ._2202 import AxialGrooveJournalBearing
    from ._2203 import AxialHoleJournalBearing
    from ._2204 import CircumferentialFeedJournalBearing
    from ._2205 import CylindricalHousingJournalBearing
    from ._2206 import MachineryEncasedJournalBearing
    from ._2207 import PadFluidFilmBearing
    from ._2208 import PedestalJournalBearing
    from ._2209 import PlainGreaseFilledJournalBearing
    from ._2210 import PlainGreaseFilledJournalBearingHousingType
    from ._2211 import PlainJournalBearing
    from ._2212 import PlainJournalHousing
    from ._2213 import PlainOilFedJournalBearing
    from ._2214 import TiltingPadJournalBearing
    from ._2215 import TiltingPadThrustBearing
else:
    import_structure = {
        "_2201": ["AxialFeedJournalBearing"],
        "_2202": ["AxialGrooveJournalBearing"],
        "_2203": ["AxialHoleJournalBearing"],
        "_2204": ["CircumferentialFeedJournalBearing"],
        "_2205": ["CylindricalHousingJournalBearing"],
        "_2206": ["MachineryEncasedJournalBearing"],
        "_2207": ["PadFluidFilmBearing"],
        "_2208": ["PedestalJournalBearing"],
        "_2209": ["PlainGreaseFilledJournalBearing"],
        "_2210": ["PlainGreaseFilledJournalBearingHousingType"],
        "_2211": ["PlainJournalBearing"],
        "_2212": ["PlainJournalHousing"],
        "_2213": ["PlainOilFedJournalBearing"],
        "_2214": ["TiltingPadJournalBearing"],
        "_2215": ["TiltingPadThrustBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialFeedJournalBearing",
    "AxialGrooveJournalBearing",
    "AxialHoleJournalBearing",
    "CircumferentialFeedJournalBearing",
    "CylindricalHousingJournalBearing",
    "MachineryEncasedJournalBearing",
    "PadFluidFilmBearing",
    "PedestalJournalBearing",
    "PlainGreaseFilledJournalBearing",
    "PlainGreaseFilledJournalBearingHousingType",
    "PlainJournalBearing",
    "PlainJournalHousing",
    "PlainOilFedJournalBearing",
    "TiltingPadJournalBearing",
    "TiltingPadThrustBearing",
)
