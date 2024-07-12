"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3784 import AbstractAssemblyStabilityAnalysis
    from ._3785 import AbstractShaftOrHousingStabilityAnalysis
    from ._3786 import AbstractShaftStabilityAnalysis
    from ._3787 import AbstractShaftToMountableComponentConnectionStabilityAnalysis
    from ._3788 import AGMAGleasonConicalGearMeshStabilityAnalysis
    from ._3789 import AGMAGleasonConicalGearSetStabilityAnalysis
    from ._3790 import AGMAGleasonConicalGearStabilityAnalysis
    from ._3791 import AssemblyStabilityAnalysis
    from ._3792 import BearingStabilityAnalysis
    from ._3793 import BeltConnectionStabilityAnalysis
    from ._3794 import BeltDriveStabilityAnalysis
    from ._3795 import BevelDifferentialGearMeshStabilityAnalysis
    from ._3796 import BevelDifferentialGearSetStabilityAnalysis
    from ._3797 import BevelDifferentialGearStabilityAnalysis
    from ._3798 import BevelDifferentialPlanetGearStabilityAnalysis
    from ._3799 import BevelDifferentialSunGearStabilityAnalysis
    from ._3800 import BevelGearMeshStabilityAnalysis
    from ._3801 import BevelGearSetStabilityAnalysis
    from ._3802 import BevelGearStabilityAnalysis
    from ._3803 import BoltedJointStabilityAnalysis
    from ._3804 import BoltStabilityAnalysis
    from ._3805 import ClutchConnectionStabilityAnalysis
    from ._3806 import ClutchHalfStabilityAnalysis
    from ._3807 import ClutchStabilityAnalysis
    from ._3808 import CoaxialConnectionStabilityAnalysis
    from ._3809 import ComponentStabilityAnalysis
    from ._3810 import ConceptCouplingConnectionStabilityAnalysis
    from ._3811 import ConceptCouplingHalfStabilityAnalysis
    from ._3812 import ConceptCouplingStabilityAnalysis
    from ._3813 import ConceptGearMeshStabilityAnalysis
    from ._3814 import ConceptGearSetStabilityAnalysis
    from ._3815 import ConceptGearStabilityAnalysis
    from ._3816 import ConicalGearMeshStabilityAnalysis
    from ._3817 import ConicalGearSetStabilityAnalysis
    from ._3818 import ConicalGearStabilityAnalysis
    from ._3819 import ConnectionStabilityAnalysis
    from ._3820 import ConnectorStabilityAnalysis
    from ._3821 import CouplingConnectionStabilityAnalysis
    from ._3822 import CouplingHalfStabilityAnalysis
    from ._3823 import CouplingStabilityAnalysis
    from ._3824 import CriticalSpeed
    from ._3825 import CVTBeltConnectionStabilityAnalysis
    from ._3826 import CVTPulleyStabilityAnalysis
    from ._3827 import CVTStabilityAnalysis
    from ._3828 import CycloidalAssemblyStabilityAnalysis
    from ._3829 import CycloidalDiscCentralBearingConnectionStabilityAnalysis
    from ._3830 import CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
    from ._3831 import CycloidalDiscStabilityAnalysis
    from ._3832 import CylindricalGearMeshStabilityAnalysis
    from ._3833 import CylindricalGearSetStabilityAnalysis
    from ._3834 import CylindricalGearStabilityAnalysis
    from ._3835 import CylindricalPlanetGearStabilityAnalysis
    from ._3836 import DatumStabilityAnalysis
    from ._3837 import DynamicModelForStabilityAnalysis
    from ._3838 import ExternalCADModelStabilityAnalysis
    from ._3839 import FaceGearMeshStabilityAnalysis
    from ._3840 import FaceGearSetStabilityAnalysis
    from ._3841 import FaceGearStabilityAnalysis
    from ._3842 import FEPartStabilityAnalysis
    from ._3843 import FlexiblePinAssemblyStabilityAnalysis
    from ._3844 import GearMeshStabilityAnalysis
    from ._3845 import GearSetStabilityAnalysis
    from ._3846 import GearStabilityAnalysis
    from ._3847 import GuideDxfModelStabilityAnalysis
    from ._3848 import HypoidGearMeshStabilityAnalysis
    from ._3849 import HypoidGearSetStabilityAnalysis
    from ._3850 import HypoidGearStabilityAnalysis
    from ._3851 import InterMountableComponentConnectionStabilityAnalysis
    from ._3852 import KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
    from ._3853 import KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
    from ._3854 import KlingelnbergCycloPalloidConicalGearStabilityAnalysis
    from ._3855 import KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
    from ._3856 import KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
    from ._3857 import KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
    from ._3858 import KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
    from ._3859 import KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
    from ._3860 import KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
    from ._3861 import MassDiscStabilityAnalysis
    from ._3862 import MeasurementComponentStabilityAnalysis
    from ._3863 import MountableComponentStabilityAnalysis
    from ._3864 import OilSealStabilityAnalysis
    from ._3865 import PartStabilityAnalysis
    from ._3866 import PartToPartShearCouplingConnectionStabilityAnalysis
    from ._3867 import PartToPartShearCouplingHalfStabilityAnalysis
    from ._3868 import PartToPartShearCouplingStabilityAnalysis
    from ._3869 import PlanetaryConnectionStabilityAnalysis
    from ._3870 import PlanetaryGearSetStabilityAnalysis
    from ._3871 import PlanetCarrierStabilityAnalysis
    from ._3872 import PointLoadStabilityAnalysis
    from ._3873 import PowerLoadStabilityAnalysis
    from ._3874 import PulleyStabilityAnalysis
    from ._3875 import RingPinsStabilityAnalysis
    from ._3876 import RingPinsToDiscConnectionStabilityAnalysis
    from ._3877 import RollingRingAssemblyStabilityAnalysis
    from ._3878 import RollingRingConnectionStabilityAnalysis
    from ._3879 import RollingRingStabilityAnalysis
    from ._3880 import RootAssemblyStabilityAnalysis
    from ._3881 import ShaftHubConnectionStabilityAnalysis
    from ._3882 import ShaftStabilityAnalysis
    from ._3883 import ShaftToMountableComponentConnectionStabilityAnalysis
    from ._3884 import SpecialisedAssemblyStabilityAnalysis
    from ._3885 import SpiralBevelGearMeshStabilityAnalysis
    from ._3886 import SpiralBevelGearSetStabilityAnalysis
    from ._3887 import SpiralBevelGearStabilityAnalysis
    from ._3888 import SpringDamperConnectionStabilityAnalysis
    from ._3889 import SpringDamperHalfStabilityAnalysis
    from ._3890 import SpringDamperStabilityAnalysis
    from ._3891 import StabilityAnalysis
    from ._3892 import StabilityAnalysisDrawStyle
    from ._3893 import StabilityAnalysisOptions
    from ._3894 import StraightBevelDiffGearMeshStabilityAnalysis
    from ._3895 import StraightBevelDiffGearSetStabilityAnalysis
    from ._3896 import StraightBevelDiffGearStabilityAnalysis
    from ._3897 import StraightBevelGearMeshStabilityAnalysis
    from ._3898 import StraightBevelGearSetStabilityAnalysis
    from ._3899 import StraightBevelGearStabilityAnalysis
    from ._3900 import StraightBevelPlanetGearStabilityAnalysis
    from ._3901 import StraightBevelSunGearStabilityAnalysis
    from ._3902 import SynchroniserHalfStabilityAnalysis
    from ._3903 import SynchroniserPartStabilityAnalysis
    from ._3904 import SynchroniserSleeveStabilityAnalysis
    from ._3905 import SynchroniserStabilityAnalysis
    from ._3906 import TorqueConverterConnectionStabilityAnalysis
    from ._3907 import TorqueConverterPumpStabilityAnalysis
    from ._3908 import TorqueConverterStabilityAnalysis
    from ._3909 import TorqueConverterTurbineStabilityAnalysis
    from ._3910 import UnbalancedMassStabilityAnalysis
    from ._3911 import VirtualComponentStabilityAnalysis
    from ._3912 import WormGearMeshStabilityAnalysis
    from ._3913 import WormGearSetStabilityAnalysis
    from ._3914 import WormGearStabilityAnalysis
    from ._3915 import ZerolBevelGearMeshStabilityAnalysis
    from ._3916 import ZerolBevelGearSetStabilityAnalysis
    from ._3917 import ZerolBevelGearStabilityAnalysis
