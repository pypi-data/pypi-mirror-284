"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2596 import BeltDrive
    from ._2597 import BeltDriveType
    from ._2598 import Clutch
    from ._2599 import ClutchHalf
    from ._2600 import ClutchType
    from ._2601 import ConceptCoupling
    from ._2602 import ConceptCouplingHalf
    from ._2603 import ConceptCouplingHalfPositioning
    from ._2604 import Coupling
    from ._2605 import CouplingHalf
    from ._2606 import CrowningSpecification
    from ._2607 import CVT
    from ._2608 import CVTPulley
    from ._2609 import PartToPartShearCoupling
    from ._2610 import PartToPartShearCouplingHalf
    from ._2611 import Pulley
    from ._2612 import RigidConnectorStiffnessType
    from ._2613 import RigidConnectorTiltStiffnessTypes
    from ._2614 import RigidConnectorToothLocation
    from ._2615 import RigidConnectorToothSpacingType
    from ._2616 import RigidConnectorTypes
    from ._2617 import RollingRing
    from ._2618 import RollingRingAssembly
    from ._2619 import ShaftHubConnection
    from ._2620 import SplineLeadRelief
    from ._2621 import SpringDamper
    from ._2622 import SpringDamperHalf
    from ._2623 import Synchroniser
    from ._2624 import SynchroniserCone
    from ._2625 import SynchroniserHalf
    from ._2626 import SynchroniserPart
    from ._2627 import SynchroniserSleeve
    from ._2628 import TorqueConverter
    from ._2629 import TorqueConverterPump
    from ._2630 import TorqueConverterSpeedRatio
    from ._2631 import TorqueConverterTurbine
else:
    import_structure = {
        "_2596": ["BeltDrive"],
        "_2597": ["BeltDriveType"],
        "_2598": ["Clutch"],
        "_2599": ["ClutchHalf"],
        "_2600": ["ClutchType"],
        "_2601": ["ConceptCoupling"],
        "_2602": ["ConceptCouplingHalf"],
        "_2603": ["ConceptCouplingHalfPositioning"],
        "_2604": ["Coupling"],
        "_2605": ["CouplingHalf"],
        "_2606": ["CrowningSpecification"],
        "_2607": ["CVT"],
        "_2608": ["CVTPulley"],
        "_2609": ["PartToPartShearCoupling"],
        "_2610": ["PartToPartShearCouplingHalf"],
        "_2611": ["Pulley"],
        "_2612": ["RigidConnectorStiffnessType"],
        "_2613": ["RigidConnectorTiltStiffnessTypes"],
        "_2614": ["RigidConnectorToothLocation"],
        "_2615": ["RigidConnectorToothSpacingType"],
        "_2616": ["RigidConnectorTypes"],
        "_2617": ["RollingRing"],
        "_2618": ["RollingRingAssembly"],
        "_2619": ["ShaftHubConnection"],
        "_2620": ["SplineLeadRelief"],
        "_2621": ["SpringDamper"],
        "_2622": ["SpringDamperHalf"],
        "_2623": ["Synchroniser"],
        "_2624": ["SynchroniserCone"],
        "_2625": ["SynchroniserHalf"],
        "_2626": ["SynchroniserPart"],
        "_2627": ["SynchroniserSleeve"],
        "_2628": ["TorqueConverter"],
        "_2629": ["TorqueConverterPump"],
        "_2630": ["TorqueConverterSpeedRatio"],
        "_2631": ["TorqueConverterTurbine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltDrive",
    "BeltDriveType",
    "Clutch",
    "ClutchHalf",
    "ClutchType",
    "ConceptCoupling",
    "ConceptCouplingHalf",
    "ConceptCouplingHalfPositioning",
    "Coupling",
    "CouplingHalf",
    "CrowningSpecification",
    "CVT",
    "CVTPulley",
    "PartToPartShearCoupling",
    "PartToPartShearCouplingHalf",
    "Pulley",
    "RigidConnectorStiffnessType",
    "RigidConnectorTiltStiffnessTypes",
    "RigidConnectorToothLocation",
    "RigidConnectorToothSpacingType",
    "RigidConnectorTypes",
    "RollingRing",
    "RollingRingAssembly",
    "ShaftHubConnection",
    "SplineLeadRelief",
    "SpringDamper",
    "SpringDamperHalf",
    "Synchroniser",
    "SynchroniserCone",
    "SynchroniserHalf",
    "SynchroniserPart",
    "SynchroniserSleeve",
    "TorqueConverter",
    "TorqueConverterPump",
    "TorqueConverterSpeedRatio",
    "TorqueConverterTurbine",
)
