"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2513 import AbstractShaftFromCAD
    from ._2514 import ClutchFromCAD
    from ._2515 import ComponentFromCAD
    from ._2516 import ConceptBearingFromCAD
    from ._2517 import ConnectorFromCAD
    from ._2518 import CylindricalGearFromCAD
    from ._2519 import CylindricalGearInPlanetarySetFromCAD
    from ._2520 import CylindricalPlanetGearFromCAD
    from ._2521 import CylindricalRingGearFromCAD
    from ._2522 import CylindricalSunGearFromCAD
    from ._2523 import HousedOrMounted
    from ._2524 import MountableComponentFromCAD
    from ._2525 import PlanetShaftFromCAD
    from ._2526 import PulleyFromCAD
    from ._2527 import RigidConnectorFromCAD
    from ._2528 import RollingBearingFromCAD
    from ._2529 import ShaftFromCAD
else:
    import_structure = {
        "_2513": ["AbstractShaftFromCAD"],
        "_2514": ["ClutchFromCAD"],
        "_2515": ["ComponentFromCAD"],
        "_2516": ["ConceptBearingFromCAD"],
        "_2517": ["ConnectorFromCAD"],
        "_2518": ["CylindricalGearFromCAD"],
        "_2519": ["CylindricalGearInPlanetarySetFromCAD"],
        "_2520": ["CylindricalPlanetGearFromCAD"],
        "_2521": ["CylindricalRingGearFromCAD"],
        "_2522": ["CylindricalSunGearFromCAD"],
        "_2523": ["HousedOrMounted"],
        "_2524": ["MountableComponentFromCAD"],
        "_2525": ["PlanetShaftFromCAD"],
        "_2526": ["PulleyFromCAD"],
        "_2527": ["RigidConnectorFromCAD"],
        "_2528": ["RollingBearingFromCAD"],
        "_2529": ["ShaftFromCAD"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftFromCAD",
    "ClutchFromCAD",
    "ComponentFromCAD",
    "ConceptBearingFromCAD",
    "ConnectorFromCAD",
    "CylindricalGearFromCAD",
    "CylindricalGearInPlanetarySetFromCAD",
    "CylindricalPlanetGearFromCAD",
    "CylindricalRingGearFromCAD",
    "CylindricalSunGearFromCAD",
    "HousedOrMounted",
    "MountableComponentFromCAD",
    "PlanetShaftFromCAD",
    "PulleyFromCAD",
    "RigidConnectorFromCAD",
    "RollingBearingFromCAD",
    "ShaftFromCAD",
)