else:
    import_structure = {
        "_3784": ["AbstractAssemblyStabilityAnalysis"],
        "_3785": ["AbstractShaftOrHousingStabilityAnalysis"],
        "_3786": ["AbstractShaftStabilityAnalysis"],
        "_3787": ["AbstractShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3788": ["AGMAGleasonConicalGearMeshStabilityAnalysis"],
        "_3789": ["AGMAGleasonConicalGearSetStabilityAnalysis"],
        "_3790": ["AGMAGleasonConicalGearStabilityAnalysis"],
        "_3791": ["AssemblyStabilityAnalysis"],
        "_3792": ["BearingStabilityAnalysis"],
        "_3793": ["BeltConnectionStabilityAnalysis"],
        "_3794": ["BeltDriveStabilityAnalysis"],
        "_3795": ["BevelDifferentialGearMeshStabilityAnalysis"],
        "_3796": ["BevelDifferentialGearSetStabilityAnalysis"],
        "_3797": ["BevelDifferentialGearStabilityAnalysis"],
        "_3798": ["BevelDifferentialPlanetGearStabilityAnalysis"],
        "_3799": ["BevelDifferentialSunGearStabilityAnalysis"],
        "_3800": ["BevelGearMeshStabilityAnalysis"],
        "_3801": ["BevelGearSetStabilityAnalysis"],
        "_3802": ["BevelGearStabilityAnalysis"],
        "_3803": ["BoltedJointStabilityAnalysis"],
        "_3804": ["BoltStabilityAnalysis"],
        "_3805": ["ClutchConnectionStabilityAnalysis"],
        "_3806": ["ClutchHalfStabilityAnalysis"],
        "_3807": ["ClutchStabilityAnalysis"],
        "_3808": ["CoaxialConnectionStabilityAnalysis"],
        "_3809": ["ComponentStabilityAnalysis"],
        "_3810": ["ConceptCouplingConnectionStabilityAnalysis"],
        "_3811": ["ConceptCouplingHalfStabilityAnalysis"],
        "_3812": ["ConceptCouplingStabilityAnalysis"],
        "_3813": ["ConceptGearMeshStabilityAnalysis"],
        "_3814": ["ConceptGearSetStabilityAnalysis"],
        "_3815": ["ConceptGearStabilityAnalysis"],
        "_3816": ["ConicalGearMeshStabilityAnalysis"],
        "_3817": ["ConicalGearSetStabilityAnalysis"],
        "_3818": ["ConicalGearStabilityAnalysis"],
        "_3819": ["ConnectionStabilityAnalysis"],
        "_3820": ["ConnectorStabilityAnalysis"],
        "_3821": ["CouplingConnectionStabilityAnalysis"],
        "_3822": ["CouplingHalfStabilityAnalysis"],
        "_3823": ["CouplingStabilityAnalysis"],
        "_3824": ["CriticalSpeed"],
        "_3825": ["CVTBeltConnectionStabilityAnalysis"],
        "_3826": ["CVTPulleyStabilityAnalysis"],
        "_3827": ["CVTStabilityAnalysis"],
        "_3828": ["CycloidalAssemblyStabilityAnalysis"],
        "_3829": ["CycloidalDiscCentralBearingConnectionStabilityAnalysis"],
        "_3830": ["CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis"],
        "_3831": ["CycloidalDiscStabilityAnalysis"],
        "_3832": ["CylindricalGearMeshStabilityAnalysis"],
        "_3833": ["CylindricalGearSetStabilityAnalysis"],
        "_3834": ["CylindricalGearStabilityAnalysis"],
        "_3835": ["CylindricalPlanetGearStabilityAnalysis"],
        "_3836": ["DatumStabilityAnalysis"],
        "_3837": ["DynamicModelForStabilityAnalysis"],
        "_3838": ["ExternalCADModelStabilityAnalysis"],
        "_3839": ["FaceGearMeshStabilityAnalysis"],
        "_3840": ["FaceGearSetStabilityAnalysis"],
        "_3841": ["FaceGearStabilityAnalysis"],
        "_3842": ["FEPartStabilityAnalysis"],
        "_3843": ["FlexiblePinAssemblyStabilityAnalysis"],
        "_3844": ["GearMeshStabilityAnalysis"],
        "_3845": ["GearSetStabilityAnalysis"],
        "_3846": ["GearStabilityAnalysis"],
        "_3847": ["GuideDxfModelStabilityAnalysis"],
        "_3848": ["HypoidGearMeshStabilityAnalysis"],
        "_3849": ["HypoidGearSetStabilityAnalysis"],
        "_3850": ["HypoidGearStabilityAnalysis"],
        "_3851": ["InterMountableComponentConnectionStabilityAnalysis"],
        "_3852": ["KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis"],
        "_3853": ["KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis"],
        "_3854": ["KlingelnbergCycloPalloidConicalGearStabilityAnalysis"],
        "_3855": ["KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis"],
        "_3856": ["KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis"],
        "_3857": ["KlingelnbergCycloPalloidHypoidGearStabilityAnalysis"],
        "_3858": ["KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis"],
        "_3859": ["KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis"],
        "_3860": ["KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis"],
        "_3861": ["MassDiscStabilityAnalysis"],
        "_3862": ["MeasurementComponentStabilityAnalysis"],
        "_3863": ["MountableComponentStabilityAnalysis"],
        "_3864": ["OilSealStabilityAnalysis"],
        "_3865": ["PartStabilityAnalysis"],
        "_3866": ["PartToPartShearCouplingConnectionStabilityAnalysis"],
        "_3867": ["PartToPartShearCouplingHalfStabilityAnalysis"],
        "_3868": ["PartToPartShearCouplingStabilityAnalysis"],
        "_3869": ["PlanetaryConnectionStabilityAnalysis"],
        "_3870": ["PlanetaryGearSetStabilityAnalysis"],
        "_3871": ["PlanetCarrierStabilityAnalysis"],
        "_3872": ["PointLoadStabilityAnalysis"],
        "_3873": ["PowerLoadStabilityAnalysis"],
        "_3874": ["PulleyStabilityAnalysis"],
        "_3875": ["RingPinsStabilityAnalysis"],
        "_3876": ["RingPinsToDiscConnectionStabilityAnalysis"],
        "_3877": ["RollingRingAssemblyStabilityAnalysis"],
        "_3878": ["RollingRingConnectionStabilityAnalysis"],
        "_3879": ["RollingRingStabilityAnalysis"],
        "_3880": ["RootAssemblyStabilityAnalysis"],
        "_3881": ["ShaftHubConnectionStabilityAnalysis"],
        "_3882": ["ShaftStabilityAnalysis"],
        "_3883": ["ShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3884": ["SpecialisedAssemblyStabilityAnalysis"],
        "_3885": ["SpiralBevelGearMeshStabilityAnalysis"],
        "_3886": ["SpiralBevelGearSetStabilityAnalysis"],
        "_3887": ["SpiralBevelGearStabilityAnalysis"],
        "_3888": ["SpringDamperConnectionStabilityAnalysis"],
        "_3889": ["SpringDamperHalfStabilityAnalysis"],
        "_3890": ["SpringDamperStabilityAnalysis"],
        "_3891": ["StabilityAnalysis"],
        "_3892": ["StabilityAnalysisDrawStyle"],
        "_3893": ["StabilityAnalysisOptions"],
        "_3894": ["StraightBevelDiffGearMeshStabilityAnalysis"],
        "_3895": ["StraightBevelDiffGearSetStabilityAnalysis"],
        "_3896": ["StraightBevelDiffGearStabilityAnalysis"],
        "_3897": ["StraightBevelGearMeshStabilityAnalysis"],
        "_3898": ["StraightBevelGearSetStabilityAnalysis"],
        "_3899": ["StraightBevelGearStabilityAnalysis"],
        "_3900": ["StraightBevelPlanetGearStabilityAnalysis"],
        "_3901": ["StraightBevelSunGearStabilityAnalysis"],
        "_3902": ["SynchroniserHalfStabilityAnalysis"],
        "_3903": ["SynchroniserPartStabilityAnalysis"],
        "_3904": ["SynchroniserSleeveStabilityAnalysis"],
        "_3905": ["SynchroniserStabilityAnalysis"],
        "_3906": ["TorqueConverterConnectionStabilityAnalysis"],
        "_3907": ["TorqueConverterPumpStabilityAnalysis"],
        "_3908": ["TorqueConverterStabilityAnalysis"],
        "_3909": ["TorqueConverterTurbineStabilityAnalysis"],
        "_3910": ["UnbalancedMassStabilityAnalysis"],
        "_3911": ["VirtualComponentStabilityAnalysis"],
        "_3912": ["WormGearMeshStabilityAnalysis"],
        "_3913": ["WormGearSetStabilityAnalysis"],
        "_3914": ["WormGearStabilityAnalysis"],
        "_3915": ["ZerolBevelGearMeshStabilityAnalysis"],
        "_3916": ["ZerolBevelGearSetStabilityAnalysis"],
        "_3917": ["ZerolBevelGearStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStabilityAnalysis",
    "AbstractShaftOrHousingStabilityAnalysis",
    "AbstractShaftStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionStabilityAnalysis",
    "AGMAGleasonConicalGearMeshStabilityAnalysis",
    "AGMAGleasonConicalGearSetStabilityAnalysis",
    "AGMAGleasonConicalGearStabilityAnalysis",
    "AssemblyStabilityAnalysis",
    "BearingStabilityAnalysis",
    "BeltConnectionStabilityAnalysis",
    "BeltDriveStabilityAnalysis",
    "BevelDifferentialGearMeshStabilityAnalysis",
    "BevelDifferentialGearSetStabilityAnalysis",
    "BevelDifferentialGearStabilityAnalysis",
    "BevelDifferentialPlanetGearStabilityAnalysis",
    "BevelDifferentialSunGearStabilityAnalysis",
    "BevelGearMeshStabilityAnalysis",
    "BevelGearSetStabilityAnalysis",
    "BevelGearStabilityAnalysis",
    "BoltedJointStabilityAnalysis",
    "BoltStabilityAnalysis",
    "ClutchConnectionStabilityAnalysis",
    "ClutchHalfStabilityAnalysis",
    "ClutchStabilityAnalysis",
    "CoaxialConnectionStabilityAnalysis",
    "ComponentStabilityAnalysis",
    "ConceptCouplingConnectionStabilityAnalysis",
    "ConceptCouplingHalfStabilityAnalysis",
    "ConceptCouplingStabilityAnalysis",
    "ConceptGearMeshStabilityAnalysis",
    "ConceptGearSetStabilityAnalysis",
    "ConceptGearStabilityAnalysis",
    "ConicalGearMeshStabilityAnalysis",
    "ConicalGearSetStabilityAnalysis",
    "ConicalGearStabilityAnalysis",
    "ConnectionStabilityAnalysis",
    "ConnectorStabilityAnalysis",
    "CouplingConnectionStabilityAnalysis",
    "CouplingHalfStabilityAnalysis",
    "CouplingStabilityAnalysis",
    "CriticalSpeed",
    "CVTBeltConnectionStabilityAnalysis",
    "CVTPulleyStabilityAnalysis",
    "CVTStabilityAnalysis",
    "CycloidalAssemblyStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
    "CycloidalDiscStabilityAnalysis",
    "CylindricalGearMeshStabilityAnalysis",
    "CylindricalGearSetStabilityAnalysis",
    "CylindricalGearStabilityAnalysis",
    "CylindricalPlanetGearStabilityAnalysis",
    "DatumStabilityAnalysis",
    "DynamicModelForStabilityAnalysis",
    "ExternalCADModelStabilityAnalysis",
    "FaceGearMeshStabilityAnalysis",
    "FaceGearSetStabilityAnalysis",
    "FaceGearStabilityAnalysis",
    "FEPartStabilityAnalysis",
    "FlexiblePinAssemblyStabilityAnalysis",
    "GearMeshStabilityAnalysis",
    "GearSetStabilityAnalysis",
    "GearStabilityAnalysis",
    "GuideDxfModelStabilityAnalysis",
    "HypoidGearMeshStabilityAnalysis",
    "HypoidGearSetStabilityAnalysis",
    "HypoidGearStabilityAnalysis",
    "InterMountableComponentConnectionStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
    "MassDiscStabilityAnalysis",
    "MeasurementComponentStabilityAnalysis",
    "MountableComponentStabilityAnalysis",
    "OilSealStabilityAnalysis",
    "PartStabilityAnalysis",
    "PartToPartShearCouplingConnectionStabilityAnalysis",
    "PartToPartShearCouplingHalfStabilityAnalysis",
    "PartToPartShearCouplingStabilityAnalysis",
    "PlanetaryConnectionStabilityAnalysis",
    "PlanetaryGearSetStabilityAnalysis",
    "PlanetCarrierStabilityAnalysis",
    "PointLoadStabilityAnalysis",
    "PowerLoadStabilityAnalysis",
    "PulleyStabilityAnalysis",
    "RingPinsStabilityAnalysis",
    "RingPinsToDiscConnectionStabilityAnalysis",
    "RollingRingAssemblyStabilityAnalysis",
    "RollingRingConnectionStabilityAnalysis",
    "RollingRingStabilityAnalysis",
    "RootAssemblyStabilityAnalysis",
    "ShaftHubConnectionStabilityAnalysis",
    "ShaftStabilityAnalysis",
    "ShaftToMountableComponentConnectionStabilityAnalysis",
    "SpecialisedAssemblyStabilityAnalysis",
    "SpiralBevelGearMeshStabilityAnalysis",
    "SpiralBevelGearSetStabilityAnalysis",
    "SpiralBevelGearStabilityAnalysis",
    "SpringDamperConnectionStabilityAnalysis",
    "SpringDamperHalfStabilityAnalysis",
    "SpringDamperStabilityAnalysis",
    "StabilityAnalysis",
    "StabilityAnalysisDrawStyle",
    "StabilityAnalysisOptions",
    "StraightBevelDiffGearMeshStabilityAnalysis",
    "StraightBevelDiffGearSetStabilityAnalysis",
    "StraightBevelDiffGearStabilityAnalysis",
    "StraightBevelGearMeshStabilityAnalysis",
    "StraightBevelGearSetStabilityAnalysis",
    "StraightBevelGearStabilityAnalysis",
    "StraightBevelPlanetGearStabilityAnalysis",
    "StraightBevelSunGearStabilityAnalysis",
    "SynchroniserHalfStabilityAnalysis",
    "SynchroniserPartStabilityAnalysis",
    "SynchroniserSleeveStabilityAnalysis",
    "SynchroniserStabilityAnalysis",
    "TorqueConverterConnectionStabilityAnalysis",
    "TorqueConverterPumpStabilityAnalysis",
    "TorqueConverterStabilityAnalysis",
    "TorqueConverterTurbineStabilityAnalysis",
    "UnbalancedMassStabilityAnalysis",
    "VirtualComponentStabilityAnalysis",
    "WormGearMeshStabilityAnalysis",
    "WormGearSetStabilityAnalysis",
    "WormGearStabilityAnalysis",
    "ZerolBevelGearMeshStabilityAnalysis",
    "ZerolBevelGearSetStabilityAnalysis",
    "ZerolBevelGearStabilityAnalysis",
)
