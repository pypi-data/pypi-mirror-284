"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2863 import CylindricalGearMeshMisalignmentValue
    from ._2864 import FlexibleGearChart
    from ._2865 import GearInMeshDeflectionResults
    from ._2866 import MeshDeflectionResults
    from ._2867 import PlanetCarrierWindup
    from ._2868 import PlanetPinWindup
    from ._2869 import RigidlyConnectedComponentGroupSystemDeflection
    from ._2870 import ShaftSystemDeflectionSectionsReport
    from ._2871 import SplineFlankContactReporting
else:
    import_structure = {
        "_2863": ["CylindricalGearMeshMisalignmentValue"],
        "_2864": ["FlexibleGearChart"],
        "_2865": ["GearInMeshDeflectionResults"],
        "_2866": ["MeshDeflectionResults"],
        "_2867": ["PlanetCarrierWindup"],
        "_2868": ["PlanetPinWindup"],
        "_2869": ["RigidlyConnectedComponentGroupSystemDeflection"],
        "_2870": ["ShaftSystemDeflectionSectionsReport"],
        "_2871": ["SplineFlankContactReporting"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearMeshMisalignmentValue",
    "FlexibleGearChart",
    "GearInMeshDeflectionResults",
    "MeshDeflectionResults",
    "PlanetCarrierWindup",
    "PlanetPinWindup",
    "RigidlyConnectedComponentGroupSystemDeflection",
    "ShaftSystemDeflectionSectionsReport",
    "SplineFlankContactReporting",
)
