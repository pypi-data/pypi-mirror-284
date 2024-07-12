"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2872 import AbstractAssemblyCompoundSystemDeflection
    from ._2873 import AbstractShaftCompoundSystemDeflection
    from ._2874 import AbstractShaftOrHousingCompoundSystemDeflection
    from ._2875 import (
        AbstractShaftToMountableComponentConnectionCompoundSystemDeflection,
    )
    from ._2876 import AGMAGleasonConicalGearCompoundSystemDeflection
    from ._2877 import AGMAGleasonConicalGearMeshCompoundSystemDeflection
    from ._2878 import AGMAGleasonConicalGearSetCompoundSystemDeflection
    from ._2879 import AssemblyCompoundSystemDeflection
    from ._2880 import BearingCompoundSystemDeflection
    from ._2881 import BeltConnectionCompoundSystemDeflection
    from ._2882 import BeltDriveCompoundSystemDeflection
    from ._2883 import BevelDifferentialGearCompoundSystemDeflection
    from ._2884 import BevelDifferentialGearMeshCompoundSystemDeflection
    from ._2885 import BevelDifferentialGearSetCompoundSystemDeflection
    from ._2886 import BevelDifferentialPlanetGearCompoundSystemDeflection
    from ._2887 import BevelDifferentialSunGearCompoundSystemDeflection
    from ._2888 import BevelGearCompoundSystemDeflection
    from ._2889 import BevelGearMeshCompoundSystemDeflection
    from ._2890 import BevelGearSetCompoundSystemDeflection
    from ._2891 import BoltCompoundSystemDeflection
    from ._2892 import BoltedJointCompoundSystemDeflection
    from ._2893 import ClutchCompoundSystemDeflection
    from ._2894 import ClutchConnectionCompoundSystemDeflection
    from ._2895 import ClutchHalfCompoundSystemDeflection
    from ._2896 import CoaxialConnectionCompoundSystemDeflection
    from ._2897 import ComponentCompoundSystemDeflection
    from ._2898 import ConceptCouplingCompoundSystemDeflection
    from ._2899 import ConceptCouplingConnectionCompoundSystemDeflection
    from ._2900 import ConceptCouplingHalfCompoundSystemDeflection
    from ._2901 import ConceptGearCompoundSystemDeflection
    from ._2902 import ConceptGearMeshCompoundSystemDeflection
    from ._2903 import ConceptGearSetCompoundSystemDeflection
    from ._2904 import ConicalGearCompoundSystemDeflection
    from ._2905 import ConicalGearMeshCompoundSystemDeflection
    from ._2906 import ConicalGearSetCompoundSystemDeflection
    from ._2907 import ConnectionCompoundSystemDeflection
    from ._2908 import ConnectorCompoundSystemDeflection
    from ._2909 import CouplingCompoundSystemDeflection
    from ._2910 import CouplingConnectionCompoundSystemDeflection
    from ._2911 import CouplingHalfCompoundSystemDeflection
    from ._2912 import CVTBeltConnectionCompoundSystemDeflection
    from ._2913 import CVTCompoundSystemDeflection
    from ._2914 import CVTPulleyCompoundSystemDeflection
    from ._2915 import CycloidalAssemblyCompoundSystemDeflection
    from ._2916 import CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
    from ._2917 import CycloidalDiscCompoundSystemDeflection
    from ._2918 import CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
    from ._2919 import CylindricalGearCompoundSystemDeflection
    from ._2920 import CylindricalGearMeshCompoundSystemDeflection
    from ._2921 import CylindricalGearSetCompoundSystemDeflection
    from ._2922 import CylindricalPlanetGearCompoundSystemDeflection
    from ._2923 import DatumCompoundSystemDeflection
    from ._2924 import DutyCycleEfficiencyResults
    from ._2925 import ExternalCADModelCompoundSystemDeflection
    from ._2926 import FaceGearCompoundSystemDeflection
    from ._2927 import FaceGearMeshCompoundSystemDeflection
    from ._2928 import FaceGearSetCompoundSystemDeflection
    from ._2929 import FEPartCompoundSystemDeflection
    from ._2930 import FlexiblePinAssemblyCompoundSystemDeflection
    from ._2931 import GearCompoundSystemDeflection
    from ._2932 import GearMeshCompoundSystemDeflection
    from ._2933 import GearSetCompoundSystemDeflection
    from ._2934 import GuideDxfModelCompoundSystemDeflection
    from ._2935 import HypoidGearCompoundSystemDeflection
    from ._2936 import HypoidGearMeshCompoundSystemDeflection
    from ._2937 import HypoidGearSetCompoundSystemDeflection
    from ._2938 import InterMountableComponentConnectionCompoundSystemDeflection
    from ._2939 import KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
    from ._2940 import KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
    from ._2941 import KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
    from ._2942 import KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
    from ._2943 import KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
    from ._2944 import KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
    from ._2945 import KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
    from ._2946 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection,
    )
    from ._2947 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection,
    )
    from ._2948 import MassDiscCompoundSystemDeflection
    from ._2949 import MeasurementComponentCompoundSystemDeflection
    from ._2950 import MountableComponentCompoundSystemDeflection
    from ._2951 import OilSealCompoundSystemDeflection
    from ._2952 import PartCompoundSystemDeflection
    from ._2953 import PartToPartShearCouplingCompoundSystemDeflection
    from ._2954 import PartToPartShearCouplingConnectionCompoundSystemDeflection
    from ._2955 import PartToPartShearCouplingHalfCompoundSystemDeflection
    from ._2956 import PlanetaryConnectionCompoundSystemDeflection
    from ._2957 import PlanetaryGearSetCompoundSystemDeflection
    from ._2958 import PlanetCarrierCompoundSystemDeflection
    from ._2959 import PointLoadCompoundSystemDeflection
    from ._2960 import PowerLoadCompoundSystemDeflection
    from ._2961 import PulleyCompoundSystemDeflection
    from ._2962 import RingPinsCompoundSystemDeflection
    from ._2963 import RingPinsToDiscConnectionCompoundSystemDeflection
    from ._2964 import RollingRingAssemblyCompoundSystemDeflection
    from ._2965 import RollingRingCompoundSystemDeflection
    from ._2966 import RollingRingConnectionCompoundSystemDeflection
    from ._2967 import RootAssemblyCompoundSystemDeflection
    from ._2968 import ShaftCompoundSystemDeflection
    from ._2969 import ShaftDutyCycleSystemDeflection
    from ._2970 import ShaftHubConnectionCompoundSystemDeflection
    from ._2971 import ShaftToMountableComponentConnectionCompoundSystemDeflection
    from ._2972 import SpecialisedAssemblyCompoundSystemDeflection
    from ._2973 import SpiralBevelGearCompoundSystemDeflection
    from ._2974 import SpiralBevelGearMeshCompoundSystemDeflection
    from ._2975 import SpiralBevelGearSetCompoundSystemDeflection
    from ._2976 import SpringDamperCompoundSystemDeflection
    from ._2977 import SpringDamperConnectionCompoundSystemDeflection
    from ._2978 import SpringDamperHalfCompoundSystemDeflection
    from ._2979 import StraightBevelDiffGearCompoundSystemDeflection
    from ._2980 import StraightBevelDiffGearMeshCompoundSystemDeflection
    from ._2981 import StraightBevelDiffGearSetCompoundSystemDeflection
    from ._2982 import StraightBevelGearCompoundSystemDeflection
    from ._2983 import StraightBevelGearMeshCompoundSystemDeflection
    from ._2984 import StraightBevelGearSetCompoundSystemDeflection
    from ._2985 import StraightBevelPlanetGearCompoundSystemDeflection
    from ._2986 import StraightBevelSunGearCompoundSystemDeflection
    from ._2987 import SynchroniserCompoundSystemDeflection
    from ._2988 import SynchroniserHalfCompoundSystemDeflection
    from ._2989 import SynchroniserPartCompoundSystemDeflection
    from ._2990 import SynchroniserSleeveCompoundSystemDeflection
    from ._2991 import TorqueConverterCompoundSystemDeflection
    from ._2992 import TorqueConverterConnectionCompoundSystemDeflection
    from ._2993 import TorqueConverterPumpCompoundSystemDeflection
    from ._2994 import TorqueConverterTurbineCompoundSystemDeflection
    from ._2995 import UnbalancedMassCompoundSystemDeflection
    from ._2996 import VirtualComponentCompoundSystemDeflection
    from ._2997 import WormGearCompoundSystemDeflection
    from ._2998 import WormGearMeshCompoundSystemDeflection
    from ._2999 import WormGearSetCompoundSystemDeflection
    from ._3000 import ZerolBevelGearCompoundSystemDeflection
    from ._3001 import ZerolBevelGearMeshCompoundSystemDeflection
    from ._3002 import ZerolBevelGearSetCompoundSystemDeflection
