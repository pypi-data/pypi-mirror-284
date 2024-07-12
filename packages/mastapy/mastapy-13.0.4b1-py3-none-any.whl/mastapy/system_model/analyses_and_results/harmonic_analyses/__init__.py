"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5699 import AbstractAssemblyHarmonicAnalysis
    from ._5700 import AbstractPeriodicExcitationDetail
    from ._5701 import AbstractShaftHarmonicAnalysis
    from ._5702 import AbstractShaftOrHousingHarmonicAnalysis
    from ._5703 import AbstractShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5704 import AGMAGleasonConicalGearHarmonicAnalysis
    from ._5705 import AGMAGleasonConicalGearMeshHarmonicAnalysis
    from ._5706 import AGMAGleasonConicalGearSetHarmonicAnalysis
    from ._5707 import AssemblyHarmonicAnalysis
    from ._5708 import BearingHarmonicAnalysis
    from ._5709 import BeltConnectionHarmonicAnalysis
    from ._5710 import BeltDriveHarmonicAnalysis
    from ._5711 import BevelDifferentialGearHarmonicAnalysis
    from ._5712 import BevelDifferentialGearMeshHarmonicAnalysis
    from ._5713 import BevelDifferentialGearSetHarmonicAnalysis
    from ._5714 import BevelDifferentialPlanetGearHarmonicAnalysis
    from ._5715 import BevelDifferentialSunGearHarmonicAnalysis
    from ._5716 import BevelGearHarmonicAnalysis
    from ._5717 import BevelGearMeshHarmonicAnalysis
    from ._5718 import BevelGearSetHarmonicAnalysis
    from ._5719 import BoltedJointHarmonicAnalysis
    from ._5720 import BoltHarmonicAnalysis
    from ._5721 import ClutchConnectionHarmonicAnalysis
    from ._5722 import ClutchHalfHarmonicAnalysis
    from ._5723 import ClutchHarmonicAnalysis
    from ._5724 import CoaxialConnectionHarmonicAnalysis
    from ._5725 import ComplianceAndForceData
    from ._5726 import ComponentHarmonicAnalysis
    from ._5727 import ConceptCouplingConnectionHarmonicAnalysis
    from ._5728 import ConceptCouplingHalfHarmonicAnalysis
    from ._5729 import ConceptCouplingHarmonicAnalysis
    from ._5730 import ConceptGearHarmonicAnalysis
    from ._5731 import ConceptGearMeshHarmonicAnalysis
    from ._5732 import ConceptGearSetHarmonicAnalysis
    from ._5733 import ConicalGearHarmonicAnalysis
    from ._5734 import ConicalGearMeshHarmonicAnalysis
    from ._5735 import ConicalGearSetHarmonicAnalysis
    from ._5736 import ConnectionHarmonicAnalysis
    from ._5737 import ConnectorHarmonicAnalysis
    from ._5738 import CouplingConnectionHarmonicAnalysis
    from ._5739 import CouplingHalfHarmonicAnalysis
    from ._5740 import CouplingHarmonicAnalysis
    from ._5741 import CVTBeltConnectionHarmonicAnalysis
    from ._5742 import CVTHarmonicAnalysis
    from ._5743 import CVTPulleyHarmonicAnalysis
    from ._5744 import CycloidalAssemblyHarmonicAnalysis
    from ._5745 import CycloidalDiscCentralBearingConnectionHarmonicAnalysis
    from ._5746 import CycloidalDiscHarmonicAnalysis
    from ._5747 import CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
    from ._5748 import CylindricalGearHarmonicAnalysis
    from ._5749 import CylindricalGearMeshHarmonicAnalysis
    from ._5750 import CylindricalGearSetHarmonicAnalysis
    from ._5751 import CylindricalPlanetGearHarmonicAnalysis
    from ._5752 import DatumHarmonicAnalysis
    from ._5753 import DynamicModelForHarmonicAnalysis
    from ._5754 import ElectricMachinePeriodicExcitationDetail
    from ._5755 import ElectricMachineRotorXForcePeriodicExcitationDetail
    from ._5756 import ElectricMachineRotorXMomentPeriodicExcitationDetail
    from ._5757 import ElectricMachineRotorYForcePeriodicExcitationDetail
    from ._5758 import ElectricMachineRotorYMomentPeriodicExcitationDetail
    from ._5759 import ElectricMachineRotorZForcePeriodicExcitationDetail
    from ._5760 import ElectricMachineStatorToothAxialLoadsExcitationDetail
    from ._5761 import ElectricMachineStatorToothLoadsExcitationDetail
    from ._5762 import ElectricMachineStatorToothMomentsExcitationDetail
    from ._5763 import ElectricMachineStatorToothRadialLoadsExcitationDetail
    from ._5764 import ElectricMachineStatorToothTangentialLoadsExcitationDetail
    from ._5765 import ElectricMachineTorqueRipplePeriodicExcitationDetail
    from ._5766 import ExportOutputType
    from ._5767 import ExternalCADModelHarmonicAnalysis
    from ._5768 import FaceGearHarmonicAnalysis
    from ._5769 import FaceGearMeshHarmonicAnalysis
    from ._5770 import FaceGearSetHarmonicAnalysis
    from ._5771 import FEPartHarmonicAnalysis
    from ._5772 import FlexiblePinAssemblyHarmonicAnalysis
    from ._5773 import FrequencyOptionsForHarmonicAnalysisResults
    from ._5774 import GearHarmonicAnalysis
    from ._5775 import GearMeshExcitationDetail
    from ._5776 import GearMeshHarmonicAnalysis
    from ._5777 import GearMeshMisalignmentExcitationDetail
    from ._5778 import GearMeshTEExcitationDetail
    from ._5779 import GearSetHarmonicAnalysis
    from ._5780 import GeneralPeriodicExcitationDetail
    from ._5781 import GuideDxfModelHarmonicAnalysis
    from ._5782 import HarmonicAnalysis
    from ._5783 import HarmonicAnalysisDrawStyle
    from ._5784 import HarmonicAnalysisExportOptions
    from ._5785 import HarmonicAnalysisFEExportOptions
    from ._5786 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._5787 import HarmonicAnalysisOptions
    from ._5788 import HarmonicAnalysisRootAssemblyExportOptions
    from ._5789 import HarmonicAnalysisShaftExportOptions
    from ._5790 import HarmonicAnalysisTorqueInputType
    from ._5791 import HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
    from ._5792 import HypoidGearHarmonicAnalysis
    from ._5793 import HypoidGearMeshHarmonicAnalysis
    from ._5794 import HypoidGearSetHarmonicAnalysis
    from ._5795 import InterMountableComponentConnectionHarmonicAnalysis
    from ._5796 import KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
    from ._5797 import KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
    from ._5798 import KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
    from ._5799 import KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
    from ._5800 import KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
    from ._5801 import KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
    from ._5802 import KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
    from ._5803 import KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
    from ._5804 import KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
    from ._5805 import MassDiscHarmonicAnalysis
    from ._5806 import MeasurementComponentHarmonicAnalysis
    from ._5807 import MountableComponentHarmonicAnalysis
    from ._5808 import OilSealHarmonicAnalysis
    from ._5809 import PartHarmonicAnalysis
    from ._5810 import PartToPartShearCouplingConnectionHarmonicAnalysis
    from ._5811 import PartToPartShearCouplingHalfHarmonicAnalysis
    from ._5812 import PartToPartShearCouplingHarmonicAnalysis
    from ._5813 import PeriodicExcitationWithReferenceShaft
    from ._5814 import PlanetaryConnectionHarmonicAnalysis
    from ._5815 import PlanetaryGearSetHarmonicAnalysis
    from ._5816 import PlanetCarrierHarmonicAnalysis
    from ._5817 import PointLoadHarmonicAnalysis
    from ._5818 import PowerLoadHarmonicAnalysis
    from ._5819 import PulleyHarmonicAnalysis
    from ._5820 import ResponseCacheLevel
    from ._5821 import RingPinsHarmonicAnalysis
    from ._5822 import RingPinsToDiscConnectionHarmonicAnalysis
    from ._5823 import RollingRingAssemblyHarmonicAnalysis
    from ._5824 import RollingRingConnectionHarmonicAnalysis
    from ._5825 import RollingRingHarmonicAnalysis
    from ._5826 import RootAssemblyHarmonicAnalysis
    from ._5827 import ShaftHarmonicAnalysis
    from ._5828 import ShaftHubConnectionHarmonicAnalysis
    from ._5829 import ShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5830 import SingleNodePeriodicExcitationWithReferenceShaft
    from ._5831 import SpecialisedAssemblyHarmonicAnalysis
    from ._5832 import SpeedOptionsForHarmonicAnalysisResults
    from ._5833 import SpiralBevelGearHarmonicAnalysis
    from ._5834 import SpiralBevelGearMeshHarmonicAnalysis
    from ._5835 import SpiralBevelGearSetHarmonicAnalysis
    from ._5836 import SpringDamperConnectionHarmonicAnalysis
    from ._5837 import SpringDamperHalfHarmonicAnalysis
    from ._5838 import SpringDamperHarmonicAnalysis
    from ._5839 import StiffnessOptionsForHarmonicAnalysis
    from ._5840 import StraightBevelDiffGearHarmonicAnalysis
    from ._5841 import StraightBevelDiffGearMeshHarmonicAnalysis
    from ._5842 import StraightBevelDiffGearSetHarmonicAnalysis
    from ._5843 import StraightBevelGearHarmonicAnalysis
    from ._5844 import StraightBevelGearMeshHarmonicAnalysis
    from ._5845 import StraightBevelGearSetHarmonicAnalysis
    from ._5846 import StraightBevelPlanetGearHarmonicAnalysis
    from ._5847 import StraightBevelSunGearHarmonicAnalysis
    from ._5848 import SynchroniserHalfHarmonicAnalysis
    from ._5849 import SynchroniserHarmonicAnalysis
    from ._5850 import SynchroniserPartHarmonicAnalysis
    from ._5851 import SynchroniserSleeveHarmonicAnalysis
    from ._5852 import TorqueConverterConnectionHarmonicAnalysis
    from ._5853 import TorqueConverterHarmonicAnalysis
    from ._5854 import TorqueConverterPumpHarmonicAnalysis
    from ._5855 import TorqueConverterTurbineHarmonicAnalysis
    from ._5856 import UnbalancedMassExcitationDetail
    from ._5857 import UnbalancedMassHarmonicAnalysis
    from ._5858 import VirtualComponentHarmonicAnalysis
    from ._5859 import WormGearHarmonicAnalysis
    from ._5860 import WormGearMeshHarmonicAnalysis
    from ._5861 import WormGearSetHarmonicAnalysis
    from ._5862 import ZerolBevelGearHarmonicAnalysis
    from ._5863 import ZerolBevelGearMeshHarmonicAnalysis
    from ._5864 import ZerolBevelGearSetHarmonicAnalysis
