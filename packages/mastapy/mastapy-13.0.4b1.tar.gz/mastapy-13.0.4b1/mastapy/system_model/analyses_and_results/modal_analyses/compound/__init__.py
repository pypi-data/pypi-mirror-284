"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4749 import AbstractAssemblyCompoundModalAnalysis
    from ._4750 import AbstractShaftCompoundModalAnalysis
    from ._4751 import AbstractShaftOrHousingCompoundModalAnalysis
    from ._4752 import AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4753 import AGMAGleasonConicalGearCompoundModalAnalysis
    from ._4754 import AGMAGleasonConicalGearMeshCompoundModalAnalysis
    from ._4755 import AGMAGleasonConicalGearSetCompoundModalAnalysis
    from ._4756 import AssemblyCompoundModalAnalysis
    from ._4757 import BearingCompoundModalAnalysis
    from ._4758 import BeltConnectionCompoundModalAnalysis
    from ._4759 import BeltDriveCompoundModalAnalysis
    from ._4760 import BevelDifferentialGearCompoundModalAnalysis
    from ._4761 import BevelDifferentialGearMeshCompoundModalAnalysis
    from ._4762 import BevelDifferentialGearSetCompoundModalAnalysis
    from ._4763 import BevelDifferentialPlanetGearCompoundModalAnalysis
    from ._4764 import BevelDifferentialSunGearCompoundModalAnalysis
    from ._4765 import BevelGearCompoundModalAnalysis
    from ._4766 import BevelGearMeshCompoundModalAnalysis
    from ._4767 import BevelGearSetCompoundModalAnalysis
    from ._4768 import BoltCompoundModalAnalysis
    from ._4769 import BoltedJointCompoundModalAnalysis
    from ._4770 import ClutchCompoundModalAnalysis
    from ._4771 import ClutchConnectionCompoundModalAnalysis
    from ._4772 import ClutchHalfCompoundModalAnalysis
    from ._4773 import CoaxialConnectionCompoundModalAnalysis
    from ._4774 import ComponentCompoundModalAnalysis
    from ._4775 import ConceptCouplingCompoundModalAnalysis
    from ._4776 import ConceptCouplingConnectionCompoundModalAnalysis
    from ._4777 import ConceptCouplingHalfCompoundModalAnalysis
    from ._4778 import ConceptGearCompoundModalAnalysis
    from ._4779 import ConceptGearMeshCompoundModalAnalysis
    from ._4780 import ConceptGearSetCompoundModalAnalysis
    from ._4781 import ConicalGearCompoundModalAnalysis
    from ._4782 import ConicalGearMeshCompoundModalAnalysis
    from ._4783 import ConicalGearSetCompoundModalAnalysis
    from ._4784 import ConnectionCompoundModalAnalysis
    from ._4785 import ConnectorCompoundModalAnalysis
    from ._4786 import CouplingCompoundModalAnalysis
    from ._4787 import CouplingConnectionCompoundModalAnalysis
    from ._4788 import CouplingHalfCompoundModalAnalysis
    from ._4789 import CVTBeltConnectionCompoundModalAnalysis
    from ._4790 import CVTCompoundModalAnalysis
    from ._4791 import CVTPulleyCompoundModalAnalysis
    from ._4792 import CycloidalAssemblyCompoundModalAnalysis
    from ._4793 import CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
    from ._4794 import CycloidalDiscCompoundModalAnalysis
    from ._4795 import CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
    from ._4796 import CylindricalGearCompoundModalAnalysis
    from ._4797 import CylindricalGearMeshCompoundModalAnalysis
    from ._4798 import CylindricalGearSetCompoundModalAnalysis
    from ._4799 import CylindricalPlanetGearCompoundModalAnalysis
    from ._4800 import DatumCompoundModalAnalysis
    from ._4801 import ExternalCADModelCompoundModalAnalysis
    from ._4802 import FaceGearCompoundModalAnalysis
    from ._4803 import FaceGearMeshCompoundModalAnalysis
    from ._4804 import FaceGearSetCompoundModalAnalysis
    from ._4805 import FEPartCompoundModalAnalysis
    from ._4806 import FlexiblePinAssemblyCompoundModalAnalysis
    from ._4807 import GearCompoundModalAnalysis
    from ._4808 import GearMeshCompoundModalAnalysis
    from ._4809 import GearSetCompoundModalAnalysis
    from ._4810 import GuideDxfModelCompoundModalAnalysis
    from ._4811 import HypoidGearCompoundModalAnalysis
    from ._4812 import HypoidGearMeshCompoundModalAnalysis
    from ._4813 import HypoidGearSetCompoundModalAnalysis
    from ._4814 import InterMountableComponentConnectionCompoundModalAnalysis
    from ._4815 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
    from ._4816 import KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
    from ._4817 import KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
    from ._4818 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
    from ._4819 import KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
    from ._4820 import KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
    from ._4821 import KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
    from ._4822 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
    from ._4823 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
    from ._4824 import MassDiscCompoundModalAnalysis
    from ._4825 import MeasurementComponentCompoundModalAnalysis
    from ._4826 import MountableComponentCompoundModalAnalysis
    from ._4827 import OilSealCompoundModalAnalysis
    from ._4828 import PartCompoundModalAnalysis
    from ._4829 import PartToPartShearCouplingCompoundModalAnalysis
    from ._4830 import PartToPartShearCouplingConnectionCompoundModalAnalysis
    from ._4831 import PartToPartShearCouplingHalfCompoundModalAnalysis
    from ._4832 import PlanetaryConnectionCompoundModalAnalysis
    from ._4833 import PlanetaryGearSetCompoundModalAnalysis
    from ._4834 import PlanetCarrierCompoundModalAnalysis
    from ._4835 import PointLoadCompoundModalAnalysis
    from ._4836 import PowerLoadCompoundModalAnalysis
    from ._4837 import PulleyCompoundModalAnalysis
    from ._4838 import RingPinsCompoundModalAnalysis
    from ._4839 import RingPinsToDiscConnectionCompoundModalAnalysis
    from ._4840 import RollingRingAssemblyCompoundModalAnalysis
    from ._4841 import RollingRingCompoundModalAnalysis
    from ._4842 import RollingRingConnectionCompoundModalAnalysis
    from ._4843 import RootAssemblyCompoundModalAnalysis
    from ._4844 import ShaftCompoundModalAnalysis
    from ._4845 import ShaftHubConnectionCompoundModalAnalysis
    from ._4846 import ShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4847 import SpecialisedAssemblyCompoundModalAnalysis
    from ._4848 import SpiralBevelGearCompoundModalAnalysis
    from ._4849 import SpiralBevelGearMeshCompoundModalAnalysis
    from ._4850 import SpiralBevelGearSetCompoundModalAnalysis
    from ._4851 import SpringDamperCompoundModalAnalysis
    from ._4852 import SpringDamperConnectionCompoundModalAnalysis
    from ._4853 import SpringDamperHalfCompoundModalAnalysis
    from ._4854 import StraightBevelDiffGearCompoundModalAnalysis
    from ._4855 import StraightBevelDiffGearMeshCompoundModalAnalysis
    from ._4856 import StraightBevelDiffGearSetCompoundModalAnalysis
    from ._4857 import StraightBevelGearCompoundModalAnalysis
    from ._4858 import StraightBevelGearMeshCompoundModalAnalysis
    from ._4859 import StraightBevelGearSetCompoundModalAnalysis
    from ._4860 import StraightBevelPlanetGearCompoundModalAnalysis
    from ._4861 import StraightBevelSunGearCompoundModalAnalysis
    from ._4862 import SynchroniserCompoundModalAnalysis
    from ._4863 import SynchroniserHalfCompoundModalAnalysis
    from ._4864 import SynchroniserPartCompoundModalAnalysis
    from ._4865 import SynchroniserSleeveCompoundModalAnalysis
    from ._4866 import TorqueConverterCompoundModalAnalysis
    from ._4867 import TorqueConverterConnectionCompoundModalAnalysis
    from ._4868 import TorqueConverterPumpCompoundModalAnalysis
    from ._4869 import TorqueConverterTurbineCompoundModalAnalysis
    from ._4870 import UnbalancedMassCompoundModalAnalysis
    from ._4871 import VirtualComponentCompoundModalAnalysis
    from ._4872 import WormGearCompoundModalAnalysis
    from ._4873 import WormGearMeshCompoundModalAnalysis
    from ._4874 import WormGearSetCompoundModalAnalysis
    from ._4875 import ZerolBevelGearCompoundModalAnalysis
    from ._4876 import ZerolBevelGearMeshCompoundModalAnalysis
    from ._4877 import ZerolBevelGearSetCompoundModalAnalysis