else:
    import_structure = {
        "_2872": ["AbstractAssemblyCompoundSystemDeflection"],
        "_2873": ["AbstractShaftCompoundSystemDeflection"],
        "_2874": ["AbstractShaftOrHousingCompoundSystemDeflection"],
        "_2875": [
            "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ],
        "_2876": ["AGMAGleasonConicalGearCompoundSystemDeflection"],
        "_2877": ["AGMAGleasonConicalGearMeshCompoundSystemDeflection"],
        "_2878": ["AGMAGleasonConicalGearSetCompoundSystemDeflection"],
        "_2879": ["AssemblyCompoundSystemDeflection"],
        "_2880": ["BearingCompoundSystemDeflection"],
        "_2881": ["BeltConnectionCompoundSystemDeflection"],
        "_2882": ["BeltDriveCompoundSystemDeflection"],
        "_2883": ["BevelDifferentialGearCompoundSystemDeflection"],
        "_2884": ["BevelDifferentialGearMeshCompoundSystemDeflection"],
        "_2885": ["BevelDifferentialGearSetCompoundSystemDeflection"],
        "_2886": ["BevelDifferentialPlanetGearCompoundSystemDeflection"],
        "_2887": ["BevelDifferentialSunGearCompoundSystemDeflection"],
        "_2888": ["BevelGearCompoundSystemDeflection"],
        "_2889": ["BevelGearMeshCompoundSystemDeflection"],
        "_2890": ["BevelGearSetCompoundSystemDeflection"],
        "_2891": ["BoltCompoundSystemDeflection"],
        "_2892": ["BoltedJointCompoundSystemDeflection"],
        "_2893": ["ClutchCompoundSystemDeflection"],
        "_2894": ["ClutchConnectionCompoundSystemDeflection"],
        "_2895": ["ClutchHalfCompoundSystemDeflection"],
        "_2896": ["CoaxialConnectionCompoundSystemDeflection"],
        "_2897": ["ComponentCompoundSystemDeflection"],
        "_2898": ["ConceptCouplingCompoundSystemDeflection"],
        "_2899": ["ConceptCouplingConnectionCompoundSystemDeflection"],
        "_2900": ["ConceptCouplingHalfCompoundSystemDeflection"],
        "_2901": ["ConceptGearCompoundSystemDeflection"],
        "_2902": ["ConceptGearMeshCompoundSystemDeflection"],
        "_2903": ["ConceptGearSetCompoundSystemDeflection"],
        "_2904": ["ConicalGearCompoundSystemDeflection"],
        "_2905": ["ConicalGearMeshCompoundSystemDeflection"],
        "_2906": ["ConicalGearSetCompoundSystemDeflection"],
        "_2907": ["ConnectionCompoundSystemDeflection"],
        "_2908": ["ConnectorCompoundSystemDeflection"],
        "_2909": ["CouplingCompoundSystemDeflection"],
        "_2910": ["CouplingConnectionCompoundSystemDeflection"],
        "_2911": ["CouplingHalfCompoundSystemDeflection"],
        "_2912": ["CVTBeltConnectionCompoundSystemDeflection"],
        "_2913": ["CVTCompoundSystemDeflection"],
        "_2914": ["CVTPulleyCompoundSystemDeflection"],
        "_2915": ["CycloidalAssemblyCompoundSystemDeflection"],
        "_2916": ["CycloidalDiscCentralBearingConnectionCompoundSystemDeflection"],
        "_2917": ["CycloidalDiscCompoundSystemDeflection"],
        "_2918": ["CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection"],
        "_2919": ["CylindricalGearCompoundSystemDeflection"],
        "_2920": ["CylindricalGearMeshCompoundSystemDeflection"],
        "_2921": ["CylindricalGearSetCompoundSystemDeflection"],
        "_2922": ["CylindricalPlanetGearCompoundSystemDeflection"],
        "_2923": ["DatumCompoundSystemDeflection"],
        "_2924": ["DutyCycleEfficiencyResults"],
        "_2925": ["ExternalCADModelCompoundSystemDeflection"],
        "_2926": ["FaceGearCompoundSystemDeflection"],
        "_2927": ["FaceGearMeshCompoundSystemDeflection"],
        "_2928": ["FaceGearSetCompoundSystemDeflection"],
        "_2929": ["FEPartCompoundSystemDeflection"],
        "_2930": ["FlexiblePinAssemblyCompoundSystemDeflection"],
        "_2931": ["GearCompoundSystemDeflection"],
        "_2932": ["GearMeshCompoundSystemDeflection"],
        "_2933": ["GearSetCompoundSystemDeflection"],
        "_2934": ["GuideDxfModelCompoundSystemDeflection"],
        "_2935": ["HypoidGearCompoundSystemDeflection"],
        "_2936": ["HypoidGearMeshCompoundSystemDeflection"],
        "_2937": ["HypoidGearSetCompoundSystemDeflection"],
        "_2938": ["InterMountableComponentConnectionCompoundSystemDeflection"],
        "_2939": ["KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection"],
        "_2940": ["KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection"],
        "_2941": ["KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection"],
        "_2942": ["KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection"],
        "_2943": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection"],
        "_2944": ["KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection"],
        "_2945": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection"],
        "_2946": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection"
        ],
        "_2947": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection"],
        "_2948": ["MassDiscCompoundSystemDeflection"],
        "_2949": ["MeasurementComponentCompoundSystemDeflection"],
        "_2950": ["MountableComponentCompoundSystemDeflection"],
        "_2951": ["OilSealCompoundSystemDeflection"],
        "_2952": ["PartCompoundSystemDeflection"],
        "_2953": ["PartToPartShearCouplingCompoundSystemDeflection"],
        "_2954": ["PartToPartShearCouplingConnectionCompoundSystemDeflection"],
        "_2955": ["PartToPartShearCouplingHalfCompoundSystemDeflection"],
        "_2956": ["PlanetaryConnectionCompoundSystemDeflection"],
        "_2957": ["PlanetaryGearSetCompoundSystemDeflection"],
        "_2958": ["PlanetCarrierCompoundSystemDeflection"],
        "_2959": ["PointLoadCompoundSystemDeflection"],
        "_2960": ["PowerLoadCompoundSystemDeflection"],
        "_2961": ["PulleyCompoundSystemDeflection"],
        "_2962": ["RingPinsCompoundSystemDeflection"],
        "_2963": ["RingPinsToDiscConnectionCompoundSystemDeflection"],
        "_2964": ["RollingRingAssemblyCompoundSystemDeflection"],
        "_2965": ["RollingRingCompoundSystemDeflection"],
        "_2966": ["RollingRingConnectionCompoundSystemDeflection"],
        "_2967": ["RootAssemblyCompoundSystemDeflection"],
        "_2968": ["ShaftCompoundSystemDeflection"],
        "_2969": ["ShaftDutyCycleSystemDeflection"],
        "_2970": ["ShaftHubConnectionCompoundSystemDeflection"],
        "_2971": ["ShaftToMountableComponentConnectionCompoundSystemDeflection"],
        "_2972": ["SpecialisedAssemblyCompoundSystemDeflection"],
        "_2973": ["SpiralBevelGearCompoundSystemDeflection"],
        "_2974": ["SpiralBevelGearMeshCompoundSystemDeflection"],
        "_2975": ["SpiralBevelGearSetCompoundSystemDeflection"],
        "_2976": ["SpringDamperCompoundSystemDeflection"],
        "_2977": ["SpringDamperConnectionCompoundSystemDeflection"],
        "_2978": ["SpringDamperHalfCompoundSystemDeflection"],
        "_2979": ["StraightBevelDiffGearCompoundSystemDeflection"],
        "_2980": ["StraightBevelDiffGearMeshCompoundSystemDeflection"],
        "_2981": ["StraightBevelDiffGearSetCompoundSystemDeflection"],
        "_2982": ["StraightBevelGearCompoundSystemDeflection"],
        "_2983": ["StraightBevelGearMeshCompoundSystemDeflection"],
        "_2984": ["StraightBevelGearSetCompoundSystemDeflection"],
        "_2985": ["StraightBevelPlanetGearCompoundSystemDeflection"],
        "_2986": ["StraightBevelSunGearCompoundSystemDeflection"],
        "_2987": ["SynchroniserCompoundSystemDeflection"],
        "_2988": ["SynchroniserHalfCompoundSystemDeflection"],
        "_2989": ["SynchroniserPartCompoundSystemDeflection"],
        "_2990": ["SynchroniserSleeveCompoundSystemDeflection"],
        "_2991": ["TorqueConverterCompoundSystemDeflection"],
        "_2992": ["TorqueConverterConnectionCompoundSystemDeflection"],
        "_2993": ["TorqueConverterPumpCompoundSystemDeflection"],
        "_2994": ["TorqueConverterTurbineCompoundSystemDeflection"],
        "_2995": ["UnbalancedMassCompoundSystemDeflection"],
        "_2996": ["VirtualComponentCompoundSystemDeflection"],
        "_2997": ["WormGearCompoundSystemDeflection"],
        "_2998": ["WormGearMeshCompoundSystemDeflection"],
        "_2999": ["WormGearSetCompoundSystemDeflection"],
        "_3000": ["ZerolBevelGearCompoundSystemDeflection"],
        "_3001": ["ZerolBevelGearMeshCompoundSystemDeflection"],
        "_3002": ["ZerolBevelGearSetCompoundSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSystemDeflection",
    "AbstractShaftCompoundSystemDeflection",
    "AbstractShaftOrHousingCompoundSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection",
    "AGMAGleasonConicalGearCompoundSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundSystemDeflection",
    "AssemblyCompoundSystemDeflection",
    "BearingCompoundSystemDeflection",
    "BeltConnectionCompoundSystemDeflection",
    "BeltDriveCompoundSystemDeflection",
    "BevelDifferentialGearCompoundSystemDeflection",
    "BevelDifferentialGearMeshCompoundSystemDeflection",
    "BevelDifferentialGearSetCompoundSystemDeflection",
    "BevelDifferentialPlanetGearCompoundSystemDeflection",
    "BevelDifferentialSunGearCompoundSystemDeflection",
    "BevelGearCompoundSystemDeflection",
    "BevelGearMeshCompoundSystemDeflection",
    "BevelGearSetCompoundSystemDeflection",
    "BoltCompoundSystemDeflection",
    "BoltedJointCompoundSystemDeflection",
    "ClutchCompoundSystemDeflection",
    "ClutchConnectionCompoundSystemDeflection",
    "ClutchHalfCompoundSystemDeflection",
    "CoaxialConnectionCompoundSystemDeflection",
    "ComponentCompoundSystemDeflection",
    "ConceptCouplingCompoundSystemDeflection",
    "ConceptCouplingConnectionCompoundSystemDeflection",
    "ConceptCouplingHalfCompoundSystemDeflection",
    "ConceptGearCompoundSystemDeflection",
    "ConceptGearMeshCompoundSystemDeflection",
    "ConceptGearSetCompoundSystemDeflection",
    "ConicalGearCompoundSystemDeflection",
    "ConicalGearMeshCompoundSystemDeflection",
    "ConicalGearSetCompoundSystemDeflection",
    "ConnectionCompoundSystemDeflection",
    "ConnectorCompoundSystemDeflection",
    "CouplingCompoundSystemDeflection",
    "CouplingConnectionCompoundSystemDeflection",
    "CouplingHalfCompoundSystemDeflection",
    "CVTBeltConnectionCompoundSystemDeflection",
    "CVTCompoundSystemDeflection",
    "CVTPulleyCompoundSystemDeflection",
    "CycloidalAssemblyCompoundSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
    "CycloidalDiscCompoundSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
    "CylindricalGearCompoundSystemDeflection",
    "CylindricalGearMeshCompoundSystemDeflection",
    "CylindricalGearSetCompoundSystemDeflection",
    "CylindricalPlanetGearCompoundSystemDeflection",
    "DatumCompoundSystemDeflection",
    "DutyCycleEfficiencyResults",
    "ExternalCADModelCompoundSystemDeflection",
    "FaceGearCompoundSystemDeflection",
    "FaceGearMeshCompoundSystemDeflection",
    "FaceGearSetCompoundSystemDeflection",
    "FEPartCompoundSystemDeflection",
    "FlexiblePinAssemblyCompoundSystemDeflection",
    "GearCompoundSystemDeflection",
    "GearMeshCompoundSystemDeflection",
    "GearSetCompoundSystemDeflection",
    "GuideDxfModelCompoundSystemDeflection",
    "HypoidGearCompoundSystemDeflection",
    "HypoidGearMeshCompoundSystemDeflection",
    "HypoidGearSetCompoundSystemDeflection",
    "InterMountableComponentConnectionCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
    "MassDiscCompoundSystemDeflection",
    "MeasurementComponentCompoundSystemDeflection",
    "MountableComponentCompoundSystemDeflection",
    "OilSealCompoundSystemDeflection",
    "PartCompoundSystemDeflection",
    "PartToPartShearCouplingCompoundSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundSystemDeflection",
    "PartToPartShearCouplingHalfCompoundSystemDeflection",
    "PlanetaryConnectionCompoundSystemDeflection",
    "PlanetaryGearSetCompoundSystemDeflection",
    "PlanetCarrierCompoundSystemDeflection",
    "PointLoadCompoundSystemDeflection",
    "PowerLoadCompoundSystemDeflection",
    "PulleyCompoundSystemDeflection",
    "RingPinsCompoundSystemDeflection",
    "RingPinsToDiscConnectionCompoundSystemDeflection",
    "RollingRingAssemblyCompoundSystemDeflection",
    "RollingRingCompoundSystemDeflection",
    "RollingRingConnectionCompoundSystemDeflection",
    "RootAssemblyCompoundSystemDeflection",
    "ShaftCompoundSystemDeflection",
    "ShaftDutyCycleSystemDeflection",
    "ShaftHubConnectionCompoundSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundSystemDeflection",
    "SpecialisedAssemblyCompoundSystemDeflection",
    "SpiralBevelGearCompoundSystemDeflection",
    "SpiralBevelGearMeshCompoundSystemDeflection",
    "SpiralBevelGearSetCompoundSystemDeflection",
    "SpringDamperCompoundSystemDeflection",
    "SpringDamperConnectionCompoundSystemDeflection",
    "SpringDamperHalfCompoundSystemDeflection",
    "StraightBevelDiffGearCompoundSystemDeflection",
    "StraightBevelDiffGearMeshCompoundSystemDeflection",
    "StraightBevelDiffGearSetCompoundSystemDeflection",
    "StraightBevelGearCompoundSystemDeflection",
    "StraightBevelGearMeshCompoundSystemDeflection",
    "StraightBevelGearSetCompoundSystemDeflection",
    "StraightBevelPlanetGearCompoundSystemDeflection",
    "StraightBevelSunGearCompoundSystemDeflection",
    "SynchroniserCompoundSystemDeflection",
    "SynchroniserHalfCompoundSystemDeflection",
    "SynchroniserPartCompoundSystemDeflection",
    "SynchroniserSleeveCompoundSystemDeflection",
    "TorqueConverterCompoundSystemDeflection",
    "TorqueConverterConnectionCompoundSystemDeflection",
    "TorqueConverterPumpCompoundSystemDeflection",
    "TorqueConverterTurbineCompoundSystemDeflection",
    "UnbalancedMassCompoundSystemDeflection",
    "VirtualComponentCompoundSystemDeflection",
    "WormGearCompoundSystemDeflection",
    "WormGearMeshCompoundSystemDeflection",
    "WormGearSetCompoundSystemDeflection",
    "ZerolBevelGearCompoundSystemDeflection",
    "ZerolBevelGearMeshCompoundSystemDeflection",
    "ZerolBevelGearSetCompoundSystemDeflection",
)
