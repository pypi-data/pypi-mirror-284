"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3396 import AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3397 import AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3398 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3399 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3400 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3401 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3402 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3403 import AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3404 import BearingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3405 import BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3406 import BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3407 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3408 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3409 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3410 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3411 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3412 import BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3413 import BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3414 import BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3415 import BoltCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3416 import BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3417 import ClutchCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3418 import ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3419 import ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3420 import CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3421 import ComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3422 import ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3423 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3424 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3425 import ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3426 import ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3427 import ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3428 import ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3429 import ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3430 import ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3431 import ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3432 import ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3433 import CouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3434 import CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3435 import CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3436 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3437 import CVTCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3438 import CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3439 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3440 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3441 import CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3442 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3443 import CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3444 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3445 import CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3446 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3447 import DatumCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3448 import ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3449 import FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3450 import FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3451 import FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3452 import FEPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3453 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3454 import GearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3455 import GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3456 import GearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3457 import GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3458 import HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3459 import HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3460 import HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3461 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3462 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3463 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3464 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3465 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3466 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3467 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3468 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3469 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3470 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3471 import MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3472 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3473 import MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3474 import OilSealCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3475 import PartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3476 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3477 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3478 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3479 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3480 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3481 import PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3482 import PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3483 import PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3484 import PulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3485 import RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3486 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3487 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3488 import RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3489 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3490 import RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3491 import ShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3492 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3493 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3494 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3495 import SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3496 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3497 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3498 import SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3499 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3500 import SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3501 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3502 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3503 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3504 import StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3505 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3506 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3507 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3508 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3509 import SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3510 import SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3511 import SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3512 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3513 import TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3514 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3515 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3516 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3517 import UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3518 import VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3519 import WormGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3520 import WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3521 import WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3522 import ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3523 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3524 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
else:
    import_structure = {
        "_3396": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3397": ["AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3398": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3399": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3400": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3401": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3402": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3403": ["AssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3404": ["BearingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3405": ["BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3406": ["BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3407": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3408": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3409": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3410": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3411": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3412": ["BevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3413": ["BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3414": ["BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3415": ["BoltCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3416": ["BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3417": ["ClutchCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3418": ["ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3419": ["ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3420": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3421": ["ComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3422": ["ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3423": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3424": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3425": ["ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3426": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3427": ["ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3428": ["ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3429": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3430": ["ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3431": ["ConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3432": ["ConnectorCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3433": ["CouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3434": ["CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3435": ["CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3436": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3437": ["CVTCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3438": ["CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3439": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3440": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3441": ["CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3442": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3443": ["CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3444": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3445": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3446": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3447": ["DatumCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3448": ["ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3449": ["FaceGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3450": ["FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3451": ["FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3452": ["FEPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3453": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3454": ["GearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3455": ["GearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3456": ["GearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3457": ["GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3458": ["HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3459": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3460": ["HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3461": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3462": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3463": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3464": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3465": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3466": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3467": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3468": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3469": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3470": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3471": ["MassDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3472": ["MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3473": ["MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3474": ["OilSealCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3475": ["PartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3476": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3477": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3478": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3479": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3480": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3481": ["PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3482": ["PointLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3483": ["PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3484": ["PulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3485": ["RingPinsCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3486": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3487": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3488": ["RollingRingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3489": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3490": ["RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3491": ["ShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3492": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3493": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3494": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3495": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3496": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3497": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3498": ["SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3499": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3500": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3501": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3502": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3503": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3504": ["StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3505": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3506": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3507": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3508": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3509": ["SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3510": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3511": ["SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3512": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3513": ["TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3514": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3515": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3516": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3517": ["UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3518": ["VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3519": ["WormGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3520": ["WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3521": ["WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3522": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3523": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3524": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "AssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "BearingCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "DatumCompoundSteadyStateSynchronousResponseOnAShaft",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "FEPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "MassDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "OilSealCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft",
    "PointLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft",
    "VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)
