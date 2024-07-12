"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7291 import AbstractAssemblyAdvancedSystemDeflection
    from ._7292 import AbstractShaftAdvancedSystemDeflection
    from ._7293 import AbstractShaftOrHousingAdvancedSystemDeflection
    from ._7294 import (
        AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection,
    )
    from ._7295 import AdvancedSystemDeflection
    from ._7296 import AdvancedSystemDeflectionOptions
    from ._7297 import AdvancedSystemDeflectionSubAnalysis
    from ._7298 import AGMAGleasonConicalGearAdvancedSystemDeflection
    from ._7299 import AGMAGleasonConicalGearMeshAdvancedSystemDeflection
    from ._7300 import AGMAGleasonConicalGearSetAdvancedSystemDeflection
    from ._7301 import AssemblyAdvancedSystemDeflection
    from ._7302 import BearingAdvancedSystemDeflection
    from ._7303 import BeltConnectionAdvancedSystemDeflection
    from ._7304 import BeltDriveAdvancedSystemDeflection
    from ._7305 import BevelDifferentialGearAdvancedSystemDeflection
    from ._7306 import BevelDifferentialGearMeshAdvancedSystemDeflection
    from ._7307 import BevelDifferentialGearSetAdvancedSystemDeflection
    from ._7308 import BevelDifferentialPlanetGearAdvancedSystemDeflection
    from ._7309 import BevelDifferentialSunGearAdvancedSystemDeflection
    from ._7310 import BevelGearAdvancedSystemDeflection
    from ._7311 import BevelGearMeshAdvancedSystemDeflection
    from ._7312 import BevelGearSetAdvancedSystemDeflection
    from ._7313 import BoltAdvancedSystemDeflection
    from ._7314 import BoltedJointAdvancedSystemDeflection
    from ._7315 import ClutchAdvancedSystemDeflection
    from ._7316 import ClutchConnectionAdvancedSystemDeflection
    from ._7317 import ClutchHalfAdvancedSystemDeflection
    from ._7318 import CoaxialConnectionAdvancedSystemDeflection
    from ._7319 import ComponentAdvancedSystemDeflection
    from ._7320 import ConceptCouplingAdvancedSystemDeflection
    from ._7321 import ConceptCouplingConnectionAdvancedSystemDeflection
    from ._7322 import ConceptCouplingHalfAdvancedSystemDeflection
    from ._7323 import ConceptGearAdvancedSystemDeflection
    from ._7324 import ConceptGearMeshAdvancedSystemDeflection
    from ._7325 import ConceptGearSetAdvancedSystemDeflection
    from ._7326 import ConicalGearAdvancedSystemDeflection
    from ._7327 import ConicalGearMeshAdvancedSystemDeflection
    from ._7328 import ConicalGearSetAdvancedSystemDeflection
    from ._7329 import ConnectionAdvancedSystemDeflection
    from ._7330 import ConnectorAdvancedSystemDeflection
    from ._7331 import ContactChartPerToothPass
    from ._7332 import CouplingAdvancedSystemDeflection
    from ._7333 import CouplingConnectionAdvancedSystemDeflection
    from ._7334 import CouplingHalfAdvancedSystemDeflection
    from ._7335 import CVTAdvancedSystemDeflection
    from ._7336 import CVTBeltConnectionAdvancedSystemDeflection
    from ._7337 import CVTPulleyAdvancedSystemDeflection
    from ._7338 import CycloidalAssemblyAdvancedSystemDeflection
    from ._7339 import CycloidalDiscAdvancedSystemDeflection
    from ._7340 import CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
    from ._7341 import CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
    from ._7342 import CylindricalGearAdvancedSystemDeflection
    from ._7343 import CylindricalGearMeshAdvancedSystemDeflection
    from ._7344 import CylindricalGearSetAdvancedSystemDeflection
    from ._7345 import CylindricalMeshedGearAdvancedSystemDeflection
    from ._7346 import CylindricalPlanetGearAdvancedSystemDeflection
    from ._7347 import DatumAdvancedSystemDeflection
    from ._7348 import ExternalCADModelAdvancedSystemDeflection
    from ._7349 import FaceGearAdvancedSystemDeflection
    from ._7350 import FaceGearMeshAdvancedSystemDeflection
    from ._7351 import FaceGearSetAdvancedSystemDeflection
    from ._7352 import FEPartAdvancedSystemDeflection
    from ._7353 import FlexiblePinAssemblyAdvancedSystemDeflection
    from ._7354 import GearAdvancedSystemDeflection
    from ._7355 import GearMeshAdvancedSystemDeflection
    from ._7356 import GearSetAdvancedSystemDeflection
    from ._7357 import GuideDxfModelAdvancedSystemDeflection
    from ._7358 import HypoidGearAdvancedSystemDeflection
    from ._7359 import HypoidGearMeshAdvancedSystemDeflection
    from ._7360 import HypoidGearSetAdvancedSystemDeflection
    from ._7361 import InterMountableComponentConnectionAdvancedSystemDeflection
    from ._7362 import KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
    from ._7363 import KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
    from ._7364 import KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
    from ._7365 import KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
    from ._7366 import KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
    from ._7367 import KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
    from ._7368 import KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
    from ._7369 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection,
    )
    from ._7370 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection,
    )
    from ._7371 import UseLtcaInAsdOption
    from ._7372 import MassDiscAdvancedSystemDeflection
    from ._7373 import MeasurementComponentAdvancedSystemDeflection
    from ._7374 import MountableComponentAdvancedSystemDeflection
    from ._7375 import OilSealAdvancedSystemDeflection
    from ._7376 import PartAdvancedSystemDeflection
    from ._7377 import PartToPartShearCouplingAdvancedSystemDeflection
    from ._7378 import PartToPartShearCouplingConnectionAdvancedSystemDeflection
    from ._7379 import PartToPartShearCouplingHalfAdvancedSystemDeflection
    from ._7380 import PlanetaryConnectionAdvancedSystemDeflection
    from ._7381 import PlanetaryGearSetAdvancedSystemDeflection
    from ._7382 import PlanetCarrierAdvancedSystemDeflection
    from ._7383 import PointLoadAdvancedSystemDeflection
    from ._7384 import PowerLoadAdvancedSystemDeflection
    from ._7385 import PulleyAdvancedSystemDeflection
    from ._7386 import RingPinsAdvancedSystemDeflection
    from ._7387 import RingPinsToDiscConnectionAdvancedSystemDeflection
    from ._7388 import RollingRingAdvancedSystemDeflection
    from ._7389 import RollingRingAssemblyAdvancedSystemDeflection
    from ._7390 import RollingRingConnectionAdvancedSystemDeflection
    from ._7391 import RootAssemblyAdvancedSystemDeflection
    from ._7392 import ShaftAdvancedSystemDeflection
    from ._7393 import ShaftHubConnectionAdvancedSystemDeflection
    from ._7394 import ShaftToMountableComponentConnectionAdvancedSystemDeflection
    from ._7395 import SpecialisedAssemblyAdvancedSystemDeflection
    from ._7396 import SpiralBevelGearAdvancedSystemDeflection
    from ._7397 import SpiralBevelGearMeshAdvancedSystemDeflection
    from ._7398 import SpiralBevelGearSetAdvancedSystemDeflection
    from ._7399 import SpringDamperAdvancedSystemDeflection
    from ._7400 import SpringDamperConnectionAdvancedSystemDeflection
    from ._7401 import SpringDamperHalfAdvancedSystemDeflection
    from ._7402 import StraightBevelDiffGearAdvancedSystemDeflection
    from ._7403 import StraightBevelDiffGearMeshAdvancedSystemDeflection
    from ._7404 import StraightBevelDiffGearSetAdvancedSystemDeflection
    from ._7405 import StraightBevelGearAdvancedSystemDeflection
    from ._7406 import StraightBevelGearMeshAdvancedSystemDeflection
    from ._7407 import StraightBevelGearSetAdvancedSystemDeflection
    from ._7408 import StraightBevelPlanetGearAdvancedSystemDeflection
    from ._7409 import StraightBevelSunGearAdvancedSystemDeflection
    from ._7410 import SynchroniserAdvancedSystemDeflection
    from ._7411 import SynchroniserHalfAdvancedSystemDeflection
    from ._7412 import SynchroniserPartAdvancedSystemDeflection
    from ._7413 import SynchroniserSleeveAdvancedSystemDeflection
    from ._7414 import TorqueConverterAdvancedSystemDeflection
    from ._7415 import TorqueConverterConnectionAdvancedSystemDeflection
    from ._7416 import TorqueConverterPumpAdvancedSystemDeflection
    from ._7417 import TorqueConverterTurbineAdvancedSystemDeflection
    from ._7418 import TransmissionErrorToOtherPowerLoad
    from ._7419 import UnbalancedMassAdvancedSystemDeflection
    from ._7420 import VirtualComponentAdvancedSystemDeflection
    from ._7421 import WormGearAdvancedSystemDeflection
    from ._7422 import WormGearMeshAdvancedSystemDeflection
    from ._7423 import WormGearSetAdvancedSystemDeflection
    from ._7424 import ZerolBevelGearAdvancedSystemDeflection
    from ._7425 import ZerolBevelGearMeshAdvancedSystemDeflection
    from ._7426 import ZerolBevelGearSetAdvancedSystemDeflection
