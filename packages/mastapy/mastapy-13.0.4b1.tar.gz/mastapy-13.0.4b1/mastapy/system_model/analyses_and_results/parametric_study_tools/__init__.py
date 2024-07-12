"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4317 import AbstractAssemblyParametricStudyTool
    from ._4318 import AbstractShaftOrHousingParametricStudyTool
    from ._4319 import AbstractShaftParametricStudyTool
    from ._4320 import AbstractShaftToMountableComponentConnectionParametricStudyTool
    from ._4321 import AGMAGleasonConicalGearMeshParametricStudyTool
    from ._4322 import AGMAGleasonConicalGearParametricStudyTool
    from ._4323 import AGMAGleasonConicalGearSetParametricStudyTool
    from ._4324 import AssemblyParametricStudyTool
    from ._4325 import BearingParametricStudyTool
    from ._4326 import BeltConnectionParametricStudyTool
    from ._4327 import BeltDriveParametricStudyTool
    from ._4328 import BevelDifferentialGearMeshParametricStudyTool
    from ._4329 import BevelDifferentialGearParametricStudyTool
    from ._4330 import BevelDifferentialGearSetParametricStudyTool
    from ._4331 import BevelDifferentialPlanetGearParametricStudyTool
    from ._4332 import BevelDifferentialSunGearParametricStudyTool
    from ._4333 import BevelGearMeshParametricStudyTool
    from ._4334 import BevelGearParametricStudyTool
    from ._4335 import BevelGearSetParametricStudyTool
    from ._4336 import BoltedJointParametricStudyTool
    from ._4337 import BoltParametricStudyTool
    from ._4338 import ClutchConnectionParametricStudyTool
    from ._4339 import ClutchHalfParametricStudyTool
    from ._4340 import ClutchParametricStudyTool
    from ._4341 import CoaxialConnectionParametricStudyTool
    from ._4342 import ComponentParametricStudyTool
    from ._4343 import ConceptCouplingConnectionParametricStudyTool
    from ._4344 import ConceptCouplingHalfParametricStudyTool
    from ._4345 import ConceptCouplingParametricStudyTool
    from ._4346 import ConceptGearMeshParametricStudyTool
    from ._4347 import ConceptGearParametricStudyTool
    from ._4348 import ConceptGearSetParametricStudyTool
    from ._4349 import ConicalGearMeshParametricStudyTool
    from ._4350 import ConicalGearParametricStudyTool
    from ._4351 import ConicalGearSetParametricStudyTool
    from ._4352 import ConnectionParametricStudyTool
    from ._4353 import ConnectorParametricStudyTool
    from ._4354 import CouplingConnectionParametricStudyTool
    from ._4355 import CouplingHalfParametricStudyTool
    from ._4356 import CouplingParametricStudyTool
    from ._4357 import CVTBeltConnectionParametricStudyTool
    from ._4358 import CVTParametricStudyTool
    from ._4359 import CVTPulleyParametricStudyTool
    from ._4360 import CycloidalAssemblyParametricStudyTool
    from ._4361 import CycloidalDiscCentralBearingConnectionParametricStudyTool
    from ._4362 import CycloidalDiscParametricStudyTool
    from ._4363 import CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
    from ._4364 import CylindricalGearMeshParametricStudyTool
    from ._4365 import CylindricalGearParametricStudyTool
    from ._4366 import CylindricalGearSetParametricStudyTool
    from ._4367 import CylindricalPlanetGearParametricStudyTool
    from ._4368 import DatumParametricStudyTool
    from ._4369 import DesignOfExperimentsVariableSetter
    from ._4370 import DoeValueSpecificationOption
    from ._4371 import DutyCycleResultsForAllComponents
    from ._4372 import DutyCycleResultsForAllGearSets
    from ._4373 import DutyCycleResultsForRootAssembly
    from ._4374 import DutyCycleResultsForSingleBearing
    from ._4375 import DutyCycleResultsForSingleShaft
    from ._4376 import ExternalCADModelParametricStudyTool
    from ._4377 import FaceGearMeshParametricStudyTool
    from ._4378 import FaceGearParametricStudyTool
    from ._4379 import FaceGearSetParametricStudyTool
    from ._4380 import FEPartParametricStudyTool
    from ._4381 import FlexiblePinAssemblyParametricStudyTool
    from ._4382 import GearMeshParametricStudyTool
    from ._4383 import GearParametricStudyTool
    from ._4384 import GearSetParametricStudyTool
    from ._4385 import GuideDxfModelParametricStudyTool
    from ._4386 import HypoidGearMeshParametricStudyTool
    from ._4387 import HypoidGearParametricStudyTool
    from ._4388 import HypoidGearSetParametricStudyTool
    from ._4389 import InterMountableComponentConnectionParametricStudyTool
    from ._4390 import KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
    from ._4391 import KlingelnbergCycloPalloidConicalGearParametricStudyTool
    from ._4392 import KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
    from ._4393 import KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
    from ._4394 import KlingelnbergCycloPalloidHypoidGearParametricStudyTool
    from ._4395 import KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
    from ._4396 import KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
    from ._4397 import KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
    from ._4398 import KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
    from ._4399 import MassDiscParametricStudyTool
    from ._4400 import MeasurementComponentParametricStudyTool
    from ._4401 import MonteCarloDistribution
    from ._4402 import MountableComponentParametricStudyTool
    from ._4403 import OilSealParametricStudyTool
    from ._4404 import ParametricStudyDimension
    from ._4405 import ParametricStudyDOEResultVariable
    from ._4406 import ParametricStudyDOEResultVariableForParallelCoordinatesPlot
    from ._4407 import ParametricStudyHistogram
    from ._4408 import ParametricStudyStaticLoad
    from ._4409 import ParametricStudyTool
    from ._4410 import ParametricStudyToolOptions
    from ._4411 import ParametricStudyToolResultsForReporting
    from ._4412 import ParametricStudyToolStepResult
    from ._4413 import ParametricStudyVariable
    from ._4414 import PartParametricStudyTool
    from ._4415 import PartToPartShearCouplingConnectionParametricStudyTool
    from ._4416 import PartToPartShearCouplingHalfParametricStudyTool
    from ._4417 import PartToPartShearCouplingParametricStudyTool
    from ._4418 import PlanetaryConnectionParametricStudyTool
    from ._4419 import PlanetaryGearSetParametricStudyTool
    from ._4420 import PlanetCarrierParametricStudyTool
    from ._4421 import PointLoadParametricStudyTool
    from ._4422 import PowerLoadParametricStudyTool
    from ._4423 import PulleyParametricStudyTool
    from ._4424 import RingPinsParametricStudyTool
    from ._4425 import RingPinsToDiscConnectionParametricStudyTool
    from ._4426 import RollingRingAssemblyParametricStudyTool
    from ._4427 import RollingRingConnectionParametricStudyTool
    from ._4428 import RollingRingParametricStudyTool
    from ._4429 import RootAssemblyParametricStudyTool
    from ._4430 import ShaftHubConnectionParametricStudyTool
    from ._4431 import ShaftParametricStudyTool
    from ._4432 import ShaftToMountableComponentConnectionParametricStudyTool
    from ._4433 import SpecialisedAssemblyParametricStudyTool
    from ._4434 import SpiralBevelGearMeshParametricStudyTool
    from ._4435 import SpiralBevelGearParametricStudyTool
    from ._4436 import SpiralBevelGearSetParametricStudyTool
    from ._4437 import SpringDamperConnectionParametricStudyTool
    from ._4438 import SpringDamperHalfParametricStudyTool
    from ._4439 import SpringDamperParametricStudyTool
    from ._4440 import StraightBevelDiffGearMeshParametricStudyTool
    from ._4441 import StraightBevelDiffGearParametricStudyTool
    from ._4442 import StraightBevelDiffGearSetParametricStudyTool
    from ._4443 import StraightBevelGearMeshParametricStudyTool
    from ._4444 import StraightBevelGearParametricStudyTool
    from ._4445 import StraightBevelGearSetParametricStudyTool
    from ._4446 import StraightBevelPlanetGearParametricStudyTool
    from ._4447 import StraightBevelSunGearParametricStudyTool
    from ._4448 import SynchroniserHalfParametricStudyTool
    from ._4449 import SynchroniserParametricStudyTool
    from ._4450 import SynchroniserPartParametricStudyTool
    from ._4451 import SynchroniserSleeveParametricStudyTool
    from ._4452 import TorqueConverterConnectionParametricStudyTool
    from ._4453 import TorqueConverterParametricStudyTool
    from ._4454 import TorqueConverterPumpParametricStudyTool
    from ._4455 import TorqueConverterTurbineParametricStudyTool
    from ._4456 import UnbalancedMassParametricStudyTool
    from ._4457 import VirtualComponentParametricStudyTool
    from ._4458 import WormGearMeshParametricStudyTool
    from ._4459 import WormGearParametricStudyTool
    from ._4460 import WormGearSetParametricStudyTool
    from ._4461 import ZerolBevelGearMeshParametricStudyTool
    from ._4462 import ZerolBevelGearParametricStudyTool
    from ._4463 import ZerolBevelGearSetParametricStudyTool
