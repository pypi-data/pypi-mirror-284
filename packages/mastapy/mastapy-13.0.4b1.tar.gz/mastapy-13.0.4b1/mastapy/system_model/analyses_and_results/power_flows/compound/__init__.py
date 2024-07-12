"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4188 import AbstractAssemblyCompoundPowerFlow
    from ._4189 import AbstractShaftCompoundPowerFlow
    from ._4190 import AbstractShaftOrHousingCompoundPowerFlow
    from ._4191 import AbstractShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4192 import AGMAGleasonConicalGearCompoundPowerFlow
    from ._4193 import AGMAGleasonConicalGearMeshCompoundPowerFlow
    from ._4194 import AGMAGleasonConicalGearSetCompoundPowerFlow
    from ._4195 import AssemblyCompoundPowerFlow
    from ._4196 import BearingCompoundPowerFlow
    from ._4197 import BeltConnectionCompoundPowerFlow
    from ._4198 import BeltDriveCompoundPowerFlow
    from ._4199 import BevelDifferentialGearCompoundPowerFlow
    from ._4200 import BevelDifferentialGearMeshCompoundPowerFlow
    from ._4201 import BevelDifferentialGearSetCompoundPowerFlow
    from ._4202 import BevelDifferentialPlanetGearCompoundPowerFlow
    from ._4203 import BevelDifferentialSunGearCompoundPowerFlow
    from ._4204 import BevelGearCompoundPowerFlow
    from ._4205 import BevelGearMeshCompoundPowerFlow
    from ._4206 import BevelGearSetCompoundPowerFlow
    from ._4207 import BoltCompoundPowerFlow
    from ._4208 import BoltedJointCompoundPowerFlow
    from ._4209 import ClutchCompoundPowerFlow
    from ._4210 import ClutchConnectionCompoundPowerFlow
    from ._4211 import ClutchHalfCompoundPowerFlow
    from ._4212 import CoaxialConnectionCompoundPowerFlow
    from ._4213 import ComponentCompoundPowerFlow
    from ._4214 import ConceptCouplingCompoundPowerFlow
    from ._4215 import ConceptCouplingConnectionCompoundPowerFlow
    from ._4216 import ConceptCouplingHalfCompoundPowerFlow
    from ._4217 import ConceptGearCompoundPowerFlow
    from ._4218 import ConceptGearMeshCompoundPowerFlow
    from ._4219 import ConceptGearSetCompoundPowerFlow
    from ._4220 import ConicalGearCompoundPowerFlow
    from ._4221 import ConicalGearMeshCompoundPowerFlow
    from ._4222 import ConicalGearSetCompoundPowerFlow
    from ._4223 import ConnectionCompoundPowerFlow
    from ._4224 import ConnectorCompoundPowerFlow
    from ._4225 import CouplingCompoundPowerFlow
    from ._4226 import CouplingConnectionCompoundPowerFlow
    from ._4227 import CouplingHalfCompoundPowerFlow
    from ._4228 import CVTBeltConnectionCompoundPowerFlow
    from ._4229 import CVTCompoundPowerFlow
    from ._4230 import CVTPulleyCompoundPowerFlow
    from ._4231 import CycloidalAssemblyCompoundPowerFlow
    from ._4232 import CycloidalDiscCentralBearingConnectionCompoundPowerFlow
    from ._4233 import CycloidalDiscCompoundPowerFlow
    from ._4234 import CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
    from ._4235 import CylindricalGearCompoundPowerFlow
    from ._4236 import CylindricalGearMeshCompoundPowerFlow
    from ._4237 import CylindricalGearSetCompoundPowerFlow
    from ._4238 import CylindricalPlanetGearCompoundPowerFlow
    from ._4239 import DatumCompoundPowerFlow
    from ._4240 import ExternalCADModelCompoundPowerFlow
    from ._4241 import FaceGearCompoundPowerFlow
    from ._4242 import FaceGearMeshCompoundPowerFlow
    from ._4243 import FaceGearSetCompoundPowerFlow
    from ._4244 import FEPartCompoundPowerFlow
    from ._4245 import FlexiblePinAssemblyCompoundPowerFlow
    from ._4246 import GearCompoundPowerFlow
    from ._4247 import GearMeshCompoundPowerFlow
    from ._4248 import GearSetCompoundPowerFlow
    from ._4249 import GuideDxfModelCompoundPowerFlow
    from ._4250 import HypoidGearCompoundPowerFlow
    from ._4251 import HypoidGearMeshCompoundPowerFlow
    from ._4252 import HypoidGearSetCompoundPowerFlow
    from ._4253 import InterMountableComponentConnectionCompoundPowerFlow
    from ._4254 import KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
    from ._4255 import KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
    from ._4256 import KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
    from ._4257 import KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
    from ._4258 import KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
    from ._4259 import KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
    from ._4260 import KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
    from ._4261 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
    from ._4262 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
    from ._4263 import MassDiscCompoundPowerFlow
    from ._4264 import MeasurementComponentCompoundPowerFlow
    from ._4265 import MountableComponentCompoundPowerFlow
    from ._4266 import OilSealCompoundPowerFlow
    from ._4267 import PartCompoundPowerFlow
    from ._4268 import PartToPartShearCouplingCompoundPowerFlow
    from ._4269 import PartToPartShearCouplingConnectionCompoundPowerFlow
    from ._4270 import PartToPartShearCouplingHalfCompoundPowerFlow
    from ._4271 import PlanetaryConnectionCompoundPowerFlow
    from ._4272 import PlanetaryGearSetCompoundPowerFlow
    from ._4273 import PlanetCarrierCompoundPowerFlow
    from ._4274 import PointLoadCompoundPowerFlow
    from ._4275 import PowerLoadCompoundPowerFlow
    from ._4276 import PulleyCompoundPowerFlow
    from ._4277 import RingPinsCompoundPowerFlow
    from ._4278 import RingPinsToDiscConnectionCompoundPowerFlow
    from ._4279 import RollingRingAssemblyCompoundPowerFlow
    from ._4280 import RollingRingCompoundPowerFlow
    from ._4281 import RollingRingConnectionCompoundPowerFlow
    from ._4282 import RootAssemblyCompoundPowerFlow
    from ._4283 import ShaftCompoundPowerFlow
    from ._4284 import ShaftHubConnectionCompoundPowerFlow
    from ._4285 import ShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4286 import SpecialisedAssemblyCompoundPowerFlow
    from ._4287 import SpiralBevelGearCompoundPowerFlow
    from ._4288 import SpiralBevelGearMeshCompoundPowerFlow
    from ._4289 import SpiralBevelGearSetCompoundPowerFlow
    from ._4290 import SpringDamperCompoundPowerFlow
    from ._4291 import SpringDamperConnectionCompoundPowerFlow
    from ._4292 import SpringDamperHalfCompoundPowerFlow
    from ._4293 import StraightBevelDiffGearCompoundPowerFlow
    from ._4294 import StraightBevelDiffGearMeshCompoundPowerFlow
    from ._4295 import StraightBevelDiffGearSetCompoundPowerFlow
    from ._4296 import StraightBevelGearCompoundPowerFlow
    from ._4297 import StraightBevelGearMeshCompoundPowerFlow
    from ._4298 import StraightBevelGearSetCompoundPowerFlow
    from ._4299 import StraightBevelPlanetGearCompoundPowerFlow
    from ._4300 import StraightBevelSunGearCompoundPowerFlow
    from ._4301 import SynchroniserCompoundPowerFlow
    from ._4302 import SynchroniserHalfCompoundPowerFlow
    from ._4303 import SynchroniserPartCompoundPowerFlow
    from ._4304 import SynchroniserSleeveCompoundPowerFlow
    from ._4305 import TorqueConverterCompoundPowerFlow
    from ._4306 import TorqueConverterConnectionCompoundPowerFlow
    from ._4307 import TorqueConverterPumpCompoundPowerFlow
    from ._4308 import TorqueConverterTurbineCompoundPowerFlow
    from ._4309 import UnbalancedMassCompoundPowerFlow
    from ._4310 import VirtualComponentCompoundPowerFlow
    from ._4311 import WormGearCompoundPowerFlow
    from ._4312 import WormGearMeshCompoundPowerFlow
    from ._4313 import WormGearSetCompoundPowerFlow
    from ._4314 import ZerolBevelGearCompoundPowerFlow
    from ._4315 import ZerolBevelGearMeshCompoundPowerFlow
    from ._4316 import ZerolBevelGearSetCompoundPowerFlow