else:
    import_structure = {
        "_5699": ["AbstractAssemblyHarmonicAnalysis"],
        "_5700": ["AbstractPeriodicExcitationDetail"],
        "_5701": ["AbstractShaftHarmonicAnalysis"],
        "_5702": ["AbstractShaftOrHousingHarmonicAnalysis"],
        "_5703": ["AbstractShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5704": ["AGMAGleasonConicalGearHarmonicAnalysis"],
        "_5705": ["AGMAGleasonConicalGearMeshHarmonicAnalysis"],
        "_5706": ["AGMAGleasonConicalGearSetHarmonicAnalysis"],
        "_5707": ["AssemblyHarmonicAnalysis"],
        "_5708": ["BearingHarmonicAnalysis"],
        "_5709": ["BeltConnectionHarmonicAnalysis"],
        "_5710": ["BeltDriveHarmonicAnalysis"],
        "_5711": ["BevelDifferentialGearHarmonicAnalysis"],
        "_5712": ["BevelDifferentialGearMeshHarmonicAnalysis"],
        "_5713": ["BevelDifferentialGearSetHarmonicAnalysis"],
        "_5714": ["BevelDifferentialPlanetGearHarmonicAnalysis"],
        "_5715": ["BevelDifferentialSunGearHarmonicAnalysis"],
        "_5716": ["BevelGearHarmonicAnalysis"],
        "_5717": ["BevelGearMeshHarmonicAnalysis"],
        "_5718": ["BevelGearSetHarmonicAnalysis"],
        "_5719": ["BoltedJointHarmonicAnalysis"],
        "_5720": ["BoltHarmonicAnalysis"],
        "_5721": ["ClutchConnectionHarmonicAnalysis"],
        "_5722": ["ClutchHalfHarmonicAnalysis"],
        "_5723": ["ClutchHarmonicAnalysis"],
        "_5724": ["CoaxialConnectionHarmonicAnalysis"],
        "_5725": ["ComplianceAndForceData"],
        "_5726": ["ComponentHarmonicAnalysis"],
        "_5727": ["ConceptCouplingConnectionHarmonicAnalysis"],
        "_5728": ["ConceptCouplingHalfHarmonicAnalysis"],
        "_5729": ["ConceptCouplingHarmonicAnalysis"],
        "_5730": ["ConceptGearHarmonicAnalysis"],
        "_5731": ["ConceptGearMeshHarmonicAnalysis"],
        "_5732": ["ConceptGearSetHarmonicAnalysis"],
        "_5733": ["ConicalGearHarmonicAnalysis"],
        "_5734": ["ConicalGearMeshHarmonicAnalysis"],
        "_5735": ["ConicalGearSetHarmonicAnalysis"],
        "_5736": ["ConnectionHarmonicAnalysis"],
        "_5737": ["ConnectorHarmonicAnalysis"],
        "_5738": ["CouplingConnectionHarmonicAnalysis"],
        "_5739": ["CouplingHalfHarmonicAnalysis"],
        "_5740": ["CouplingHarmonicAnalysis"],
        "_5741": ["CVTBeltConnectionHarmonicAnalysis"],
        "_5742": ["CVTHarmonicAnalysis"],
        "_5743": ["CVTPulleyHarmonicAnalysis"],
        "_5744": ["CycloidalAssemblyHarmonicAnalysis"],
        "_5745": ["CycloidalDiscCentralBearingConnectionHarmonicAnalysis"],
        "_5746": ["CycloidalDiscHarmonicAnalysis"],
        "_5747": ["CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis"],
        "_5748": ["CylindricalGearHarmonicAnalysis"],
        "_5749": ["CylindricalGearMeshHarmonicAnalysis"],
        "_5750": ["CylindricalGearSetHarmonicAnalysis"],
        "_5751": ["CylindricalPlanetGearHarmonicAnalysis"],
        "_5752": ["DatumHarmonicAnalysis"],
        "_5753": ["DynamicModelForHarmonicAnalysis"],
        "_5754": ["ElectricMachinePeriodicExcitationDetail"],
        "_5755": ["ElectricMachineRotorXForcePeriodicExcitationDetail"],
        "_5756": ["ElectricMachineRotorXMomentPeriodicExcitationDetail"],
        "_5757": ["ElectricMachineRotorYForcePeriodicExcitationDetail"],
        "_5758": ["ElectricMachineRotorYMomentPeriodicExcitationDetail"],
        "_5759": ["ElectricMachineRotorZForcePeriodicExcitationDetail"],
        "_5760": ["ElectricMachineStatorToothAxialLoadsExcitationDetail"],
        "_5761": ["ElectricMachineStatorToothLoadsExcitationDetail"],
        "_5762": ["ElectricMachineStatorToothMomentsExcitationDetail"],
        "_5763": ["ElectricMachineStatorToothRadialLoadsExcitationDetail"],
        "_5764": ["ElectricMachineStatorToothTangentialLoadsExcitationDetail"],
        "_5765": ["ElectricMachineTorqueRipplePeriodicExcitationDetail"],
        "_5766": ["ExportOutputType"],
        "_5767": ["ExternalCADModelHarmonicAnalysis"],
        "_5768": ["FaceGearHarmonicAnalysis"],
        "_5769": ["FaceGearMeshHarmonicAnalysis"],
        "_5770": ["FaceGearSetHarmonicAnalysis"],
        "_5771": ["FEPartHarmonicAnalysis"],
        "_5772": ["FlexiblePinAssemblyHarmonicAnalysis"],
        "_5773": ["FrequencyOptionsForHarmonicAnalysisResults"],
        "_5774": ["GearHarmonicAnalysis"],
        "_5775": ["GearMeshExcitationDetail"],
        "_5776": ["GearMeshHarmonicAnalysis"],
        "_5777": ["GearMeshMisalignmentExcitationDetail"],
        "_5778": ["GearMeshTEExcitationDetail"],
        "_5779": ["GearSetHarmonicAnalysis"],
        "_5780": ["GeneralPeriodicExcitationDetail"],
        "_5781": ["GuideDxfModelHarmonicAnalysis"],
        "_5782": ["HarmonicAnalysis"],
        "_5783": ["HarmonicAnalysisDrawStyle"],
        "_5784": ["HarmonicAnalysisExportOptions"],
        "_5785": ["HarmonicAnalysisFEExportOptions"],
        "_5786": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_5787": ["HarmonicAnalysisOptions"],
        "_5788": ["HarmonicAnalysisRootAssemblyExportOptions"],
        "_5789": ["HarmonicAnalysisShaftExportOptions"],
        "_5790": ["HarmonicAnalysisTorqueInputType"],
        "_5791": ["HarmonicAnalysisWithVaryingStiffnessStaticLoadCase"],
        "_5792": ["HypoidGearHarmonicAnalysis"],
        "_5793": ["HypoidGearMeshHarmonicAnalysis"],
        "_5794": ["HypoidGearSetHarmonicAnalysis"],
        "_5795": ["InterMountableComponentConnectionHarmonicAnalysis"],
        "_5796": ["KlingelnbergCycloPalloidConicalGearHarmonicAnalysis"],
        "_5797": ["KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis"],
        "_5798": ["KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis"],
        "_5799": ["KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis"],
        "_5800": ["KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis"],
        "_5801": ["KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis"],
        "_5802": ["KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis"],
        "_5803": ["KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis"],
        "_5804": ["KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis"],
        "_5805": ["MassDiscHarmonicAnalysis"],
        "_5806": ["MeasurementComponentHarmonicAnalysis"],
        "_5807": ["MountableComponentHarmonicAnalysis"],
        "_5808": ["OilSealHarmonicAnalysis"],
        "_5809": ["PartHarmonicAnalysis"],
        "_5810": ["PartToPartShearCouplingConnectionHarmonicAnalysis"],
        "_5811": ["PartToPartShearCouplingHalfHarmonicAnalysis"],
        "_5812": ["PartToPartShearCouplingHarmonicAnalysis"],
        "_5813": ["PeriodicExcitationWithReferenceShaft"],
        "_5814": ["PlanetaryConnectionHarmonicAnalysis"],
        "_5815": ["PlanetaryGearSetHarmonicAnalysis"],
        "_5816": ["PlanetCarrierHarmonicAnalysis"],
        "_5817": ["PointLoadHarmonicAnalysis"],
        "_5818": ["PowerLoadHarmonicAnalysis"],
        "_5819": ["PulleyHarmonicAnalysis"],
        "_5820": ["ResponseCacheLevel"],
        "_5821": ["RingPinsHarmonicAnalysis"],
        "_5822": ["RingPinsToDiscConnectionHarmonicAnalysis"],
        "_5823": ["RollingRingAssemblyHarmonicAnalysis"],
        "_5824": ["RollingRingConnectionHarmonicAnalysis"],
        "_5825": ["RollingRingHarmonicAnalysis"],
        "_5826": ["RootAssemblyHarmonicAnalysis"],
        "_5827": ["ShaftHarmonicAnalysis"],
        "_5828": ["ShaftHubConnectionHarmonicAnalysis"],
        "_5829": ["ShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5830": ["SingleNodePeriodicExcitationWithReferenceShaft"],
        "_5831": ["SpecialisedAssemblyHarmonicAnalysis"],
        "_5832": ["SpeedOptionsForHarmonicAnalysisResults"],
        "_5833": ["SpiralBevelGearHarmonicAnalysis"],
        "_5834": ["SpiralBevelGearMeshHarmonicAnalysis"],
        "_5835": ["SpiralBevelGearSetHarmonicAnalysis"],
        "_5836": ["SpringDamperConnectionHarmonicAnalysis"],
        "_5837": ["SpringDamperHalfHarmonicAnalysis"],
        "_5838": ["SpringDamperHarmonicAnalysis"],
        "_5839": ["StiffnessOptionsForHarmonicAnalysis"],
        "_5840": ["StraightBevelDiffGearHarmonicAnalysis"],
        "_5841": ["StraightBevelDiffGearMeshHarmonicAnalysis"],
        "_5842": ["StraightBevelDiffGearSetHarmonicAnalysis"],
        "_5843": ["StraightBevelGearHarmonicAnalysis"],
        "_5844": ["StraightBevelGearMeshHarmonicAnalysis"],
        "_5845": ["StraightBevelGearSetHarmonicAnalysis"],
        "_5846": ["StraightBevelPlanetGearHarmonicAnalysis"],
        "_5847": ["StraightBevelSunGearHarmonicAnalysis"],
        "_5848": ["SynchroniserHalfHarmonicAnalysis"],
        "_5849": ["SynchroniserHarmonicAnalysis"],
        "_5850": ["SynchroniserPartHarmonicAnalysis"],
        "_5851": ["SynchroniserSleeveHarmonicAnalysis"],
        "_5852": ["TorqueConverterConnectionHarmonicAnalysis"],
        "_5853": ["TorqueConverterHarmonicAnalysis"],
        "_5854": ["TorqueConverterPumpHarmonicAnalysis"],
        "_5855": ["TorqueConverterTurbineHarmonicAnalysis"],
        "_5856": ["UnbalancedMassExcitationDetail"],
        "_5857": ["UnbalancedMassHarmonicAnalysis"],
        "_5858": ["VirtualComponentHarmonicAnalysis"],
        "_5859": ["WormGearHarmonicAnalysis"],
        "_5860": ["WormGearMeshHarmonicAnalysis"],
        "_5861": ["WormGearSetHarmonicAnalysis"],
        "_5862": ["ZerolBevelGearHarmonicAnalysis"],
        "_5863": ["ZerolBevelGearMeshHarmonicAnalysis"],
        "_5864": ["ZerolBevelGearSetHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyHarmonicAnalysis",
    "AbstractPeriodicExcitationDetail",
    "AbstractShaftHarmonicAnalysis",
    "AbstractShaftOrHousingHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
    "AGMAGleasonConicalGearHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshHarmonicAnalysis",
    "AGMAGleasonConicalGearSetHarmonicAnalysis",
    "AssemblyHarmonicAnalysis",
    "BearingHarmonicAnalysis",
    "BeltConnectionHarmonicAnalysis",
    "BeltDriveHarmonicAnalysis",
    "BevelDifferentialGearHarmonicAnalysis",
    "BevelDifferentialGearMeshHarmonicAnalysis",
    "BevelDifferentialGearSetHarmonicAnalysis",
    "BevelDifferentialPlanetGearHarmonicAnalysis",
    "BevelDifferentialSunGearHarmonicAnalysis",
    "BevelGearHarmonicAnalysis",
    "BevelGearMeshHarmonicAnalysis",
    "BevelGearSetHarmonicAnalysis",
    "BoltedJointHarmonicAnalysis",
    "BoltHarmonicAnalysis",
    "ClutchConnectionHarmonicAnalysis",
    "ClutchHalfHarmonicAnalysis",
    "ClutchHarmonicAnalysis",
    "CoaxialConnectionHarmonicAnalysis",
    "ComplianceAndForceData",
    "ComponentHarmonicAnalysis",
    "ConceptCouplingConnectionHarmonicAnalysis",
    "ConceptCouplingHalfHarmonicAnalysis",
    "ConceptCouplingHarmonicAnalysis",
    "ConceptGearHarmonicAnalysis",
    "ConceptGearMeshHarmonicAnalysis",
    "ConceptGearSetHarmonicAnalysis",
    "ConicalGearHarmonicAnalysis",
    "ConicalGearMeshHarmonicAnalysis",
    "ConicalGearSetHarmonicAnalysis",
    "ConnectionHarmonicAnalysis",
    "ConnectorHarmonicAnalysis",
    "CouplingConnectionHarmonicAnalysis",
    "CouplingHalfHarmonicAnalysis",
    "CouplingHarmonicAnalysis",
    "CVTBeltConnectionHarmonicAnalysis",
    "CVTHarmonicAnalysis",
    "CVTPulleyHarmonicAnalysis",
    "CycloidalAssemblyHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
    "CycloidalDiscHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
    "CylindricalGearHarmonicAnalysis",
    "CylindricalGearMeshHarmonicAnalysis",
    "CylindricalGearSetHarmonicAnalysis",
    "CylindricalPlanetGearHarmonicAnalysis",
    "DatumHarmonicAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "ElectricMachinePeriodicExcitationDetail",
    "ElectricMachineRotorXForcePeriodicExcitationDetail",
    "ElectricMachineRotorXMomentPeriodicExcitationDetail",
    "ElectricMachineRotorYForcePeriodicExcitationDetail",
    "ElectricMachineRotorYMomentPeriodicExcitationDetail",
    "ElectricMachineRotorZForcePeriodicExcitationDetail",
    "ElectricMachineStatorToothAxialLoadsExcitationDetail",
    "ElectricMachineStatorToothLoadsExcitationDetail",
    "ElectricMachineStatorToothMomentsExcitationDetail",
    "ElectricMachineStatorToothRadialLoadsExcitationDetail",
    "ElectricMachineStatorToothTangentialLoadsExcitationDetail",
    "ElectricMachineTorqueRipplePeriodicExcitationDetail",
    "ExportOutputType",
    "ExternalCADModelHarmonicAnalysis",
    "FaceGearHarmonicAnalysis",
    "FaceGearMeshHarmonicAnalysis",
    "FaceGearSetHarmonicAnalysis",
    "FEPartHarmonicAnalysis",
    "FlexiblePinAssemblyHarmonicAnalysis",
    "FrequencyOptionsForHarmonicAnalysisResults",
    "GearHarmonicAnalysis",
    "GearMeshExcitationDetail",
    "GearMeshHarmonicAnalysis",
    "GearMeshMisalignmentExcitationDetail",
    "GearMeshTEExcitationDetail",
    "GearSetHarmonicAnalysis",
    "GeneralPeriodicExcitationDetail",
    "GuideDxfModelHarmonicAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisDrawStyle",
    "HarmonicAnalysisExportOptions",
    "HarmonicAnalysisFEExportOptions",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptions",
    "HarmonicAnalysisRootAssemblyExportOptions",
    "HarmonicAnalysisShaftExportOptions",
    "HarmonicAnalysisTorqueInputType",
    "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
    "HypoidGearHarmonicAnalysis",
    "HypoidGearMeshHarmonicAnalysis",
    "HypoidGearSetHarmonicAnalysis",
    "InterMountableComponentConnectionHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
    "MassDiscHarmonicAnalysis",
    "MeasurementComponentHarmonicAnalysis",
    "MountableComponentHarmonicAnalysis",
    "OilSealHarmonicAnalysis",
    "PartHarmonicAnalysis",
    "PartToPartShearCouplingConnectionHarmonicAnalysis",
    "PartToPartShearCouplingHalfHarmonicAnalysis",
    "PartToPartShearCouplingHarmonicAnalysis",
    "PeriodicExcitationWithReferenceShaft",
    "PlanetaryConnectionHarmonicAnalysis",
    "PlanetaryGearSetHarmonicAnalysis",
    "PlanetCarrierHarmonicAnalysis",
    "PointLoadHarmonicAnalysis",
    "PowerLoadHarmonicAnalysis",
    "PulleyHarmonicAnalysis",
    "ResponseCacheLevel",
    "RingPinsHarmonicAnalysis",
    "RingPinsToDiscConnectionHarmonicAnalysis",
    "RollingRingAssemblyHarmonicAnalysis",
    "RollingRingConnectionHarmonicAnalysis",
    "RollingRingHarmonicAnalysis",
    "RootAssemblyHarmonicAnalysis",
    "ShaftHarmonicAnalysis",
    "ShaftHubConnectionHarmonicAnalysis",
    "ShaftToMountableComponentConnectionHarmonicAnalysis",
    "SingleNodePeriodicExcitationWithReferenceShaft",
    "SpecialisedAssemblyHarmonicAnalysis",
    "SpeedOptionsForHarmonicAnalysisResults",
    "SpiralBevelGearHarmonicAnalysis",
    "SpiralBevelGearMeshHarmonicAnalysis",
    "SpiralBevelGearSetHarmonicAnalysis",
    "SpringDamperConnectionHarmonicAnalysis",
    "SpringDamperHalfHarmonicAnalysis",
    "SpringDamperHarmonicAnalysis",
    "StiffnessOptionsForHarmonicAnalysis",
    "StraightBevelDiffGearHarmonicAnalysis",
    "StraightBevelDiffGearMeshHarmonicAnalysis",
    "StraightBevelDiffGearSetHarmonicAnalysis",
    "StraightBevelGearHarmonicAnalysis",
    "StraightBevelGearMeshHarmonicAnalysis",
    "StraightBevelGearSetHarmonicAnalysis",
    "StraightBevelPlanetGearHarmonicAnalysis",
    "StraightBevelSunGearHarmonicAnalysis",
    "SynchroniserHalfHarmonicAnalysis",
    "SynchroniserHarmonicAnalysis",
    "SynchroniserPartHarmonicAnalysis",
    "SynchroniserSleeveHarmonicAnalysis",
    "TorqueConverterConnectionHarmonicAnalysis",
    "TorqueConverterHarmonicAnalysis",
    "TorqueConverterPumpHarmonicAnalysis",
    "TorqueConverterTurbineHarmonicAnalysis",
    "UnbalancedMassExcitationDetail",
    "UnbalancedMassHarmonicAnalysis",
    "VirtualComponentHarmonicAnalysis",
    "WormGearHarmonicAnalysis",
    "WormGearMeshHarmonicAnalysis",
    "WormGearSetHarmonicAnalysis",
    "ZerolBevelGearHarmonicAnalysis",
    "ZerolBevelGearMeshHarmonicAnalysis",
    "ZerolBevelGearSetHarmonicAnalysis",
)
