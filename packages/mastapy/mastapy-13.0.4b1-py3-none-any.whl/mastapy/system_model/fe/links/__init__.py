"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2438 import FELink
    from ._2439 import ElectricMachineStatorFELink
    from ._2440 import FELinkWithSelection
    from ._2441 import GearMeshFELink
    from ._2442 import GearWithDuplicatedMeshesFELink
    from ._2443 import MultiAngleConnectionFELink
    from ._2444 import MultiNodeConnectorFELink
    from ._2445 import MultiNodeFELink
    from ._2446 import PlanetaryConnectorMultiNodeFELink
    from ._2447 import PlanetBasedFELink
    from ._2448 import PlanetCarrierFELink
    from ._2449 import PointLoadFELink
    from ._2450 import RollingRingConnectionFELink
    from ._2451 import ShaftHubConnectionFELink
    from ._2452 import SingleNodeFELink
else:
    import_structure = {
        "_2438": ["FELink"],
        "_2439": ["ElectricMachineStatorFELink"],
        "_2440": ["FELinkWithSelection"],
        "_2441": ["GearMeshFELink"],
        "_2442": ["GearWithDuplicatedMeshesFELink"],
        "_2443": ["MultiAngleConnectionFELink"],
        "_2444": ["MultiNodeConnectorFELink"],
        "_2445": ["MultiNodeFELink"],
        "_2446": ["PlanetaryConnectorMultiNodeFELink"],
        "_2447": ["PlanetBasedFELink"],
        "_2448": ["PlanetCarrierFELink"],
        "_2449": ["PointLoadFELink"],
        "_2450": ["RollingRingConnectionFELink"],
        "_2451": ["ShaftHubConnectionFELink"],
        "_2452": ["SingleNodeFELink"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FELink",
    "ElectricMachineStatorFELink",
    "FELinkWithSelection",
    "GearMeshFELink",
    "GearWithDuplicatedMeshesFELink",
    "MultiAngleConnectionFELink",
    "MultiNodeConnectorFELink",
    "MultiNodeFELink",
    "PlanetaryConnectorMultiNodeFELink",
    "PlanetBasedFELink",
    "PlanetCarrierFELink",
    "PointLoadFELink",
    "RollingRingConnectionFELink",
    "ShaftHubConnectionFELink",
    "SingleNodeFELink",
)
