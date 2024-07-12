"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2530 import ActiveCylindricalGearSetDesignSelection
    from ._2531 import ActiveGearSetDesignSelection
    from ._2532 import ActiveGearSetDesignSelectionGroup
    from ._2533 import AGMAGleasonConicalGear
    from ._2534 import AGMAGleasonConicalGearSet
    from ._2535 import BevelDifferentialGear
    from ._2536 import BevelDifferentialGearSet
    from ._2537 import BevelDifferentialPlanetGear
    from ._2538 import BevelDifferentialSunGear
    from ._2539 import BevelGear
    from ._2540 import BevelGearSet
    from ._2541 import ConceptGear
    from ._2542 import ConceptGearSet
    from ._2543 import ConicalGear
    from ._2544 import ConicalGearSet
    from ._2545 import CylindricalGear
    from ._2546 import CylindricalGearSet
    from ._2547 import CylindricalPlanetGear
    from ._2548 import FaceGear
    from ._2549 import FaceGearSet
    from ._2550 import Gear
    from ._2551 import GearOrientations
    from ._2552 import GearSet
    from ._2553 import GearSetConfiguration
    from ._2554 import HypoidGear
    from ._2555 import HypoidGearSet
    from ._2556 import KlingelnbergCycloPalloidConicalGear
    from ._2557 import KlingelnbergCycloPalloidConicalGearSet
    from ._2558 import KlingelnbergCycloPalloidHypoidGear
    from ._2559 import KlingelnbergCycloPalloidHypoidGearSet
    from ._2560 import KlingelnbergCycloPalloidSpiralBevelGear
    from ._2561 import KlingelnbergCycloPalloidSpiralBevelGearSet
    from ._2562 import PlanetaryGearSet
    from ._2563 import SpiralBevelGear
    from ._2564 import SpiralBevelGearSet
    from ._2565 import StraightBevelDiffGear
    from ._2566 import StraightBevelDiffGearSet
    from ._2567 import StraightBevelGear
    from ._2568 import StraightBevelGearSet
    from ._2569 import StraightBevelPlanetGear
    from ._2570 import StraightBevelSunGear
    from ._2571 import WormGear
    from ._2572 import WormGearSet
    from ._2573 import ZerolBevelGear
    from ._2574 import ZerolBevelGearSet
else:
    import_structure = {
        "_2530": ["ActiveCylindricalGearSetDesignSelection"],
        "_2531": ["ActiveGearSetDesignSelection"],
        "_2532": ["ActiveGearSetDesignSelectionGroup"],
        "_2533": ["AGMAGleasonConicalGear"],
        "_2534": ["AGMAGleasonConicalGearSet"],
        "_2535": ["BevelDifferentialGear"],
        "_2536": ["BevelDifferentialGearSet"],
        "_2537": ["BevelDifferentialPlanetGear"],
        "_2538": ["BevelDifferentialSunGear"],
        "_2539": ["BevelGear"],
        "_2540": ["BevelGearSet"],
        "_2541": ["ConceptGear"],
        "_2542": ["ConceptGearSet"],
        "_2543": ["ConicalGear"],
        "_2544": ["ConicalGearSet"],
        "_2545": ["CylindricalGear"],
        "_2546": ["CylindricalGearSet"],
        "_2547": ["CylindricalPlanetGear"],
        "_2548": ["FaceGear"],
        "_2549": ["FaceGearSet"],
        "_2550": ["Gear"],
        "_2551": ["GearOrientations"],
        "_2552": ["GearSet"],
        "_2553": ["GearSetConfiguration"],
        "_2554": ["HypoidGear"],
        "_2555": ["HypoidGearSet"],
        "_2556": ["KlingelnbergCycloPalloidConicalGear"],
        "_2557": ["KlingelnbergCycloPalloidConicalGearSet"],
        "_2558": ["KlingelnbergCycloPalloidHypoidGear"],
        "_2559": ["KlingelnbergCycloPalloidHypoidGearSet"],
        "_2560": ["KlingelnbergCycloPalloidSpiralBevelGear"],
        "_2561": ["KlingelnbergCycloPalloidSpiralBevelGearSet"],
        "_2562": ["PlanetaryGearSet"],
        "_2563": ["SpiralBevelGear"],
        "_2564": ["SpiralBevelGearSet"],
        "_2565": ["StraightBevelDiffGear"],
        "_2566": ["StraightBevelDiffGearSet"],
        "_2567": ["StraightBevelGear"],
        "_2568": ["StraightBevelGearSet"],
        "_2569": ["StraightBevelPlanetGear"],
        "_2570": ["StraightBevelSunGear"],
        "_2571": ["WormGear"],
        "_2572": ["WormGearSet"],
        "_2573": ["ZerolBevelGear"],
        "_2574": ["ZerolBevelGearSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveCylindricalGearSetDesignSelection",
    "ActiveGearSetDesignSelection",
    "ActiveGearSetDesignSelectionGroup",
    "AGMAGleasonConicalGear",
    "AGMAGleasonConicalGearSet",
    "BevelDifferentialGear",
    "BevelDifferentialGearSet",
    "BevelDifferentialPlanetGear",
    "BevelDifferentialSunGear",
    "BevelGear",
    "BevelGearSet",
    "ConceptGear",
    "ConceptGearSet",
    "ConicalGear",
    "ConicalGearSet",
    "CylindricalGear",
    "CylindricalGearSet",
    "CylindricalPlanetGear",
    "FaceGear",
    "FaceGearSet",
    "Gear",
    "GearOrientations",
    "GearSet",
    "GearSetConfiguration",
    "HypoidGear",
    "HypoidGearSet",
    "KlingelnbergCycloPalloidConicalGear",
    "KlingelnbergCycloPalloidConicalGearSet",
    "KlingelnbergCycloPalloidHypoidGear",
    "KlingelnbergCycloPalloidHypoidGearSet",
    "KlingelnbergCycloPalloidSpiralBevelGear",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
    "PlanetaryGearSet",
    "SpiralBevelGear",
    "SpiralBevelGearSet",
    "StraightBevelDiffGear",
    "StraightBevelDiffGearSet",
    "StraightBevelGear",
    "StraightBevelGearSet",
    "StraightBevelPlanetGear",
    "StraightBevelSunGear",
    "WormGear",
    "WormGearSet",
    "ZerolBevelGear",
    "ZerolBevelGearSet",
)
