"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4464 import AbstractAssemblyCompoundParametricStudyTool
    from ._4465 import AbstractShaftCompoundParametricStudyTool
    from ._4466 import AbstractShaftOrHousingCompoundParametricStudyTool
    from ._4467 import (
        AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool,
    )
    from ._4468 import AGMAGleasonConicalGearCompoundParametricStudyTool
    from ._4469 import AGMAGleasonConicalGearMeshCompoundParametricStudyTool
    from ._4470 import AGMAGleasonConicalGearSetCompoundParametricStudyTool
    from ._4471 import AssemblyCompoundParametricStudyTool
    from ._4472 import BearingCompoundParametricStudyTool
    from ._4473 import BeltConnectionCompoundParametricStudyTool
    from ._4474 import BeltDriveCompoundParametricStudyTool
    from ._4475 import BevelDifferentialGearCompoundParametricStudyTool
    from ._4476 import BevelDifferentialGearMeshCompoundParametricStudyTool
    from ._4477 import BevelDifferentialGearSetCompoundParametricStudyTool
    from ._4478 import BevelDifferentialPlanetGearCompoundParametricStudyTool
    from ._4479 import BevelDifferentialSunGearCompoundParametricStudyTool
    from ._4480 import BevelGearCompoundParametricStudyTool
    from ._4481 import BevelGearMeshCompoundParametricStudyTool
    from ._4482 import BevelGearSetCompoundParametricStudyTool
    from ._4483 import BoltCompoundParametricStudyTool
    from ._4484 import BoltedJointCompoundParametricStudyTool
    from ._4485 import ClutchCompoundParametricStudyTool
    from ._4486 import ClutchConnectionCompoundParametricStudyTool
    from ._4487 import ClutchHalfCompoundParametricStudyTool
    from ._4488 import CoaxialConnectionCompoundParametricStudyTool
    from ._4489 import ComponentCompoundParametricStudyTool
    from ._4490 import ConceptCouplingCompoundParametricStudyTool
    from ._4491 import ConceptCouplingConnectionCompoundParametricStudyTool
    from ._4492 import ConceptCouplingHalfCompoundParametricStudyTool
    from ._4493 import ConceptGearCompoundParametricStudyTool
    from ._4494 import ConceptGearMeshCompoundParametricStudyTool
    from ._4495 import ConceptGearSetCompoundParametricStudyTool
    from ._4496 import ConicalGearCompoundParametricStudyTool
    from ._4497 import ConicalGearMeshCompoundParametricStudyTool
    from ._4498 import ConicalGearSetCompoundParametricStudyTool
    from ._4499 import ConnectionCompoundParametricStudyTool
    from ._4500 import ConnectorCompoundParametricStudyTool
    from ._4501 import CouplingCompoundParametricStudyTool
    from ._4502 import CouplingConnectionCompoundParametricStudyTool
    from ._4503 import CouplingHalfCompoundParametricStudyTool
    from ._4504 import CVTBeltConnectionCompoundParametricStudyTool
    from ._4505 import CVTCompoundParametricStudyTool
    from ._4506 import CVTPulleyCompoundParametricStudyTool
    from ._4507 import CycloidalAssemblyCompoundParametricStudyTool
    from ._4508 import CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
    from ._4509 import CycloidalDiscCompoundParametricStudyTool
    from ._4510 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool,
    )
    from ._4511 import CylindricalGearCompoundParametricStudyTool
    from ._4512 import CylindricalGearMeshCompoundParametricStudyTool
    from ._4513 import CylindricalGearSetCompoundParametricStudyTool
    from ._4514 import CylindricalPlanetGearCompoundParametricStudyTool
    from ._4515 import DatumCompoundParametricStudyTool
    from ._4516 import ExternalCADModelCompoundParametricStudyTool
    from ._4517 import FaceGearCompoundParametricStudyTool
    from ._4518 import FaceGearMeshCompoundParametricStudyTool
    from ._4519 import FaceGearSetCompoundParametricStudyTool
    from ._4520 import FEPartCompoundParametricStudyTool
    from ._4521 import FlexiblePinAssemblyCompoundParametricStudyTool
    from ._4522 import GearCompoundParametricStudyTool
    from ._4523 import GearMeshCompoundParametricStudyTool
    from ._4524 import GearSetCompoundParametricStudyTool
    from ._4525 import GuideDxfModelCompoundParametricStudyTool
    from ._4526 import HypoidGearCompoundParametricStudyTool
    from ._4527 import HypoidGearMeshCompoundParametricStudyTool
    from ._4528 import HypoidGearSetCompoundParametricStudyTool
    from ._4529 import InterMountableComponentConnectionCompoundParametricStudyTool
    from ._4530 import KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
    from ._4531 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool,
    )
    from ._4532 import KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
    from ._4533 import KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
    from ._4534 import KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
    from ._4535 import KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
    from ._4536 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool,
    )
    from ._4537 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool,
    )
    from ._4538 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool,
    )
    from ._4539 import MassDiscCompoundParametricStudyTool
    from ._4540 import MeasurementComponentCompoundParametricStudyTool
    from ._4541 import MountableComponentCompoundParametricStudyTool
    from ._4542 import OilSealCompoundParametricStudyTool
    from ._4543 import PartCompoundParametricStudyTool
    from ._4544 import PartToPartShearCouplingCompoundParametricStudyTool
    from ._4545 import PartToPartShearCouplingConnectionCompoundParametricStudyTool
    from ._4546 import PartToPartShearCouplingHalfCompoundParametricStudyTool
    from ._4547 import PlanetaryConnectionCompoundParametricStudyTool
    from ._4548 import PlanetaryGearSetCompoundParametricStudyTool
    from ._4549 import PlanetCarrierCompoundParametricStudyTool
    from ._4550 import PointLoadCompoundParametricStudyTool
    from ._4551 import PowerLoadCompoundParametricStudyTool
    from ._4552 import PulleyCompoundParametricStudyTool
    from ._4553 import RingPinsCompoundParametricStudyTool
    from ._4554 import RingPinsToDiscConnectionCompoundParametricStudyTool
    from ._4555 import RollingRingAssemblyCompoundParametricStudyTool
    from ._4556 import RollingRingCompoundParametricStudyTool
    from ._4557 import RollingRingConnectionCompoundParametricStudyTool
    from ._4558 import RootAssemblyCompoundParametricStudyTool
    from ._4559 import ShaftCompoundParametricStudyTool
    from ._4560 import ShaftHubConnectionCompoundParametricStudyTool
    from ._4561 import ShaftToMountableComponentConnectionCompoundParametricStudyTool
    from ._4562 import SpecialisedAssemblyCompoundParametricStudyTool
    from ._4563 import SpiralBevelGearCompoundParametricStudyTool
    from ._4564 import SpiralBevelGearMeshCompoundParametricStudyTool
    from ._4565 import SpiralBevelGearSetCompoundParametricStudyTool
    from ._4566 import SpringDamperCompoundParametricStudyTool
    from ._4567 import SpringDamperConnectionCompoundParametricStudyTool
    from ._4568 import SpringDamperHalfCompoundParametricStudyTool
    from ._4569 import StraightBevelDiffGearCompoundParametricStudyTool
    from ._4570 import StraightBevelDiffGearMeshCompoundParametricStudyTool
    from ._4571 import StraightBevelDiffGearSetCompoundParametricStudyTool
    from ._4572 import StraightBevelGearCompoundParametricStudyTool
    from ._4573 import StraightBevelGearMeshCompoundParametricStudyTool
    from ._4574 import StraightBevelGearSetCompoundParametricStudyTool
    from ._4575 import StraightBevelPlanetGearCompoundParametricStudyTool
    from ._4576 import StraightBevelSunGearCompoundParametricStudyTool
    from ._4577 import SynchroniserCompoundParametricStudyTool
    from ._4578 import SynchroniserHalfCompoundParametricStudyTool
    from ._4579 import SynchroniserPartCompoundParametricStudyTool
    from ._4580 import SynchroniserSleeveCompoundParametricStudyTool
    from ._4581 import TorqueConverterCompoundParametricStudyTool
    from ._4582 import TorqueConverterConnectionCompoundParametricStudyTool
    from ._4583 import TorqueConverterPumpCompoundParametricStudyTool
    from ._4584 import TorqueConverterTurbineCompoundParametricStudyTool
    from ._4585 import UnbalancedMassCompoundParametricStudyTool
    from ._4586 import VirtualComponentCompoundParametricStudyTool
    from ._4587 import WormGearCompoundParametricStudyTool
    from ._4588 import WormGearMeshCompoundParametricStudyTool
    from ._4589 import WormGearSetCompoundParametricStudyTool
    from ._4590 import ZerolBevelGearCompoundParametricStudyTool
    from ._4591 import ZerolBevelGearMeshCompoundParametricStudyTool
    from ._4592 import ZerolBevelGearSetCompoundParametricStudyTool
