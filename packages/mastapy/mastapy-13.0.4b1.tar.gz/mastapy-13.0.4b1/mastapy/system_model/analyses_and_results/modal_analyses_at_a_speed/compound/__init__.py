"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5268 import AbstractAssemblyCompoundModalAnalysisAtASpeed
    from ._5269 import AbstractShaftCompoundModalAnalysisAtASpeed
    from ._5270 import AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
    from ._5271 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5272 import AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
    from ._5273 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5274 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5275 import AssemblyCompoundModalAnalysisAtASpeed
    from ._5276 import BearingCompoundModalAnalysisAtASpeed
    from ._5277 import BeltConnectionCompoundModalAnalysisAtASpeed
    from ._5278 import BeltDriveCompoundModalAnalysisAtASpeed
    from ._5279 import BevelDifferentialGearCompoundModalAnalysisAtASpeed
    from ._5280 import BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
    from ._5281 import BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
    from ._5282 import BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
    from ._5283 import BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
    from ._5284 import BevelGearCompoundModalAnalysisAtASpeed
    from ._5285 import BevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5286 import BevelGearSetCompoundModalAnalysisAtASpeed
    from ._5287 import BoltCompoundModalAnalysisAtASpeed
    from ._5288 import BoltedJointCompoundModalAnalysisAtASpeed
    from ._5289 import ClutchCompoundModalAnalysisAtASpeed
    from ._5290 import ClutchConnectionCompoundModalAnalysisAtASpeed
    from ._5291 import ClutchHalfCompoundModalAnalysisAtASpeed
    from ._5292 import CoaxialConnectionCompoundModalAnalysisAtASpeed
    from ._5293 import ComponentCompoundModalAnalysisAtASpeed
    from ._5294 import ConceptCouplingCompoundModalAnalysisAtASpeed
    from ._5295 import ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5296 import ConceptCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5297 import ConceptGearCompoundModalAnalysisAtASpeed
    from ._5298 import ConceptGearMeshCompoundModalAnalysisAtASpeed
    from ._5299 import ConceptGearSetCompoundModalAnalysisAtASpeed
    from ._5300 import ConicalGearCompoundModalAnalysisAtASpeed
    from ._5301 import ConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5302 import ConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5303 import ConnectionCompoundModalAnalysisAtASpeed
    from ._5304 import ConnectorCompoundModalAnalysisAtASpeed
    from ._5305 import CouplingCompoundModalAnalysisAtASpeed
    from ._5306 import CouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5307 import CouplingHalfCompoundModalAnalysisAtASpeed
    from ._5308 import CVTBeltConnectionCompoundModalAnalysisAtASpeed
    from ._5309 import CVTCompoundModalAnalysisAtASpeed
    from ._5310 import CVTPulleyCompoundModalAnalysisAtASpeed
    from ._5311 import CycloidalAssemblyCompoundModalAnalysisAtASpeed
    from ._5312 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5313 import CycloidalDiscCompoundModalAnalysisAtASpeed
    from ._5314 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5315 import CylindricalGearCompoundModalAnalysisAtASpeed
    from ._5316 import CylindricalGearMeshCompoundModalAnalysisAtASpeed
    from ._5317 import CylindricalGearSetCompoundModalAnalysisAtASpeed
    from ._5318 import CylindricalPlanetGearCompoundModalAnalysisAtASpeed
    from ._5319 import DatumCompoundModalAnalysisAtASpeed
    from ._5320 import ExternalCADModelCompoundModalAnalysisAtASpeed
    from ._5321 import FaceGearCompoundModalAnalysisAtASpeed
    from ._5322 import FaceGearMeshCompoundModalAnalysisAtASpeed
    from ._5323 import FaceGearSetCompoundModalAnalysisAtASpeed
    from ._5324 import FEPartCompoundModalAnalysisAtASpeed
    from ._5325 import FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
    from ._5326 import GearCompoundModalAnalysisAtASpeed
    from ._5327 import GearMeshCompoundModalAnalysisAtASpeed
    from ._5328 import GearSetCompoundModalAnalysisAtASpeed
    from ._5329 import GuideDxfModelCompoundModalAnalysisAtASpeed
    from ._5330 import HypoidGearCompoundModalAnalysisAtASpeed
    from ._5331 import HypoidGearMeshCompoundModalAnalysisAtASpeed
    from ._5332 import HypoidGearSetCompoundModalAnalysisAtASpeed
    from ._5333 import InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5334 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
    from ._5335 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5336 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5337 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
    from ._5338 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5339 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5340 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed,
    )
    from ._5341 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5342 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5343 import MassDiscCompoundModalAnalysisAtASpeed
    from ._5344 import MeasurementComponentCompoundModalAnalysisAtASpeed
    from ._5345 import MountableComponentCompoundModalAnalysisAtASpeed
    from ._5346 import OilSealCompoundModalAnalysisAtASpeed
    from ._5347 import PartCompoundModalAnalysisAtASpeed
    from ._5348 import PartToPartShearCouplingCompoundModalAnalysisAtASpeed
    from ._5349 import PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5350 import PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5351 import PlanetaryConnectionCompoundModalAnalysisAtASpeed
    from ._5352 import PlanetaryGearSetCompoundModalAnalysisAtASpeed
    from ._5353 import PlanetCarrierCompoundModalAnalysisAtASpeed
    from ._5354 import PointLoadCompoundModalAnalysisAtASpeed
    from ._5355 import PowerLoadCompoundModalAnalysisAtASpeed
    from ._5356 import PulleyCompoundModalAnalysisAtASpeed
    from ._5357 import RingPinsCompoundModalAnalysisAtASpeed
    from ._5358 import RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
    from ._5359 import RollingRingAssemblyCompoundModalAnalysisAtASpeed
    from ._5360 import RollingRingCompoundModalAnalysisAtASpeed
    from ._5361 import RollingRingConnectionCompoundModalAnalysisAtASpeed
    from ._5362 import RootAssemblyCompoundModalAnalysisAtASpeed
    from ._5363 import ShaftCompoundModalAnalysisAtASpeed
    from ._5364 import ShaftHubConnectionCompoundModalAnalysisAtASpeed
    from ._5365 import ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5366 import SpecialisedAssemblyCompoundModalAnalysisAtASpeed
    from ._5367 import SpiralBevelGearCompoundModalAnalysisAtASpeed
    from ._5368 import SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5369 import SpiralBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5370 import SpringDamperCompoundModalAnalysisAtASpeed
    from ._5371 import SpringDamperConnectionCompoundModalAnalysisAtASpeed
    from ._5372 import SpringDamperHalfCompoundModalAnalysisAtASpeed
    from ._5373 import StraightBevelDiffGearCompoundModalAnalysisAtASpeed
    from ._5374 import StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
    from ._5375 import StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
    from ._5376 import StraightBevelGearCompoundModalAnalysisAtASpeed
    from ._5377 import StraightBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5378 import StraightBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5379 import StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
    from ._5380 import StraightBevelSunGearCompoundModalAnalysisAtASpeed
    from ._5381 import SynchroniserCompoundModalAnalysisAtASpeed
    from ._5382 import SynchroniserHalfCompoundModalAnalysisAtASpeed
    from ._5383 import SynchroniserPartCompoundModalAnalysisAtASpeed
    from ._5384 import SynchroniserSleeveCompoundModalAnalysisAtASpeed
    from ._5385 import TorqueConverterCompoundModalAnalysisAtASpeed
    from ._5386 import TorqueConverterConnectionCompoundModalAnalysisAtASpeed
    from ._5387 import TorqueConverterPumpCompoundModalAnalysisAtASpeed
    from ._5388 import TorqueConverterTurbineCompoundModalAnalysisAtASpeed
    from ._5389 import UnbalancedMassCompoundModalAnalysisAtASpeed
    from ._5390 import VirtualComponentCompoundModalAnalysisAtASpeed
    from ._5391 import WormGearCompoundModalAnalysisAtASpeed
    from ._5392 import WormGearMeshCompoundModalAnalysisAtASpeed
    from ._5393 import WormGearSetCompoundModalAnalysisAtASpeed
    from ._5394 import ZerolBevelGearCompoundModalAnalysisAtASpeed
    from ._5395 import ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5396 import ZerolBevelGearSetCompoundModalAnalysisAtASpeed
