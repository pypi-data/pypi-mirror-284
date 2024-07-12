"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3918 import AbstractAssemblyCompoundStabilityAnalysis
    from ._3919 import AbstractShaftCompoundStabilityAnalysis
    from ._3920 import AbstractShaftOrHousingCompoundStabilityAnalysis
    from ._3921 import (
        AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis,
    )
    from ._3922 import AGMAGleasonConicalGearCompoundStabilityAnalysis
    from ._3923 import AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
    from ._3924 import AGMAGleasonConicalGearSetCompoundStabilityAnalysis
    from ._3925 import AssemblyCompoundStabilityAnalysis
    from ._3926 import BearingCompoundStabilityAnalysis
    from ._3927 import BeltConnectionCompoundStabilityAnalysis
    from ._3928 import BeltDriveCompoundStabilityAnalysis
    from ._3929 import BevelDifferentialGearCompoundStabilityAnalysis
    from ._3930 import BevelDifferentialGearMeshCompoundStabilityAnalysis
    from ._3931 import BevelDifferentialGearSetCompoundStabilityAnalysis
    from ._3932 import BevelDifferentialPlanetGearCompoundStabilityAnalysis
    from ._3933 import BevelDifferentialSunGearCompoundStabilityAnalysis
    from ._3934 import BevelGearCompoundStabilityAnalysis
    from ._3935 import BevelGearMeshCompoundStabilityAnalysis
    from ._3936 import BevelGearSetCompoundStabilityAnalysis
    from ._3937 import BoltCompoundStabilityAnalysis
    from ._3938 import BoltedJointCompoundStabilityAnalysis
    from ._3939 import ClutchCompoundStabilityAnalysis
    from ._3940 import ClutchConnectionCompoundStabilityAnalysis
    from ._3941 import ClutchHalfCompoundStabilityAnalysis
    from ._3942 import CoaxialConnectionCompoundStabilityAnalysis
    from ._3943 import ComponentCompoundStabilityAnalysis
    from ._3944 import ConceptCouplingCompoundStabilityAnalysis
    from ._3945 import ConceptCouplingConnectionCompoundStabilityAnalysis
    from ._3946 import ConceptCouplingHalfCompoundStabilityAnalysis
    from ._3947 import ConceptGearCompoundStabilityAnalysis
    from ._3948 import ConceptGearMeshCompoundStabilityAnalysis
    from ._3949 import ConceptGearSetCompoundStabilityAnalysis
    from ._3950 import ConicalGearCompoundStabilityAnalysis
    from ._3951 import ConicalGearMeshCompoundStabilityAnalysis
    from ._3952 import ConicalGearSetCompoundStabilityAnalysis
    from ._3953 import ConnectionCompoundStabilityAnalysis
    from ._3954 import ConnectorCompoundStabilityAnalysis
    from ._3955 import CouplingCompoundStabilityAnalysis
    from ._3956 import CouplingConnectionCompoundStabilityAnalysis
    from ._3957 import CouplingHalfCompoundStabilityAnalysis
    from ._3958 import CVTBeltConnectionCompoundStabilityAnalysis
    from ._3959 import CVTCompoundStabilityAnalysis
    from ._3960 import CVTPulleyCompoundStabilityAnalysis
    from ._3961 import CycloidalAssemblyCompoundStabilityAnalysis
    from ._3962 import CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
    from ._3963 import CycloidalDiscCompoundStabilityAnalysis
    from ._3964 import CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
    from ._3965 import CylindricalGearCompoundStabilityAnalysis
    from ._3966 import CylindricalGearMeshCompoundStabilityAnalysis
    from ._3967 import CylindricalGearSetCompoundStabilityAnalysis
    from ._3968 import CylindricalPlanetGearCompoundStabilityAnalysis
    from ._3969 import DatumCompoundStabilityAnalysis
    from ._3970 import ExternalCADModelCompoundStabilityAnalysis
    from ._3971 import FaceGearCompoundStabilityAnalysis
    from ._3972 import FaceGearMeshCompoundStabilityAnalysis
    from ._3973 import FaceGearSetCompoundStabilityAnalysis
    from ._3974 import FEPartCompoundStabilityAnalysis
    from ._3975 import FlexiblePinAssemblyCompoundStabilityAnalysis
    from ._3976 import GearCompoundStabilityAnalysis
    from ._3977 import GearMeshCompoundStabilityAnalysis
    from ._3978 import GearSetCompoundStabilityAnalysis
    from ._3979 import GuideDxfModelCompoundStabilityAnalysis
    from ._3980 import HypoidGearCompoundStabilityAnalysis
    from ._3981 import HypoidGearMeshCompoundStabilityAnalysis
    from ._3982 import HypoidGearSetCompoundStabilityAnalysis
    from ._3983 import InterMountableComponentConnectionCompoundStabilityAnalysis
    from ._3984 import KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
    from ._3985 import KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
    from ._3986 import KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
    from ._3987 import KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
    from ._3988 import KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
    from ._3989 import KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
    from ._3990 import KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
    from ._3991 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis,
    )
    from ._3992 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis,
    )
    from ._3993 import MassDiscCompoundStabilityAnalysis
    from ._3994 import MeasurementComponentCompoundStabilityAnalysis
    from ._3995 import MountableComponentCompoundStabilityAnalysis
    from ._3996 import OilSealCompoundStabilityAnalysis
    from ._3997 import PartCompoundStabilityAnalysis
    from ._3998 import PartToPartShearCouplingCompoundStabilityAnalysis
    from ._3999 import PartToPartShearCouplingConnectionCompoundStabilityAnalysis
    from ._4000 import PartToPartShearCouplingHalfCompoundStabilityAnalysis
    from ._4001 import PlanetaryConnectionCompoundStabilityAnalysis
    from ._4002 import PlanetaryGearSetCompoundStabilityAnalysis
    from ._4003 import PlanetCarrierCompoundStabilityAnalysis
    from ._4004 import PointLoadCompoundStabilityAnalysis
    from ._4005 import PowerLoadCompoundStabilityAnalysis
    from ._4006 import PulleyCompoundStabilityAnalysis
    from ._4007 import RingPinsCompoundStabilityAnalysis
    from ._4008 import RingPinsToDiscConnectionCompoundStabilityAnalysis
    from ._4009 import RollingRingAssemblyCompoundStabilityAnalysis
    from ._4010 import RollingRingCompoundStabilityAnalysis
    from ._4011 import RollingRingConnectionCompoundStabilityAnalysis
    from ._4012 import RootAssemblyCompoundStabilityAnalysis
    from ._4013 import ShaftCompoundStabilityAnalysis
    from ._4014 import ShaftHubConnectionCompoundStabilityAnalysis
    from ._4015 import ShaftToMountableComponentConnectionCompoundStabilityAnalysis
    from ._4016 import SpecialisedAssemblyCompoundStabilityAnalysis
    from ._4017 import SpiralBevelGearCompoundStabilityAnalysis
    from ._4018 import SpiralBevelGearMeshCompoundStabilityAnalysis
    from ._4019 import SpiralBevelGearSetCompoundStabilityAnalysis
    from ._4020 import SpringDamperCompoundStabilityAnalysis
    from ._4021 import SpringDamperConnectionCompoundStabilityAnalysis
    from ._4022 import SpringDamperHalfCompoundStabilityAnalysis
    from ._4023 import StraightBevelDiffGearCompoundStabilityAnalysis
    from ._4024 import StraightBevelDiffGearMeshCompoundStabilityAnalysis
    from ._4025 import StraightBevelDiffGearSetCompoundStabilityAnalysis
    from ._4026 import StraightBevelGearCompoundStabilityAnalysis
    from ._4027 import StraightBevelGearMeshCompoundStabilityAnalysis
    from ._4028 import StraightBevelGearSetCompoundStabilityAnalysis
    from ._4029 import StraightBevelPlanetGearCompoundStabilityAnalysis
    from ._4030 import StraightBevelSunGearCompoundStabilityAnalysis
    from ._4031 import SynchroniserCompoundStabilityAnalysis
    from ._4032 import SynchroniserHalfCompoundStabilityAnalysis
    from ._4033 import SynchroniserPartCompoundStabilityAnalysis
    from ._4034 import SynchroniserSleeveCompoundStabilityAnalysis
    from ._4035 import TorqueConverterCompoundStabilityAnalysis
    from ._4036 import TorqueConverterConnectionCompoundStabilityAnalysis
    from ._4037 import TorqueConverterPumpCompoundStabilityAnalysis
    from ._4038 import TorqueConverterTurbineCompoundStabilityAnalysis
    from ._4039 import UnbalancedMassCompoundStabilityAnalysis
    from ._4040 import VirtualComponentCompoundStabilityAnalysis
    from ._4041 import WormGearCompoundStabilityAnalysis
    from ._4042 import WormGearMeshCompoundStabilityAnalysis
    from ._4043 import WormGearSetCompoundStabilityAnalysis
    from ._4044 import ZerolBevelGearCompoundStabilityAnalysis
    from ._4045 import ZerolBevelGearMeshCompoundStabilityAnalysis
    from ._4046 import ZerolBevelGearSetCompoundStabilityAnalysis
