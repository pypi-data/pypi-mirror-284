"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4053 import AbstractAssemblyPowerFlow
    from ._4054 import AbstractShaftOrHousingPowerFlow
    from ._4055 import AbstractShaftPowerFlow
    from ._4056 import AbstractShaftToMountableComponentConnectionPowerFlow
    from ._4057 import AGMAGleasonConicalGearMeshPowerFlow
    from ._4058 import AGMAGleasonConicalGearPowerFlow
    from ._4059 import AGMAGleasonConicalGearSetPowerFlow
    from ._4060 import AssemblyPowerFlow
    from ._4061 import BearingPowerFlow
    from ._4062 import BeltConnectionPowerFlow
    from ._4063 import BeltDrivePowerFlow
    from ._4064 import BevelDifferentialGearMeshPowerFlow
    from ._4065 import BevelDifferentialGearPowerFlow
    from ._4066 import BevelDifferentialGearSetPowerFlow
    from ._4067 import BevelDifferentialPlanetGearPowerFlow
    from ._4068 import BevelDifferentialSunGearPowerFlow
    from ._4069 import BevelGearMeshPowerFlow
    from ._4070 import BevelGearPowerFlow
    from ._4071 import BevelGearSetPowerFlow
    from ._4072 import BoltedJointPowerFlow
    from ._4073 import BoltPowerFlow
    from ._4074 import ClutchConnectionPowerFlow
    from ._4075 import ClutchHalfPowerFlow
    from ._4076 import ClutchPowerFlow
    from ._4077 import CoaxialConnectionPowerFlow
    from ._4078 import ComponentPowerFlow
    from ._4079 import ConceptCouplingConnectionPowerFlow
    from ._4080 import ConceptCouplingHalfPowerFlow
    from ._4081 import ConceptCouplingPowerFlow
    from ._4082 import ConceptGearMeshPowerFlow
    from ._4083 import ConceptGearPowerFlow
    from ._4084 import ConceptGearSetPowerFlow
    from ._4085 import ConicalGearMeshPowerFlow
    from ._4086 import ConicalGearPowerFlow
    from ._4087 import ConicalGearSetPowerFlow
    from ._4088 import ConnectionPowerFlow
    from ._4089 import ConnectorPowerFlow
    from ._4090 import CouplingConnectionPowerFlow
    from ._4091 import CouplingHalfPowerFlow
    from ._4092 import CouplingPowerFlow
    from ._4093 import CVTBeltConnectionPowerFlow
    from ._4094 import CVTPowerFlow
    from ._4095 import CVTPulleyPowerFlow
    from ._4096 import CycloidalAssemblyPowerFlow
    from ._4097 import CycloidalDiscCentralBearingConnectionPowerFlow
    from ._4098 import CycloidalDiscPlanetaryBearingConnectionPowerFlow
    from ._4099 import CycloidalDiscPowerFlow
    from ._4100 import CylindricalGearGeometricEntityDrawStyle
    from ._4101 import CylindricalGearMeshPowerFlow
    from ._4102 import CylindricalGearPowerFlow
    from ._4103 import CylindricalGearSetPowerFlow
    from ._4104 import CylindricalPlanetGearPowerFlow
    from ._4105 import DatumPowerFlow
    from ._4106 import ExternalCADModelPowerFlow
    from ._4107 import FaceGearMeshPowerFlow
    from ._4108 import FaceGearPowerFlow
    from ._4109 import FaceGearSetPowerFlow
    from ._4110 import FastPowerFlow
    from ._4111 import FastPowerFlowSolution
    from ._4112 import FEPartPowerFlow
    from ._4113 import FlexiblePinAssemblyPowerFlow
    from ._4114 import GearMeshPowerFlow
    from ._4115 import GearPowerFlow
    from ._4116 import GearSetPowerFlow
    from ._4117 import GuideDxfModelPowerFlow
    from ._4118 import HypoidGearMeshPowerFlow
    from ._4119 import HypoidGearPowerFlow
    from ._4120 import HypoidGearSetPowerFlow
    from ._4121 import InterMountableComponentConnectionPowerFlow
    from ._4122 import KlingelnbergCycloPalloidConicalGearMeshPowerFlow
    from ._4123 import KlingelnbergCycloPalloidConicalGearPowerFlow
    from ._4124 import KlingelnbergCycloPalloidConicalGearSetPowerFlow
    from ._4125 import KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
    from ._4126 import KlingelnbergCycloPalloidHypoidGearPowerFlow
    from ._4127 import KlingelnbergCycloPalloidHypoidGearSetPowerFlow
    from ._4128 import KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
    from ._4129 import KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
    from ._4130 import KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
    from ._4131 import MassDiscPowerFlow
    from ._4132 import MeasurementComponentPowerFlow
    from ._4133 import MountableComponentPowerFlow
    from ._4134 import OilSealPowerFlow
    from ._4135 import PartPowerFlow
    from ._4136 import PartToPartShearCouplingConnectionPowerFlow
    from ._4137 import PartToPartShearCouplingHalfPowerFlow
    from ._4138 import PartToPartShearCouplingPowerFlow
    from ._4139 import PlanetaryConnectionPowerFlow
    from ._4140 import PlanetaryGearSetPowerFlow
    from ._4141 import PlanetCarrierPowerFlow
    from ._4142 import PointLoadPowerFlow
    from ._4143 import PowerFlow
    from ._4144 import PowerFlowDrawStyle
    from ._4145 import PowerLoadPowerFlow
    from ._4146 import PulleyPowerFlow
    from ._4147 import RingPinsPowerFlow
    from ._4148 import RingPinsToDiscConnectionPowerFlow
    from ._4149 import RollingRingAssemblyPowerFlow
    from ._4150 import RollingRingConnectionPowerFlow
    from ._4151 import RollingRingPowerFlow
    from ._4152 import RootAssemblyPowerFlow
    from ._4153 import ShaftHubConnectionPowerFlow
    from ._4154 import ShaftPowerFlow
    from ._4155 import ShaftToMountableComponentConnectionPowerFlow
    from ._4156 import SpecialisedAssemblyPowerFlow
    from ._4157 import SpiralBevelGearMeshPowerFlow
    from ._4158 import SpiralBevelGearPowerFlow
    from ._4159 import SpiralBevelGearSetPowerFlow
    from ._4160 import SpringDamperConnectionPowerFlow
    from ._4161 import SpringDamperHalfPowerFlow
    from ._4162 import SpringDamperPowerFlow
    from ._4163 import StraightBevelDiffGearMeshPowerFlow
    from ._4164 import StraightBevelDiffGearPowerFlow
    from ._4165 import StraightBevelDiffGearSetPowerFlow
    from ._4166 import StraightBevelGearMeshPowerFlow
    from ._4167 import StraightBevelGearPowerFlow
    from ._4168 import StraightBevelGearSetPowerFlow
    from ._4169 import StraightBevelPlanetGearPowerFlow
    from ._4170 import StraightBevelSunGearPowerFlow
    from ._4171 import SynchroniserHalfPowerFlow
    from ._4172 import SynchroniserPartPowerFlow
    from ._4173 import SynchroniserPowerFlow
    from ._4174 import SynchroniserSleevePowerFlow
    from ._4175 import ToothPassingHarmonic
    from ._4176 import TorqueConverterConnectionPowerFlow
    from ._4177 import TorqueConverterPowerFlow
    from ._4178 import TorqueConverterPumpPowerFlow
    from ._4179 import TorqueConverterTurbinePowerFlow
    from ._4180 import UnbalancedMassPowerFlow
    from ._4181 import VirtualComponentPowerFlow
    from ._4182 import WormGearMeshPowerFlow
    from ._4183 import WormGearPowerFlow
    from ._4184 import WormGearSetPowerFlow
    from ._4185 import ZerolBevelGearMeshPowerFlow
    from ._4186 import ZerolBevelGearPowerFlow
    from ._4187 import ZerolBevelGearSetPowerFlow