else:
    import_structure = {
        "_4749": ["AbstractAssemblyCompoundModalAnalysis"],
        "_4750": ["AbstractShaftCompoundModalAnalysis"],
        "_4751": ["AbstractShaftOrHousingCompoundModalAnalysis"],
        "_4752": ["AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4753": ["AGMAGleasonConicalGearCompoundModalAnalysis"],
        "_4754": ["AGMAGleasonConicalGearMeshCompoundModalAnalysis"],
        "_4755": ["AGMAGleasonConicalGearSetCompoundModalAnalysis"],
        "_4756": ["AssemblyCompoundModalAnalysis"],
        "_4757": ["BearingCompoundModalAnalysis"],
        "_4758": ["BeltConnectionCompoundModalAnalysis"],
        "_4759": ["BeltDriveCompoundModalAnalysis"],
        "_4760": ["BevelDifferentialGearCompoundModalAnalysis"],
        "_4761": ["BevelDifferentialGearMeshCompoundModalAnalysis"],
        "_4762": ["BevelDifferentialGearSetCompoundModalAnalysis"],
        "_4763": ["BevelDifferentialPlanetGearCompoundModalAnalysis"],
        "_4764": ["BevelDifferentialSunGearCompoundModalAnalysis"],
        "_4765": ["BevelGearCompoundModalAnalysis"],
        "_4766": ["BevelGearMeshCompoundModalAnalysis"],
        "_4767": ["BevelGearSetCompoundModalAnalysis"],
        "_4768": ["BoltCompoundModalAnalysis"],
        "_4769": ["BoltedJointCompoundModalAnalysis"],
        "_4770": ["ClutchCompoundModalAnalysis"],
        "_4771": ["ClutchConnectionCompoundModalAnalysis"],
        "_4772": ["ClutchHalfCompoundModalAnalysis"],
        "_4773": ["CoaxialConnectionCompoundModalAnalysis"],
        "_4774": ["ComponentCompoundModalAnalysis"],
        "_4775": ["ConceptCouplingCompoundModalAnalysis"],
        "_4776": ["ConceptCouplingConnectionCompoundModalAnalysis"],
        "_4777": ["ConceptCouplingHalfCompoundModalAnalysis"],
        "_4778": ["ConceptGearCompoundModalAnalysis"],
        "_4779": ["ConceptGearMeshCompoundModalAnalysis"],
        "_4780": ["ConceptGearSetCompoundModalAnalysis"],
        "_4781": ["ConicalGearCompoundModalAnalysis"],
        "_4782": ["ConicalGearMeshCompoundModalAnalysis"],
        "_4783": ["ConicalGearSetCompoundModalAnalysis"],
        "_4784": ["ConnectionCompoundModalAnalysis"],
        "_4785": ["ConnectorCompoundModalAnalysis"],
        "_4786": ["CouplingCompoundModalAnalysis"],
        "_4787": ["CouplingConnectionCompoundModalAnalysis"],
        "_4788": ["CouplingHalfCompoundModalAnalysis"],
        "_4789": ["CVTBeltConnectionCompoundModalAnalysis"],
        "_4790": ["CVTCompoundModalAnalysis"],
        "_4791": ["CVTPulleyCompoundModalAnalysis"],
        "_4792": ["CycloidalAssemblyCompoundModalAnalysis"],
        "_4793": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysis"],
        "_4794": ["CycloidalDiscCompoundModalAnalysis"],
        "_4795": ["CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis"],
        "_4796": ["CylindricalGearCompoundModalAnalysis"],
        "_4797": ["CylindricalGearMeshCompoundModalAnalysis"],
        "_4798": ["CylindricalGearSetCompoundModalAnalysis"],
        "_4799": ["CylindricalPlanetGearCompoundModalAnalysis"],
        "_4800": ["DatumCompoundModalAnalysis"],
        "_4801": ["ExternalCADModelCompoundModalAnalysis"],
        "_4802": ["FaceGearCompoundModalAnalysis"],
        "_4803": ["FaceGearMeshCompoundModalAnalysis"],
        "_4804": ["FaceGearSetCompoundModalAnalysis"],
        "_4805": ["FEPartCompoundModalAnalysis"],
        "_4806": ["FlexiblePinAssemblyCompoundModalAnalysis"],
        "_4807": ["GearCompoundModalAnalysis"],
        "_4808": ["GearMeshCompoundModalAnalysis"],
        "_4809": ["GearSetCompoundModalAnalysis"],
        "_4810": ["GuideDxfModelCompoundModalAnalysis"],
        "_4811": ["HypoidGearCompoundModalAnalysis"],
        "_4812": ["HypoidGearMeshCompoundModalAnalysis"],
        "_4813": ["HypoidGearSetCompoundModalAnalysis"],
        "_4814": ["InterMountableComponentConnectionCompoundModalAnalysis"],
        "_4815": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis"],
        "_4816": ["KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"],
        "_4817": ["KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"],
        "_4818": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis"],
        "_4819": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis"],
        "_4820": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis"],
        "_4821": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis"],
        "_4822": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis"],
        "_4823": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis"],
        "_4824": ["MassDiscCompoundModalAnalysis"],
        "_4825": ["MeasurementComponentCompoundModalAnalysis"],
        "_4826": ["MountableComponentCompoundModalAnalysis"],
        "_4827": ["OilSealCompoundModalAnalysis"],
        "_4828": ["PartCompoundModalAnalysis"],
        "_4829": ["PartToPartShearCouplingCompoundModalAnalysis"],
        "_4830": ["PartToPartShearCouplingConnectionCompoundModalAnalysis"],
        "_4831": ["PartToPartShearCouplingHalfCompoundModalAnalysis"],
        "_4832": ["PlanetaryConnectionCompoundModalAnalysis"],
        "_4833": ["PlanetaryGearSetCompoundModalAnalysis"],
        "_4834": ["PlanetCarrierCompoundModalAnalysis"],
        "_4835": ["PointLoadCompoundModalAnalysis"],
        "_4836": ["PowerLoadCompoundModalAnalysis"],
        "_4837": ["PulleyCompoundModalAnalysis"],
        "_4838": ["RingPinsCompoundModalAnalysis"],
        "_4839": ["RingPinsToDiscConnectionCompoundModalAnalysis"],
        "_4840": ["RollingRingAssemblyCompoundModalAnalysis"],
        "_4841": ["RollingRingCompoundModalAnalysis"],
        "_4842": ["RollingRingConnectionCompoundModalAnalysis"],
        "_4843": ["RootAssemblyCompoundModalAnalysis"],
        "_4844": ["ShaftCompoundModalAnalysis"],
        "_4845": ["ShaftHubConnectionCompoundModalAnalysis"],
        "_4846": ["ShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4847": ["SpecialisedAssemblyCompoundModalAnalysis"],
        "_4848": ["SpiralBevelGearCompoundModalAnalysis"],
        "_4849": ["SpiralBevelGearMeshCompoundModalAnalysis"],
        "_4850": ["SpiralBevelGearSetCompoundModalAnalysis"],
        "_4851": ["SpringDamperCompoundModalAnalysis"],
        "_4852": ["SpringDamperConnectionCompoundModalAnalysis"],
        "_4853": ["SpringDamperHalfCompoundModalAnalysis"],
        "_4854": ["StraightBevelDiffGearCompoundModalAnalysis"],
        "_4855": ["StraightBevelDiffGearMeshCompoundModalAnalysis"],
        "_4856": ["StraightBevelDiffGearSetCompoundModalAnalysis"],
        "_4857": ["StraightBevelGearCompoundModalAnalysis"],
        "_4858": ["StraightBevelGearMeshCompoundModalAnalysis"],
        "_4859": ["StraightBevelGearSetCompoundModalAnalysis"],
        "_4860": ["StraightBevelPlanetGearCompoundModalAnalysis"],
        "_4861": ["StraightBevelSunGearCompoundModalAnalysis"],
        "_4862": ["SynchroniserCompoundModalAnalysis"],
        "_4863": ["SynchroniserHalfCompoundModalAnalysis"],
        "_4864": ["SynchroniserPartCompoundModalAnalysis"],
        "_4865": ["SynchroniserSleeveCompoundModalAnalysis"],
        "_4866": ["TorqueConverterCompoundModalAnalysis"],
        "_4867": ["TorqueConverterConnectionCompoundModalAnalysis"],
        "_4868": ["TorqueConverterPumpCompoundModalAnalysis"],
        "_4869": ["TorqueConverterTurbineCompoundModalAnalysis"],
        "_4870": ["UnbalancedMassCompoundModalAnalysis"],
        "_4871": ["VirtualComponentCompoundModalAnalysis"],
        "_4872": ["WormGearCompoundModalAnalysis"],
        "_4873": ["WormGearMeshCompoundModalAnalysis"],
        "_4874": ["WormGearSetCompoundModalAnalysis"],
        "_4875": ["ZerolBevelGearCompoundModalAnalysis"],
        "_4876": ["ZerolBevelGearMeshCompoundModalAnalysis"],
        "_4877": ["ZerolBevelGearSetCompoundModalAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysis",
    "AbstractShaftCompoundModalAnalysis",
    "AbstractShaftOrHousingCompoundModalAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
    "AGMAGleasonConicalGearCompoundModalAnalysis",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysis",
    "AGMAGleasonConicalGearSetCompoundModalAnalysis",
    "AssemblyCompoundModalAnalysis",
    "BearingCompoundModalAnalysis",
    "BeltConnectionCompoundModalAnalysis",
    "BeltDriveCompoundModalAnalysis",
    "BevelDifferentialGearCompoundModalAnalysis",
    "BevelDifferentialGearMeshCompoundModalAnalysis",
    "BevelDifferentialGearSetCompoundModalAnalysis",
    "BevelDifferentialPlanetGearCompoundModalAnalysis",
    "BevelDifferentialSunGearCompoundModalAnalysis",
    "BevelGearCompoundModalAnalysis",
    "BevelGearMeshCompoundModalAnalysis",
    "BevelGearSetCompoundModalAnalysis",
    "BoltCompoundModalAnalysis",
    "BoltedJointCompoundModalAnalysis",
    "ClutchCompoundModalAnalysis",
    "ClutchConnectionCompoundModalAnalysis",
    "ClutchHalfCompoundModalAnalysis",
    "CoaxialConnectionCompoundModalAnalysis",
    "ComponentCompoundModalAnalysis",
    "ConceptCouplingCompoundModalAnalysis",
    "ConceptCouplingConnectionCompoundModalAnalysis",
    "ConceptCouplingHalfCompoundModalAnalysis",
    "ConceptGearCompoundModalAnalysis",
    "ConceptGearMeshCompoundModalAnalysis",
    "ConceptGearSetCompoundModalAnalysis",
    "ConicalGearCompoundModalAnalysis",
    "ConicalGearMeshCompoundModalAnalysis",
    "ConicalGearSetCompoundModalAnalysis",
    "ConnectionCompoundModalAnalysis",
    "ConnectorCompoundModalAnalysis",
    "CouplingCompoundModalAnalysis",
    "CouplingConnectionCompoundModalAnalysis",
    "CouplingHalfCompoundModalAnalysis",
    "CVTBeltConnectionCompoundModalAnalysis",
    "CVTCompoundModalAnalysis",
    "CVTPulleyCompoundModalAnalysis",
    "CycloidalAssemblyCompoundModalAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
    "CycloidalDiscCompoundModalAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
    "CylindricalGearCompoundModalAnalysis",
    "CylindricalGearMeshCompoundModalAnalysis",
    "CylindricalGearSetCompoundModalAnalysis",
    "CylindricalPlanetGearCompoundModalAnalysis",
    "DatumCompoundModalAnalysis",
    "ExternalCADModelCompoundModalAnalysis",
    "FaceGearCompoundModalAnalysis",
    "FaceGearMeshCompoundModalAnalysis",
    "FaceGearSetCompoundModalAnalysis",
    "FEPartCompoundModalAnalysis",
    "FlexiblePinAssemblyCompoundModalAnalysis",
    "GearCompoundModalAnalysis",
    "GearMeshCompoundModalAnalysis",
    "GearSetCompoundModalAnalysis",
    "GuideDxfModelCompoundModalAnalysis",
    "HypoidGearCompoundModalAnalysis",
    "HypoidGearMeshCompoundModalAnalysis",
    "HypoidGearSetCompoundModalAnalysis",
    "InterMountableComponentConnectionCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
    "MassDiscCompoundModalAnalysis",
    "MeasurementComponentCompoundModalAnalysis",
    "MountableComponentCompoundModalAnalysis",
    "OilSealCompoundModalAnalysis",
    "PartCompoundModalAnalysis",
    "PartToPartShearCouplingCompoundModalAnalysis",
    "PartToPartShearCouplingConnectionCompoundModalAnalysis",
    "PartToPartShearCouplingHalfCompoundModalAnalysis",
    "PlanetaryConnectionCompoundModalAnalysis",
    "PlanetaryGearSetCompoundModalAnalysis",
    "PlanetCarrierCompoundModalAnalysis",
    "PointLoadCompoundModalAnalysis",
    "PowerLoadCompoundModalAnalysis",
    "PulleyCompoundModalAnalysis",
    "RingPinsCompoundModalAnalysis",
    "RingPinsToDiscConnectionCompoundModalAnalysis",
    "RollingRingAssemblyCompoundModalAnalysis",
    "RollingRingCompoundModalAnalysis",
    "RollingRingConnectionCompoundModalAnalysis",
    "RootAssemblyCompoundModalAnalysis",
    "ShaftCompoundModalAnalysis",
    "ShaftHubConnectionCompoundModalAnalysis",
    "ShaftToMountableComponentConnectionCompoundModalAnalysis",
    "SpecialisedAssemblyCompoundModalAnalysis",
    "SpiralBevelGearCompoundModalAnalysis",
    "SpiralBevelGearMeshCompoundModalAnalysis",
    "SpiralBevelGearSetCompoundModalAnalysis",
    "SpringDamperCompoundModalAnalysis",
    "SpringDamperConnectionCompoundModalAnalysis",
    "SpringDamperHalfCompoundModalAnalysis",
    "StraightBevelDiffGearCompoundModalAnalysis",
    "StraightBevelDiffGearMeshCompoundModalAnalysis",
    "StraightBevelDiffGearSetCompoundModalAnalysis",
    "StraightBevelGearCompoundModalAnalysis",
    "StraightBevelGearMeshCompoundModalAnalysis",
    "StraightBevelGearSetCompoundModalAnalysis",
    "StraightBevelPlanetGearCompoundModalAnalysis",
    "StraightBevelSunGearCompoundModalAnalysis",
    "SynchroniserCompoundModalAnalysis",
    "SynchroniserHalfCompoundModalAnalysis",
    "SynchroniserPartCompoundModalAnalysis",
    "SynchroniserSleeveCompoundModalAnalysis",
    "TorqueConverterCompoundModalAnalysis",
    "TorqueConverterConnectionCompoundModalAnalysis",
    "TorqueConverterPumpCompoundModalAnalysis",
    "TorqueConverterTurbineCompoundModalAnalysis",
    "UnbalancedMassCompoundModalAnalysis",
    "VirtualComponentCompoundModalAnalysis",
    "WormGearCompoundModalAnalysis",
    "WormGearMeshCompoundModalAnalysis",
    "WormGearSetCompoundModalAnalysis",
    "ZerolBevelGearCompoundModalAnalysis",
    "ZerolBevelGearMeshCompoundModalAnalysis",
    "ZerolBevelGearSetCompoundModalAnalysis",
)