else:
    import_structure = {
        "_3918": ["AbstractAssemblyCompoundStabilityAnalysis"],
        "_3919": ["AbstractShaftCompoundStabilityAnalysis"],
        "_3920": ["AbstractShaftOrHousingCompoundStabilityAnalysis"],
        "_3921": [
            "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ],
        "_3922": ["AGMAGleasonConicalGearCompoundStabilityAnalysis"],
        "_3923": ["AGMAGleasonConicalGearMeshCompoundStabilityAnalysis"],
        "_3924": ["AGMAGleasonConicalGearSetCompoundStabilityAnalysis"],
        "_3925": ["AssemblyCompoundStabilityAnalysis"],
        "_3926": ["BearingCompoundStabilityAnalysis"],
        "_3927": ["BeltConnectionCompoundStabilityAnalysis"],
        "_3928": ["BeltDriveCompoundStabilityAnalysis"],
        "_3929": ["BevelDifferentialGearCompoundStabilityAnalysis"],
        "_3930": ["BevelDifferentialGearMeshCompoundStabilityAnalysis"],
        "_3931": ["BevelDifferentialGearSetCompoundStabilityAnalysis"],
        "_3932": ["BevelDifferentialPlanetGearCompoundStabilityAnalysis"],
        "_3933": ["BevelDifferentialSunGearCompoundStabilityAnalysis"],
        "_3934": ["BevelGearCompoundStabilityAnalysis"],
        "_3935": ["BevelGearMeshCompoundStabilityAnalysis"],
        "_3936": ["BevelGearSetCompoundStabilityAnalysis"],
        "_3937": ["BoltCompoundStabilityAnalysis"],
        "_3938": ["BoltedJointCompoundStabilityAnalysis"],
        "_3939": ["ClutchCompoundStabilityAnalysis"],
        "_3940": ["ClutchConnectionCompoundStabilityAnalysis"],
        "_3941": ["ClutchHalfCompoundStabilityAnalysis"],
        "_3942": ["CoaxialConnectionCompoundStabilityAnalysis"],
        "_3943": ["ComponentCompoundStabilityAnalysis"],
        "_3944": ["ConceptCouplingCompoundStabilityAnalysis"],
        "_3945": ["ConceptCouplingConnectionCompoundStabilityAnalysis"],
        "_3946": ["ConceptCouplingHalfCompoundStabilityAnalysis"],
        "_3947": ["ConceptGearCompoundStabilityAnalysis"],
        "_3948": ["ConceptGearMeshCompoundStabilityAnalysis"],
        "_3949": ["ConceptGearSetCompoundStabilityAnalysis"],
        "_3950": ["ConicalGearCompoundStabilityAnalysis"],
        "_3951": ["ConicalGearMeshCompoundStabilityAnalysis"],
        "_3952": ["ConicalGearSetCompoundStabilityAnalysis"],
        "_3953": ["ConnectionCompoundStabilityAnalysis"],
        "_3954": ["ConnectorCompoundStabilityAnalysis"],
        "_3955": ["CouplingCompoundStabilityAnalysis"],
        "_3956": ["CouplingConnectionCompoundStabilityAnalysis"],
        "_3957": ["CouplingHalfCompoundStabilityAnalysis"],
        "_3958": ["CVTBeltConnectionCompoundStabilityAnalysis"],
        "_3959": ["CVTCompoundStabilityAnalysis"],
        "_3960": ["CVTPulleyCompoundStabilityAnalysis"],
        "_3961": ["CycloidalAssemblyCompoundStabilityAnalysis"],
        "_3962": ["CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis"],
        "_3963": ["CycloidalDiscCompoundStabilityAnalysis"],
        "_3964": ["CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis"],
        "_3965": ["CylindricalGearCompoundStabilityAnalysis"],
        "_3966": ["CylindricalGearMeshCompoundStabilityAnalysis"],
        "_3967": ["CylindricalGearSetCompoundStabilityAnalysis"],
        "_3968": ["CylindricalPlanetGearCompoundStabilityAnalysis"],
        "_3969": ["DatumCompoundStabilityAnalysis"],
        "_3970": ["ExternalCADModelCompoundStabilityAnalysis"],
        "_3971": ["FaceGearCompoundStabilityAnalysis"],
        "_3972": ["FaceGearMeshCompoundStabilityAnalysis"],
        "_3973": ["FaceGearSetCompoundStabilityAnalysis"],
        "_3974": ["FEPartCompoundStabilityAnalysis"],
        "_3975": ["FlexiblePinAssemblyCompoundStabilityAnalysis"],
        "_3976": ["GearCompoundStabilityAnalysis"],
        "_3977": ["GearMeshCompoundStabilityAnalysis"],
        "_3978": ["GearSetCompoundStabilityAnalysis"],
        "_3979": ["GuideDxfModelCompoundStabilityAnalysis"],
        "_3980": ["HypoidGearCompoundStabilityAnalysis"],
        "_3981": ["HypoidGearMeshCompoundStabilityAnalysis"],
        "_3982": ["HypoidGearSetCompoundStabilityAnalysis"],
        "_3983": ["InterMountableComponentConnectionCompoundStabilityAnalysis"],
        "_3984": ["KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis"],
        "_3985": ["KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis"],
        "_3986": ["KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis"],
        "_3987": ["KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis"],
        "_3988": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis"],
        "_3989": ["KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis"],
        "_3990": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis"],
        "_3991": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ],
        "_3992": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ],
        "_3993": ["MassDiscCompoundStabilityAnalysis"],
        "_3994": ["MeasurementComponentCompoundStabilityAnalysis"],
        "_3995": ["MountableComponentCompoundStabilityAnalysis"],
        "_3996": ["OilSealCompoundStabilityAnalysis"],
        "_3997": ["PartCompoundStabilityAnalysis"],
        "_3998": ["PartToPartShearCouplingCompoundStabilityAnalysis"],
        "_3999": ["PartToPartShearCouplingConnectionCompoundStabilityAnalysis"],
        "_4000": ["PartToPartShearCouplingHalfCompoundStabilityAnalysis"],
        "_4001": ["PlanetaryConnectionCompoundStabilityAnalysis"],
        "_4002": ["PlanetaryGearSetCompoundStabilityAnalysis"],
        "_4003": ["PlanetCarrierCompoundStabilityAnalysis"],
        "_4004": ["PointLoadCompoundStabilityAnalysis"],
        "_4005": ["PowerLoadCompoundStabilityAnalysis"],
        "_4006": ["PulleyCompoundStabilityAnalysis"],
        "_4007": ["RingPinsCompoundStabilityAnalysis"],
        "_4008": ["RingPinsToDiscConnectionCompoundStabilityAnalysis"],
        "_4009": ["RollingRingAssemblyCompoundStabilityAnalysis"],
        "_4010": ["RollingRingCompoundStabilityAnalysis"],
        "_4011": ["RollingRingConnectionCompoundStabilityAnalysis"],
        "_4012": ["RootAssemblyCompoundStabilityAnalysis"],
        "_4013": ["ShaftCompoundStabilityAnalysis"],
        "_4014": ["ShaftHubConnectionCompoundStabilityAnalysis"],
        "_4015": ["ShaftToMountableComponentConnectionCompoundStabilityAnalysis"],
        "_4016": ["SpecialisedAssemblyCompoundStabilityAnalysis"],
        "_4017": ["SpiralBevelGearCompoundStabilityAnalysis"],
        "_4018": ["SpiralBevelGearMeshCompoundStabilityAnalysis"],
        "_4019": ["SpiralBevelGearSetCompoundStabilityAnalysis"],
        "_4020": ["SpringDamperCompoundStabilityAnalysis"],
        "_4021": ["SpringDamperConnectionCompoundStabilityAnalysis"],
        "_4022": ["SpringDamperHalfCompoundStabilityAnalysis"],
        "_4023": ["StraightBevelDiffGearCompoundStabilityAnalysis"],
        "_4024": ["StraightBevelDiffGearMeshCompoundStabilityAnalysis"],
        "_4025": ["StraightBevelDiffGearSetCompoundStabilityAnalysis"],
        "_4026": ["StraightBevelGearCompoundStabilityAnalysis"],
        "_4027": ["StraightBevelGearMeshCompoundStabilityAnalysis"],
        "_4028": ["StraightBevelGearSetCompoundStabilityAnalysis"],
        "_4029": ["StraightBevelPlanetGearCompoundStabilityAnalysis"],
        "_4030": ["StraightBevelSunGearCompoundStabilityAnalysis"],
        "_4031": ["SynchroniserCompoundStabilityAnalysis"],
        "_4032": ["SynchroniserHalfCompoundStabilityAnalysis"],
        "_4033": ["SynchroniserPartCompoundStabilityAnalysis"],
        "_4034": ["SynchroniserSleeveCompoundStabilityAnalysis"],
        "_4035": ["TorqueConverterCompoundStabilityAnalysis"],
        "_4036": ["TorqueConverterConnectionCompoundStabilityAnalysis"],
        "_4037": ["TorqueConverterPumpCompoundStabilityAnalysis"],
        "_4038": ["TorqueConverterTurbineCompoundStabilityAnalysis"],
        "_4039": ["UnbalancedMassCompoundStabilityAnalysis"],
        "_4040": ["VirtualComponentCompoundStabilityAnalysis"],
        "_4041": ["WormGearCompoundStabilityAnalysis"],
        "_4042": ["WormGearMeshCompoundStabilityAnalysis"],
        "_4043": ["WormGearSetCompoundStabilityAnalysis"],
        "_4044": ["ZerolBevelGearCompoundStabilityAnalysis"],
        "_4045": ["ZerolBevelGearMeshCompoundStabilityAnalysis"],
        "_4046": ["ZerolBevelGearSetCompoundStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundStabilityAnalysis",
    "AbstractShaftCompoundStabilityAnalysis",
    "AbstractShaftOrHousingCompoundStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
    "AssemblyCompoundStabilityAnalysis",
    "BearingCompoundStabilityAnalysis",
    "BeltConnectionCompoundStabilityAnalysis",
    "BeltDriveCompoundStabilityAnalysis",
    "BevelDifferentialGearCompoundStabilityAnalysis",
    "BevelDifferentialGearMeshCompoundStabilityAnalysis",
    "BevelDifferentialGearSetCompoundStabilityAnalysis",
    "BevelDifferentialPlanetGearCompoundStabilityAnalysis",
    "BevelDifferentialSunGearCompoundStabilityAnalysis",
    "BevelGearCompoundStabilityAnalysis",
    "BevelGearMeshCompoundStabilityAnalysis",
    "BevelGearSetCompoundStabilityAnalysis",
    "BoltCompoundStabilityAnalysis",
    "BoltedJointCompoundStabilityAnalysis",
    "ClutchCompoundStabilityAnalysis",
    "ClutchConnectionCompoundStabilityAnalysis",
    "ClutchHalfCompoundStabilityAnalysis",
    "CoaxialConnectionCompoundStabilityAnalysis",
    "ComponentCompoundStabilityAnalysis",
    "ConceptCouplingCompoundStabilityAnalysis",
    "ConceptCouplingConnectionCompoundStabilityAnalysis",
    "ConceptCouplingHalfCompoundStabilityAnalysis",
    "ConceptGearCompoundStabilityAnalysis",
    "ConceptGearMeshCompoundStabilityAnalysis",
    "ConceptGearSetCompoundStabilityAnalysis",
    "ConicalGearCompoundStabilityAnalysis",
    "ConicalGearMeshCompoundStabilityAnalysis",
    "ConicalGearSetCompoundStabilityAnalysis",
    "ConnectionCompoundStabilityAnalysis",
    "ConnectorCompoundStabilityAnalysis",
    "CouplingCompoundStabilityAnalysis",
    "CouplingConnectionCompoundStabilityAnalysis",
    "CouplingHalfCompoundStabilityAnalysis",
    "CVTBeltConnectionCompoundStabilityAnalysis",
    "CVTCompoundStabilityAnalysis",
    "CVTPulleyCompoundStabilityAnalysis",
    "CycloidalAssemblyCompoundStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
    "CycloidalDiscCompoundStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis",
    "CylindricalGearCompoundStabilityAnalysis",
    "CylindricalGearMeshCompoundStabilityAnalysis",
    "CylindricalGearSetCompoundStabilityAnalysis",
    "CylindricalPlanetGearCompoundStabilityAnalysis",
    "DatumCompoundStabilityAnalysis",
    "ExternalCADModelCompoundStabilityAnalysis",
    "FaceGearCompoundStabilityAnalysis",
    "FaceGearMeshCompoundStabilityAnalysis",
    "FaceGearSetCompoundStabilityAnalysis",
    "FEPartCompoundStabilityAnalysis",
    "FlexiblePinAssemblyCompoundStabilityAnalysis",
    "GearCompoundStabilityAnalysis",
    "GearMeshCompoundStabilityAnalysis",
    "GearSetCompoundStabilityAnalysis",
    "GuideDxfModelCompoundStabilityAnalysis",
    "HypoidGearCompoundStabilityAnalysis",
    "HypoidGearMeshCompoundStabilityAnalysis",
    "HypoidGearSetCompoundStabilityAnalysis",
    "InterMountableComponentConnectionCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
    "MassDiscCompoundStabilityAnalysis",
    "MeasurementComponentCompoundStabilityAnalysis",
    "MountableComponentCompoundStabilityAnalysis",
    "OilSealCompoundStabilityAnalysis",
    "PartCompoundStabilityAnalysis",
    "PartToPartShearCouplingCompoundStabilityAnalysis",
    "PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
    "PartToPartShearCouplingHalfCompoundStabilityAnalysis",
    "PlanetaryConnectionCompoundStabilityAnalysis",
    "PlanetaryGearSetCompoundStabilityAnalysis",
    "PlanetCarrierCompoundStabilityAnalysis",
    "PointLoadCompoundStabilityAnalysis",
    "PowerLoadCompoundStabilityAnalysis",
    "PulleyCompoundStabilityAnalysis",
    "RingPinsCompoundStabilityAnalysis",
    "RingPinsToDiscConnectionCompoundStabilityAnalysis",
    "RollingRingAssemblyCompoundStabilityAnalysis",
    "RollingRingCompoundStabilityAnalysis",
    "RollingRingConnectionCompoundStabilityAnalysis",
    "RootAssemblyCompoundStabilityAnalysis",
    "ShaftCompoundStabilityAnalysis",
    "ShaftHubConnectionCompoundStabilityAnalysis",
    "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "SpecialisedAssemblyCompoundStabilityAnalysis",
    "SpiralBevelGearCompoundStabilityAnalysis",
    "SpiralBevelGearMeshCompoundStabilityAnalysis",
    "SpiralBevelGearSetCompoundStabilityAnalysis",
    "SpringDamperCompoundStabilityAnalysis",
    "SpringDamperConnectionCompoundStabilityAnalysis",
    "SpringDamperHalfCompoundStabilityAnalysis",
    "StraightBevelDiffGearCompoundStabilityAnalysis",
    "StraightBevelDiffGearMeshCompoundStabilityAnalysis",
    "StraightBevelDiffGearSetCompoundStabilityAnalysis",
    "StraightBevelGearCompoundStabilityAnalysis",
    "StraightBevelGearMeshCompoundStabilityAnalysis",
    "StraightBevelGearSetCompoundStabilityAnalysis",
    "StraightBevelPlanetGearCompoundStabilityAnalysis",
    "StraightBevelSunGearCompoundStabilityAnalysis",
    "SynchroniserCompoundStabilityAnalysis",
    "SynchroniserHalfCompoundStabilityAnalysis",
    "SynchroniserPartCompoundStabilityAnalysis",
    "SynchroniserSleeveCompoundStabilityAnalysis",
    "TorqueConverterCompoundStabilityAnalysis",
    "TorqueConverterConnectionCompoundStabilityAnalysis",
    "TorqueConverterPumpCompoundStabilityAnalysis",
    "TorqueConverterTurbineCompoundStabilityAnalysis",
    "UnbalancedMassCompoundStabilityAnalysis",
    "VirtualComponentCompoundStabilityAnalysis",
    "WormGearCompoundStabilityAnalysis",
    "WormGearMeshCompoundStabilityAnalysis",
    "WormGearSetCompoundStabilityAnalysis",
    "ZerolBevelGearCompoundStabilityAnalysis",
    "ZerolBevelGearMeshCompoundStabilityAnalysis",
    "ZerolBevelGearSetCompoundStabilityAnalysis",
)