else:
    import_structure = {
        "_4188": ["AbstractAssemblyCompoundPowerFlow"],
        "_4189": ["AbstractShaftCompoundPowerFlow"],
        "_4190": ["AbstractShaftOrHousingCompoundPowerFlow"],
        "_4191": ["AbstractShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4192": ["AGMAGleasonConicalGearCompoundPowerFlow"],
        "_4193": ["AGMAGleasonConicalGearMeshCompoundPowerFlow"],
        "_4194": ["AGMAGleasonConicalGearSetCompoundPowerFlow"],
        "_4195": ["AssemblyCompoundPowerFlow"],
        "_4196": ["BearingCompoundPowerFlow"],
        "_4197": ["BeltConnectionCompoundPowerFlow"],
        "_4198": ["BeltDriveCompoundPowerFlow"],
        "_4199": ["BevelDifferentialGearCompoundPowerFlow"],
        "_4200": ["BevelDifferentialGearMeshCompoundPowerFlow"],
        "_4201": ["BevelDifferentialGearSetCompoundPowerFlow"],
        "_4202": ["BevelDifferentialPlanetGearCompoundPowerFlow"],
        "_4203": ["BevelDifferentialSunGearCompoundPowerFlow"],
        "_4204": ["BevelGearCompoundPowerFlow"],
        "_4205": ["BevelGearMeshCompoundPowerFlow"],
        "_4206": ["BevelGearSetCompoundPowerFlow"],
        "_4207": ["BoltCompoundPowerFlow"],
        "_4208": ["BoltedJointCompoundPowerFlow"],
        "_4209": ["ClutchCompoundPowerFlow"],
        "_4210": ["ClutchConnectionCompoundPowerFlow"],
        "_4211": ["ClutchHalfCompoundPowerFlow"],
        "_4212": ["CoaxialConnectionCompoundPowerFlow"],
        "_4213": ["ComponentCompoundPowerFlow"],
        "_4214": ["ConceptCouplingCompoundPowerFlow"],
        "_4215": ["ConceptCouplingConnectionCompoundPowerFlow"],
        "_4216": ["ConceptCouplingHalfCompoundPowerFlow"],
        "_4217": ["ConceptGearCompoundPowerFlow"],
        "_4218": ["ConceptGearMeshCompoundPowerFlow"],
        "_4219": ["ConceptGearSetCompoundPowerFlow"],
        "_4220": ["ConicalGearCompoundPowerFlow"],
        "_4221": ["ConicalGearMeshCompoundPowerFlow"],
        "_4222": ["ConicalGearSetCompoundPowerFlow"],
        "_4223": ["ConnectionCompoundPowerFlow"],
        "_4224": ["ConnectorCompoundPowerFlow"],
        "_4225": ["CouplingCompoundPowerFlow"],
        "_4226": ["CouplingConnectionCompoundPowerFlow"],
        "_4227": ["CouplingHalfCompoundPowerFlow"],
        "_4228": ["CVTBeltConnectionCompoundPowerFlow"],
        "_4229": ["CVTCompoundPowerFlow"],
        "_4230": ["CVTPulleyCompoundPowerFlow"],
        "_4231": ["CycloidalAssemblyCompoundPowerFlow"],
        "_4232": ["CycloidalDiscCentralBearingConnectionCompoundPowerFlow"],
        "_4233": ["CycloidalDiscCompoundPowerFlow"],
        "_4234": ["CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow"],
        "_4235": ["CylindricalGearCompoundPowerFlow"],
        "_4236": ["CylindricalGearMeshCompoundPowerFlow"],
        "_4237": ["CylindricalGearSetCompoundPowerFlow"],
        "_4238": ["CylindricalPlanetGearCompoundPowerFlow"],
        "_4239": ["DatumCompoundPowerFlow"],
        "_4240": ["ExternalCADModelCompoundPowerFlow"],
        "_4241": ["FaceGearCompoundPowerFlow"],
        "_4242": ["FaceGearMeshCompoundPowerFlow"],
        "_4243": ["FaceGearSetCompoundPowerFlow"],
        "_4244": ["FEPartCompoundPowerFlow"],
        "_4245": ["FlexiblePinAssemblyCompoundPowerFlow"],
        "_4246": ["GearCompoundPowerFlow"],
        "_4247": ["GearMeshCompoundPowerFlow"],
        "_4248": ["GearSetCompoundPowerFlow"],
        "_4249": ["GuideDxfModelCompoundPowerFlow"],
        "_4250": ["HypoidGearCompoundPowerFlow"],
        "_4251": ["HypoidGearMeshCompoundPowerFlow"],
        "_4252": ["HypoidGearSetCompoundPowerFlow"],
        "_4253": ["InterMountableComponentConnectionCompoundPowerFlow"],
        "_4254": ["KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"],
        "_4255": ["KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow"],
        "_4256": ["KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow"],
        "_4257": ["KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow"],
        "_4258": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow"],
        "_4259": ["KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow"],
        "_4260": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow"],
        "_4261": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow"],
        "_4262": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow"],
        "_4263": ["MassDiscCompoundPowerFlow"],
        "_4264": ["MeasurementComponentCompoundPowerFlow"],
        "_4265": ["MountableComponentCompoundPowerFlow"],
        "_4266": ["OilSealCompoundPowerFlow"],
        "_4267": ["PartCompoundPowerFlow"],
        "_4268": ["PartToPartShearCouplingCompoundPowerFlow"],
        "_4269": ["PartToPartShearCouplingConnectionCompoundPowerFlow"],
        "_4270": ["PartToPartShearCouplingHalfCompoundPowerFlow"],
        "_4271": ["PlanetaryConnectionCompoundPowerFlow"],
        "_4272": ["PlanetaryGearSetCompoundPowerFlow"],
        "_4273": ["PlanetCarrierCompoundPowerFlow"],
        "_4274": ["PointLoadCompoundPowerFlow"],
        "_4275": ["PowerLoadCompoundPowerFlow"],
        "_4276": ["PulleyCompoundPowerFlow"],
        "_4277": ["RingPinsCompoundPowerFlow"],
        "_4278": ["RingPinsToDiscConnectionCompoundPowerFlow"],
        "_4279": ["RollingRingAssemblyCompoundPowerFlow"],
        "_4280": ["RollingRingCompoundPowerFlow"],
        "_4281": ["RollingRingConnectionCompoundPowerFlow"],
        "_4282": ["RootAssemblyCompoundPowerFlow"],
        "_4283": ["ShaftCompoundPowerFlow"],
        "_4284": ["ShaftHubConnectionCompoundPowerFlow"],
        "_4285": ["ShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4286": ["SpecialisedAssemblyCompoundPowerFlow"],
        "_4287": ["SpiralBevelGearCompoundPowerFlow"],
        "_4288": ["SpiralBevelGearMeshCompoundPowerFlow"],
        "_4289": ["SpiralBevelGearSetCompoundPowerFlow"],
        "_4290": ["SpringDamperCompoundPowerFlow"],
        "_4291": ["SpringDamperConnectionCompoundPowerFlow"],
        "_4292": ["SpringDamperHalfCompoundPowerFlow"],
        "_4293": ["StraightBevelDiffGearCompoundPowerFlow"],
        "_4294": ["StraightBevelDiffGearMeshCompoundPowerFlow"],
        "_4295": ["StraightBevelDiffGearSetCompoundPowerFlow"],
        "_4296": ["StraightBevelGearCompoundPowerFlow"],
        "_4297": ["StraightBevelGearMeshCompoundPowerFlow"],
        "_4298": ["StraightBevelGearSetCompoundPowerFlow"],
        "_4299": ["StraightBevelPlanetGearCompoundPowerFlow"],
        "_4300": ["StraightBevelSunGearCompoundPowerFlow"],
        "_4301": ["SynchroniserCompoundPowerFlow"],
        "_4302": ["SynchroniserHalfCompoundPowerFlow"],
        "_4303": ["SynchroniserPartCompoundPowerFlow"],
        "_4304": ["SynchroniserSleeveCompoundPowerFlow"],
        "_4305": ["TorqueConverterCompoundPowerFlow"],
        "_4306": ["TorqueConverterConnectionCompoundPowerFlow"],
        "_4307": ["TorqueConverterPumpCompoundPowerFlow"],
        "_4308": ["TorqueConverterTurbineCompoundPowerFlow"],
        "_4309": ["UnbalancedMassCompoundPowerFlow"],
        "_4310": ["VirtualComponentCompoundPowerFlow"],
        "_4311": ["WormGearCompoundPowerFlow"],
        "_4312": ["WormGearMeshCompoundPowerFlow"],
        "_4313": ["WormGearSetCompoundPowerFlow"],
        "_4314": ["ZerolBevelGearCompoundPowerFlow"],
        "_4315": ["ZerolBevelGearMeshCompoundPowerFlow"],
        "_4316": ["ZerolBevelGearSetCompoundPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundPowerFlow",
    "AbstractShaftCompoundPowerFlow",
    "AbstractShaftOrHousingCompoundPowerFlow",
    "AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
    "AGMAGleasonConicalGearCompoundPowerFlow",
    "AGMAGleasonConicalGearMeshCompoundPowerFlow",
    "AGMAGleasonConicalGearSetCompoundPowerFlow",
    "AssemblyCompoundPowerFlow",
    "BearingCompoundPowerFlow",
    "BeltConnectionCompoundPowerFlow",
    "BeltDriveCompoundPowerFlow",
    "BevelDifferentialGearCompoundPowerFlow",
    "BevelDifferentialGearMeshCompoundPowerFlow",
    "BevelDifferentialGearSetCompoundPowerFlow",
    "BevelDifferentialPlanetGearCompoundPowerFlow",
    "BevelDifferentialSunGearCompoundPowerFlow",
    "BevelGearCompoundPowerFlow",
    "BevelGearMeshCompoundPowerFlow",
    "BevelGearSetCompoundPowerFlow",
    "BoltCompoundPowerFlow",
    "BoltedJointCompoundPowerFlow",
    "ClutchCompoundPowerFlow",
    "ClutchConnectionCompoundPowerFlow",
    "ClutchHalfCompoundPowerFlow",
    "CoaxialConnectionCompoundPowerFlow",
    "ComponentCompoundPowerFlow",
    "ConceptCouplingCompoundPowerFlow",
    "ConceptCouplingConnectionCompoundPowerFlow",
    "ConceptCouplingHalfCompoundPowerFlow",
    "ConceptGearCompoundPowerFlow",
    "ConceptGearMeshCompoundPowerFlow",
    "ConceptGearSetCompoundPowerFlow",
    "ConicalGearCompoundPowerFlow",
    "ConicalGearMeshCompoundPowerFlow",
    "ConicalGearSetCompoundPowerFlow",
    "ConnectionCompoundPowerFlow",
    "ConnectorCompoundPowerFlow",
    "CouplingCompoundPowerFlow",
    "CouplingConnectionCompoundPowerFlow",
    "CouplingHalfCompoundPowerFlow",
    "CVTBeltConnectionCompoundPowerFlow",
    "CVTCompoundPowerFlow",
    "CVTPulleyCompoundPowerFlow",
    "CycloidalAssemblyCompoundPowerFlow",
    "CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
    "CycloidalDiscCompoundPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow",
    "CylindricalGearCompoundPowerFlow",
    "CylindricalGearMeshCompoundPowerFlow",
    "CylindricalGearSetCompoundPowerFlow",
    "CylindricalPlanetGearCompoundPowerFlow",
    "DatumCompoundPowerFlow",
    "ExternalCADModelCompoundPowerFlow",
    "FaceGearCompoundPowerFlow",
    "FaceGearMeshCompoundPowerFlow",
    "FaceGearSetCompoundPowerFlow",
    "FEPartCompoundPowerFlow",
    "FlexiblePinAssemblyCompoundPowerFlow",
    "GearCompoundPowerFlow",
    "GearMeshCompoundPowerFlow",
    "GearSetCompoundPowerFlow",
    "GuideDxfModelCompoundPowerFlow",
    "HypoidGearCompoundPowerFlow",
    "HypoidGearMeshCompoundPowerFlow",
    "HypoidGearSetCompoundPowerFlow",
    "InterMountableComponentConnectionCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
    "MassDiscCompoundPowerFlow",
    "MeasurementComponentCompoundPowerFlow",
    "MountableComponentCompoundPowerFlow",
    "OilSealCompoundPowerFlow",
    "PartCompoundPowerFlow",
    "PartToPartShearCouplingCompoundPowerFlow",
    "PartToPartShearCouplingConnectionCompoundPowerFlow",
    "PartToPartShearCouplingHalfCompoundPowerFlow",
    "PlanetaryConnectionCompoundPowerFlow",
    "PlanetaryGearSetCompoundPowerFlow",
    "PlanetCarrierCompoundPowerFlow",
    "PointLoadCompoundPowerFlow",
    "PowerLoadCompoundPowerFlow",
    "PulleyCompoundPowerFlow",
    "RingPinsCompoundPowerFlow",
    "RingPinsToDiscConnectionCompoundPowerFlow",
    "RollingRingAssemblyCompoundPowerFlow",
    "RollingRingCompoundPowerFlow",
    "RollingRingConnectionCompoundPowerFlow",
    "RootAssemblyCompoundPowerFlow",
    "ShaftCompoundPowerFlow",
    "ShaftHubConnectionCompoundPowerFlow",
    "ShaftToMountableComponentConnectionCompoundPowerFlow",
    "SpecialisedAssemblyCompoundPowerFlow",
    "SpiralBevelGearCompoundPowerFlow",
    "SpiralBevelGearMeshCompoundPowerFlow",
    "SpiralBevelGearSetCompoundPowerFlow",
    "SpringDamperCompoundPowerFlow",
    "SpringDamperConnectionCompoundPowerFlow",
    "SpringDamperHalfCompoundPowerFlow",
    "StraightBevelDiffGearCompoundPowerFlow",
    "StraightBevelDiffGearMeshCompoundPowerFlow",
    "StraightBevelDiffGearSetCompoundPowerFlow",
    "StraightBevelGearCompoundPowerFlow",
    "StraightBevelGearMeshCompoundPowerFlow",
    "StraightBevelGearSetCompoundPowerFlow",
    "StraightBevelPlanetGearCompoundPowerFlow",
    "StraightBevelSunGearCompoundPowerFlow",
    "SynchroniserCompoundPowerFlow",
    "SynchroniserHalfCompoundPowerFlow",
    "SynchroniserPartCompoundPowerFlow",
    "SynchroniserSleeveCompoundPowerFlow",
    "TorqueConverterCompoundPowerFlow",
    "TorqueConverterConnectionCompoundPowerFlow",
    "TorqueConverterPumpCompoundPowerFlow",
    "TorqueConverterTurbineCompoundPowerFlow",
    "UnbalancedMassCompoundPowerFlow",
    "VirtualComponentCompoundPowerFlow",
    "WormGearCompoundPowerFlow",
    "WormGearMeshCompoundPowerFlow",
    "WormGearSetCompoundPowerFlow",
    "ZerolBevelGearCompoundPowerFlow",
    "ZerolBevelGearMeshCompoundPowerFlow",
    "ZerolBevelGearSetCompoundPowerFlow",
)
