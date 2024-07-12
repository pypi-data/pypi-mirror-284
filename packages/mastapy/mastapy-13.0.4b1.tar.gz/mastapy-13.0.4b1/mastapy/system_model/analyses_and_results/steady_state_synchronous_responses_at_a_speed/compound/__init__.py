"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3655 import AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3656 import AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3657 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3658 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3659 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3660 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3661 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3662 import AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3663 import BearingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3664 import BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3665 import BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3666 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3667 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3668 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3669 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3670 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3671 import BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3672 import BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3673 import BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3674 import BoltCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3675 import BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3676 import ClutchCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3677 import ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3678 import ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3679 import CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3680 import ComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3681 import ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3682 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3683 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3684 import ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3685 import ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3686 import ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3687 import ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3688 import ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3689 import ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3690 import ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3691 import ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3692 import CouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3693 import CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3694 import CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3695 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3696 import CVTCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3697 import CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3698 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3699 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3700 import CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3701 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3702 import CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3703 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3704 import CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3705 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3706 import DatumCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3707 import ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3708 import FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3709 import FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3710 import FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3711 import FEPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3712 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3713 import GearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3714 import GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3715 import GearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3716 import GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3717 import HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3718 import HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3719 import HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3720 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3721 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3722 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3723 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3724 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3725 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3726 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3727 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3728 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3729 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3730 import MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3731 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3732 import MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3733 import OilSealCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3734 import PartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3735 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3736 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3737 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3738 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3739 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3740 import PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3741 import PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3742 import PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3743 import PulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3744 import RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3745 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3746 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3747 import RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3748 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3749 import RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3750 import ShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3751 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3752 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3753 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3754 import SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3755 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3756 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3757 import SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3758 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3759 import SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3760 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3761 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3762 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3763 import StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3764 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3765 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3766 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3767 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3768 import SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3769 import SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3770 import SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3771 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3772 import TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3773 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3774 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3775 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3776 import UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3777 import VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3778 import WormGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3779 import WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3780 import WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3781 import ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3782 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3783 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        "_3655": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3656": ["AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3657": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3658": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3659": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3660": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3661": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3662": ["AssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3663": ["BearingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3664": ["BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3665": ["BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3666": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3667": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3668": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3669": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3670": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3671": ["BevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3672": ["BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3673": ["BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3674": ["BoltCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3675": ["BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3676": ["ClutchCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3677": ["ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3678": ["ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3679": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3680": ["ComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3681": ["ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3682": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3683": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3684": ["ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3685": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3686": ["ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3687": ["ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3688": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3689": ["ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3690": ["ConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3691": ["ConnectorCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3692": ["CouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3693": ["CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3694": ["CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3695": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3696": ["CVTCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3697": ["CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3698": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3699": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3700": ["CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3701": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3702": ["CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3703": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3704": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3705": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3706": ["DatumCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3707": ["ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3708": ["FaceGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3709": ["FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3710": ["FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3711": ["FEPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3712": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3713": ["GearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3714": ["GearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3715": ["GearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3716": ["GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3717": ["HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3718": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3719": ["HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3720": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3721": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3722": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3723": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3724": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3725": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3726": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3727": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3728": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3729": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3730": ["MassDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3731": ["MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3732": ["MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3733": ["OilSealCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3734": ["PartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3735": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3736": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3737": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3738": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3739": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3740": ["PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3741": ["PointLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3742": ["PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3743": ["PulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3744": ["RingPinsCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3745": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3746": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3747": ["RollingRingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3748": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3749": ["RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3750": ["ShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3751": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3752": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3753": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3754": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3755": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3756": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3757": ["SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3758": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3759": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3760": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3761": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3762": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3763": ["StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3764": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3765": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3766": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3767": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3768": ["SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3769": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3770": ["SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3771": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3772": ["TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3773": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3774": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3775": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3776": ["UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3777": ["VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3778": ["WormGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3779": ["WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3780": ["WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3781": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3782": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3783": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "AssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "BearingCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "DatumCompoundSteadyStateSynchronousResponseAtASpeed",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "FEPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "MassDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "OilSealCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed",
    "PointLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
    "VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)
