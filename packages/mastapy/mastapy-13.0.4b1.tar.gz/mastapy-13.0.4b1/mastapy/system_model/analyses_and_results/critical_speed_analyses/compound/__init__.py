"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6696 import AbstractAssemblyCompoundCriticalSpeedAnalysis
    from ._6697 import AbstractShaftCompoundCriticalSpeedAnalysis
    from ._6698 import AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
    from ._6699 import (
        AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6700 import AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
    from ._6701 import AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6702 import AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6703 import AssemblyCompoundCriticalSpeedAnalysis
    from ._6704 import BearingCompoundCriticalSpeedAnalysis
    from ._6705 import BeltConnectionCompoundCriticalSpeedAnalysis
    from ._6706 import BeltDriveCompoundCriticalSpeedAnalysis
    from ._6707 import BevelDifferentialGearCompoundCriticalSpeedAnalysis
    from ._6708 import BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
    from ._6709 import BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
    from ._6710 import BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
    from ._6711 import BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
    from ._6712 import BevelGearCompoundCriticalSpeedAnalysis
    from ._6713 import BevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6714 import BevelGearSetCompoundCriticalSpeedAnalysis
    from ._6715 import BoltCompoundCriticalSpeedAnalysis
    from ._6716 import BoltedJointCompoundCriticalSpeedAnalysis
    from ._6717 import ClutchCompoundCriticalSpeedAnalysis
    from ._6718 import ClutchConnectionCompoundCriticalSpeedAnalysis
    from ._6719 import ClutchHalfCompoundCriticalSpeedAnalysis
    from ._6720 import CoaxialConnectionCompoundCriticalSpeedAnalysis
    from ._6721 import ComponentCompoundCriticalSpeedAnalysis
    from ._6722 import ConceptCouplingCompoundCriticalSpeedAnalysis
    from ._6723 import ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6724 import ConceptCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6725 import ConceptGearCompoundCriticalSpeedAnalysis
    from ._6726 import ConceptGearMeshCompoundCriticalSpeedAnalysis
    from ._6727 import ConceptGearSetCompoundCriticalSpeedAnalysis
    from ._6728 import ConicalGearCompoundCriticalSpeedAnalysis
    from ._6729 import ConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6730 import ConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6731 import ConnectionCompoundCriticalSpeedAnalysis
    from ._6732 import ConnectorCompoundCriticalSpeedAnalysis
    from ._6733 import CouplingCompoundCriticalSpeedAnalysis
    from ._6734 import CouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6735 import CouplingHalfCompoundCriticalSpeedAnalysis
    from ._6736 import CVTBeltConnectionCompoundCriticalSpeedAnalysis
    from ._6737 import CVTCompoundCriticalSpeedAnalysis
    from ._6738 import CVTPulleyCompoundCriticalSpeedAnalysis
    from ._6739 import CycloidalAssemblyCompoundCriticalSpeedAnalysis
    from ._6740 import (
        CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6741 import CycloidalDiscCompoundCriticalSpeedAnalysis
    from ._6742 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6743 import CylindricalGearCompoundCriticalSpeedAnalysis
    from ._6744 import CylindricalGearMeshCompoundCriticalSpeedAnalysis
    from ._6745 import CylindricalGearSetCompoundCriticalSpeedAnalysis
    from ._6746 import CylindricalPlanetGearCompoundCriticalSpeedAnalysis
    from ._6747 import DatumCompoundCriticalSpeedAnalysis
    from ._6748 import ExternalCADModelCompoundCriticalSpeedAnalysis
    from ._6749 import FaceGearCompoundCriticalSpeedAnalysis
    from ._6750 import FaceGearMeshCompoundCriticalSpeedAnalysis
    from ._6751 import FaceGearSetCompoundCriticalSpeedAnalysis
    from ._6752 import FEPartCompoundCriticalSpeedAnalysis
    from ._6753 import FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
    from ._6754 import GearCompoundCriticalSpeedAnalysis
    from ._6755 import GearMeshCompoundCriticalSpeedAnalysis
    from ._6756 import GearSetCompoundCriticalSpeedAnalysis
    from ._6757 import GuideDxfModelCompoundCriticalSpeedAnalysis
    from ._6758 import HypoidGearCompoundCriticalSpeedAnalysis
    from ._6759 import HypoidGearMeshCompoundCriticalSpeedAnalysis
    from ._6760 import HypoidGearSetCompoundCriticalSpeedAnalysis
    from ._6761 import InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6762 import KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
    from ._6763 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6764 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6765 import KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
    from ._6766 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6767 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6768 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis,
    )
    from ._6769 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6770 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6771 import MassDiscCompoundCriticalSpeedAnalysis
    from ._6772 import MeasurementComponentCompoundCriticalSpeedAnalysis
    from ._6773 import MountableComponentCompoundCriticalSpeedAnalysis
    from ._6774 import OilSealCompoundCriticalSpeedAnalysis
    from ._6775 import PartCompoundCriticalSpeedAnalysis
    from ._6776 import PartToPartShearCouplingCompoundCriticalSpeedAnalysis
    from ._6777 import PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6778 import PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6779 import PlanetaryConnectionCompoundCriticalSpeedAnalysis
    from ._6780 import PlanetaryGearSetCompoundCriticalSpeedAnalysis
    from ._6781 import PlanetCarrierCompoundCriticalSpeedAnalysis
    from ._6782 import PointLoadCompoundCriticalSpeedAnalysis
    from ._6783 import PowerLoadCompoundCriticalSpeedAnalysis
    from ._6784 import PulleyCompoundCriticalSpeedAnalysis
    from ._6785 import RingPinsCompoundCriticalSpeedAnalysis
    from ._6786 import RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
    from ._6787 import RollingRingAssemblyCompoundCriticalSpeedAnalysis
    from ._6788 import RollingRingCompoundCriticalSpeedAnalysis
    from ._6789 import RollingRingConnectionCompoundCriticalSpeedAnalysis
    from ._6790 import RootAssemblyCompoundCriticalSpeedAnalysis
    from ._6791 import ShaftCompoundCriticalSpeedAnalysis
    from ._6792 import ShaftHubConnectionCompoundCriticalSpeedAnalysis
    from ._6793 import ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6794 import SpecialisedAssemblyCompoundCriticalSpeedAnalysis
    from ._6795 import SpiralBevelGearCompoundCriticalSpeedAnalysis
    from ._6796 import SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6797 import SpiralBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6798 import SpringDamperCompoundCriticalSpeedAnalysis
    from ._6799 import SpringDamperConnectionCompoundCriticalSpeedAnalysis
    from ._6800 import SpringDamperHalfCompoundCriticalSpeedAnalysis
    from ._6801 import StraightBevelDiffGearCompoundCriticalSpeedAnalysis
    from ._6802 import StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
    from ._6803 import StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
    from ._6804 import StraightBevelGearCompoundCriticalSpeedAnalysis
    from ._6805 import StraightBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6806 import StraightBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6807 import StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
    from ._6808 import StraightBevelSunGearCompoundCriticalSpeedAnalysis
    from ._6809 import SynchroniserCompoundCriticalSpeedAnalysis
    from ._6810 import SynchroniserHalfCompoundCriticalSpeedAnalysis
    from ._6811 import SynchroniserPartCompoundCriticalSpeedAnalysis
    from ._6812 import SynchroniserSleeveCompoundCriticalSpeedAnalysis
    from ._6813 import TorqueConverterCompoundCriticalSpeedAnalysis
    from ._6814 import TorqueConverterConnectionCompoundCriticalSpeedAnalysis
    from ._6815 import TorqueConverterPumpCompoundCriticalSpeedAnalysis
    from ._6816 import TorqueConverterTurbineCompoundCriticalSpeedAnalysis
    from ._6817 import UnbalancedMassCompoundCriticalSpeedAnalysis
    from ._6818 import VirtualComponentCompoundCriticalSpeedAnalysis
    from ._6819 import WormGearCompoundCriticalSpeedAnalysis
    from ._6820 import WormGearMeshCompoundCriticalSpeedAnalysis
    from ._6821 import WormGearSetCompoundCriticalSpeedAnalysis
    from ._6822 import ZerolBevelGearCompoundCriticalSpeedAnalysis
    from ._6823 import ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6824 import ZerolBevelGearSetCompoundCriticalSpeedAnalysis
else:
    import_structure = {
        "_6696": ["AbstractAssemblyCompoundCriticalSpeedAnalysis"],
        "_6697": ["AbstractShaftCompoundCriticalSpeedAnalysis"],
        "_6698": ["AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"],
        "_6699": [
            "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6700": ["AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis"],
        "_6701": ["AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6702": ["AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6703": ["AssemblyCompoundCriticalSpeedAnalysis"],
        "_6704": ["BearingCompoundCriticalSpeedAnalysis"],
        "_6705": ["BeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6706": ["BeltDriveCompoundCriticalSpeedAnalysis"],
        "_6707": ["BevelDifferentialGearCompoundCriticalSpeedAnalysis"],
        "_6708": ["BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis"],
        "_6709": ["BevelDifferentialGearSetCompoundCriticalSpeedAnalysis"],
        "_6710": ["BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6711": ["BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"],
        "_6712": ["BevelGearCompoundCriticalSpeedAnalysis"],
        "_6713": ["BevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6714": ["BevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6715": ["BoltCompoundCriticalSpeedAnalysis"],
        "_6716": ["BoltedJointCompoundCriticalSpeedAnalysis"],
        "_6717": ["ClutchCompoundCriticalSpeedAnalysis"],
        "_6718": ["ClutchConnectionCompoundCriticalSpeedAnalysis"],
        "_6719": ["ClutchHalfCompoundCriticalSpeedAnalysis"],
        "_6720": ["CoaxialConnectionCompoundCriticalSpeedAnalysis"],
        "_6721": ["ComponentCompoundCriticalSpeedAnalysis"],
        "_6722": ["ConceptCouplingCompoundCriticalSpeedAnalysis"],
        "_6723": ["ConceptCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6724": ["ConceptCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6725": ["ConceptGearCompoundCriticalSpeedAnalysis"],
        "_6726": ["ConceptGearMeshCompoundCriticalSpeedAnalysis"],
        "_6727": ["ConceptGearSetCompoundCriticalSpeedAnalysis"],
        "_6728": ["ConicalGearCompoundCriticalSpeedAnalysis"],
        "_6729": ["ConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6730": ["ConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6731": ["ConnectionCompoundCriticalSpeedAnalysis"],
        "_6732": ["ConnectorCompoundCriticalSpeedAnalysis"],
        "_6733": ["CouplingCompoundCriticalSpeedAnalysis"],
        "_6734": ["CouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6735": ["CouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6736": ["CVTBeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6737": ["CVTCompoundCriticalSpeedAnalysis"],
        "_6738": ["CVTPulleyCompoundCriticalSpeedAnalysis"],
        "_6739": ["CycloidalAssemblyCompoundCriticalSpeedAnalysis"],
        "_6740": ["CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis"],
        "_6741": ["CycloidalDiscCompoundCriticalSpeedAnalysis"],
        "_6742": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6743": ["CylindricalGearCompoundCriticalSpeedAnalysis"],
        "_6744": ["CylindricalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6745": ["CylindricalGearSetCompoundCriticalSpeedAnalysis"],
        "_6746": ["CylindricalPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6747": ["DatumCompoundCriticalSpeedAnalysis"],
        "_6748": ["ExternalCADModelCompoundCriticalSpeedAnalysis"],
        "_6749": ["FaceGearCompoundCriticalSpeedAnalysis"],
        "_6750": ["FaceGearMeshCompoundCriticalSpeedAnalysis"],
        "_6751": ["FaceGearSetCompoundCriticalSpeedAnalysis"],
        "_6752": ["FEPartCompoundCriticalSpeedAnalysis"],
        "_6753": ["FlexiblePinAssemblyCompoundCriticalSpeedAnalysis"],
        "_6754": ["GearCompoundCriticalSpeedAnalysis"],
        "_6755": ["GearMeshCompoundCriticalSpeedAnalysis"],
        "_6756": ["GearSetCompoundCriticalSpeedAnalysis"],
        "_6757": ["GuideDxfModelCompoundCriticalSpeedAnalysis"],
        "_6758": ["HypoidGearCompoundCriticalSpeedAnalysis"],
        "_6759": ["HypoidGearMeshCompoundCriticalSpeedAnalysis"],
        "_6760": ["HypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6761": ["InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6762": ["KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis"],
        "_6763": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6764": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6765": ["KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis"],
        "_6766": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6767": ["KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6768": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ],
        "_6769": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6770": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6771": ["MassDiscCompoundCriticalSpeedAnalysis"],
        "_6772": ["MeasurementComponentCompoundCriticalSpeedAnalysis"],
        "_6773": ["MountableComponentCompoundCriticalSpeedAnalysis"],
        "_6774": ["OilSealCompoundCriticalSpeedAnalysis"],
        "_6775": ["PartCompoundCriticalSpeedAnalysis"],
        "_6776": ["PartToPartShearCouplingCompoundCriticalSpeedAnalysis"],
        "_6777": ["PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6778": ["PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6779": ["PlanetaryConnectionCompoundCriticalSpeedAnalysis"],
        "_6780": ["PlanetaryGearSetCompoundCriticalSpeedAnalysis"],
        "_6781": ["PlanetCarrierCompoundCriticalSpeedAnalysis"],
        "_6782": ["PointLoadCompoundCriticalSpeedAnalysis"],
        "_6783": ["PowerLoadCompoundCriticalSpeedAnalysis"],
        "_6784": ["PulleyCompoundCriticalSpeedAnalysis"],
        "_6785": ["RingPinsCompoundCriticalSpeedAnalysis"],
        "_6786": ["RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis"],
        "_6787": ["RollingRingAssemblyCompoundCriticalSpeedAnalysis"],
        "_6788": ["RollingRingCompoundCriticalSpeedAnalysis"],
        "_6789": ["RollingRingConnectionCompoundCriticalSpeedAnalysis"],
        "_6790": ["RootAssemblyCompoundCriticalSpeedAnalysis"],
        "_6791": ["ShaftCompoundCriticalSpeedAnalysis"],
        "_6792": ["ShaftHubConnectionCompoundCriticalSpeedAnalysis"],
        "_6793": ["ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6794": ["SpecialisedAssemblyCompoundCriticalSpeedAnalysis"],
        "_6795": ["SpiralBevelGearCompoundCriticalSpeedAnalysis"],
        "_6796": ["SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6797": ["SpiralBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6798": ["SpringDamperCompoundCriticalSpeedAnalysis"],
        "_6799": ["SpringDamperConnectionCompoundCriticalSpeedAnalysis"],
        "_6800": ["SpringDamperHalfCompoundCriticalSpeedAnalysis"],
        "_6801": ["StraightBevelDiffGearCompoundCriticalSpeedAnalysis"],
        "_6802": ["StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis"],
        "_6803": ["StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis"],
        "_6804": ["StraightBevelGearCompoundCriticalSpeedAnalysis"],
        "_6805": ["StraightBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6806": ["StraightBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6807": ["StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6808": ["StraightBevelSunGearCompoundCriticalSpeedAnalysis"],
        "_6809": ["SynchroniserCompoundCriticalSpeedAnalysis"],
        "_6810": ["SynchroniserHalfCompoundCriticalSpeedAnalysis"],
        "_6811": ["SynchroniserPartCompoundCriticalSpeedAnalysis"],
        "_6812": ["SynchroniserSleeveCompoundCriticalSpeedAnalysis"],
        "_6813": ["TorqueConverterCompoundCriticalSpeedAnalysis"],
        "_6814": ["TorqueConverterConnectionCompoundCriticalSpeedAnalysis"],
        "_6815": ["TorqueConverterPumpCompoundCriticalSpeedAnalysis"],
        "_6816": ["TorqueConverterTurbineCompoundCriticalSpeedAnalysis"],
        "_6817": ["UnbalancedMassCompoundCriticalSpeedAnalysis"],
        "_6818": ["VirtualComponentCompoundCriticalSpeedAnalysis"],
        "_6819": ["WormGearCompoundCriticalSpeedAnalysis"],
        "_6820": ["WormGearMeshCompoundCriticalSpeedAnalysis"],
        "_6821": ["WormGearSetCompoundCriticalSpeedAnalysis"],
        "_6822": ["ZerolBevelGearCompoundCriticalSpeedAnalysis"],
        "_6823": ["ZerolBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6824": ["ZerolBevelGearSetCompoundCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundCriticalSpeedAnalysis",
    "AbstractShaftCompoundCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
    "AssemblyCompoundCriticalSpeedAnalysis",
    "BearingCompoundCriticalSpeedAnalysis",
    "BeltConnectionCompoundCriticalSpeedAnalysis",
    "BeltDriveCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCompoundCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
    "BevelGearCompoundCriticalSpeedAnalysis",
    "BevelGearMeshCompoundCriticalSpeedAnalysis",
    "BevelGearSetCompoundCriticalSpeedAnalysis",
    "BoltCompoundCriticalSpeedAnalysis",
    "BoltedJointCompoundCriticalSpeedAnalysis",
    "ClutchCompoundCriticalSpeedAnalysis",
    "ClutchConnectionCompoundCriticalSpeedAnalysis",
    "ClutchHalfCompoundCriticalSpeedAnalysis",
    "CoaxialConnectionCompoundCriticalSpeedAnalysis",
    "ComponentCompoundCriticalSpeedAnalysis",
    "ConceptCouplingCompoundCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
    "ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
    "ConceptGearCompoundCriticalSpeedAnalysis",
    "ConceptGearMeshCompoundCriticalSpeedAnalysis",
    "ConceptGearSetCompoundCriticalSpeedAnalysis",
    "ConicalGearCompoundCriticalSpeedAnalysis",
    "ConicalGearMeshCompoundCriticalSpeedAnalysis",
    "ConicalGearSetCompoundCriticalSpeedAnalysis",
    "ConnectionCompoundCriticalSpeedAnalysis",
    "ConnectorCompoundCriticalSpeedAnalysis",
    "CouplingCompoundCriticalSpeedAnalysis",
    "CouplingConnectionCompoundCriticalSpeedAnalysis",
    "CouplingHalfCompoundCriticalSpeedAnalysis",
    "CVTBeltConnectionCompoundCriticalSpeedAnalysis",
    "CVTCompoundCriticalSpeedAnalysis",
    "CVTPulleyCompoundCriticalSpeedAnalysis",
    "CycloidalAssemblyCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCompoundCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis",
    "CylindricalGearCompoundCriticalSpeedAnalysis",
    "CylindricalGearMeshCompoundCriticalSpeedAnalysis",
    "CylindricalGearSetCompoundCriticalSpeedAnalysis",
    "CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
    "DatumCompoundCriticalSpeedAnalysis",
    "ExternalCADModelCompoundCriticalSpeedAnalysis",
    "FaceGearCompoundCriticalSpeedAnalysis",
    "FaceGearMeshCompoundCriticalSpeedAnalysis",
    "FaceGearSetCompoundCriticalSpeedAnalysis",
    "FEPartCompoundCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
    "GearCompoundCriticalSpeedAnalysis",
    "GearMeshCompoundCriticalSpeedAnalysis",
    "GearSetCompoundCriticalSpeedAnalysis",
    "GuideDxfModelCompoundCriticalSpeedAnalysis",
    "HypoidGearCompoundCriticalSpeedAnalysis",
    "HypoidGearMeshCompoundCriticalSpeedAnalysis",
    "HypoidGearSetCompoundCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "MassDiscCompoundCriticalSpeedAnalysis",
    "MeasurementComponentCompoundCriticalSpeedAnalysis",
    "MountableComponentCompoundCriticalSpeedAnalysis",
    "OilSealCompoundCriticalSpeedAnalysis",
    "PartCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
    "PlanetaryConnectionCompoundCriticalSpeedAnalysis",
    "PlanetaryGearSetCompoundCriticalSpeedAnalysis",
    "PlanetCarrierCompoundCriticalSpeedAnalysis",
    "PointLoadCompoundCriticalSpeedAnalysis",
    "PowerLoadCompoundCriticalSpeedAnalysis",
    "PulleyCompoundCriticalSpeedAnalysis",
    "RingPinsCompoundCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
    "RollingRingAssemblyCompoundCriticalSpeedAnalysis",
    "RollingRingCompoundCriticalSpeedAnalysis",
    "RollingRingConnectionCompoundCriticalSpeedAnalysis",
    "RootAssemblyCompoundCriticalSpeedAnalysis",
    "ShaftCompoundCriticalSpeedAnalysis",
    "ShaftHubConnectionCompoundCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "SpringDamperCompoundCriticalSpeedAnalysis",
    "SpringDamperConnectionCompoundCriticalSpeedAnalysis",
    "SpringDamperHalfCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelGearCompoundCriticalSpeedAnalysis",
    "StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
    "StraightBevelSunGearCompoundCriticalSpeedAnalysis",
    "SynchroniserCompoundCriticalSpeedAnalysis",
    "SynchroniserHalfCompoundCriticalSpeedAnalysis",
    "SynchroniserPartCompoundCriticalSpeedAnalysis",
    "SynchroniserSleeveCompoundCriticalSpeedAnalysis",
    "TorqueConverterCompoundCriticalSpeedAnalysis",
    "TorqueConverterConnectionCompoundCriticalSpeedAnalysis",
    "TorqueConverterPumpCompoundCriticalSpeedAnalysis",
    "TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
    "UnbalancedMassCompoundCriticalSpeedAnalysis",
    "VirtualComponentCompoundCriticalSpeedAnalysis",
    "WormGearCompoundCriticalSpeedAnalysis",
    "WormGearMeshCompoundCriticalSpeedAnalysis",
    "WormGearSetCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
)
