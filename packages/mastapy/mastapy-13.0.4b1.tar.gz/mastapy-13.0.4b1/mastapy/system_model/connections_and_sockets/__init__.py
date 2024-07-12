"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2285 import AbstractShaftToMountableComponentConnection
    from ._2286 import BearingInnerSocket
    from ._2287 import BearingOuterSocket
    from ._2288 import BeltConnection
    from ._2289 import CoaxialConnection
    from ._2290 import ComponentConnection
    from ._2291 import ComponentMeasurer
    from ._2292 import Connection
    from ._2293 import CVTBeltConnection
    from ._2294 import CVTPulleySocket
    from ._2295 import CylindricalComponentConnection
    from ._2296 import CylindricalSocket
    from ._2297 import DatumMeasurement
    from ._2298 import ElectricMachineStatorSocket
    from ._2299 import InnerShaftSocket
    from ._2300 import InnerShaftSocketBase
    from ._2301 import InterMountableComponentConnection
    from ._2302 import MountableComponentInnerSocket
    from ._2303 import MountableComponentOuterSocket
    from ._2304 import MountableComponentSocket
    from ._2305 import OuterShaftSocket
    from ._2306 import OuterShaftSocketBase
    from ._2307 import PlanetaryConnection
    from ._2308 import PlanetarySocket
    from ._2309 import PlanetarySocketBase
    from ._2310 import PulleySocket
    from ._2311 import RealignmentResult
    from ._2312 import RollingRingConnection
    from ._2313 import RollingRingSocket
    from ._2314 import ShaftSocket
    from ._2315 import ShaftToMountableComponentConnection
    from ._2316 import Socket
    from ._2317 import SocketConnectionOptions
    from ._2318 import SocketConnectionSelection
else:
    import_structure = {
        "_2285": ["AbstractShaftToMountableComponentConnection"],
        "_2286": ["BearingInnerSocket"],
        "_2287": ["BearingOuterSocket"],
        "_2288": ["BeltConnection"],
        "_2289": ["CoaxialConnection"],
        "_2290": ["ComponentConnection"],
        "_2291": ["ComponentMeasurer"],
        "_2292": ["Connection"],
        "_2293": ["CVTBeltConnection"],
        "_2294": ["CVTPulleySocket"],
        "_2295": ["CylindricalComponentConnection"],
        "_2296": ["CylindricalSocket"],
        "_2297": ["DatumMeasurement"],
        "_2298": ["ElectricMachineStatorSocket"],
        "_2299": ["InnerShaftSocket"],
        "_2300": ["InnerShaftSocketBase"],
        "_2301": ["InterMountableComponentConnection"],
        "_2302": ["MountableComponentInnerSocket"],
        "_2303": ["MountableComponentOuterSocket"],
        "_2304": ["MountableComponentSocket"],
        "_2305": ["OuterShaftSocket"],
        "_2306": ["OuterShaftSocketBase"],
        "_2307": ["PlanetaryConnection"],
        "_2308": ["PlanetarySocket"],
        "_2309": ["PlanetarySocketBase"],
        "_2310": ["PulleySocket"],
        "_2311": ["RealignmentResult"],
        "_2312": ["RollingRingConnection"],
        "_2313": ["RollingRingSocket"],
        "_2314": ["ShaftSocket"],
        "_2315": ["ShaftToMountableComponentConnection"],
        "_2316": ["Socket"],
        "_2317": ["SocketConnectionOptions"],
        "_2318": ["SocketConnectionSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftToMountableComponentConnection",
    "BearingInnerSocket",
    "BearingOuterSocket",
    "BeltConnection",
    "CoaxialConnection",
    "ComponentConnection",
    "ComponentMeasurer",
    "Connection",
    "CVTBeltConnection",
    "CVTPulleySocket",
    "CylindricalComponentConnection",
    "CylindricalSocket",
    "DatumMeasurement",
    "ElectricMachineStatorSocket",
    "InnerShaftSocket",
    "InnerShaftSocketBase",
    "InterMountableComponentConnection",
    "MountableComponentInnerSocket",
    "MountableComponentOuterSocket",
    "MountableComponentSocket",
    "OuterShaftSocket",
    "OuterShaftSocketBase",
    "PlanetaryConnection",
    "PlanetarySocket",
    "PlanetarySocketBase",
    "PulleySocket",
    "RealignmentResult",
    "RollingRingConnection",
    "RollingRingSocket",
    "ShaftSocket",
    "ShaftToMountableComponentConnection",
    "Socket",
    "SocketConnectionOptions",
    "SocketConnectionSelection",
)
