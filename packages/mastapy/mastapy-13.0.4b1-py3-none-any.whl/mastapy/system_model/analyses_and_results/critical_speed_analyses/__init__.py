"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6564 import AbstractAssemblyCriticalSpeedAnalysis
    from ._6565 import AbstractShaftCriticalSpeedAnalysis
    from ._6566 import AbstractShaftOrHousingCriticalSpeedAnalysis
    from ._6567 import AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6568 import AGMAGleasonConicalGearCriticalSpeedAnalysis
    from ._6569 import AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
    from ._6570 import AGMAGleasonConicalGearSetCriticalSpeedAnalysis
    from ._6571 import AssemblyCriticalSpeedAnalysis
    from ._6572 import BearingCriticalSpeedAnalysis
    from ._6573 import BeltConnectionCriticalSpeedAnalysis
    from ._6574 import BeltDriveCriticalSpeedAnalysis
    from ._6575 import BevelDifferentialGearCriticalSpeedAnalysis
    from ._6576 import BevelDifferentialGearMeshCriticalSpeedAnalysis
    from ._6577 import BevelDifferentialGearSetCriticalSpeedAnalysis
    from ._6578 import BevelDifferentialPlanetGearCriticalSpeedAnalysis
    from ._6579 import BevelDifferentialSunGearCriticalSpeedAnalysis
    from ._6580 import BevelGearCriticalSpeedAnalysis
    from ._6581 import BevelGearMeshCriticalSpeedAnalysis
    from ._6582 import BevelGearSetCriticalSpeedAnalysis
    from ._6583 import BoltCriticalSpeedAnalysis
    from ._6584 import BoltedJointCriticalSpeedAnalysis
    from ._6585 import ClutchConnectionCriticalSpeedAnalysis
    from ._6586 import ClutchCriticalSpeedAnalysis
    from ._6587 import ClutchHalfCriticalSpeedAnalysis
    from ._6588 import CoaxialConnectionCriticalSpeedAnalysis
    from ._6589 import ComponentCriticalSpeedAnalysis
    from ._6590 import ConceptCouplingConnectionCriticalSpeedAnalysis
    from ._6591 import ConceptCouplingCriticalSpeedAnalysis
    from ._6592 import ConceptCouplingHalfCriticalSpeedAnalysis
    from ._6593 import ConceptGearCriticalSpeedAnalysis
    from ._6594 import ConceptGearMeshCriticalSpeedAnalysis
    from ._6595 import ConceptGearSetCriticalSpeedAnalysis
    from ._6596 import ConicalGearCriticalSpeedAnalysis
    from ._6597 import ConicalGearMeshCriticalSpeedAnalysis
    from ._6598 import ConicalGearSetCriticalSpeedAnalysis
    from ._6599 import ConnectionCriticalSpeedAnalysis
    from ._6600 import ConnectorCriticalSpeedAnalysis
    from ._6601 import CouplingConnectionCriticalSpeedAnalysis
    from ._6602 import CouplingCriticalSpeedAnalysis
    from ._6603 import CouplingHalfCriticalSpeedAnalysis
    from ._6604 import CriticalSpeedAnalysis
    from ._6605 import CriticalSpeedAnalysisDrawStyle
    from ._6606 import CriticalSpeedAnalysisOptions
    from ._6607 import CVTBeltConnectionCriticalSpeedAnalysis
    from ._6608 import CVTCriticalSpeedAnalysis
    from ._6609 import CVTPulleyCriticalSpeedAnalysis
    from ._6610 import CycloidalAssemblyCriticalSpeedAnalysis
    from ._6611 import CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
    from ._6612 import CycloidalDiscCriticalSpeedAnalysis
    from ._6613 import CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
    from ._6614 import CylindricalGearCriticalSpeedAnalysis
    from ._6615 import CylindricalGearMeshCriticalSpeedAnalysis
    from ._6616 import CylindricalGearSetCriticalSpeedAnalysis
    from ._6617 import CylindricalPlanetGearCriticalSpeedAnalysis
    from ._6618 import DatumCriticalSpeedAnalysis
    from ._6619 import ExternalCADModelCriticalSpeedAnalysis
    from ._6620 import FaceGearCriticalSpeedAnalysis
    from ._6621 import FaceGearMeshCriticalSpeedAnalysis
    from ._6622 import FaceGearSetCriticalSpeedAnalysis
    from ._6623 import FEPartCriticalSpeedAnalysis
    from ._6624 import FlexiblePinAssemblyCriticalSpeedAnalysis
    from ._6625 import GearCriticalSpeedAnalysis
    from ._6626 import GearMeshCriticalSpeedAnalysis
    from ._6627 import GearSetCriticalSpeedAnalysis
    from ._6628 import GuideDxfModelCriticalSpeedAnalysis
    from ._6629 import HypoidGearCriticalSpeedAnalysis
    from ._6630 import HypoidGearMeshCriticalSpeedAnalysis
    from ._6631 import HypoidGearSetCriticalSpeedAnalysis
    from ._6632 import InterMountableComponentConnectionCriticalSpeedAnalysis
    from ._6633 import KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
    from ._6634 import KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
    from ._6635 import KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
    from ._6636 import KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
    from ._6637 import KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
    from ._6638 import KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
    from ._6639 import KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
    from ._6640 import KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6641 import KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
    from ._6642 import MassDiscCriticalSpeedAnalysis
    from ._6643 import MeasurementComponentCriticalSpeedAnalysis
    from ._6644 import MountableComponentCriticalSpeedAnalysis
    from ._6645 import OilSealCriticalSpeedAnalysis
    from ._6646 import PartCriticalSpeedAnalysis
    from ._6647 import PartToPartShearCouplingConnectionCriticalSpeedAnalysis
    from ._6648 import PartToPartShearCouplingCriticalSpeedAnalysis
    from ._6649 import PartToPartShearCouplingHalfCriticalSpeedAnalysis
    from ._6650 import PlanetaryConnectionCriticalSpeedAnalysis
    from ._6651 import PlanetaryGearSetCriticalSpeedAnalysis
    from ._6652 import PlanetCarrierCriticalSpeedAnalysis
    from ._6653 import PointLoadCriticalSpeedAnalysis
    from ._6654 import PowerLoadCriticalSpeedAnalysis
    from ._6655 import PulleyCriticalSpeedAnalysis
    from ._6656 import RingPinsCriticalSpeedAnalysis
    from ._6657 import RingPinsToDiscConnectionCriticalSpeedAnalysis
    from ._6658 import RollingRingAssemblyCriticalSpeedAnalysis
    from ._6659 import RollingRingConnectionCriticalSpeedAnalysis
    from ._6660 import RollingRingCriticalSpeedAnalysis
    from ._6661 import RootAssemblyCriticalSpeedAnalysis
    from ._6662 import ShaftCriticalSpeedAnalysis
    from ._6663 import ShaftHubConnectionCriticalSpeedAnalysis
    from ._6664 import ShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6665 import SpecialisedAssemblyCriticalSpeedAnalysis
    from ._6666 import SpiralBevelGearCriticalSpeedAnalysis
    from ._6667 import SpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6668 import SpiralBevelGearSetCriticalSpeedAnalysis
    from ._6669 import SpringDamperConnectionCriticalSpeedAnalysis
    from ._6670 import SpringDamperCriticalSpeedAnalysis
    from ._6671 import SpringDamperHalfCriticalSpeedAnalysis
    from ._6672 import StraightBevelDiffGearCriticalSpeedAnalysis
    from ._6673 import StraightBevelDiffGearMeshCriticalSpeedAnalysis
    from ._6674 import StraightBevelDiffGearSetCriticalSpeedAnalysis
    from ._6675 import StraightBevelGearCriticalSpeedAnalysis
    from ._6676 import StraightBevelGearMeshCriticalSpeedAnalysis
    from ._6677 import StraightBevelGearSetCriticalSpeedAnalysis
    from ._6678 import StraightBevelPlanetGearCriticalSpeedAnalysis
    from ._6679 import StraightBevelSunGearCriticalSpeedAnalysis
    from ._6680 import SynchroniserCriticalSpeedAnalysis
    from ._6681 import SynchroniserHalfCriticalSpeedAnalysis
    from ._6682 import SynchroniserPartCriticalSpeedAnalysis
    from ._6683 import SynchroniserSleeveCriticalSpeedAnalysis
    from ._6684 import TorqueConverterConnectionCriticalSpeedAnalysis
    from ._6685 import TorqueConverterCriticalSpeedAnalysis
    from ._6686 import TorqueConverterPumpCriticalSpeedAnalysis
    from ._6687 import TorqueConverterTurbineCriticalSpeedAnalysis
    from ._6688 import UnbalancedMassCriticalSpeedAnalysis
    from ._6689 import VirtualComponentCriticalSpeedAnalysis
    from ._6690 import WormGearCriticalSpeedAnalysis
    from ._6691 import WormGearMeshCriticalSpeedAnalysis
    from ._6692 import WormGearSetCriticalSpeedAnalysis
    from ._6693 import ZerolBevelGearCriticalSpeedAnalysis
    from ._6694 import ZerolBevelGearMeshCriticalSpeedAnalysis
    from ._6695 import ZerolBevelGearSetCriticalSpeedAnalysis