else:
    import_structure = {
        "_4317": ["AbstractAssemblyParametricStudyTool"],
        "_4318": ["AbstractShaftOrHousingParametricStudyTool"],
        "_4319": ["AbstractShaftParametricStudyTool"],
        "_4320": ["AbstractShaftToMountableComponentConnectionParametricStudyTool"],
        "_4321": ["AGMAGleasonConicalGearMeshParametricStudyTool"],
        "_4322": ["AGMAGleasonConicalGearParametricStudyTool"],
        "_4323": ["AGMAGleasonConicalGearSetParametricStudyTool"],
        "_4324": ["AssemblyParametricStudyTool"],
        "_4325": ["BearingParametricStudyTool"],
        "_4326": ["BeltConnectionParametricStudyTool"],
        "_4327": ["BeltDriveParametricStudyTool"],
        "_4328": ["BevelDifferentialGearMeshParametricStudyTool"],
        "_4329": ["BevelDifferentialGearParametricStudyTool"],
        "_4330": ["BevelDifferentialGearSetParametricStudyTool"],
        "_4331": ["BevelDifferentialPlanetGearParametricStudyTool"],
        "_4332": ["BevelDifferentialSunGearParametricStudyTool"],
        "_4333": ["BevelGearMeshParametricStudyTool"],
        "_4334": ["BevelGearParametricStudyTool"],
        "_4335": ["BevelGearSetParametricStudyTool"],
        "_4336": ["BoltedJointParametricStudyTool"],
        "_4337": ["BoltParametricStudyTool"],
        "_4338": ["ClutchConnectionParametricStudyTool"],
        "_4339": ["ClutchHalfParametricStudyTool"],
        "_4340": ["ClutchParametricStudyTool"],
        "_4341": ["CoaxialConnectionParametricStudyTool"],
        "_4342": ["ComponentParametricStudyTool"],
        "_4343": ["ConceptCouplingConnectionParametricStudyTool"],
        "_4344": ["ConceptCouplingHalfParametricStudyTool"],
        "_4345": ["ConceptCouplingParametricStudyTool"],
        "_4346": ["ConceptGearMeshParametricStudyTool"],
        "_4347": ["ConceptGearParametricStudyTool"],
        "_4348": ["ConceptGearSetParametricStudyTool"],
        "_4349": ["ConicalGearMeshParametricStudyTool"],
        "_4350": ["ConicalGearParametricStudyTool"],
        "_4351": ["ConicalGearSetParametricStudyTool"],
        "_4352": ["ConnectionParametricStudyTool"],
        "_4353": ["ConnectorParametricStudyTool"],
        "_4354": ["CouplingConnectionParametricStudyTool"],
        "_4355": ["CouplingHalfParametricStudyTool"],
        "_4356": ["CouplingParametricStudyTool"],
        "_4357": ["CVTBeltConnectionParametricStudyTool"],
        "_4358": ["CVTParametricStudyTool"],
        "_4359": ["CVTPulleyParametricStudyTool"],
        "_4360": ["CycloidalAssemblyParametricStudyTool"],
        "_4361": ["CycloidalDiscCentralBearingConnectionParametricStudyTool"],
        "_4362": ["CycloidalDiscParametricStudyTool"],
        "_4363": ["CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"],
        "_4364": ["CylindricalGearMeshParametricStudyTool"],
        "_4365": ["CylindricalGearParametricStudyTool"],
        "_4366": ["CylindricalGearSetParametricStudyTool"],
        "_4367": ["CylindricalPlanetGearParametricStudyTool"],
        "_4368": ["DatumParametricStudyTool"],
        "_4369": ["DesignOfExperimentsVariableSetter"],
        "_4370": ["DoeValueSpecificationOption"],
        "_4371": ["DutyCycleResultsForAllComponents"],
        "_4372": ["DutyCycleResultsForAllGearSets"],
        "_4373": ["DutyCycleResultsForRootAssembly"],
        "_4374": ["DutyCycleResultsForSingleBearing"],
        "_4375": ["DutyCycleResultsForSingleShaft"],
        "_4376": ["ExternalCADModelParametricStudyTool"],
        "_4377": ["FaceGearMeshParametricStudyTool"],
        "_4378": ["FaceGearParametricStudyTool"],
        "_4379": ["FaceGearSetParametricStudyTool"],
        "_4380": ["FEPartParametricStudyTool"],
        "_4381": ["FlexiblePinAssemblyParametricStudyTool"],
        "_4382": ["GearMeshParametricStudyTool"],
        "_4383": ["GearParametricStudyTool"],
        "_4384": ["GearSetParametricStudyTool"],
        "_4385": ["GuideDxfModelParametricStudyTool"],
        "_4386": ["HypoidGearMeshParametricStudyTool"],
        "_4387": ["HypoidGearParametricStudyTool"],
        "_4388": ["HypoidGearSetParametricStudyTool"],
        "_4389": ["InterMountableComponentConnectionParametricStudyTool"],
        "_4390": ["KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool"],
        "_4391": ["KlingelnbergCycloPalloidConicalGearParametricStudyTool"],
        "_4392": ["KlingelnbergCycloPalloidConicalGearSetParametricStudyTool"],
        "_4393": ["KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool"],
        "_4394": ["KlingelnbergCycloPalloidHypoidGearParametricStudyTool"],
        "_4395": ["KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool"],
        "_4396": ["KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool"],
        "_4397": ["KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool"],
        "_4398": ["KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool"],
        "_4399": ["MassDiscParametricStudyTool"],
        "_4400": ["MeasurementComponentParametricStudyTool"],
        "_4401": ["MonteCarloDistribution"],
        "_4402": ["MountableComponentParametricStudyTool"],
        "_4403": ["OilSealParametricStudyTool"],
        "_4404": ["ParametricStudyDimension"],
        "_4405": ["ParametricStudyDOEResultVariable"],
        "_4406": ["ParametricStudyDOEResultVariableForParallelCoordinatesPlot"],
        "_4407": ["ParametricStudyHistogram"],
        "_4408": ["ParametricStudyStaticLoad"],
        "_4409": ["ParametricStudyTool"],
        "_4410": ["ParametricStudyToolOptions"],
        "_4411": ["ParametricStudyToolResultsForReporting"],
        "_4412": ["ParametricStudyToolStepResult"],
        "_4413": ["ParametricStudyVariable"],
        "_4414": ["PartParametricStudyTool"],
        "_4415": ["PartToPartShearCouplingConnectionParametricStudyTool"],
        "_4416": ["PartToPartShearCouplingHalfParametricStudyTool"],
        "_4417": ["PartToPartShearCouplingParametricStudyTool"],
        "_4418": ["PlanetaryConnectionParametricStudyTool"],
        "_4419": ["PlanetaryGearSetParametricStudyTool"],
        "_4420": ["PlanetCarrierParametricStudyTool"],
        "_4421": ["PointLoadParametricStudyTool"],
        "_4422": ["PowerLoadParametricStudyTool"],
        "_4423": ["PulleyParametricStudyTool"],
        "_4424": ["RingPinsParametricStudyTool"],
        "_4425": ["RingPinsToDiscConnectionParametricStudyTool"],
        "_4426": ["RollingRingAssemblyParametricStudyTool"],
        "_4427": ["RollingRingConnectionParametricStudyTool"],
        "_4428": ["RollingRingParametricStudyTool"],
        "_4429": ["RootAssemblyParametricStudyTool"],
        "_4430": ["ShaftHubConnectionParametricStudyTool"],
        "_4431": ["ShaftParametricStudyTool"],
        "_4432": ["ShaftToMountableComponentConnectionParametricStudyTool"],
        "_4433": ["SpecialisedAssemblyParametricStudyTool"],
        "_4434": ["SpiralBevelGearMeshParametricStudyTool"],
        "_4435": ["SpiralBevelGearParametricStudyTool"],
        "_4436": ["SpiralBevelGearSetParametricStudyTool"],
        "_4437": ["SpringDamperConnectionParametricStudyTool"],
        "_4438": ["SpringDamperHalfParametricStudyTool"],
        "_4439": ["SpringDamperParametricStudyTool"],
        "_4440": ["StraightBevelDiffGearMeshParametricStudyTool"],
        "_4441": ["StraightBevelDiffGearParametricStudyTool"],
        "_4442": ["StraightBevelDiffGearSetParametricStudyTool"],
        "_4443": ["StraightBevelGearMeshParametricStudyTool"],
        "_4444": ["StraightBevelGearParametricStudyTool"],
        "_4445": ["StraightBevelGearSetParametricStudyTool"],
        "_4446": ["StraightBevelPlanetGearParametricStudyTool"],
        "_4447": ["StraightBevelSunGearParametricStudyTool"],
        "_4448": ["SynchroniserHalfParametricStudyTool"],
        "_4449": ["SynchroniserParametricStudyTool"],
        "_4450": ["SynchroniserPartParametricStudyTool"],
        "_4451": ["SynchroniserSleeveParametricStudyTool"],
        "_4452": ["TorqueConverterConnectionParametricStudyTool"],
        "_4453": ["TorqueConverterParametricStudyTool"],
        "_4454": ["TorqueConverterPumpParametricStudyTool"],
        "_4455": ["TorqueConverterTurbineParametricStudyTool"],
        "_4456": ["UnbalancedMassParametricStudyTool"],
        "_4457": ["VirtualComponentParametricStudyTool"],
        "_4458": ["WormGearMeshParametricStudyTool"],
        "_4459": ["WormGearParametricStudyTool"],
        "_4460": ["WormGearSetParametricStudyTool"],
        "_4461": ["ZerolBevelGearMeshParametricStudyTool"],
        "_4462": ["ZerolBevelGearParametricStudyTool"],
        "_4463": ["ZerolBevelGearSetParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyParametricStudyTool",
    "AbstractShaftOrHousingParametricStudyTool",
    "AbstractShaftParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionParametricStudyTool",
    "AGMAGleasonConicalGearMeshParametricStudyTool",
    "AGMAGleasonConicalGearParametricStudyTool",
    "AGMAGleasonConicalGearSetParametricStudyTool",
    "AssemblyParametricStudyTool",
    "BearingParametricStudyTool",
    "BeltConnectionParametricStudyTool",
    "BeltDriveParametricStudyTool",
    "BevelDifferentialGearMeshParametricStudyTool",
    "BevelDifferentialGearParametricStudyTool",
    "BevelDifferentialGearSetParametricStudyTool",
    "BevelDifferentialPlanetGearParametricStudyTool",
    "BevelDifferentialSunGearParametricStudyTool",
    "BevelGearMeshParametricStudyTool",
    "BevelGearParametricStudyTool",
    "BevelGearSetParametricStudyTool",
    "BoltedJointParametricStudyTool",
    "BoltParametricStudyTool",
    "ClutchConnectionParametricStudyTool",
    "ClutchHalfParametricStudyTool",
    "ClutchParametricStudyTool",
    "CoaxialConnectionParametricStudyTool",
    "ComponentParametricStudyTool",
    "ConceptCouplingConnectionParametricStudyTool",
    "ConceptCouplingHalfParametricStudyTool",
    "ConceptCouplingParametricStudyTool",
    "ConceptGearMeshParametricStudyTool",
    "ConceptGearParametricStudyTool",
    "ConceptGearSetParametricStudyTool",
    "ConicalGearMeshParametricStudyTool",
    "ConicalGearParametricStudyTool",
    "ConicalGearSetParametricStudyTool",
    "ConnectionParametricStudyTool",
    "ConnectorParametricStudyTool",
    "CouplingConnectionParametricStudyTool",
    "CouplingHalfParametricStudyTool",
    "CouplingParametricStudyTool",
    "CVTBeltConnectionParametricStudyTool",
    "CVTParametricStudyTool",
    "CVTPulleyParametricStudyTool",
    "CycloidalAssemblyParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionParametricStudyTool",
    "CycloidalDiscParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
    "CylindricalGearMeshParametricStudyTool",
    "CylindricalGearParametricStudyTool",
    "CylindricalGearSetParametricStudyTool",
    "CylindricalPlanetGearParametricStudyTool",
    "DatumParametricStudyTool",
    "DesignOfExperimentsVariableSetter",
    "DoeValueSpecificationOption",
    "DutyCycleResultsForAllComponents",
    "DutyCycleResultsForAllGearSets",
    "DutyCycleResultsForRootAssembly",
    "DutyCycleResultsForSingleBearing",
    "DutyCycleResultsForSingleShaft",
    "ExternalCADModelParametricStudyTool",
    "FaceGearMeshParametricStudyTool",
    "FaceGearParametricStudyTool",
    "FaceGearSetParametricStudyTool",
    "FEPartParametricStudyTool",
    "FlexiblePinAssemblyParametricStudyTool",
    "GearMeshParametricStudyTool",
    "GearParametricStudyTool",
    "GearSetParametricStudyTool",
    "GuideDxfModelParametricStudyTool",
    "HypoidGearMeshParametricStudyTool",
    "HypoidGearParametricStudyTool",
    "HypoidGearSetParametricStudyTool",
    "InterMountableComponentConnectionParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool",
    "MassDiscParametricStudyTool",
    "MeasurementComponentParametricStudyTool",
    "MonteCarloDistribution",
    "MountableComponentParametricStudyTool",
    "OilSealParametricStudyTool",
    "ParametricStudyDimension",
    "ParametricStudyDOEResultVariable",
    "ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
    "ParametricStudyHistogram",
    "ParametricStudyStaticLoad",
    "ParametricStudyTool",
    "ParametricStudyToolOptions",
    "ParametricStudyToolResultsForReporting",
    "ParametricStudyToolStepResult",
    "ParametricStudyVariable",
    "PartParametricStudyTool",
    "PartToPartShearCouplingConnectionParametricStudyTool",
    "PartToPartShearCouplingHalfParametricStudyTool",
    "PartToPartShearCouplingParametricStudyTool",
    "PlanetaryConnectionParametricStudyTool",
    "PlanetaryGearSetParametricStudyTool",
    "PlanetCarrierParametricStudyTool",
    "PointLoadParametricStudyTool",
    "PowerLoadParametricStudyTool",
    "PulleyParametricStudyTool",
    "RingPinsParametricStudyTool",
    "RingPinsToDiscConnectionParametricStudyTool",
    "RollingRingAssemblyParametricStudyTool",
    "RollingRingConnectionParametricStudyTool",
    "RollingRingParametricStudyTool",
    "RootAssemblyParametricStudyTool",
    "ShaftHubConnectionParametricStudyTool",
    "ShaftParametricStudyTool",
    "ShaftToMountableComponentConnectionParametricStudyTool",
    "SpecialisedAssemblyParametricStudyTool",
    "SpiralBevelGearMeshParametricStudyTool",
    "SpiralBevelGearParametricStudyTool",
    "SpiralBevelGearSetParametricStudyTool",
    "SpringDamperConnectionParametricStudyTool",
    "SpringDamperHalfParametricStudyTool",
    "SpringDamperParametricStudyTool",
    "StraightBevelDiffGearMeshParametricStudyTool",
    "StraightBevelDiffGearParametricStudyTool",
    "StraightBevelDiffGearSetParametricStudyTool",
    "StraightBevelGearMeshParametricStudyTool",
    "StraightBevelGearParametricStudyTool",
    "StraightBevelGearSetParametricStudyTool",
    "StraightBevelPlanetGearParametricStudyTool",
    "StraightBevelSunGearParametricStudyTool",
    "SynchroniserHalfParametricStudyTool",
    "SynchroniserParametricStudyTool",
    "SynchroniserPartParametricStudyTool",
    "SynchroniserSleeveParametricStudyTool",
    "TorqueConverterConnectionParametricStudyTool",
    "TorqueConverterParametricStudyTool",
    "TorqueConverterPumpParametricStudyTool",
    "TorqueConverterTurbineParametricStudyTool",
    "UnbalancedMassParametricStudyTool",
    "VirtualComponentParametricStudyTool",
    "WormGearMeshParametricStudyTool",
    "WormGearParametricStudyTool",
    "WormGearSetParametricStudyTool",
    "ZerolBevelGearMeshParametricStudyTool",
    "ZerolBevelGearParametricStudyTool",
    "ZerolBevelGearSetParametricStudyTool",
)