else:
    import_structure = {
        "_4053": ["AbstractAssemblyPowerFlow"],
        "_4054": ["AbstractShaftOrHousingPowerFlow"],
        "_4055": ["AbstractShaftPowerFlow"],
        "_4056": ["AbstractShaftToMountableComponentConnectionPowerFlow"],
        "_4057": ["AGMAGleasonConicalGearMeshPowerFlow"],
        "_4058": ["AGMAGleasonConicalGearPowerFlow"],
        "_4059": ["AGMAGleasonConicalGearSetPowerFlow"],
        "_4060": ["AssemblyPowerFlow"],
        "_4061": ["BearingPowerFlow"],
        "_4062": ["BeltConnectionPowerFlow"],
        "_4063": ["BeltDrivePowerFlow"],
        "_4064": ["BevelDifferentialGearMeshPowerFlow"],
        "_4065": ["BevelDifferentialGearPowerFlow"],
        "_4066": ["BevelDifferentialGearSetPowerFlow"],
        "_4067": ["BevelDifferentialPlanetGearPowerFlow"],
        "_4068": ["BevelDifferentialSunGearPowerFlow"],
        "_4069": ["BevelGearMeshPowerFlow"],
        "_4070": ["BevelGearPowerFlow"],
        "_4071": ["BevelGearSetPowerFlow"],
        "_4072": ["BoltedJointPowerFlow"],
        "_4073": ["BoltPowerFlow"],
        "_4074": ["ClutchConnectionPowerFlow"],
        "_4075": ["ClutchHalfPowerFlow"],
        "_4076": ["ClutchPowerFlow"],
        "_4077": ["CoaxialConnectionPowerFlow"],
        "_4078": ["ComponentPowerFlow"],
        "_4079": ["ConceptCouplingConnectionPowerFlow"],
        "_4080": ["ConceptCouplingHalfPowerFlow"],
        "_4081": ["ConceptCouplingPowerFlow"],
        "_4082": ["ConceptGearMeshPowerFlow"],
        "_4083": ["ConceptGearPowerFlow"],
        "_4084": ["ConceptGearSetPowerFlow"],
        "_4085": ["ConicalGearMeshPowerFlow"],
        "_4086": ["ConicalGearPowerFlow"],
        "_4087": ["ConicalGearSetPowerFlow"],
        "_4088": ["ConnectionPowerFlow"],
        "_4089": ["ConnectorPowerFlow"],
        "_4090": ["CouplingConnectionPowerFlow"],
        "_4091": ["CouplingHalfPowerFlow"],
        "_4092": ["CouplingPowerFlow"],
        "_4093": ["CVTBeltConnectionPowerFlow"],
        "_4094": ["CVTPowerFlow"],
        "_4095": ["CVTPulleyPowerFlow"],
        "_4096": ["CycloidalAssemblyPowerFlow"],
        "_4097": ["CycloidalDiscCentralBearingConnectionPowerFlow"],
        "_4098": ["CycloidalDiscPlanetaryBearingConnectionPowerFlow"],
        "_4099": ["CycloidalDiscPowerFlow"],
        "_4100": ["CylindricalGearGeometricEntityDrawStyle"],
        "_4101": ["CylindricalGearMeshPowerFlow"],
        "_4102": ["CylindricalGearPowerFlow"],
        "_4103": ["CylindricalGearSetPowerFlow"],
        "_4104": ["CylindricalPlanetGearPowerFlow"],
        "_4105": ["DatumPowerFlow"],
        "_4106": ["ExternalCADModelPowerFlow"],
        "_4107": ["FaceGearMeshPowerFlow"],
        "_4108": ["FaceGearPowerFlow"],
        "_4109": ["FaceGearSetPowerFlow"],
        "_4110": ["FastPowerFlow"],
        "_4111": ["FastPowerFlowSolution"],
        "_4112": ["FEPartPowerFlow"],
        "_4113": ["FlexiblePinAssemblyPowerFlow"],
        "_4114": ["GearMeshPowerFlow"],
        "_4115": ["GearPowerFlow"],
        "_4116": ["GearSetPowerFlow"],
        "_4117": ["GuideDxfModelPowerFlow"],
        "_4118": ["HypoidGearMeshPowerFlow"],
        "_4119": ["HypoidGearPowerFlow"],
        "_4120": ["HypoidGearSetPowerFlow"],
        "_4121": ["InterMountableComponentConnectionPowerFlow"],
        "_4122": ["KlingelnbergCycloPalloidConicalGearMeshPowerFlow"],
        "_4123": ["KlingelnbergCycloPalloidConicalGearPowerFlow"],
        "_4124": ["KlingelnbergCycloPalloidConicalGearSetPowerFlow"],
        "_4125": ["KlingelnbergCycloPalloidHypoidGearMeshPowerFlow"],
        "_4126": ["KlingelnbergCycloPalloidHypoidGearPowerFlow"],
        "_4127": ["KlingelnbergCycloPalloidHypoidGearSetPowerFlow"],
        "_4128": ["KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow"],
        "_4129": ["KlingelnbergCycloPalloidSpiralBevelGearPowerFlow"],
        "_4130": ["KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow"],
        "_4131": ["MassDiscPowerFlow"],
        "_4132": ["MeasurementComponentPowerFlow"],
        "_4133": ["MountableComponentPowerFlow"],
        "_4134": ["OilSealPowerFlow"],
        "_4135": ["PartPowerFlow"],
        "_4136": ["PartToPartShearCouplingConnectionPowerFlow"],
        "_4137": ["PartToPartShearCouplingHalfPowerFlow"],
        "_4138": ["PartToPartShearCouplingPowerFlow"],
        "_4139": ["PlanetaryConnectionPowerFlow"],
        "_4140": ["PlanetaryGearSetPowerFlow"],
        "_4141": ["PlanetCarrierPowerFlow"],
        "_4142": ["PointLoadPowerFlow"],
        "_4143": ["PowerFlow"],
        "_4144": ["PowerFlowDrawStyle"],
        "_4145": ["PowerLoadPowerFlow"],
        "_4146": ["PulleyPowerFlow"],
        "_4147": ["RingPinsPowerFlow"],
        "_4148": ["RingPinsToDiscConnectionPowerFlow"],
        "_4149": ["RollingRingAssemblyPowerFlow"],
        "_4150": ["RollingRingConnectionPowerFlow"],
        "_4151": ["RollingRingPowerFlow"],
        "_4152": ["RootAssemblyPowerFlow"],
        "_4153": ["ShaftHubConnectionPowerFlow"],
        "_4154": ["ShaftPowerFlow"],
        "_4155": ["ShaftToMountableComponentConnectionPowerFlow"],
        "_4156": ["SpecialisedAssemblyPowerFlow"],
        "_4157": ["SpiralBevelGearMeshPowerFlow"],
        "_4158": ["SpiralBevelGearPowerFlow"],
        "_4159": ["SpiralBevelGearSetPowerFlow"],
        "_4160": ["SpringDamperConnectionPowerFlow"],
        "_4161": ["SpringDamperHalfPowerFlow"],
        "_4162": ["SpringDamperPowerFlow"],
        "_4163": ["StraightBevelDiffGearMeshPowerFlow"],
        "_4164": ["StraightBevelDiffGearPowerFlow"],
        "_4165": ["StraightBevelDiffGearSetPowerFlow"],
        "_4166": ["StraightBevelGearMeshPowerFlow"],
        "_4167": ["StraightBevelGearPowerFlow"],
        "_4168": ["StraightBevelGearSetPowerFlow"],
        "_4169": ["StraightBevelPlanetGearPowerFlow"],
        "_4170": ["StraightBevelSunGearPowerFlow"],
        "_4171": ["SynchroniserHalfPowerFlow"],
        "_4172": ["SynchroniserPartPowerFlow"],
        "_4173": ["SynchroniserPowerFlow"],
        "_4174": ["SynchroniserSleevePowerFlow"],
        "_4175": ["ToothPassingHarmonic"],
        "_4176": ["TorqueConverterConnectionPowerFlow"],
        "_4177": ["TorqueConverterPowerFlow"],
        "_4178": ["TorqueConverterPumpPowerFlow"],
        "_4179": ["TorqueConverterTurbinePowerFlow"],
        "_4180": ["UnbalancedMassPowerFlow"],
        "_4181": ["VirtualComponentPowerFlow"],
        "_4182": ["WormGearMeshPowerFlow"],
        "_4183": ["WormGearPowerFlow"],
        "_4184": ["WormGearSetPowerFlow"],
        "_4185": ["ZerolBevelGearMeshPowerFlow"],
        "_4186": ["ZerolBevelGearPowerFlow"],
        "_4187": ["ZerolBevelGearSetPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyPowerFlow",
    "AbstractShaftOrHousingPowerFlow",
    "AbstractShaftPowerFlow",
    "AbstractShaftToMountableComponentConnectionPowerFlow",
    "AGMAGleasonConicalGearMeshPowerFlow",
    "AGMAGleasonConicalGearPowerFlow",
    "AGMAGleasonConicalGearSetPowerFlow",
    "AssemblyPowerFlow",
    "BearingPowerFlow",
    "BeltConnectionPowerFlow",
    "BeltDrivePowerFlow",
    "BevelDifferentialGearMeshPowerFlow",
    "BevelDifferentialGearPowerFlow",
    "BevelDifferentialGearSetPowerFlow",
    "BevelDifferentialPlanetGearPowerFlow",
    "BevelDifferentialSunGearPowerFlow",
    "BevelGearMeshPowerFlow",
    "BevelGearPowerFlow",
    "BevelGearSetPowerFlow",
    "BoltedJointPowerFlow",
    "BoltPowerFlow",
    "ClutchConnectionPowerFlow",
    "ClutchHalfPowerFlow",
    "ClutchPowerFlow",
    "CoaxialConnectionPowerFlow",
    "ComponentPowerFlow",
    "ConceptCouplingConnectionPowerFlow",
    "ConceptCouplingHalfPowerFlow",
    "ConceptCouplingPowerFlow",
    "ConceptGearMeshPowerFlow",
    "ConceptGearPowerFlow",
    "ConceptGearSetPowerFlow",
    "ConicalGearMeshPowerFlow",
    "ConicalGearPowerFlow",
    "ConicalGearSetPowerFlow",
    "ConnectionPowerFlow",
    "ConnectorPowerFlow",
    "CouplingConnectionPowerFlow",
    "CouplingHalfPowerFlow",
    "CouplingPowerFlow",
    "CVTBeltConnectionPowerFlow",
    "CVTPowerFlow",
    "CVTPulleyPowerFlow",
    "CycloidalAssemblyPowerFlow",
    "CycloidalDiscCentralBearingConnectionPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionPowerFlow",
    "CycloidalDiscPowerFlow",
    "CylindricalGearGeometricEntityDrawStyle",
    "CylindricalGearMeshPowerFlow",
    "CylindricalGearPowerFlow",
    "CylindricalGearSetPowerFlow",
    "CylindricalPlanetGearPowerFlow",
    "DatumPowerFlow",
    "ExternalCADModelPowerFlow",
    "FaceGearMeshPowerFlow",
    "FaceGearPowerFlow",
    "FaceGearSetPowerFlow",
    "FastPowerFlow",
    "FastPowerFlowSolution",
    "FEPartPowerFlow",
    "FlexiblePinAssemblyPowerFlow",
    "GearMeshPowerFlow",
    "GearPowerFlow",
    "GearSetPowerFlow",
    "GuideDxfModelPowerFlow",
    "HypoidGearMeshPowerFlow",
    "HypoidGearPowerFlow",
    "HypoidGearSetPowerFlow",
    "InterMountableComponentConnectionPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
    "KlingelnbergCycloPalloidConicalGearPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
    "MassDiscPowerFlow",
    "MeasurementComponentPowerFlow",
    "MountableComponentPowerFlow",
    "OilSealPowerFlow",
    "PartPowerFlow",
    "PartToPartShearCouplingConnectionPowerFlow",
    "PartToPartShearCouplingHalfPowerFlow",
    "PartToPartShearCouplingPowerFlow",
    "PlanetaryConnectionPowerFlow",
    "PlanetaryGearSetPowerFlow",
    "PlanetCarrierPowerFlow",
    "PointLoadPowerFlow",
    "PowerFlow",
    "PowerFlowDrawStyle",
    "PowerLoadPowerFlow",
    "PulleyPowerFlow",
    "RingPinsPowerFlow",
    "RingPinsToDiscConnectionPowerFlow",
    "RollingRingAssemblyPowerFlow",
    "RollingRingConnectionPowerFlow",
    "RollingRingPowerFlow",
    "RootAssemblyPowerFlow",
    "ShaftHubConnectionPowerFlow",
    "ShaftPowerFlow",
    "ShaftToMountableComponentConnectionPowerFlow",
    "SpecialisedAssemblyPowerFlow",
    "SpiralBevelGearMeshPowerFlow",
    "SpiralBevelGearPowerFlow",
    "SpiralBevelGearSetPowerFlow",
    "SpringDamperConnectionPowerFlow",
    "SpringDamperHalfPowerFlow",
    "SpringDamperPowerFlow",
    "StraightBevelDiffGearMeshPowerFlow",
    "StraightBevelDiffGearPowerFlow",
    "StraightBevelDiffGearSetPowerFlow",
    "StraightBevelGearMeshPowerFlow",
    "StraightBevelGearPowerFlow",
    "StraightBevelGearSetPowerFlow",
    "StraightBevelPlanetGearPowerFlow",
    "StraightBevelSunGearPowerFlow",
    "SynchroniserHalfPowerFlow",
    "SynchroniserPartPowerFlow",
    "SynchroniserPowerFlow",
    "SynchroniserSleevePowerFlow",
    "ToothPassingHarmonic",
    "TorqueConverterConnectionPowerFlow",
    "TorqueConverterPowerFlow",
    "TorqueConverterPumpPowerFlow",
    "TorqueConverterTurbinePowerFlow",
    "UnbalancedMassPowerFlow",
    "VirtualComponentPowerFlow",
    "WormGearMeshPowerFlow",
    "WormGearPowerFlow",
    "WormGearSetPowerFlow",
    "ZerolBevelGearMeshPowerFlow",
    "ZerolBevelGearPowerFlow",
    "ZerolBevelGearSetPowerFlow",
)