else:
    import_structure = {
        "_6564": ["AbstractAssemblyCriticalSpeedAnalysis"],
        "_6565": ["AbstractShaftCriticalSpeedAnalysis"],
        "_6566": ["AbstractShaftOrHousingCriticalSpeedAnalysis"],
        "_6567": ["AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6568": ["AGMAGleasonConicalGearCriticalSpeedAnalysis"],
        "_6569": ["AGMAGleasonConicalGearMeshCriticalSpeedAnalysis"],
        "_6570": ["AGMAGleasonConicalGearSetCriticalSpeedAnalysis"],
        "_6571": ["AssemblyCriticalSpeedAnalysis"],
        "_6572": ["BearingCriticalSpeedAnalysis"],
        "_6573": ["BeltConnectionCriticalSpeedAnalysis"],
        "_6574": ["BeltDriveCriticalSpeedAnalysis"],
        "_6575": ["BevelDifferentialGearCriticalSpeedAnalysis"],
        "_6576": ["BevelDifferentialGearMeshCriticalSpeedAnalysis"],
        "_6577": ["BevelDifferentialGearSetCriticalSpeedAnalysis"],
        "_6578": ["BevelDifferentialPlanetGearCriticalSpeedAnalysis"],
        "_6579": ["BevelDifferentialSunGearCriticalSpeedAnalysis"],
        "_6580": ["BevelGearCriticalSpeedAnalysis"],
        "_6581": ["BevelGearMeshCriticalSpeedAnalysis"],
        "_6582": ["BevelGearSetCriticalSpeedAnalysis"],
        "_6583": ["BoltCriticalSpeedAnalysis"],
        "_6584": ["BoltedJointCriticalSpeedAnalysis"],
        "_6585": ["ClutchConnectionCriticalSpeedAnalysis"],
        "_6586": ["ClutchCriticalSpeedAnalysis"],
        "_6587": ["ClutchHalfCriticalSpeedAnalysis"],
        "_6588": ["CoaxialConnectionCriticalSpeedAnalysis"],
        "_6589": ["ComponentCriticalSpeedAnalysis"],
        "_6590": ["ConceptCouplingConnectionCriticalSpeedAnalysis"],
        "_6591": ["ConceptCouplingCriticalSpeedAnalysis"],
        "_6592": ["ConceptCouplingHalfCriticalSpeedAnalysis"],
        "_6593": ["ConceptGearCriticalSpeedAnalysis"],
        "_6594": ["ConceptGearMeshCriticalSpeedAnalysis"],
        "_6595": ["ConceptGearSetCriticalSpeedAnalysis"],
        "_6596": ["ConicalGearCriticalSpeedAnalysis"],
        "_6597": ["ConicalGearMeshCriticalSpeedAnalysis"],
        "_6598": ["ConicalGearSetCriticalSpeedAnalysis"],
        "_6599": ["ConnectionCriticalSpeedAnalysis"],
        "_6600": ["ConnectorCriticalSpeedAnalysis"],
        "_6601": ["CouplingConnectionCriticalSpeedAnalysis"],
        "_6602": ["CouplingCriticalSpeedAnalysis"],
        "_6603": ["CouplingHalfCriticalSpeedAnalysis"],
        "_6604": ["CriticalSpeedAnalysis"],
        "_6605": ["CriticalSpeedAnalysisDrawStyle"],
        "_6606": ["CriticalSpeedAnalysisOptions"],
        "_6607": ["CVTBeltConnectionCriticalSpeedAnalysis"],
        "_6608": ["CVTCriticalSpeedAnalysis"],
        "_6609": ["CVTPulleyCriticalSpeedAnalysis"],
        "_6610": ["CycloidalAssemblyCriticalSpeedAnalysis"],
        "_6611": ["CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis"],
        "_6612": ["CycloidalDiscCriticalSpeedAnalysis"],
        "_6613": ["CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis"],
        "_6614": ["CylindricalGearCriticalSpeedAnalysis"],
        "_6615": ["CylindricalGearMeshCriticalSpeedAnalysis"],
        "_6616": ["CylindricalGearSetCriticalSpeedAnalysis"],
        "_6617": ["CylindricalPlanetGearCriticalSpeedAnalysis"],
        "_6618": ["DatumCriticalSpeedAnalysis"],
        "_6619": ["ExternalCADModelCriticalSpeedAnalysis"],
        "_6620": ["FaceGearCriticalSpeedAnalysis"],
        "_6621": ["FaceGearMeshCriticalSpeedAnalysis"],
        "_6622": ["FaceGearSetCriticalSpeedAnalysis"],
        "_6623": ["FEPartCriticalSpeedAnalysis"],
        "_6624": ["FlexiblePinAssemblyCriticalSpeedAnalysis"],
        "_6625": ["GearCriticalSpeedAnalysis"],
        "_6626": ["GearMeshCriticalSpeedAnalysis"],
        "_6627": ["GearSetCriticalSpeedAnalysis"],
        "_6628": ["GuideDxfModelCriticalSpeedAnalysis"],
        "_6629": ["HypoidGearCriticalSpeedAnalysis"],
        "_6630": ["HypoidGearMeshCriticalSpeedAnalysis"],
        "_6631": ["HypoidGearSetCriticalSpeedAnalysis"],
        "_6632": ["InterMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6633": ["KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis"],
        "_6634": ["KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis"],
        "_6635": ["KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"],
        "_6636": ["KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis"],
        "_6637": ["KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis"],
        "_6638": ["KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis"],
        "_6639": ["KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis"],
        "_6640": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6641": ["KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6642": ["MassDiscCriticalSpeedAnalysis"],
        "_6643": ["MeasurementComponentCriticalSpeedAnalysis"],
        "_6644": ["MountableComponentCriticalSpeedAnalysis"],
        "_6645": ["OilSealCriticalSpeedAnalysis"],
        "_6646": ["PartCriticalSpeedAnalysis"],
        "_6647": ["PartToPartShearCouplingConnectionCriticalSpeedAnalysis"],
        "_6648": ["PartToPartShearCouplingCriticalSpeedAnalysis"],
        "_6649": ["PartToPartShearCouplingHalfCriticalSpeedAnalysis"],
        "_6650": ["PlanetaryConnectionCriticalSpeedAnalysis"],
        "_6651": ["PlanetaryGearSetCriticalSpeedAnalysis"],
        "_6652": ["PlanetCarrierCriticalSpeedAnalysis"],
        "_6653": ["PointLoadCriticalSpeedAnalysis"],
        "_6654": ["PowerLoadCriticalSpeedAnalysis"],
        "_6655": ["PulleyCriticalSpeedAnalysis"],
        "_6656": ["RingPinsCriticalSpeedAnalysis"],
        "_6657": ["RingPinsToDiscConnectionCriticalSpeedAnalysis"],
        "_6658": ["RollingRingAssemblyCriticalSpeedAnalysis"],
        "_6659": ["RollingRingConnectionCriticalSpeedAnalysis"],
        "_6660": ["RollingRingCriticalSpeedAnalysis"],
        "_6661": ["RootAssemblyCriticalSpeedAnalysis"],
        "_6662": ["ShaftCriticalSpeedAnalysis"],
        "_6663": ["ShaftHubConnectionCriticalSpeedAnalysis"],
        "_6664": ["ShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6665": ["SpecialisedAssemblyCriticalSpeedAnalysis"],
        "_6666": ["SpiralBevelGearCriticalSpeedAnalysis"],
        "_6667": ["SpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6668": ["SpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6669": ["SpringDamperConnectionCriticalSpeedAnalysis"],
        "_6670": ["SpringDamperCriticalSpeedAnalysis"],
        "_6671": ["SpringDamperHalfCriticalSpeedAnalysis"],
        "_6672": ["StraightBevelDiffGearCriticalSpeedAnalysis"],
        "_6673": ["StraightBevelDiffGearMeshCriticalSpeedAnalysis"],
        "_6674": ["StraightBevelDiffGearSetCriticalSpeedAnalysis"],
        "_6675": ["StraightBevelGearCriticalSpeedAnalysis"],
        "_6676": ["StraightBevelGearMeshCriticalSpeedAnalysis"],
        "_6677": ["StraightBevelGearSetCriticalSpeedAnalysis"],
        "_6678": ["StraightBevelPlanetGearCriticalSpeedAnalysis"],
        "_6679": ["StraightBevelSunGearCriticalSpeedAnalysis"],
        "_6680": ["SynchroniserCriticalSpeedAnalysis"],
        "_6681": ["SynchroniserHalfCriticalSpeedAnalysis"],
        "_6682": ["SynchroniserPartCriticalSpeedAnalysis"],
        "_6683": ["SynchroniserSleeveCriticalSpeedAnalysis"],
        "_6684": ["TorqueConverterConnectionCriticalSpeedAnalysis"],
        "_6685": ["TorqueConverterCriticalSpeedAnalysis"],
        "_6686": ["TorqueConverterPumpCriticalSpeedAnalysis"],
        "_6687": ["TorqueConverterTurbineCriticalSpeedAnalysis"],
        "_6688": ["UnbalancedMassCriticalSpeedAnalysis"],
        "_6689": ["VirtualComponentCriticalSpeedAnalysis"],
        "_6690": ["WormGearCriticalSpeedAnalysis"],
        "_6691": ["WormGearMeshCriticalSpeedAnalysis"],
        "_6692": ["WormGearSetCriticalSpeedAnalysis"],
        "_6693": ["ZerolBevelGearCriticalSpeedAnalysis"],
        "_6694": ["ZerolBevelGearMeshCriticalSpeedAnalysis"],
        "_6695": ["ZerolBevelGearSetCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCriticalSpeedAnalysis",
    "AbstractShaftCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
    "AssemblyCriticalSpeedAnalysis",
    "BearingCriticalSpeedAnalysis",
    "BeltConnectionCriticalSpeedAnalysis",
    "BeltDriveCriticalSpeedAnalysis",
    "BevelDifferentialGearCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCriticalSpeedAnalysis",
    "BevelGearCriticalSpeedAnalysis",
    "BevelGearMeshCriticalSpeedAnalysis",
    "BevelGearSetCriticalSpeedAnalysis",
    "BoltCriticalSpeedAnalysis",
    "BoltedJointCriticalSpeedAnalysis",
    "ClutchConnectionCriticalSpeedAnalysis",
    "ClutchCriticalSpeedAnalysis",
    "ClutchHalfCriticalSpeedAnalysis",
    "CoaxialConnectionCriticalSpeedAnalysis",
    "ComponentCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCriticalSpeedAnalysis",
    "ConceptCouplingCriticalSpeedAnalysis",
    "ConceptCouplingHalfCriticalSpeedAnalysis",
    "ConceptGearCriticalSpeedAnalysis",
    "ConceptGearMeshCriticalSpeedAnalysis",
    "ConceptGearSetCriticalSpeedAnalysis",
    "ConicalGearCriticalSpeedAnalysis",
    "ConicalGearMeshCriticalSpeedAnalysis",
    "ConicalGearSetCriticalSpeedAnalysis",
    "ConnectionCriticalSpeedAnalysis",
    "ConnectorCriticalSpeedAnalysis",
    "CouplingConnectionCriticalSpeedAnalysis",
    "CouplingCriticalSpeedAnalysis",
    "CouplingHalfCriticalSpeedAnalysis",
    "CriticalSpeedAnalysis",
    "CriticalSpeedAnalysisDrawStyle",
    "CriticalSpeedAnalysisOptions",
    "CVTBeltConnectionCriticalSpeedAnalysis",
    "CVTCriticalSpeedAnalysis",
    "CVTPulleyCriticalSpeedAnalysis",
    "CycloidalAssemblyCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
    "CycloidalDiscCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
    "CylindricalGearCriticalSpeedAnalysis",
    "CylindricalGearMeshCriticalSpeedAnalysis",
    "CylindricalGearSetCriticalSpeedAnalysis",
    "CylindricalPlanetGearCriticalSpeedAnalysis",
    "DatumCriticalSpeedAnalysis",
    "ExternalCADModelCriticalSpeedAnalysis",
    "FaceGearCriticalSpeedAnalysis",
    "FaceGearMeshCriticalSpeedAnalysis",
    "FaceGearSetCriticalSpeedAnalysis",
    "FEPartCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCriticalSpeedAnalysis",
    "GearCriticalSpeedAnalysis",
    "GearMeshCriticalSpeedAnalysis",
    "GearSetCriticalSpeedAnalysis",
    "GuideDxfModelCriticalSpeedAnalysis",
    "HypoidGearCriticalSpeedAnalysis",
    "HypoidGearMeshCriticalSpeedAnalysis",
    "HypoidGearSetCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
    "MassDiscCriticalSpeedAnalysis",
    "MeasurementComponentCriticalSpeedAnalysis",
    "MountableComponentCriticalSpeedAnalysis",
    "OilSealCriticalSpeedAnalysis",
    "PartCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCriticalSpeedAnalysis",
    "PartToPartShearCouplingCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCriticalSpeedAnalysis",
    "PlanetaryConnectionCriticalSpeedAnalysis",
    "PlanetaryGearSetCriticalSpeedAnalysis",
    "PlanetCarrierCriticalSpeedAnalysis",
    "PointLoadCriticalSpeedAnalysis",
    "PowerLoadCriticalSpeedAnalysis",
    "PulleyCriticalSpeedAnalysis",
    "RingPinsCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCriticalSpeedAnalysis",
    "RollingRingAssemblyCriticalSpeedAnalysis",
    "RollingRingConnectionCriticalSpeedAnalysis",
    "RollingRingCriticalSpeedAnalysis",
    "RootAssemblyCriticalSpeedAnalysis",
    "ShaftCriticalSpeedAnalysis",
    "ShaftHubConnectionCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "SpecialisedAssemblyCriticalSpeedAnalysis",
    "SpiralBevelGearCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCriticalSpeedAnalysis",
    "SpiralBevelGearSetCriticalSpeedAnalysis",
    "SpringDamperConnectionCriticalSpeedAnalysis",
    "SpringDamperCriticalSpeedAnalysis",
    "SpringDamperHalfCriticalSpeedAnalysis",
    "StraightBevelDiffGearCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCriticalSpeedAnalysis",
    "StraightBevelGearCriticalSpeedAnalysis",
    "StraightBevelGearMeshCriticalSpeedAnalysis",
    "StraightBevelGearSetCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCriticalSpeedAnalysis",
    "StraightBevelSunGearCriticalSpeedAnalysis",
    "SynchroniserCriticalSpeedAnalysis",
    "SynchroniserHalfCriticalSpeedAnalysis",
    "SynchroniserPartCriticalSpeedAnalysis",
    "SynchroniserSleeveCriticalSpeedAnalysis",
    "TorqueConverterConnectionCriticalSpeedAnalysis",
    "TorqueConverterCriticalSpeedAnalysis",
    "TorqueConverterPumpCriticalSpeedAnalysis",
    "TorqueConverterTurbineCriticalSpeedAnalysis",
    "UnbalancedMassCriticalSpeedAnalysis",
    "VirtualComponentCriticalSpeedAnalysis",
    "WormGearCriticalSpeedAnalysis",
    "WormGearMeshCriticalSpeedAnalysis",
    "WormGearSetCriticalSpeedAnalysis",
    "ZerolBevelGearCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCriticalSpeedAnalysis",
    "ZerolBevelGearSetCriticalSpeedAnalysis",
)
