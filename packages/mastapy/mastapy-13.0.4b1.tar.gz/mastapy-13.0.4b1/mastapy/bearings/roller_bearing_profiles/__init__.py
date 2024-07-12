"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1947 import ProfileDataToUse
    from ._1948 import ProfileSet
    from ._1949 import ProfileToFit
    from ._1950 import RollerBearingConicalProfile
    from ._1951 import RollerBearingCrownedProfile
    from ._1952 import RollerBearingDinLundbergProfile
    from ._1953 import RollerBearingFlatProfile
    from ._1954 import RollerBearingJohnsGoharProfile
    from ._1955 import RollerBearingLundbergProfile
    from ._1956 import RollerBearingProfile
    from ._1957 import RollerBearingUserSpecifiedProfile
    from ._1958 import RollerRaceProfilePoint
    from ._1959 import UserSpecifiedProfilePoint
    from ._1960 import UserSpecifiedRollerRaceProfilePoint
else:
    import_structure = {
        "_1947": ["ProfileDataToUse"],
        "_1948": ["ProfileSet"],
        "_1949": ["ProfileToFit"],
        "_1950": ["RollerBearingConicalProfile"],
        "_1951": ["RollerBearingCrownedProfile"],
        "_1952": ["RollerBearingDinLundbergProfile"],
        "_1953": ["RollerBearingFlatProfile"],
        "_1954": ["RollerBearingJohnsGoharProfile"],
        "_1955": ["RollerBearingLundbergProfile"],
        "_1956": ["RollerBearingProfile"],
        "_1957": ["RollerBearingUserSpecifiedProfile"],
        "_1958": ["RollerRaceProfilePoint"],
        "_1959": ["UserSpecifiedProfilePoint"],
        "_1960": ["UserSpecifiedRollerRaceProfilePoint"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProfileDataToUse",
    "ProfileSet",
    "ProfileToFit",
    "RollerBearingConicalProfile",
    "RollerBearingCrownedProfile",
    "RollerBearingDinLundbergProfile",
    "RollerBearingFlatProfile",
    "RollerBearingJohnsGoharProfile",
    "RollerBearingLundbergProfile",
    "RollerBearingProfile",
    "RollerBearingUserSpecifiedProfile",
    "RollerRaceProfilePoint",
    "UserSpecifiedProfilePoint",
    "UserSpecifiedRollerRaceProfilePoint",
)
