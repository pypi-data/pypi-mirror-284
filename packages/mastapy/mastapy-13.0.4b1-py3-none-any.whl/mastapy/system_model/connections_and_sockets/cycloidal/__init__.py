"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2353 import CycloidalDiscAxialLeftSocket
    from ._2354 import CycloidalDiscAxialRightSocket
    from ._2355 import CycloidalDiscCentralBearingConnection
    from ._2356 import CycloidalDiscInnerSocket
    from ._2357 import CycloidalDiscOuterSocket
    from ._2358 import CycloidalDiscPlanetaryBearingConnection
    from ._2359 import CycloidalDiscPlanetaryBearingSocket
    from ._2360 import RingPinsSocket
    from ._2361 import RingPinsToDiscConnection
else:
    import_structure = {
        "_2353": ["CycloidalDiscAxialLeftSocket"],
        "_2354": ["CycloidalDiscAxialRightSocket"],
        "_2355": ["CycloidalDiscCentralBearingConnection"],
        "_2356": ["CycloidalDiscInnerSocket"],
        "_2357": ["CycloidalDiscOuterSocket"],
        "_2358": ["CycloidalDiscPlanetaryBearingConnection"],
        "_2359": ["CycloidalDiscPlanetaryBearingSocket"],
        "_2360": ["RingPinsSocket"],
        "_2361": ["RingPinsToDiscConnection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalDiscAxialLeftSocket",
    "CycloidalDiscAxialRightSocket",
    "CycloidalDiscCentralBearingConnection",
    "CycloidalDiscInnerSocket",
    "CycloidalDiscOuterSocket",
    "CycloidalDiscPlanetaryBearingConnection",
    "CycloidalDiscPlanetaryBearingSocket",
    "RingPinsSocket",
    "RingPinsToDiscConnection",
)