else:
    import_structure = {
        "_4464": ["AbstractAssemblyCompoundParametricStudyTool"],
        "_4465": ["AbstractShaftCompoundParametricStudyTool"],
        "_4466": ["AbstractShaftOrHousingCompoundParametricStudyTool"],
        "_4467": [
            "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool"
        ],
        "_4468": ["AGMAGleasonConicalGearCompoundParametricStudyTool"],
        "_4469": ["AGMAGleasonConicalGearMeshCompoundParametricStudyTool"],
        "_4470": ["AGMAGleasonConicalGearSetCompoundParametricStudyTool"],
        "_4471": ["AssemblyCompoundParametricStudyTool"],
        "_4472": ["BearingCompoundParametricStudyTool"],
        "_4473": ["BeltConnectionCompoundParametricStudyTool"],
        "_4474": ["BeltDriveCompoundParametricStudyTool"],
        "_4475": ["BevelDifferentialGearCompoundParametricStudyTool"],
        "_4476": ["BevelDifferentialGearMeshCompoundParametricStudyTool"],
        "_4477": ["BevelDifferentialGearSetCompoundParametricStudyTool"],
        "_4478": ["BevelDifferentialPlanetGearCompoundParametricStudyTool"],
        "_4479": ["BevelDifferentialSunGearCompoundParametricStudyTool"],
        "_4480": ["BevelGearCompoundParametricStudyTool"],
        "_4481": ["BevelGearMeshCompoundParametricStudyTool"],
        "_4482": ["BevelGearSetCompoundParametricStudyTool"],
        "_4483": ["BoltCompoundParametricStudyTool"],
        "_4484": ["BoltedJointCompoundParametricStudyTool"],
        "_4485": ["ClutchCompoundParametricStudyTool"],
        "_4486": ["ClutchConnectionCompoundParametricStudyTool"],
        "_4487": ["ClutchHalfCompoundParametricStudyTool"],
        "_4488": ["CoaxialConnectionCompoundParametricStudyTool"],
        "_4489": ["ComponentCompoundParametricStudyTool"],
        "_4490": ["ConceptCouplingCompoundParametricStudyTool"],
        "_4491": ["ConceptCouplingConnectionCompoundParametricStudyTool"],
        "_4492": ["ConceptCouplingHalfCompoundParametricStudyTool"],
        "_4493": ["ConceptGearCompoundParametricStudyTool"],
        "_4494": ["ConceptGearMeshCompoundParametricStudyTool"],
        "_4495": ["ConceptGearSetCompoundParametricStudyTool"],
        "_4496": ["ConicalGearCompoundParametricStudyTool"],
        "_4497": ["ConicalGearMeshCompoundParametricStudyTool"],
        "_4498": ["ConicalGearSetCompoundParametricStudyTool"],
        "_4499": ["ConnectionCompoundParametricStudyTool"],
        "_4500": ["ConnectorCompoundParametricStudyTool"],
        "_4501": ["CouplingCompoundParametricStudyTool"],
        "_4502": ["CouplingConnectionCompoundParametricStudyTool"],
        "_4503": ["CouplingHalfCompoundParametricStudyTool"],
        "_4504": ["CVTBeltConnectionCompoundParametricStudyTool"],
        "_4505": ["CVTCompoundParametricStudyTool"],
        "_4506": ["CVTPulleyCompoundParametricStudyTool"],
        "_4507": ["CycloidalAssemblyCompoundParametricStudyTool"],
        "_4508": ["CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"],
        "_4509": ["CycloidalDiscCompoundParametricStudyTool"],
        "_4510": ["CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool"],
        "_4511": ["CylindricalGearCompoundParametricStudyTool"],
        "_4512": ["CylindricalGearMeshCompoundParametricStudyTool"],
        "_4513": ["CylindricalGearSetCompoundParametricStudyTool"],
        "_4514": ["CylindricalPlanetGearCompoundParametricStudyTool"],
        "_4515": ["DatumCompoundParametricStudyTool"],
        "_4516": ["ExternalCADModelCompoundParametricStudyTool"],
        "_4517": ["FaceGearCompoundParametricStudyTool"],
        "_4518": ["FaceGearMeshCompoundParametricStudyTool"],
        "_4519": ["FaceGearSetCompoundParametricStudyTool"],
        "_4520": ["FEPartCompoundParametricStudyTool"],
        "_4521": ["FlexiblePinAssemblyCompoundParametricStudyTool"],
        "_4522": ["GearCompoundParametricStudyTool"],
        "_4523": ["GearMeshCompoundParametricStudyTool"],
        "_4524": ["GearSetCompoundParametricStudyTool"],
        "_4525": ["GuideDxfModelCompoundParametricStudyTool"],
        "_4526": ["HypoidGearCompoundParametricStudyTool"],
        "_4527": ["HypoidGearMeshCompoundParametricStudyTool"],
        "_4528": ["HypoidGearSetCompoundParametricStudyTool"],
        "_4529": ["InterMountableComponentConnectionCompoundParametricStudyTool"],
        "_4530": ["KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool"],
        "_4531": ["KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool"],
        "_4532": ["KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool"],
        "_4533": ["KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"],
        "_4534": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool"],
        "_4535": ["KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool"],
        "_4536": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool"],
        "_4537": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool"
        ],
        "_4538": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool"
        ],
        "_4539": ["MassDiscCompoundParametricStudyTool"],
        "_4540": ["MeasurementComponentCompoundParametricStudyTool"],
        "_4541": ["MountableComponentCompoundParametricStudyTool"],
        "_4542": ["OilSealCompoundParametricStudyTool"],
        "_4543": ["PartCompoundParametricStudyTool"],
        "_4544": ["PartToPartShearCouplingCompoundParametricStudyTool"],
        "_4545": ["PartToPartShearCouplingConnectionCompoundParametricStudyTool"],
        "_4546": ["PartToPartShearCouplingHalfCompoundParametricStudyTool"],
        "_4547": ["PlanetaryConnectionCompoundParametricStudyTool"],
        "_4548": ["PlanetaryGearSetCompoundParametricStudyTool"],
        "_4549": ["PlanetCarrierCompoundParametricStudyTool"],
        "_4550": ["PointLoadCompoundParametricStudyTool"],
        "_4551": ["PowerLoadCompoundParametricStudyTool"],
        "_4552": ["PulleyCompoundParametricStudyTool"],
        "_4553": ["RingPinsCompoundParametricStudyTool"],
        "_4554": ["RingPinsToDiscConnectionCompoundParametricStudyTool"],
        "_4555": ["RollingRingAssemblyCompoundParametricStudyTool"],
        "_4556": ["RollingRingCompoundParametricStudyTool"],
        "_4557": ["RollingRingConnectionCompoundParametricStudyTool"],
        "_4558": ["RootAssemblyCompoundParametricStudyTool"],
        "_4559": ["ShaftCompoundParametricStudyTool"],
        "_4560": ["ShaftHubConnectionCompoundParametricStudyTool"],
        "_4561": ["ShaftToMountableComponentConnectionCompoundParametricStudyTool"],
        "_4562": ["SpecialisedAssemblyCompoundParametricStudyTool"],
        "_4563": ["SpiralBevelGearCompoundParametricStudyTool"],
        "_4564": ["SpiralBevelGearMeshCompoundParametricStudyTool"],
        "_4565": ["SpiralBevelGearSetCompoundParametricStudyTool"],
        "_4566": ["SpringDamperCompoundParametricStudyTool"],
        "_4567": ["SpringDamperConnectionCompoundParametricStudyTool"],
        "_4568": ["SpringDamperHalfCompoundParametricStudyTool"],
        "_4569": ["StraightBevelDiffGearCompoundParametricStudyTool"],
        "_4570": ["StraightBevelDiffGearMeshCompoundParametricStudyTool"],
        "_4571": ["StraightBevelDiffGearSetCompoundParametricStudyTool"],
        "_4572": ["StraightBevelGearCompoundParametricStudyTool"],
        "_4573": ["StraightBevelGearMeshCompoundParametricStudyTool"],
        "_4574": ["StraightBevelGearSetCompoundParametricStudyTool"],
        "_4575": ["StraightBevelPlanetGearCompoundParametricStudyTool"],
        "_4576": ["StraightBevelSunGearCompoundParametricStudyTool"],
        "_4577": ["SynchroniserCompoundParametricStudyTool"],
        "_4578": ["SynchroniserHalfCompoundParametricStudyTool"],
        "_4579": ["SynchroniserPartCompoundParametricStudyTool"],
        "_4580": ["SynchroniserSleeveCompoundParametricStudyTool"],
        "_4581": ["TorqueConverterCompoundParametricStudyTool"],
        "_4582": ["TorqueConverterConnectionCompoundParametricStudyTool"],
        "_4583": ["TorqueConverterPumpCompoundParametricStudyTool"],
        "_4584": ["TorqueConverterTurbineCompoundParametricStudyTool"],
        "_4585": ["UnbalancedMassCompoundParametricStudyTool"],
        "_4586": ["VirtualComponentCompoundParametricStudyTool"],
        "_4587": ["WormGearCompoundParametricStudyTool"],
        "_4588": ["WormGearMeshCompoundParametricStudyTool"],
        "_4589": ["WormGearSetCompoundParametricStudyTool"],
        "_4590": ["ZerolBevelGearCompoundParametricStudyTool"],
        "_4591": ["ZerolBevelGearMeshCompoundParametricStudyTool"],
        "_4592": ["ZerolBevelGearSetCompoundParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundParametricStudyTool",
    "AbstractShaftCompoundParametricStudyTool",
    "AbstractShaftOrHousingCompoundParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "AGMAGleasonConicalGearCompoundParametricStudyTool",
    "AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
    "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
    "AssemblyCompoundParametricStudyTool",
    "BearingCompoundParametricStudyTool",
    "BeltConnectionCompoundParametricStudyTool",
    "BeltDriveCompoundParametricStudyTool",
    "BevelDifferentialGearCompoundParametricStudyTool",
    "BevelDifferentialGearMeshCompoundParametricStudyTool",
    "BevelDifferentialGearSetCompoundParametricStudyTool",
    "BevelDifferentialPlanetGearCompoundParametricStudyTool",
    "BevelDifferentialSunGearCompoundParametricStudyTool",
    "BevelGearCompoundParametricStudyTool",
    "BevelGearMeshCompoundParametricStudyTool",
    "BevelGearSetCompoundParametricStudyTool",
    "BoltCompoundParametricStudyTool",
    "BoltedJointCompoundParametricStudyTool",
    "ClutchCompoundParametricStudyTool",
    "ClutchConnectionCompoundParametricStudyTool",
    "ClutchHalfCompoundParametricStudyTool",
    "CoaxialConnectionCompoundParametricStudyTool",
    "ComponentCompoundParametricStudyTool",
    "ConceptCouplingCompoundParametricStudyTool",
    "ConceptCouplingConnectionCompoundParametricStudyTool",
    "ConceptCouplingHalfCompoundParametricStudyTool",
    "ConceptGearCompoundParametricStudyTool",
    "ConceptGearMeshCompoundParametricStudyTool",
    "ConceptGearSetCompoundParametricStudyTool",
    "ConicalGearCompoundParametricStudyTool",
    "ConicalGearMeshCompoundParametricStudyTool",
    "ConicalGearSetCompoundParametricStudyTool",
    "ConnectionCompoundParametricStudyTool",
    "ConnectorCompoundParametricStudyTool",
    "CouplingCompoundParametricStudyTool",
    "CouplingConnectionCompoundParametricStudyTool",
    "CouplingHalfCompoundParametricStudyTool",
    "CVTBeltConnectionCompoundParametricStudyTool",
    "CVTCompoundParametricStudyTool",
    "CVTPulleyCompoundParametricStudyTool",
    "CycloidalAssemblyCompoundParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    "CycloidalDiscCompoundParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool",
    "CylindricalGearCompoundParametricStudyTool",
    "CylindricalGearMeshCompoundParametricStudyTool",
    "CylindricalGearSetCompoundParametricStudyTool",
    "CylindricalPlanetGearCompoundParametricStudyTool",
    "DatumCompoundParametricStudyTool",
    "ExternalCADModelCompoundParametricStudyTool",
    "FaceGearCompoundParametricStudyTool",
    "FaceGearMeshCompoundParametricStudyTool",
    "FaceGearSetCompoundParametricStudyTool",
    "FEPartCompoundParametricStudyTool",
    "FlexiblePinAssemblyCompoundParametricStudyTool",
    "GearCompoundParametricStudyTool",
    "GearMeshCompoundParametricStudyTool",
    "GearSetCompoundParametricStudyTool",
    "GuideDxfModelCompoundParametricStudyTool",
    "HypoidGearCompoundParametricStudyTool",
    "HypoidGearMeshCompoundParametricStudyTool",
    "HypoidGearSetCompoundParametricStudyTool",
    "InterMountableComponentConnectionCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool",
    "MassDiscCompoundParametricStudyTool",
    "MeasurementComponentCompoundParametricStudyTool",
    "MountableComponentCompoundParametricStudyTool",
    "OilSealCompoundParametricStudyTool",
    "PartCompoundParametricStudyTool",
    "PartToPartShearCouplingCompoundParametricStudyTool",
    "PartToPartShearCouplingConnectionCompoundParametricStudyTool",
    "PartToPartShearCouplingHalfCompoundParametricStudyTool",
    "PlanetaryConnectionCompoundParametricStudyTool",
    "PlanetaryGearSetCompoundParametricStudyTool",
    "PlanetCarrierCompoundParametricStudyTool",
    "PointLoadCompoundParametricStudyTool",
    "PowerLoadCompoundParametricStudyTool",
    "PulleyCompoundParametricStudyTool",
    "RingPinsCompoundParametricStudyTool",
    "RingPinsToDiscConnectionCompoundParametricStudyTool",
    "RollingRingAssemblyCompoundParametricStudyTool",
    "RollingRingCompoundParametricStudyTool",
    "RollingRingConnectionCompoundParametricStudyTool",
    "RootAssemblyCompoundParametricStudyTool",
    "ShaftCompoundParametricStudyTool",
    "ShaftHubConnectionCompoundParametricStudyTool",
    "ShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "SpecialisedAssemblyCompoundParametricStudyTool",
    "SpiralBevelGearCompoundParametricStudyTool",
    "SpiralBevelGearMeshCompoundParametricStudyTool",
    "SpiralBevelGearSetCompoundParametricStudyTool",
    "SpringDamperCompoundParametricStudyTool",
    "SpringDamperConnectionCompoundParametricStudyTool",
    "SpringDamperHalfCompoundParametricStudyTool",
    "StraightBevelDiffGearCompoundParametricStudyTool",
    "StraightBevelDiffGearMeshCompoundParametricStudyTool",
    "StraightBevelDiffGearSetCompoundParametricStudyTool",
    "StraightBevelGearCompoundParametricStudyTool",
    "StraightBevelGearMeshCompoundParametricStudyTool",
    "StraightBevelGearSetCompoundParametricStudyTool",
    "StraightBevelPlanetGearCompoundParametricStudyTool",
    "StraightBevelSunGearCompoundParametricStudyTool",
    "SynchroniserCompoundParametricStudyTool",
    "SynchroniserHalfCompoundParametricStudyTool",
    "SynchroniserPartCompoundParametricStudyTool",
    "SynchroniserSleeveCompoundParametricStudyTool",
    "TorqueConverterCompoundParametricStudyTool",
    "TorqueConverterConnectionCompoundParametricStudyTool",
    "TorqueConverterPumpCompoundParametricStudyTool",
    "TorqueConverterTurbineCompoundParametricStudyTool",
    "UnbalancedMassCompoundParametricStudyTool",
    "VirtualComponentCompoundParametricStudyTool",
    "WormGearCompoundParametricStudyTool",
    "WormGearMeshCompoundParametricStudyTool",
    "WormGearSetCompoundParametricStudyTool",
    "ZerolBevelGearCompoundParametricStudyTool",
    "ZerolBevelGearMeshCompoundParametricStudyTool",
    "ZerolBevelGearSetCompoundParametricStudyTool",
)