else:
    import_structure = {
        "_7291": ["AbstractAssemblyAdvancedSystemDeflection"],
        "_7292": ["AbstractShaftAdvancedSystemDeflection"],
        "_7293": ["AbstractShaftOrHousingAdvancedSystemDeflection"],
        "_7294": [
            "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
        ],
        "_7295": ["AdvancedSystemDeflection"],
        "_7296": ["AdvancedSystemDeflectionOptions"],
        "_7297": ["AdvancedSystemDeflectionSubAnalysis"],
        "_7298": ["AGMAGleasonConicalGearAdvancedSystemDeflection"],
        "_7299": ["AGMAGleasonConicalGearMeshAdvancedSystemDeflection"],
        "_7300": ["AGMAGleasonConicalGearSetAdvancedSystemDeflection"],
        "_7301": ["AssemblyAdvancedSystemDeflection"],
        "_7302": ["BearingAdvancedSystemDeflection"],
        "_7303": ["BeltConnectionAdvancedSystemDeflection"],
        "_7304": ["BeltDriveAdvancedSystemDeflection"],
        "_7305": ["BevelDifferentialGearAdvancedSystemDeflection"],
        "_7306": ["BevelDifferentialGearMeshAdvancedSystemDeflection"],
        "_7307": ["BevelDifferentialGearSetAdvancedSystemDeflection"],
        "_7308": ["BevelDifferentialPlanetGearAdvancedSystemDeflection"],
        "_7309": ["BevelDifferentialSunGearAdvancedSystemDeflection"],
        "_7310": ["BevelGearAdvancedSystemDeflection"],
        "_7311": ["BevelGearMeshAdvancedSystemDeflection"],
        "_7312": ["BevelGearSetAdvancedSystemDeflection"],
        "_7313": ["BoltAdvancedSystemDeflection"],
        "_7314": ["BoltedJointAdvancedSystemDeflection"],
        "_7315": ["ClutchAdvancedSystemDeflection"],
        "_7316": ["ClutchConnectionAdvancedSystemDeflection"],
        "_7317": ["ClutchHalfAdvancedSystemDeflection"],
        "_7318": ["CoaxialConnectionAdvancedSystemDeflection"],
        "_7319": ["ComponentAdvancedSystemDeflection"],
        "_7320": ["ConceptCouplingAdvancedSystemDeflection"],
        "_7321": ["ConceptCouplingConnectionAdvancedSystemDeflection"],
        "_7322": ["ConceptCouplingHalfAdvancedSystemDeflection"],
        "_7323": ["ConceptGearAdvancedSystemDeflection"],
        "_7324": ["ConceptGearMeshAdvancedSystemDeflection"],
        "_7325": ["ConceptGearSetAdvancedSystemDeflection"],
        "_7326": ["ConicalGearAdvancedSystemDeflection"],
        "_7327": ["ConicalGearMeshAdvancedSystemDeflection"],
        "_7328": ["ConicalGearSetAdvancedSystemDeflection"],
        "_7329": ["ConnectionAdvancedSystemDeflection"],
        "_7330": ["ConnectorAdvancedSystemDeflection"],
        "_7331": ["ContactChartPerToothPass"],
        "_7332": ["CouplingAdvancedSystemDeflection"],
        "_7333": ["CouplingConnectionAdvancedSystemDeflection"],
        "_7334": ["CouplingHalfAdvancedSystemDeflection"],
        "_7335": ["CVTAdvancedSystemDeflection"],
        "_7336": ["CVTBeltConnectionAdvancedSystemDeflection"],
        "_7337": ["CVTPulleyAdvancedSystemDeflection"],
        "_7338": ["CycloidalAssemblyAdvancedSystemDeflection"],
        "_7339": ["CycloidalDiscAdvancedSystemDeflection"],
        "_7340": ["CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"],
        "_7341": ["CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection"],
        "_7342": ["CylindricalGearAdvancedSystemDeflection"],
        "_7343": ["CylindricalGearMeshAdvancedSystemDeflection"],
        "_7344": ["CylindricalGearSetAdvancedSystemDeflection"],
        "_7345": ["CylindricalMeshedGearAdvancedSystemDeflection"],
        "_7346": ["CylindricalPlanetGearAdvancedSystemDeflection"],
        "_7347": ["DatumAdvancedSystemDeflection"],
        "_7348": ["ExternalCADModelAdvancedSystemDeflection"],
        "_7349": ["FaceGearAdvancedSystemDeflection"],
        "_7350": ["FaceGearMeshAdvancedSystemDeflection"],
        "_7351": ["FaceGearSetAdvancedSystemDeflection"],
        "_7352": ["FEPartAdvancedSystemDeflection"],
        "_7353": ["FlexiblePinAssemblyAdvancedSystemDeflection"],
        "_7354": ["GearAdvancedSystemDeflection"],
        "_7355": ["GearMeshAdvancedSystemDeflection"],
        "_7356": ["GearSetAdvancedSystemDeflection"],
        "_7357": ["GuideDxfModelAdvancedSystemDeflection"],
        "_7358": ["HypoidGearAdvancedSystemDeflection"],
        "_7359": ["HypoidGearMeshAdvancedSystemDeflection"],
        "_7360": ["HypoidGearSetAdvancedSystemDeflection"],
        "_7361": ["InterMountableComponentConnectionAdvancedSystemDeflection"],
        "_7362": ["KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"],
        "_7363": ["KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection"],
        "_7364": ["KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"],
        "_7365": ["KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection"],
        "_7366": ["KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection"],
        "_7367": ["KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection"],
        "_7368": ["KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection"],
        "_7369": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ],
        "_7370": ["KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection"],
        "_7371": ["UseLtcaInAsdOption"],
        "_7372": ["MassDiscAdvancedSystemDeflection"],
        "_7373": ["MeasurementComponentAdvancedSystemDeflection"],
        "_7374": ["MountableComponentAdvancedSystemDeflection"],
        "_7375": ["OilSealAdvancedSystemDeflection"],
        "_7376": ["PartAdvancedSystemDeflection"],
        "_7377": ["PartToPartShearCouplingAdvancedSystemDeflection"],
        "_7378": ["PartToPartShearCouplingConnectionAdvancedSystemDeflection"],
        "_7379": ["PartToPartShearCouplingHalfAdvancedSystemDeflection"],
        "_7380": ["PlanetaryConnectionAdvancedSystemDeflection"],
        "_7381": ["PlanetaryGearSetAdvancedSystemDeflection"],
        "_7382": ["PlanetCarrierAdvancedSystemDeflection"],
        "_7383": ["PointLoadAdvancedSystemDeflection"],
        "_7384": ["PowerLoadAdvancedSystemDeflection"],
        "_7385": ["PulleyAdvancedSystemDeflection"],
        "_7386": ["RingPinsAdvancedSystemDeflection"],
        "_7387": ["RingPinsToDiscConnectionAdvancedSystemDeflection"],
        "_7388": ["RollingRingAdvancedSystemDeflection"],
        "_7389": ["RollingRingAssemblyAdvancedSystemDeflection"],
        "_7390": ["RollingRingConnectionAdvancedSystemDeflection"],
        "_7391": ["RootAssemblyAdvancedSystemDeflection"],
        "_7392": ["ShaftAdvancedSystemDeflection"],
        "_7393": ["ShaftHubConnectionAdvancedSystemDeflection"],
        "_7394": ["ShaftToMountableComponentConnectionAdvancedSystemDeflection"],
        "_7395": ["SpecialisedAssemblyAdvancedSystemDeflection"],
        "_7396": ["SpiralBevelGearAdvancedSystemDeflection"],
        "_7397": ["SpiralBevelGearMeshAdvancedSystemDeflection"],
        "_7398": ["SpiralBevelGearSetAdvancedSystemDeflection"],
        "_7399": ["SpringDamperAdvancedSystemDeflection"],
        "_7400": ["SpringDamperConnectionAdvancedSystemDeflection"],
        "_7401": ["SpringDamperHalfAdvancedSystemDeflection"],
        "_7402": ["StraightBevelDiffGearAdvancedSystemDeflection"],
        "_7403": ["StraightBevelDiffGearMeshAdvancedSystemDeflection"],
        "_7404": ["StraightBevelDiffGearSetAdvancedSystemDeflection"],
        "_7405": ["StraightBevelGearAdvancedSystemDeflection"],
        "_7406": ["StraightBevelGearMeshAdvancedSystemDeflection"],
        "_7407": ["StraightBevelGearSetAdvancedSystemDeflection"],
        "_7408": ["StraightBevelPlanetGearAdvancedSystemDeflection"],
        "_7409": ["StraightBevelSunGearAdvancedSystemDeflection"],
        "_7410": ["SynchroniserAdvancedSystemDeflection"],
        "_7411": ["SynchroniserHalfAdvancedSystemDeflection"],
        "_7412": ["SynchroniserPartAdvancedSystemDeflection"],
        "_7413": ["SynchroniserSleeveAdvancedSystemDeflection"],
        "_7414": ["TorqueConverterAdvancedSystemDeflection"],
        "_7415": ["TorqueConverterConnectionAdvancedSystemDeflection"],
        "_7416": ["TorqueConverterPumpAdvancedSystemDeflection"],
        "_7417": ["TorqueConverterTurbineAdvancedSystemDeflection"],
        "_7418": ["TransmissionErrorToOtherPowerLoad"],
        "_7419": ["UnbalancedMassAdvancedSystemDeflection"],
        "_7420": ["VirtualComponentAdvancedSystemDeflection"],
        "_7421": ["WormGearAdvancedSystemDeflection"],
        "_7422": ["WormGearMeshAdvancedSystemDeflection"],
        "_7423": ["WormGearSetAdvancedSystemDeflection"],
        "_7424": ["ZerolBevelGearAdvancedSystemDeflection"],
        "_7425": ["ZerolBevelGearMeshAdvancedSystemDeflection"],
        "_7426": ["ZerolBevelGearSetAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedSystemDeflection",
    "AbstractShaftAdvancedSystemDeflection",
    "AbstractShaftOrHousingAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "AdvancedSystemDeflection",
    "AdvancedSystemDeflectionOptions",
    "AdvancedSystemDeflectionSubAnalysis",
    "AGMAGleasonConicalGearAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetAdvancedSystemDeflection",
    "AssemblyAdvancedSystemDeflection",
    "BearingAdvancedSystemDeflection",
    "BeltConnectionAdvancedSystemDeflection",
    "BeltDriveAdvancedSystemDeflection",
    "BevelDifferentialGearAdvancedSystemDeflection",
    "BevelDifferentialGearMeshAdvancedSystemDeflection",
    "BevelDifferentialGearSetAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearAdvancedSystemDeflection",
    "BevelDifferentialSunGearAdvancedSystemDeflection",
    "BevelGearAdvancedSystemDeflection",
    "BevelGearMeshAdvancedSystemDeflection",
    "BevelGearSetAdvancedSystemDeflection",
    "BoltAdvancedSystemDeflection",
    "BoltedJointAdvancedSystemDeflection",
    "ClutchAdvancedSystemDeflection",
    "ClutchConnectionAdvancedSystemDeflection",
    "ClutchHalfAdvancedSystemDeflection",
    "CoaxialConnectionAdvancedSystemDeflection",
    "ComponentAdvancedSystemDeflection",
    "ConceptCouplingAdvancedSystemDeflection",
    "ConceptCouplingConnectionAdvancedSystemDeflection",
    "ConceptCouplingHalfAdvancedSystemDeflection",
    "ConceptGearAdvancedSystemDeflection",
    "ConceptGearMeshAdvancedSystemDeflection",
    "ConceptGearSetAdvancedSystemDeflection",
    "ConicalGearAdvancedSystemDeflection",
    "ConicalGearMeshAdvancedSystemDeflection",
    "ConicalGearSetAdvancedSystemDeflection",
    "ConnectionAdvancedSystemDeflection",
    "ConnectorAdvancedSystemDeflection",
    "ContactChartPerToothPass",
    "CouplingAdvancedSystemDeflection",
    "CouplingConnectionAdvancedSystemDeflection",
    "CouplingHalfAdvancedSystemDeflection",
    "CVTAdvancedSystemDeflection",
    "CVTBeltConnectionAdvancedSystemDeflection",
    "CVTPulleyAdvancedSystemDeflection",
    "CycloidalAssemblyAdvancedSystemDeflection",
    "CycloidalDiscAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection",
    "CylindricalGearAdvancedSystemDeflection",
    "CylindricalGearMeshAdvancedSystemDeflection",
    "CylindricalGearSetAdvancedSystemDeflection",
    "CylindricalMeshedGearAdvancedSystemDeflection",
    "CylindricalPlanetGearAdvancedSystemDeflection",
    "DatumAdvancedSystemDeflection",
    "ExternalCADModelAdvancedSystemDeflection",
    "FaceGearAdvancedSystemDeflection",
    "FaceGearMeshAdvancedSystemDeflection",
    "FaceGearSetAdvancedSystemDeflection",
    "FEPartAdvancedSystemDeflection",
    "FlexiblePinAssemblyAdvancedSystemDeflection",
    "GearAdvancedSystemDeflection",
    "GearMeshAdvancedSystemDeflection",
    "GearSetAdvancedSystemDeflection",
    "GuideDxfModelAdvancedSystemDeflection",
    "HypoidGearAdvancedSystemDeflection",
    "HypoidGearMeshAdvancedSystemDeflection",
    "HypoidGearSetAdvancedSystemDeflection",
    "InterMountableComponentConnectionAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
    "UseLtcaInAsdOption",
    "MassDiscAdvancedSystemDeflection",
    "MeasurementComponentAdvancedSystemDeflection",
    "MountableComponentAdvancedSystemDeflection",
    "OilSealAdvancedSystemDeflection",
    "PartAdvancedSystemDeflection",
    "PartToPartShearCouplingAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfAdvancedSystemDeflection",
    "PlanetaryConnectionAdvancedSystemDeflection",
    "PlanetaryGearSetAdvancedSystemDeflection",
    "PlanetCarrierAdvancedSystemDeflection",
    "PointLoadAdvancedSystemDeflection",
    "PowerLoadAdvancedSystemDeflection",
    "PulleyAdvancedSystemDeflection",
    "RingPinsAdvancedSystemDeflection",
    "RingPinsToDiscConnectionAdvancedSystemDeflection",
    "RollingRingAdvancedSystemDeflection",
    "RollingRingAssemblyAdvancedSystemDeflection",
    "RollingRingConnectionAdvancedSystemDeflection",
    "RootAssemblyAdvancedSystemDeflection",
    "ShaftAdvancedSystemDeflection",
    "ShaftHubConnectionAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "SpecialisedAssemblyAdvancedSystemDeflection",
    "SpiralBevelGearAdvancedSystemDeflection",
    "SpiralBevelGearMeshAdvancedSystemDeflection",
    "SpiralBevelGearSetAdvancedSystemDeflection",
    "SpringDamperAdvancedSystemDeflection",
    "SpringDamperConnectionAdvancedSystemDeflection",
    "SpringDamperHalfAdvancedSystemDeflection",
    "StraightBevelDiffGearAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshAdvancedSystemDeflection",
    "StraightBevelDiffGearSetAdvancedSystemDeflection",
    "StraightBevelGearAdvancedSystemDeflection",
    "StraightBevelGearMeshAdvancedSystemDeflection",
    "StraightBevelGearSetAdvancedSystemDeflection",
    "StraightBevelPlanetGearAdvancedSystemDeflection",
    "StraightBevelSunGearAdvancedSystemDeflection",
    "SynchroniserAdvancedSystemDeflection",
    "SynchroniserHalfAdvancedSystemDeflection",
    "SynchroniserPartAdvancedSystemDeflection",
    "SynchroniserSleeveAdvancedSystemDeflection",
    "TorqueConverterAdvancedSystemDeflection",
    "TorqueConverterConnectionAdvancedSystemDeflection",
    "TorqueConverterPumpAdvancedSystemDeflection",
    "TorqueConverterTurbineAdvancedSystemDeflection",
    "TransmissionErrorToOtherPowerLoad",
    "UnbalancedMassAdvancedSystemDeflection",
    "VirtualComponentAdvancedSystemDeflection",
    "WormGearAdvancedSystemDeflection",
    "WormGearMeshAdvancedSystemDeflection",
    "WormGearSetAdvancedSystemDeflection",
    "ZerolBevelGearAdvancedSystemDeflection",
    "ZerolBevelGearMeshAdvancedSystemDeflection",
    "ZerolBevelGearSetAdvancedSystemDeflection",
)
