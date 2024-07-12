"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2319 import AGMAGleasonConicalGearMesh
    from ._2320 import AGMAGleasonConicalGearTeethSocket
    from ._2321 import BevelDifferentialGearMesh
    from ._2322 import BevelDifferentialGearTeethSocket
    from ._2323 import BevelGearMesh
    from ._2324 import BevelGearTeethSocket
    from ._2325 import ConceptGearMesh
    from ._2326 import ConceptGearTeethSocket
    from ._2327 import ConicalGearMesh
    from ._2328 import ConicalGearTeethSocket
    from ._2329 import CylindricalGearMesh
    from ._2330 import CylindricalGearTeethSocket
    from ._2331 import FaceGearMesh
    from ._2332 import FaceGearTeethSocket
    from ._2333 import GearMesh
    from ._2334 import GearTeethSocket
    from ._2335 import HypoidGearMesh
    from ._2336 import HypoidGearTeethSocket
    from ._2337 import KlingelnbergConicalGearTeethSocket
    from ._2338 import KlingelnbergCycloPalloidConicalGearMesh
    from ._2339 import KlingelnbergCycloPalloidHypoidGearMesh
    from ._2340 import KlingelnbergCycloPalloidSpiralBevelGearMesh
    from ._2341 import KlingelnbergHypoidGearTeethSocket
    from ._2342 import KlingelnbergSpiralBevelGearTeethSocket
    from ._2343 import SpiralBevelGearMesh
    from ._2344 import SpiralBevelGearTeethSocket
    from ._2345 import StraightBevelDiffGearMesh
    from ._2346 import StraightBevelDiffGearTeethSocket
    from ._2347 import StraightBevelGearMesh
    from ._2348 import StraightBevelGearTeethSocket
    from ._2349 import WormGearMesh
    from ._2350 import WormGearTeethSocket
    from ._2351 import ZerolBevelGearMesh
    from ._2352 import ZerolBevelGearTeethSocket
else:
    import_structure = {
        "_2319": ["AGMAGleasonConicalGearMesh"],
        "_2320": ["AGMAGleasonConicalGearTeethSocket"],
        "_2321": ["BevelDifferentialGearMesh"],
        "_2322": ["BevelDifferentialGearTeethSocket"],
        "_2323": ["BevelGearMesh"],
        "_2324": ["BevelGearTeethSocket"],
        "_2325": ["ConceptGearMesh"],
        "_2326": ["ConceptGearTeethSocket"],
        "_2327": ["ConicalGearMesh"],
        "_2328": ["ConicalGearTeethSocket"],
        "_2329": ["CylindricalGearMesh"],
        "_2330": ["CylindricalGearTeethSocket"],
        "_2331": ["FaceGearMesh"],
        "_2332": ["FaceGearTeethSocket"],
        "_2333": ["GearMesh"],
        "_2334": ["GearTeethSocket"],
        "_2335": ["HypoidGearMesh"],
        "_2336": ["HypoidGearTeethSocket"],
        "_2337": ["KlingelnbergConicalGearTeethSocket"],
        "_2338": ["KlingelnbergCycloPalloidConicalGearMesh"],
        "_2339": ["KlingelnbergCycloPalloidHypoidGearMesh"],
        "_2340": ["KlingelnbergCycloPalloidSpiralBevelGearMesh"],
        "_2341": ["KlingelnbergHypoidGearTeethSocket"],
        "_2342": ["KlingelnbergSpiralBevelGearTeethSocket"],
        "_2343": ["SpiralBevelGearMesh"],
        "_2344": ["SpiralBevelGearTeethSocket"],
        "_2345": ["StraightBevelDiffGearMesh"],
        "_2346": ["StraightBevelDiffGearTeethSocket"],
        "_2347": ["StraightBevelGearMesh"],
        "_2348": ["StraightBevelGearTeethSocket"],
        "_2349": ["WormGearMesh"],
        "_2350": ["WormGearTeethSocket"],
        "_2351": ["ZerolBevelGearMesh"],
        "_2352": ["ZerolBevelGearTeethSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearMesh",
    "AGMAGleasonConicalGearTeethSocket",
    "BevelDifferentialGearMesh",
    "BevelDifferentialGearTeethSocket",
    "BevelGearMesh",
    "BevelGearTeethSocket",
    "ConceptGearMesh",
    "ConceptGearTeethSocket",
    "ConicalGearMesh",
    "ConicalGearTeethSocket",
    "CylindricalGearMesh",
    "CylindricalGearTeethSocket",
    "FaceGearMesh",
    "FaceGearTeethSocket",
    "GearMesh",
    "GearTeethSocket",
    "HypoidGearMesh",
    "HypoidGearTeethSocket",
    "KlingelnbergConicalGearTeethSocket",
    "KlingelnbergCycloPalloidConicalGearMesh",
    "KlingelnbergCycloPalloidHypoidGearMesh",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
    "KlingelnbergHypoidGearTeethSocket",
    "KlingelnbergSpiralBevelGearTeethSocket",
    "SpiralBevelGearMesh",
    "SpiralBevelGearTeethSocket",
    "StraightBevelDiffGearMesh",
    "StraightBevelDiffGearTeethSocket",
    "StraightBevelGearMesh",
    "StraightBevelGearTeethSocket",
    "WormGearMesh",
    "WormGearTeethSocket",
    "ZerolBevelGearMesh",
    "ZerolBevelGearTeethSocket",
)