else:
    import_structure = {
        "_5268": ["AbstractAssemblyCompoundModalAnalysisAtASpeed"],
        "_5269": ["AbstractShaftCompoundModalAnalysisAtASpeed"],
        "_5270": ["AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"],
        "_5271": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5272": ["AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"],
        "_5273": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5274": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5275": ["AssemblyCompoundModalAnalysisAtASpeed"],
        "_5276": ["BearingCompoundModalAnalysisAtASpeed"],
        "_5277": ["BeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5278": ["BeltDriveCompoundModalAnalysisAtASpeed"],
        "_5279": ["BevelDifferentialGearCompoundModalAnalysisAtASpeed"],
        "_5280": ["BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed"],
        "_5281": ["BevelDifferentialGearSetCompoundModalAnalysisAtASpeed"],
        "_5282": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5283": ["BevelDifferentialSunGearCompoundModalAnalysisAtASpeed"],
        "_5284": ["BevelGearCompoundModalAnalysisAtASpeed"],
        "_5285": ["BevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5286": ["BevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5287": ["BoltCompoundModalAnalysisAtASpeed"],
        "_5288": ["BoltedJointCompoundModalAnalysisAtASpeed"],
        "_5289": ["ClutchCompoundModalAnalysisAtASpeed"],
        "_5290": ["ClutchConnectionCompoundModalAnalysisAtASpeed"],
        "_5291": ["ClutchHalfCompoundModalAnalysisAtASpeed"],
        "_5292": ["CoaxialConnectionCompoundModalAnalysisAtASpeed"],
        "_5293": ["ComponentCompoundModalAnalysisAtASpeed"],
        "_5294": ["ConceptCouplingCompoundModalAnalysisAtASpeed"],
        "_5295": ["ConceptCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5296": ["ConceptCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5297": ["ConceptGearCompoundModalAnalysisAtASpeed"],
        "_5298": ["ConceptGearMeshCompoundModalAnalysisAtASpeed"],
        "_5299": ["ConceptGearSetCompoundModalAnalysisAtASpeed"],
        "_5300": ["ConicalGearCompoundModalAnalysisAtASpeed"],
        "_5301": ["ConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5302": ["ConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5303": ["ConnectionCompoundModalAnalysisAtASpeed"],
        "_5304": ["ConnectorCompoundModalAnalysisAtASpeed"],
        "_5305": ["CouplingCompoundModalAnalysisAtASpeed"],
        "_5306": ["CouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5307": ["CouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5308": ["CVTBeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5309": ["CVTCompoundModalAnalysisAtASpeed"],
        "_5310": ["CVTPulleyCompoundModalAnalysisAtASpeed"],
        "_5311": ["CycloidalAssemblyCompoundModalAnalysisAtASpeed"],
        "_5312": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed"],
        "_5313": ["CycloidalDiscCompoundModalAnalysisAtASpeed"],
        "_5314": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5315": ["CylindricalGearCompoundModalAnalysisAtASpeed"],
        "_5316": ["CylindricalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5317": ["CylindricalGearSetCompoundModalAnalysisAtASpeed"],
        "_5318": ["CylindricalPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5319": ["DatumCompoundModalAnalysisAtASpeed"],
        "_5320": ["ExternalCADModelCompoundModalAnalysisAtASpeed"],
        "_5321": ["FaceGearCompoundModalAnalysisAtASpeed"],
        "_5322": ["FaceGearMeshCompoundModalAnalysisAtASpeed"],
        "_5323": ["FaceGearSetCompoundModalAnalysisAtASpeed"],
        "_5324": ["FEPartCompoundModalAnalysisAtASpeed"],
        "_5325": ["FlexiblePinAssemblyCompoundModalAnalysisAtASpeed"],
        "_5326": ["GearCompoundModalAnalysisAtASpeed"],
        "_5327": ["GearMeshCompoundModalAnalysisAtASpeed"],
        "_5328": ["GearSetCompoundModalAnalysisAtASpeed"],
        "_5329": ["GuideDxfModelCompoundModalAnalysisAtASpeed"],
        "_5330": ["HypoidGearCompoundModalAnalysisAtASpeed"],
        "_5331": ["HypoidGearMeshCompoundModalAnalysisAtASpeed"],
        "_5332": ["HypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5333": ["InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5334": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed"],
        "_5335": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5336": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5337": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed"],
        "_5338": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5339": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5340": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ],
        "_5341": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5342": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5343": ["MassDiscCompoundModalAnalysisAtASpeed"],
        "_5344": ["MeasurementComponentCompoundModalAnalysisAtASpeed"],
        "_5345": ["MountableComponentCompoundModalAnalysisAtASpeed"],
        "_5346": ["OilSealCompoundModalAnalysisAtASpeed"],
        "_5347": ["PartCompoundModalAnalysisAtASpeed"],
        "_5348": ["PartToPartShearCouplingCompoundModalAnalysisAtASpeed"],
        "_5349": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5350": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5351": ["PlanetaryConnectionCompoundModalAnalysisAtASpeed"],
        "_5352": ["PlanetaryGearSetCompoundModalAnalysisAtASpeed"],
        "_5353": ["PlanetCarrierCompoundModalAnalysisAtASpeed"],
        "_5354": ["PointLoadCompoundModalAnalysisAtASpeed"],
        "_5355": ["PowerLoadCompoundModalAnalysisAtASpeed"],
        "_5356": ["PulleyCompoundModalAnalysisAtASpeed"],
        "_5357": ["RingPinsCompoundModalAnalysisAtASpeed"],
        "_5358": ["RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed"],
        "_5359": ["RollingRingAssemblyCompoundModalAnalysisAtASpeed"],
        "_5360": ["RollingRingCompoundModalAnalysisAtASpeed"],
        "_5361": ["RollingRingConnectionCompoundModalAnalysisAtASpeed"],
        "_5362": ["RootAssemblyCompoundModalAnalysisAtASpeed"],
        "_5363": ["ShaftCompoundModalAnalysisAtASpeed"],
        "_5364": ["ShaftHubConnectionCompoundModalAnalysisAtASpeed"],
        "_5365": ["ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5366": ["SpecialisedAssemblyCompoundModalAnalysisAtASpeed"],
        "_5367": ["SpiralBevelGearCompoundModalAnalysisAtASpeed"],
        "_5368": ["SpiralBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5369": ["SpiralBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5370": ["SpringDamperCompoundModalAnalysisAtASpeed"],
        "_5371": ["SpringDamperConnectionCompoundModalAnalysisAtASpeed"],
        "_5372": ["SpringDamperHalfCompoundModalAnalysisAtASpeed"],
        "_5373": ["StraightBevelDiffGearCompoundModalAnalysisAtASpeed"],
        "_5374": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed"],
        "_5375": ["StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed"],
        "_5376": ["StraightBevelGearCompoundModalAnalysisAtASpeed"],
        "_5377": ["StraightBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5378": ["StraightBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5379": ["StraightBevelPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5380": ["StraightBevelSunGearCompoundModalAnalysisAtASpeed"],
        "_5381": ["SynchroniserCompoundModalAnalysisAtASpeed"],
        "_5382": ["SynchroniserHalfCompoundModalAnalysisAtASpeed"],
        "_5383": ["SynchroniserPartCompoundModalAnalysisAtASpeed"],
        "_5384": ["SynchroniserSleeveCompoundModalAnalysisAtASpeed"],
        "_5385": ["TorqueConverterCompoundModalAnalysisAtASpeed"],
        "_5386": ["TorqueConverterConnectionCompoundModalAnalysisAtASpeed"],
        "_5387": ["TorqueConverterPumpCompoundModalAnalysisAtASpeed"],
        "_5388": ["TorqueConverterTurbineCompoundModalAnalysisAtASpeed"],
        "_5389": ["UnbalancedMassCompoundModalAnalysisAtASpeed"],
        "_5390": ["VirtualComponentCompoundModalAnalysisAtASpeed"],
        "_5391": ["WormGearCompoundModalAnalysisAtASpeed"],
        "_5392": ["WormGearMeshCompoundModalAnalysisAtASpeed"],
        "_5393": ["WormGearSetCompoundModalAnalysisAtASpeed"],
        "_5394": ["ZerolBevelGearCompoundModalAnalysisAtASpeed"],
        "_5395": ["ZerolBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5396": ["ZerolBevelGearSetCompoundModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtASpeed",
    "AbstractShaftCompoundModalAnalysisAtASpeed",
    "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
    "AssemblyCompoundModalAnalysisAtASpeed",
    "BearingCompoundModalAnalysisAtASpeed",
    "BeltConnectionCompoundModalAnalysisAtASpeed",
    "BeltDriveCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearSetCompoundModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialSunGearCompoundModalAnalysisAtASpeed",
    "BevelGearCompoundModalAnalysisAtASpeed",
    "BevelGearMeshCompoundModalAnalysisAtASpeed",
    "BevelGearSetCompoundModalAnalysisAtASpeed",
    "BoltCompoundModalAnalysisAtASpeed",
    "BoltedJointCompoundModalAnalysisAtASpeed",
    "ClutchCompoundModalAnalysisAtASpeed",
    "ClutchConnectionCompoundModalAnalysisAtASpeed",
    "ClutchHalfCompoundModalAnalysisAtASpeed",
    "CoaxialConnectionCompoundModalAnalysisAtASpeed",
    "ComponentCompoundModalAnalysisAtASpeed",
    "ConceptCouplingCompoundModalAnalysisAtASpeed",
    "ConceptCouplingConnectionCompoundModalAnalysisAtASpeed",
    "ConceptCouplingHalfCompoundModalAnalysisAtASpeed",
    "ConceptGearCompoundModalAnalysisAtASpeed",
    "ConceptGearMeshCompoundModalAnalysisAtASpeed",
    "ConceptGearSetCompoundModalAnalysisAtASpeed",
    "ConicalGearCompoundModalAnalysisAtASpeed",
    "ConicalGearMeshCompoundModalAnalysisAtASpeed",
    "ConicalGearSetCompoundModalAnalysisAtASpeed",
    "ConnectionCompoundModalAnalysisAtASpeed",
    "ConnectorCompoundModalAnalysisAtASpeed",
    "CouplingCompoundModalAnalysisAtASpeed",
    "CouplingConnectionCompoundModalAnalysisAtASpeed",
    "CouplingHalfCompoundModalAnalysisAtASpeed",
    "CVTBeltConnectionCompoundModalAnalysisAtASpeed",
    "CVTCompoundModalAnalysisAtASpeed",
    "CVTPulleyCompoundModalAnalysisAtASpeed",
    "CycloidalAssemblyCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCompoundModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
    "CylindricalGearCompoundModalAnalysisAtASpeed",
    "CylindricalGearMeshCompoundModalAnalysisAtASpeed",
    "CylindricalGearSetCompoundModalAnalysisAtASpeed",
    "CylindricalPlanetGearCompoundModalAnalysisAtASpeed",
    "DatumCompoundModalAnalysisAtASpeed",
    "ExternalCADModelCompoundModalAnalysisAtASpeed",
    "FaceGearCompoundModalAnalysisAtASpeed",
    "FaceGearMeshCompoundModalAnalysisAtASpeed",
    "FaceGearSetCompoundModalAnalysisAtASpeed",
    "FEPartCompoundModalAnalysisAtASpeed",
    "FlexiblePinAssemblyCompoundModalAnalysisAtASpeed",
    "GearCompoundModalAnalysisAtASpeed",
    "GearMeshCompoundModalAnalysisAtASpeed",
    "GearSetCompoundModalAnalysisAtASpeed",
    "GuideDxfModelCompoundModalAnalysisAtASpeed",
    "HypoidGearCompoundModalAnalysisAtASpeed",
    "HypoidGearMeshCompoundModalAnalysisAtASpeed",
    "HypoidGearSetCompoundModalAnalysisAtASpeed",
    "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "MassDiscCompoundModalAnalysisAtASpeed",
    "MeasurementComponentCompoundModalAnalysisAtASpeed",
    "MountableComponentCompoundModalAnalysisAtASpeed",
    "OilSealCompoundModalAnalysisAtASpeed",
    "PartCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
    "PlanetaryConnectionCompoundModalAnalysisAtASpeed",
    "PlanetaryGearSetCompoundModalAnalysisAtASpeed",
    "PlanetCarrierCompoundModalAnalysisAtASpeed",
    "PointLoadCompoundModalAnalysisAtASpeed",
    "PowerLoadCompoundModalAnalysisAtASpeed",
    "PulleyCompoundModalAnalysisAtASpeed",
    "RingPinsCompoundModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed",
    "RollingRingAssemblyCompoundModalAnalysisAtASpeed",
    "RollingRingCompoundModalAnalysisAtASpeed",
    "RollingRingConnectionCompoundModalAnalysisAtASpeed",
    "RootAssemblyCompoundModalAnalysisAtASpeed",
    "ShaftCompoundModalAnalysisAtASpeed",
    "ShaftHubConnectionCompoundModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "SpringDamperCompoundModalAnalysisAtASpeed",
    "SpringDamperConnectionCompoundModalAnalysisAtASpeed",
    "SpringDamperHalfCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelGearCompoundModalAnalysisAtASpeed",
    "StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
    "StraightBevelSunGearCompoundModalAnalysisAtASpeed",
    "SynchroniserCompoundModalAnalysisAtASpeed",
    "SynchroniserHalfCompoundModalAnalysisAtASpeed",
    "SynchroniserPartCompoundModalAnalysisAtASpeed",
    "SynchroniserSleeveCompoundModalAnalysisAtASpeed",
    "TorqueConverterCompoundModalAnalysisAtASpeed",
    "TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
    "TorqueConverterPumpCompoundModalAnalysisAtASpeed",
    "TorqueConverterTurbineCompoundModalAnalysisAtASpeed",
    "UnbalancedMassCompoundModalAnalysisAtASpeed",
    "VirtualComponentCompoundModalAnalysisAtASpeed",
    "WormGearCompoundModalAnalysisAtASpeed",
    "WormGearMeshCompoundModalAnalysisAtASpeed",
    "WormGearSetCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearMeshCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
)
