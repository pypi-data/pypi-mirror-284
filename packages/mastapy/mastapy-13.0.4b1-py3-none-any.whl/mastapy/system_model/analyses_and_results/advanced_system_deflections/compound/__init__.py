"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7427 import AbstractAssemblyCompoundAdvancedSystemDeflection
    from ._7428 import AbstractShaftCompoundAdvancedSystemDeflection
    from ._7429 import AbstractShaftOrHousingCompoundAdvancedSystemDeflection
    from ._7430 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7431 import AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
    from ._7432 import AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7433 import AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
    from ._7434 import AssemblyCompoundAdvancedSystemDeflection
    from ._7435 import BearingCompoundAdvancedSystemDeflection
    from ._7436 import BeltConnectionCompoundAdvancedSystemDeflection
    from ._7437 import BeltDriveCompoundAdvancedSystemDeflection
    from ._7438 import BevelDifferentialGearCompoundAdvancedSystemDeflection
    from ._7439 import BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
    from ._7440 import BevelDifferentialGearSetCompoundAdvancedSystemDeflection
    from ._7441 import BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
    from ._7442 import BevelDifferentialSunGearCompoundAdvancedSystemDeflection
    from ._7443 import BevelGearCompoundAdvancedSystemDeflection
    from ._7444 import BevelGearMeshCompoundAdvancedSystemDeflection
    from ._7445 import BevelGearSetCompoundAdvancedSystemDeflection
    from ._7446 import BoltCompoundAdvancedSystemDeflection
    from ._7447 import BoltedJointCompoundAdvancedSystemDeflection
    from ._7448 import ClutchCompoundAdvancedSystemDeflection
    from ._7449 import ClutchConnectionCompoundAdvancedSystemDeflection
    from ._7450 import ClutchHalfCompoundAdvancedSystemDeflection
    from ._7451 import CoaxialConnectionCompoundAdvancedSystemDeflection
    from ._7452 import ComponentCompoundAdvancedSystemDeflection
    from ._7453 import ConceptCouplingCompoundAdvancedSystemDeflection
    from ._7454 import ConceptCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7455 import ConceptCouplingHalfCompoundAdvancedSystemDeflection
    from ._7456 import ConceptGearCompoundAdvancedSystemDeflection
    from ._7457 import ConceptGearMeshCompoundAdvancedSystemDeflection
    from ._7458 import ConceptGearSetCompoundAdvancedSystemDeflection
    from ._7459 import ConicalGearCompoundAdvancedSystemDeflection
    from ._7460 import ConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7461 import ConicalGearSetCompoundAdvancedSystemDeflection
    from ._7462 import ConnectionCompoundAdvancedSystemDeflection
    from ._7463 import ConnectorCompoundAdvancedSystemDeflection
    from ._7464 import CouplingCompoundAdvancedSystemDeflection
    from ._7465 import CouplingConnectionCompoundAdvancedSystemDeflection
    from ._7466 import CouplingHalfCompoundAdvancedSystemDeflection
    from ._7467 import CVTBeltConnectionCompoundAdvancedSystemDeflection
    from ._7468 import CVTCompoundAdvancedSystemDeflection
    from ._7469 import CVTPulleyCompoundAdvancedSystemDeflection
    from ._7470 import CycloidalAssemblyCompoundAdvancedSystemDeflection
    from ._7471 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7472 import CycloidalDiscCompoundAdvancedSystemDeflection
    from ._7473 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7474 import CylindricalGearCompoundAdvancedSystemDeflection
    from ._7475 import CylindricalGearMeshCompoundAdvancedSystemDeflection
    from ._7476 import CylindricalGearSetCompoundAdvancedSystemDeflection
    from ._7477 import CylindricalPlanetGearCompoundAdvancedSystemDeflection
    from ._7478 import DatumCompoundAdvancedSystemDeflection
    from ._7479 import ExternalCADModelCompoundAdvancedSystemDeflection
    from ._7480 import FaceGearCompoundAdvancedSystemDeflection
    from ._7481 import FaceGearMeshCompoundAdvancedSystemDeflection
    from ._7482 import FaceGearSetCompoundAdvancedSystemDeflection
    from ._7483 import FEPartCompoundAdvancedSystemDeflection
    from ._7484 import FlexiblePinAssemblyCompoundAdvancedSystemDeflection
    from ._7485 import GearCompoundAdvancedSystemDeflection
    from ._7486 import GearMeshCompoundAdvancedSystemDeflection
    from ._7487 import GearSetCompoundAdvancedSystemDeflection
    from ._7488 import GuideDxfModelCompoundAdvancedSystemDeflection
    from ._7489 import HypoidGearCompoundAdvancedSystemDeflection
    from ._7490 import HypoidGearMeshCompoundAdvancedSystemDeflection
    from ._7491 import HypoidGearSetCompoundAdvancedSystemDeflection
    from ._7492 import InterMountableComponentConnectionCompoundAdvancedSystemDeflection
    from ._7493 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection,
    )
    from ._7494 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7495 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7496 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection,
    )
    from ._7497 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7498 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7499 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection,
    )
    from ._7500 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7501 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7502 import MassDiscCompoundAdvancedSystemDeflection
    from ._7503 import MeasurementComponentCompoundAdvancedSystemDeflection
    from ._7504 import MountableComponentCompoundAdvancedSystemDeflection
    from ._7505 import OilSealCompoundAdvancedSystemDeflection
    from ._7506 import PartCompoundAdvancedSystemDeflection
    from ._7507 import PartToPartShearCouplingCompoundAdvancedSystemDeflection
    from ._7508 import PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7509 import PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
    from ._7510 import PlanetaryConnectionCompoundAdvancedSystemDeflection
    from ._7511 import PlanetaryGearSetCompoundAdvancedSystemDeflection
    from ._7512 import PlanetCarrierCompoundAdvancedSystemDeflection
    from ._7513 import PointLoadCompoundAdvancedSystemDeflection
    from ._7514 import PowerLoadCompoundAdvancedSystemDeflection
    from ._7515 import PulleyCompoundAdvancedSystemDeflection
    from ._7516 import RingPinsCompoundAdvancedSystemDeflection
    from ._7517 import RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
    from ._7518 import RollingRingAssemblyCompoundAdvancedSystemDeflection
    from ._7519 import RollingRingCompoundAdvancedSystemDeflection
    from ._7520 import RollingRingConnectionCompoundAdvancedSystemDeflection
    from ._7521 import RootAssemblyCompoundAdvancedSystemDeflection
    from ._7522 import ShaftCompoundAdvancedSystemDeflection
    from ._7523 import ShaftHubConnectionCompoundAdvancedSystemDeflection
    from ._7524 import (
        ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7525 import SpecialisedAssemblyCompoundAdvancedSystemDeflection
    from ._7526 import SpiralBevelGearCompoundAdvancedSystemDeflection
    from ._7527 import SpiralBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7528 import SpiralBevelGearSetCompoundAdvancedSystemDeflection
    from ._7529 import SpringDamperCompoundAdvancedSystemDeflection
    from ._7530 import SpringDamperConnectionCompoundAdvancedSystemDeflection
    from ._7531 import SpringDamperHalfCompoundAdvancedSystemDeflection
    from ._7532 import StraightBevelDiffGearCompoundAdvancedSystemDeflection
    from ._7533 import StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
    from ._7534 import StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
    from ._7535 import StraightBevelGearCompoundAdvancedSystemDeflection
    from ._7536 import StraightBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7537 import StraightBevelGearSetCompoundAdvancedSystemDeflection
    from ._7538 import StraightBevelPlanetGearCompoundAdvancedSystemDeflection
    from ._7539 import StraightBevelSunGearCompoundAdvancedSystemDeflection
    from ._7540 import SynchroniserCompoundAdvancedSystemDeflection
    from ._7541 import SynchroniserHalfCompoundAdvancedSystemDeflection
    from ._7542 import SynchroniserPartCompoundAdvancedSystemDeflection
    from ._7543 import SynchroniserSleeveCompoundAdvancedSystemDeflection
    from ._7544 import TorqueConverterCompoundAdvancedSystemDeflection
    from ._7545 import TorqueConverterConnectionCompoundAdvancedSystemDeflection
    from ._7546 import TorqueConverterPumpCompoundAdvancedSystemDeflection
    from ._7547 import TorqueConverterTurbineCompoundAdvancedSystemDeflection
    from ._7548 import UnbalancedMassCompoundAdvancedSystemDeflection
    from ._7549 import VirtualComponentCompoundAdvancedSystemDeflection
    from ._7550 import WormGearCompoundAdvancedSystemDeflection
    from ._7551 import WormGearMeshCompoundAdvancedSystemDeflection
    from ._7552 import WormGearSetCompoundAdvancedSystemDeflection
    from ._7553 import ZerolBevelGearCompoundAdvancedSystemDeflection
    from ._7554 import ZerolBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7555 import ZerolBevelGearSetCompoundAdvancedSystemDeflection
else:
    import_structure = {
        "_7427": ["AbstractAssemblyCompoundAdvancedSystemDeflection"],
        "_7428": ["AbstractShaftCompoundAdvancedSystemDeflection"],
        "_7429": ["AbstractShaftOrHousingCompoundAdvancedSystemDeflection"],
        "_7430": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7431": ["AGMAGleasonConicalGearCompoundAdvancedSystemDeflection"],
        "_7432": ["AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7433": ["AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7434": ["AssemblyCompoundAdvancedSystemDeflection"],
        "_7435": ["BearingCompoundAdvancedSystemDeflection"],
        "_7436": ["BeltConnectionCompoundAdvancedSystemDeflection"],
        "_7437": ["BeltDriveCompoundAdvancedSystemDeflection"],
        "_7438": ["BevelDifferentialGearCompoundAdvancedSystemDeflection"],
        "_7439": ["BevelDifferentialGearMeshCompoundAdvancedSystemDeflection"],
        "_7440": ["BevelDifferentialGearSetCompoundAdvancedSystemDeflection"],
        "_7441": ["BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection"],
        "_7442": ["BevelDifferentialSunGearCompoundAdvancedSystemDeflection"],
        "_7443": ["BevelGearCompoundAdvancedSystemDeflection"],
        "_7444": ["BevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7445": ["BevelGearSetCompoundAdvancedSystemDeflection"],
        "_7446": ["BoltCompoundAdvancedSystemDeflection"],
        "_7447": ["BoltedJointCompoundAdvancedSystemDeflection"],
        "_7448": ["ClutchCompoundAdvancedSystemDeflection"],
        "_7449": ["ClutchConnectionCompoundAdvancedSystemDeflection"],
        "_7450": ["ClutchHalfCompoundAdvancedSystemDeflection"],
        "_7451": ["CoaxialConnectionCompoundAdvancedSystemDeflection"],
        "_7452": ["ComponentCompoundAdvancedSystemDeflection"],
        "_7453": ["ConceptCouplingCompoundAdvancedSystemDeflection"],
        "_7454": ["ConceptCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7455": ["ConceptCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7456": ["ConceptGearCompoundAdvancedSystemDeflection"],
        "_7457": ["ConceptGearMeshCompoundAdvancedSystemDeflection"],
        "_7458": ["ConceptGearSetCompoundAdvancedSystemDeflection"],
        "_7459": ["ConicalGearCompoundAdvancedSystemDeflection"],
        "_7460": ["ConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7461": ["ConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7462": ["ConnectionCompoundAdvancedSystemDeflection"],
        "_7463": ["ConnectorCompoundAdvancedSystemDeflection"],
        "_7464": ["CouplingCompoundAdvancedSystemDeflection"],
        "_7465": ["CouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7466": ["CouplingHalfCompoundAdvancedSystemDeflection"],
        "_7467": ["CVTBeltConnectionCompoundAdvancedSystemDeflection"],
        "_7468": ["CVTCompoundAdvancedSystemDeflection"],
        "_7469": ["CVTPulleyCompoundAdvancedSystemDeflection"],
        "_7470": ["CycloidalAssemblyCompoundAdvancedSystemDeflection"],
        "_7471": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7472": ["CycloidalDiscCompoundAdvancedSystemDeflection"],
        "_7473": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7474": ["CylindricalGearCompoundAdvancedSystemDeflection"],
        "_7475": ["CylindricalGearMeshCompoundAdvancedSystemDeflection"],
        "_7476": ["CylindricalGearSetCompoundAdvancedSystemDeflection"],
        "_7477": ["CylindricalPlanetGearCompoundAdvancedSystemDeflection"],
        "_7478": ["DatumCompoundAdvancedSystemDeflection"],
        "_7479": ["ExternalCADModelCompoundAdvancedSystemDeflection"],
        "_7480": ["FaceGearCompoundAdvancedSystemDeflection"],
        "_7481": ["FaceGearMeshCompoundAdvancedSystemDeflection"],
        "_7482": ["FaceGearSetCompoundAdvancedSystemDeflection"],
        "_7483": ["FEPartCompoundAdvancedSystemDeflection"],
        "_7484": ["FlexiblePinAssemblyCompoundAdvancedSystemDeflection"],
        "_7485": ["GearCompoundAdvancedSystemDeflection"],
        "_7486": ["GearMeshCompoundAdvancedSystemDeflection"],
        "_7487": ["GearSetCompoundAdvancedSystemDeflection"],
        "_7488": ["GuideDxfModelCompoundAdvancedSystemDeflection"],
        "_7489": ["HypoidGearCompoundAdvancedSystemDeflection"],
        "_7490": ["HypoidGearMeshCompoundAdvancedSystemDeflection"],
        "_7491": ["HypoidGearSetCompoundAdvancedSystemDeflection"],
        "_7492": ["InterMountableComponentConnectionCompoundAdvancedSystemDeflection"],
        "_7493": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ],
        "_7494": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7495": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7496": ["KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection"],
        "_7497": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7498": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7499": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
        ],
        "_7500": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7501": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7502": ["MassDiscCompoundAdvancedSystemDeflection"],
        "_7503": ["MeasurementComponentCompoundAdvancedSystemDeflection"],
        "_7504": ["MountableComponentCompoundAdvancedSystemDeflection"],
        "_7505": ["OilSealCompoundAdvancedSystemDeflection"],
        "_7506": ["PartCompoundAdvancedSystemDeflection"],
        "_7507": ["PartToPartShearCouplingCompoundAdvancedSystemDeflection"],
        "_7508": ["PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7509": ["PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7510": ["PlanetaryConnectionCompoundAdvancedSystemDeflection"],
        "_7511": ["PlanetaryGearSetCompoundAdvancedSystemDeflection"],
        "_7512": ["PlanetCarrierCompoundAdvancedSystemDeflection"],
        "_7513": ["PointLoadCompoundAdvancedSystemDeflection"],
        "_7514": ["PowerLoadCompoundAdvancedSystemDeflection"],
        "_7515": ["PulleyCompoundAdvancedSystemDeflection"],
        "_7516": ["RingPinsCompoundAdvancedSystemDeflection"],
        "_7517": ["RingPinsToDiscConnectionCompoundAdvancedSystemDeflection"],
        "_7518": ["RollingRingAssemblyCompoundAdvancedSystemDeflection"],
        "_7519": ["RollingRingCompoundAdvancedSystemDeflection"],
        "_7520": ["RollingRingConnectionCompoundAdvancedSystemDeflection"],
        "_7521": ["RootAssemblyCompoundAdvancedSystemDeflection"],
        "_7522": ["ShaftCompoundAdvancedSystemDeflection"],
        "_7523": ["ShaftHubConnectionCompoundAdvancedSystemDeflection"],
        "_7524": [
            "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7525": ["SpecialisedAssemblyCompoundAdvancedSystemDeflection"],
        "_7526": ["SpiralBevelGearCompoundAdvancedSystemDeflection"],
        "_7527": ["SpiralBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7528": ["SpiralBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7529": ["SpringDamperCompoundAdvancedSystemDeflection"],
        "_7530": ["SpringDamperConnectionCompoundAdvancedSystemDeflection"],
        "_7531": ["SpringDamperHalfCompoundAdvancedSystemDeflection"],
        "_7532": ["StraightBevelDiffGearCompoundAdvancedSystemDeflection"],
        "_7533": ["StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection"],
        "_7534": ["StraightBevelDiffGearSetCompoundAdvancedSystemDeflection"],
        "_7535": ["StraightBevelGearCompoundAdvancedSystemDeflection"],
        "_7536": ["StraightBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7537": ["StraightBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7538": ["StraightBevelPlanetGearCompoundAdvancedSystemDeflection"],
        "_7539": ["StraightBevelSunGearCompoundAdvancedSystemDeflection"],
        "_7540": ["SynchroniserCompoundAdvancedSystemDeflection"],
        "_7541": ["SynchroniserHalfCompoundAdvancedSystemDeflection"],
        "_7542": ["SynchroniserPartCompoundAdvancedSystemDeflection"],
        "_7543": ["SynchroniserSleeveCompoundAdvancedSystemDeflection"],
        "_7544": ["TorqueConverterCompoundAdvancedSystemDeflection"],
        "_7545": ["TorqueConverterConnectionCompoundAdvancedSystemDeflection"],
        "_7546": ["TorqueConverterPumpCompoundAdvancedSystemDeflection"],
        "_7547": ["TorqueConverterTurbineCompoundAdvancedSystemDeflection"],
        "_7548": ["UnbalancedMassCompoundAdvancedSystemDeflection"],
        "_7549": ["VirtualComponentCompoundAdvancedSystemDeflection"],
        "_7550": ["WormGearCompoundAdvancedSystemDeflection"],
        "_7551": ["WormGearMeshCompoundAdvancedSystemDeflection"],
        "_7552": ["WormGearSetCompoundAdvancedSystemDeflection"],
        "_7553": ["ZerolBevelGearCompoundAdvancedSystemDeflection"],
        "_7554": ["ZerolBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7555": ["ZerolBevelGearSetCompoundAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedSystemDeflection",
    "AbstractShaftCompoundAdvancedSystemDeflection",
    "AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
    "AssemblyCompoundAdvancedSystemDeflection",
    "BearingCompoundAdvancedSystemDeflection",
    "BeltConnectionCompoundAdvancedSystemDeflection",
    "BeltDriveCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
    "BevelGearCompoundAdvancedSystemDeflection",
    "BevelGearMeshCompoundAdvancedSystemDeflection",
    "BevelGearSetCompoundAdvancedSystemDeflection",
    "BoltCompoundAdvancedSystemDeflection",
    "BoltedJointCompoundAdvancedSystemDeflection",
    "ClutchCompoundAdvancedSystemDeflection",
    "ClutchConnectionCompoundAdvancedSystemDeflection",
    "ClutchHalfCompoundAdvancedSystemDeflection",
    "CoaxialConnectionCompoundAdvancedSystemDeflection",
    "ComponentCompoundAdvancedSystemDeflection",
    "ConceptCouplingCompoundAdvancedSystemDeflection",
    "ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
    "ConceptCouplingHalfCompoundAdvancedSystemDeflection",
    "ConceptGearCompoundAdvancedSystemDeflection",
    "ConceptGearMeshCompoundAdvancedSystemDeflection",
    "ConceptGearSetCompoundAdvancedSystemDeflection",
    "ConicalGearCompoundAdvancedSystemDeflection",
    "ConicalGearMeshCompoundAdvancedSystemDeflection",
    "ConicalGearSetCompoundAdvancedSystemDeflection",
    "ConnectionCompoundAdvancedSystemDeflection",
    "ConnectorCompoundAdvancedSystemDeflection",
    "CouplingCompoundAdvancedSystemDeflection",
    "CouplingConnectionCompoundAdvancedSystemDeflection",
    "CouplingHalfCompoundAdvancedSystemDeflection",
    "CVTBeltConnectionCompoundAdvancedSystemDeflection",
    "CVTCompoundAdvancedSystemDeflection",
    "CVTPulleyCompoundAdvancedSystemDeflection",
    "CycloidalAssemblyCompoundAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
    "CycloidalDiscCompoundAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
    "CylindricalGearCompoundAdvancedSystemDeflection",
    "CylindricalGearMeshCompoundAdvancedSystemDeflection",
    "CylindricalGearSetCompoundAdvancedSystemDeflection",
    "CylindricalPlanetGearCompoundAdvancedSystemDeflection",
    "DatumCompoundAdvancedSystemDeflection",
    "ExternalCADModelCompoundAdvancedSystemDeflection",
    "FaceGearCompoundAdvancedSystemDeflection",
    "FaceGearMeshCompoundAdvancedSystemDeflection",
    "FaceGearSetCompoundAdvancedSystemDeflection",
    "FEPartCompoundAdvancedSystemDeflection",
    "FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
    "GearCompoundAdvancedSystemDeflection",
    "GearMeshCompoundAdvancedSystemDeflection",
    "GearSetCompoundAdvancedSystemDeflection",
    "GuideDxfModelCompoundAdvancedSystemDeflection",
    "HypoidGearCompoundAdvancedSystemDeflection",
    "HypoidGearMeshCompoundAdvancedSystemDeflection",
    "HypoidGearSetCompoundAdvancedSystemDeflection",
    "InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "MassDiscCompoundAdvancedSystemDeflection",
    "MeasurementComponentCompoundAdvancedSystemDeflection",
    "MountableComponentCompoundAdvancedSystemDeflection",
    "OilSealCompoundAdvancedSystemDeflection",
    "PartCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection",
    "PlanetaryConnectionCompoundAdvancedSystemDeflection",
    "PlanetaryGearSetCompoundAdvancedSystemDeflection",
    "PlanetCarrierCompoundAdvancedSystemDeflection",
    "PointLoadCompoundAdvancedSystemDeflection",
    "PowerLoadCompoundAdvancedSystemDeflection",
    "PulleyCompoundAdvancedSystemDeflection",
    "RingPinsCompoundAdvancedSystemDeflection",
    "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
    "RollingRingAssemblyCompoundAdvancedSystemDeflection",
    "RollingRingCompoundAdvancedSystemDeflection",
    "RollingRingConnectionCompoundAdvancedSystemDeflection",
    "RootAssemblyCompoundAdvancedSystemDeflection",
    "ShaftCompoundAdvancedSystemDeflection",
    "ShaftHubConnectionCompoundAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
    "SpiralBevelGearCompoundAdvancedSystemDeflection",
    "SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "SpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "SpringDamperCompoundAdvancedSystemDeflection",
    "SpringDamperConnectionCompoundAdvancedSystemDeflection",
    "SpringDamperHalfCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelGearCompoundAdvancedSystemDeflection",
    "StraightBevelGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
    "StraightBevelSunGearCompoundAdvancedSystemDeflection",
    "SynchroniserCompoundAdvancedSystemDeflection",
    "SynchroniserHalfCompoundAdvancedSystemDeflection",
    "SynchroniserPartCompoundAdvancedSystemDeflection",
    "SynchroniserSleeveCompoundAdvancedSystemDeflection",
    "TorqueConverterCompoundAdvancedSystemDeflection",
    "TorqueConverterConnectionCompoundAdvancedSystemDeflection",
    "TorqueConverterPumpCompoundAdvancedSystemDeflection",
    "TorqueConverterTurbineCompoundAdvancedSystemDeflection",
    "UnbalancedMassCompoundAdvancedSystemDeflection",
    "VirtualComponentCompoundAdvancedSystemDeflection",
    "WormGearCompoundAdvancedSystemDeflection",
    "WormGearMeshCompoundAdvancedSystemDeflection",
    "WormGearSetCompoundAdvancedSystemDeflection",
    "ZerolBevelGearCompoundAdvancedSystemDeflection",
    "ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
    "ZerolBevelGearSetCompoundAdvancedSystemDeflection",
)
