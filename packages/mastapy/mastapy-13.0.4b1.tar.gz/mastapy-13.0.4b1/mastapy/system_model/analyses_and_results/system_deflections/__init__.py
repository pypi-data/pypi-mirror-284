"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2706 import AbstractAssemblySystemDeflection
    from ._2707 import AbstractShaftOrHousingSystemDeflection
    from ._2708 import AbstractShaftSystemDeflection
    from ._2709 import AbstractShaftToMountableComponentConnectionSystemDeflection
    from ._2710 import AGMAGleasonConicalGearMeshSystemDeflection
    from ._2711 import AGMAGleasonConicalGearSetSystemDeflection
    from ._2712 import AGMAGleasonConicalGearSystemDeflection
    from ._2713 import AssemblySystemDeflection
    from ._2714 import BearingDynamicElementContactPropertyWrapper
    from ._2715 import BearingDynamicElementPropertyWrapper
    from ._2716 import BearingDynamicPostAnalysisResultWrapper
    from ._2717 import BearingDynamicResultsPropertyWrapper
    from ._2718 import BearingDynamicResultsUIWrapper
    from ._2719 import BearingSystemDeflection
    from ._2720 import BeltConnectionSystemDeflection
    from ._2721 import BeltDriveSystemDeflection
    from ._2722 import BevelDifferentialGearMeshSystemDeflection
    from ._2723 import BevelDifferentialGearSetSystemDeflection
    from ._2724 import BevelDifferentialGearSystemDeflection
    from ._2725 import BevelDifferentialPlanetGearSystemDeflection
    from ._2726 import BevelDifferentialSunGearSystemDeflection
    from ._2727 import BevelGearMeshSystemDeflection
    from ._2728 import BevelGearSetSystemDeflection
    from ._2729 import BevelGearSystemDeflection
    from ._2730 import BoltedJointSystemDeflection
    from ._2731 import BoltSystemDeflection
    from ._2732 import ClutchConnectionSystemDeflection
    from ._2733 import ClutchHalfSystemDeflection
    from ._2734 import ClutchSystemDeflection
    from ._2735 import CoaxialConnectionSystemDeflection
    from ._2736 import ComponentSystemDeflection
    from ._2737 import ConcentricPartGroupCombinationSystemDeflectionResults
    from ._2738 import ConceptCouplingConnectionSystemDeflection
    from ._2739 import ConceptCouplingHalfSystemDeflection
    from ._2740 import ConceptCouplingSystemDeflection
    from ._2741 import ConceptGearMeshSystemDeflection
    from ._2742 import ConceptGearSetSystemDeflection
    from ._2743 import ConceptGearSystemDeflection
    from ._2744 import ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2745 import ConicalGearMeshSystemDeflection
    from ._2746 import ConicalGearSetSystemDeflection
    from ._2747 import ConicalGearSystemDeflection
    from ._2748 import ConnectionSystemDeflection
    from ._2749 import ConnectorSystemDeflection
    from ._2750 import CouplingConnectionSystemDeflection
    from ._2751 import CouplingHalfSystemDeflection
    from ._2752 import CouplingSystemDeflection
    from ._2753 import CVTBeltConnectionSystemDeflection
    from ._2754 import CVTPulleySystemDeflection
    from ._2755 import CVTSystemDeflection
    from ._2756 import CycloidalAssemblySystemDeflection
    from ._2757 import CycloidalDiscCentralBearingConnectionSystemDeflection
    from ._2758 import CycloidalDiscPlanetaryBearingConnectionSystemDeflection
    from ._2759 import CycloidalDiscSystemDeflection
    from ._2760 import CylindricalGearMeshSystemDeflection
    from ._2761 import CylindricalGearMeshSystemDeflectionTimestep
    from ._2762 import CylindricalGearMeshSystemDeflectionWithLTCAResults
    from ._2763 import CylindricalGearSetSystemDeflection
    from ._2764 import CylindricalGearSetSystemDeflectionTimestep
    from ._2765 import CylindricalGearSetSystemDeflectionWithLTCAResults
    from ._2766 import CylindricalGearSystemDeflection
    from ._2767 import CylindricalGearSystemDeflectionTimestep
    from ._2768 import CylindricalGearSystemDeflectionWithLTCAResults
    from ._2769 import CylindricalMeshedGearFlankSystemDeflection
    from ._2770 import CylindricalMeshedGearSystemDeflection
    from ._2771 import CylindricalPlanetGearSystemDeflection
    from ._2772 import DatumSystemDeflection
    from ._2773 import ExternalCADModelSystemDeflection
    from ._2774 import FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2775 import FaceGearMeshSystemDeflection
    from ._2776 import FaceGearSetSystemDeflection
    from ._2777 import FaceGearSystemDeflection
    from ._2778 import FEPartSystemDeflection
    from ._2779 import FlexiblePinAssemblySystemDeflection
    from ._2780 import GearMeshSystemDeflection
    from ._2781 import GearSetSystemDeflection
    from ._2782 import GearSystemDeflection
    from ._2783 import GuideDxfModelSystemDeflection
    from ._2784 import HypoidGearMeshSystemDeflection
    from ._2785 import HypoidGearSetSystemDeflection
    from ._2786 import HypoidGearSystemDeflection
    from ._2787 import InformationForContactAtPointAlongFaceWidth
    from ._2788 import InterMountableComponentConnectionSystemDeflection
    from ._2789 import KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
    from ._2790 import KlingelnbergCycloPalloidConicalGearSetSystemDeflection
    from ._2791 import KlingelnbergCycloPalloidConicalGearSystemDeflection
    from ._2792 import KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
    from ._2793 import KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
    from ._2794 import KlingelnbergCycloPalloidHypoidGearSystemDeflection
    from ._2795 import KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
    from ._2796 import KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
    from ._2797 import KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
    from ._2798 import LoadCaseOverallEfficiencyResult
    from ._2799 import LoadSharingFactorReporter
    from ._2800 import MassDiscSystemDeflection
    from ._2801 import MeasurementComponentSystemDeflection
    from ._2802 import MeshSeparationsAtFaceWidth
    from ._2803 import MountableComponentSystemDeflection
    from ._2804 import ObservedPinStiffnessReporter
    from ._2805 import OilSealSystemDeflection
    from ._2806 import PartSystemDeflection
    from ._2807 import PartToPartShearCouplingConnectionSystemDeflection
    from ._2808 import PartToPartShearCouplingHalfSystemDeflection
    from ._2809 import PartToPartShearCouplingSystemDeflection
    from ._2810 import PlanetaryConnectionSystemDeflection
    from ._2811 import PlanetCarrierSystemDeflection
    from ._2812 import PointLoadSystemDeflection
    from ._2813 import PowerLoadSystemDeflection
    from ._2814 import PulleySystemDeflection
    from ._2815 import RingPinsSystemDeflection
    from ._2816 import RingPinsToDiscConnectionSystemDeflection
    from ._2817 import RingPinToDiscContactReporting
    from ._2818 import RollingRingAssemblySystemDeflection
    from ._2819 import RollingRingConnectionSystemDeflection
    from ._2820 import RollingRingSystemDeflection
    from ._2821 import RootAssemblySystemDeflection
    from ._2822 import ShaftHubConnectionSystemDeflection
    from ._2823 import ShaftSectionEndResultsSystemDeflection
    from ._2824 import ShaftSectionSystemDeflection
    from ._2825 import ShaftSystemDeflection
    from ._2826 import ShaftToMountableComponentConnectionSystemDeflection
    from ._2827 import SpecialisedAssemblySystemDeflection
    from ._2828 import SpiralBevelGearMeshSystemDeflection
    from ._2829 import SpiralBevelGearSetSystemDeflection
    from ._2830 import SpiralBevelGearSystemDeflection
    from ._2831 import SpringDamperConnectionSystemDeflection
    from ._2832 import SpringDamperHalfSystemDeflection
    from ._2833 import SpringDamperSystemDeflection
    from ._2834 import StraightBevelDiffGearMeshSystemDeflection
    from ._2835 import StraightBevelDiffGearSetSystemDeflection
    from ._2836 import StraightBevelDiffGearSystemDeflection
    from ._2837 import StraightBevelGearMeshSystemDeflection
    from ._2838 import StraightBevelGearSetSystemDeflection
    from ._2839 import StraightBevelGearSystemDeflection
    from ._2840 import StraightBevelPlanetGearSystemDeflection
    from ._2841 import StraightBevelSunGearSystemDeflection
    from ._2842 import SynchroniserHalfSystemDeflection
    from ._2843 import SynchroniserPartSystemDeflection
    from ._2844 import SynchroniserSleeveSystemDeflection
    from ._2845 import SynchroniserSystemDeflection
    from ._2846 import SystemDeflection
    from ._2847 import SystemDeflectionDrawStyle
    from ._2848 import SystemDeflectionOptions
    from ._2849 import TorqueConverterConnectionSystemDeflection
    from ._2850 import TorqueConverterPumpSystemDeflection
    from ._2851 import TorqueConverterSystemDeflection
    from ._2852 import TorqueConverterTurbineSystemDeflection
    from ._2853 import TorsionalSystemDeflection
    from ._2854 import TransmissionErrorResult
    from ._2855 import UnbalancedMassSystemDeflection
    from ._2856 import VirtualComponentSystemDeflection
    from ._2857 import WormGearMeshSystemDeflection
    from ._2858 import WormGearSetSystemDeflection
    from ._2859 import WormGearSystemDeflection
    from ._2860 import ZerolBevelGearMeshSystemDeflection
    from ._2861 import ZerolBevelGearSetSystemDeflection
    from ._2862 import ZerolBevelGearSystemDeflection
else:
    import_structure = {
        "_2706": ["AbstractAssemblySystemDeflection"],
        "_2707": ["AbstractShaftOrHousingSystemDeflection"],
        "_2708": ["AbstractShaftSystemDeflection"],
        "_2709": ["AbstractShaftToMountableComponentConnectionSystemDeflection"],
        "_2710": ["AGMAGleasonConicalGearMeshSystemDeflection"],
        "_2711": ["AGMAGleasonConicalGearSetSystemDeflection"],
        "_2712": ["AGMAGleasonConicalGearSystemDeflection"],
        "_2713": ["AssemblySystemDeflection"],
        "_2714": ["BearingDynamicElementContactPropertyWrapper"],
        "_2715": ["BearingDynamicElementPropertyWrapper"],
        "_2716": ["BearingDynamicPostAnalysisResultWrapper"],
        "_2717": ["BearingDynamicResultsPropertyWrapper"],
        "_2718": ["BearingDynamicResultsUIWrapper"],
        "_2719": ["BearingSystemDeflection"],
        "_2720": ["BeltConnectionSystemDeflection"],
        "_2721": ["BeltDriveSystemDeflection"],
        "_2722": ["BevelDifferentialGearMeshSystemDeflection"],
        "_2723": ["BevelDifferentialGearSetSystemDeflection"],
        "_2724": ["BevelDifferentialGearSystemDeflection"],
        "_2725": ["BevelDifferentialPlanetGearSystemDeflection"],
        "_2726": ["BevelDifferentialSunGearSystemDeflection"],
        "_2727": ["BevelGearMeshSystemDeflection"],
        "_2728": ["BevelGearSetSystemDeflection"],
        "_2729": ["BevelGearSystemDeflection"],
        "_2730": ["BoltedJointSystemDeflection"],
        "_2731": ["BoltSystemDeflection"],
        "_2732": ["ClutchConnectionSystemDeflection"],
        "_2733": ["ClutchHalfSystemDeflection"],
        "_2734": ["ClutchSystemDeflection"],
        "_2735": ["CoaxialConnectionSystemDeflection"],
        "_2736": ["ComponentSystemDeflection"],
        "_2737": ["ConcentricPartGroupCombinationSystemDeflectionResults"],
        "_2738": ["ConceptCouplingConnectionSystemDeflection"],
        "_2739": ["ConceptCouplingHalfSystemDeflection"],
        "_2740": ["ConceptCouplingSystemDeflection"],
        "_2741": ["ConceptGearMeshSystemDeflection"],
        "_2742": ["ConceptGearSetSystemDeflection"],
        "_2743": ["ConceptGearSystemDeflection"],
        "_2744": ["ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2745": ["ConicalGearMeshSystemDeflection"],
        "_2746": ["ConicalGearSetSystemDeflection"],
        "_2747": ["ConicalGearSystemDeflection"],
        "_2748": ["ConnectionSystemDeflection"],
        "_2749": ["ConnectorSystemDeflection"],
        "_2750": ["CouplingConnectionSystemDeflection"],
        "_2751": ["CouplingHalfSystemDeflection"],
        "_2752": ["CouplingSystemDeflection"],
        "_2753": ["CVTBeltConnectionSystemDeflection"],
        "_2754": ["CVTPulleySystemDeflection"],
        "_2755": ["CVTSystemDeflection"],
        "_2756": ["CycloidalAssemblySystemDeflection"],
        "_2757": ["CycloidalDiscCentralBearingConnectionSystemDeflection"],
        "_2758": ["CycloidalDiscPlanetaryBearingConnectionSystemDeflection"],
        "_2759": ["CycloidalDiscSystemDeflection"],
        "_2760": ["CylindricalGearMeshSystemDeflection"],
        "_2761": ["CylindricalGearMeshSystemDeflectionTimestep"],
        "_2762": ["CylindricalGearMeshSystemDeflectionWithLTCAResults"],
        "_2763": ["CylindricalGearSetSystemDeflection"],
        "_2764": ["CylindricalGearSetSystemDeflectionTimestep"],
        "_2765": ["CylindricalGearSetSystemDeflectionWithLTCAResults"],
        "_2766": ["CylindricalGearSystemDeflection"],
        "_2767": ["CylindricalGearSystemDeflectionTimestep"],
        "_2768": ["CylindricalGearSystemDeflectionWithLTCAResults"],
        "_2769": ["CylindricalMeshedGearFlankSystemDeflection"],
        "_2770": ["CylindricalMeshedGearSystemDeflection"],
        "_2771": ["CylindricalPlanetGearSystemDeflection"],
        "_2772": ["DatumSystemDeflection"],
        "_2773": ["ExternalCADModelSystemDeflection"],
        "_2774": ["FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2775": ["FaceGearMeshSystemDeflection"],
        "_2776": ["FaceGearSetSystemDeflection"],
        "_2777": ["FaceGearSystemDeflection"],
        "_2778": ["FEPartSystemDeflection"],
        "_2779": ["FlexiblePinAssemblySystemDeflection"],
        "_2780": ["GearMeshSystemDeflection"],
        "_2781": ["GearSetSystemDeflection"],
        "_2782": ["GearSystemDeflection"],
        "_2783": ["GuideDxfModelSystemDeflection"],
        "_2784": ["HypoidGearMeshSystemDeflection"],
        "_2785": ["HypoidGearSetSystemDeflection"],
        "_2786": ["HypoidGearSystemDeflection"],
        "_2787": ["InformationForContactAtPointAlongFaceWidth"],
        "_2788": ["InterMountableComponentConnectionSystemDeflection"],
        "_2789": ["KlingelnbergCycloPalloidConicalGearMeshSystemDeflection"],
        "_2790": ["KlingelnbergCycloPalloidConicalGearSetSystemDeflection"],
        "_2791": ["KlingelnbergCycloPalloidConicalGearSystemDeflection"],
        "_2792": ["KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection"],
        "_2793": ["KlingelnbergCycloPalloidHypoidGearSetSystemDeflection"],
        "_2794": ["KlingelnbergCycloPalloidHypoidGearSystemDeflection"],
        "_2795": ["KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection"],
        "_2796": ["KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection"],
        "_2797": ["KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection"],
        "_2798": ["LoadCaseOverallEfficiencyResult"],
        "_2799": ["LoadSharingFactorReporter"],
        "_2800": ["MassDiscSystemDeflection"],
        "_2801": ["MeasurementComponentSystemDeflection"],
        "_2802": ["MeshSeparationsAtFaceWidth"],
        "_2803": ["MountableComponentSystemDeflection"],
        "_2804": ["ObservedPinStiffnessReporter"],
        "_2805": ["OilSealSystemDeflection"],
        "_2806": ["PartSystemDeflection"],
        "_2807": ["PartToPartShearCouplingConnectionSystemDeflection"],
        "_2808": ["PartToPartShearCouplingHalfSystemDeflection"],
        "_2809": ["PartToPartShearCouplingSystemDeflection"],
        "_2810": ["PlanetaryConnectionSystemDeflection"],
        "_2811": ["PlanetCarrierSystemDeflection"],
        "_2812": ["PointLoadSystemDeflection"],
        "_2813": ["PowerLoadSystemDeflection"],
        "_2814": ["PulleySystemDeflection"],
        "_2815": ["RingPinsSystemDeflection"],
        "_2816": ["RingPinsToDiscConnectionSystemDeflection"],
        "_2817": ["RingPinToDiscContactReporting"],
        "_2818": ["RollingRingAssemblySystemDeflection"],
        "_2819": ["RollingRingConnectionSystemDeflection"],
        "_2820": ["RollingRingSystemDeflection"],
        "_2821": ["RootAssemblySystemDeflection"],
        "_2822": ["ShaftHubConnectionSystemDeflection"],
        "_2823": ["ShaftSectionEndResultsSystemDeflection"],
        "_2824": ["ShaftSectionSystemDeflection"],
        "_2825": ["ShaftSystemDeflection"],
        "_2826": ["ShaftToMountableComponentConnectionSystemDeflection"],
        "_2827": ["SpecialisedAssemblySystemDeflection"],
        "_2828": ["SpiralBevelGearMeshSystemDeflection"],
        "_2829": ["SpiralBevelGearSetSystemDeflection"],
        "_2830": ["SpiralBevelGearSystemDeflection"],
        "_2831": ["SpringDamperConnectionSystemDeflection"],
        "_2832": ["SpringDamperHalfSystemDeflection"],
        "_2833": ["SpringDamperSystemDeflection"],
        "_2834": ["StraightBevelDiffGearMeshSystemDeflection"],
        "_2835": ["StraightBevelDiffGearSetSystemDeflection"],
        "_2836": ["StraightBevelDiffGearSystemDeflection"],
        "_2837": ["StraightBevelGearMeshSystemDeflection"],
        "_2838": ["StraightBevelGearSetSystemDeflection"],
        "_2839": ["StraightBevelGearSystemDeflection"],
        "_2840": ["StraightBevelPlanetGearSystemDeflection"],
        "_2841": ["StraightBevelSunGearSystemDeflection"],
        "_2842": ["SynchroniserHalfSystemDeflection"],
        "_2843": ["SynchroniserPartSystemDeflection"],
        "_2844": ["SynchroniserSleeveSystemDeflection"],
        "_2845": ["SynchroniserSystemDeflection"],
        "_2846": ["SystemDeflection"],
        "_2847": ["SystemDeflectionDrawStyle"],
        "_2848": ["SystemDeflectionOptions"],
        "_2849": ["TorqueConverterConnectionSystemDeflection"],
        "_2850": ["TorqueConverterPumpSystemDeflection"],
        "_2851": ["TorqueConverterSystemDeflection"],
        "_2852": ["TorqueConverterTurbineSystemDeflection"],
        "_2853": ["TorsionalSystemDeflection"],
        "_2854": ["TransmissionErrorResult"],
        "_2855": ["UnbalancedMassSystemDeflection"],
        "_2856": ["VirtualComponentSystemDeflection"],
        "_2857": ["WormGearMeshSystemDeflection"],
        "_2858": ["WormGearSetSystemDeflection"],
        "_2859": ["WormGearSystemDeflection"],
        "_2860": ["ZerolBevelGearMeshSystemDeflection"],
        "_2861": ["ZerolBevelGearSetSystemDeflection"],
        "_2862": ["ZerolBevelGearSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblySystemDeflection",
    "AbstractShaftOrHousingSystemDeflection",
    "AbstractShaftSystemDeflection",
    "AbstractShaftToMountableComponentConnectionSystemDeflection",
    "AGMAGleasonConicalGearMeshSystemDeflection",
    "AGMAGleasonConicalGearSetSystemDeflection",
    "AGMAGleasonConicalGearSystemDeflection",
    "AssemblySystemDeflection",
    "BearingDynamicElementContactPropertyWrapper",
    "BearingDynamicElementPropertyWrapper",
    "BearingDynamicPostAnalysisResultWrapper",
    "BearingDynamicResultsPropertyWrapper",
    "BearingDynamicResultsUIWrapper",
    "BearingSystemDeflection",
    "BeltConnectionSystemDeflection",
    "BeltDriveSystemDeflection",
    "BevelDifferentialGearMeshSystemDeflection",
    "BevelDifferentialGearSetSystemDeflection",
    "BevelDifferentialGearSystemDeflection",
    "BevelDifferentialPlanetGearSystemDeflection",
    "BevelDifferentialSunGearSystemDeflection",
    "BevelGearMeshSystemDeflection",
    "BevelGearSetSystemDeflection",
    "BevelGearSystemDeflection",
    "BoltedJointSystemDeflection",
    "BoltSystemDeflection",
    "ClutchConnectionSystemDeflection",
    "ClutchHalfSystemDeflection",
    "ClutchSystemDeflection",
    "CoaxialConnectionSystemDeflection",
    "ComponentSystemDeflection",
    "ConcentricPartGroupCombinationSystemDeflectionResults",
    "ConceptCouplingConnectionSystemDeflection",
    "ConceptCouplingHalfSystemDeflection",
    "ConceptCouplingSystemDeflection",
    "ConceptGearMeshSystemDeflection",
    "ConceptGearSetSystemDeflection",
    "ConceptGearSystemDeflection",
    "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "ConicalGearMeshSystemDeflection",
    "ConicalGearSetSystemDeflection",
    "ConicalGearSystemDeflection",
    "ConnectionSystemDeflection",
    "ConnectorSystemDeflection",
    "CouplingConnectionSystemDeflection",
    "CouplingHalfSystemDeflection",
    "CouplingSystemDeflection",
    "CVTBeltConnectionSystemDeflection",
    "CVTPulleySystemDeflection",
    "CVTSystemDeflection",
    "CycloidalAssemblySystemDeflection",
    "CycloidalDiscCentralBearingConnectionSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
    "CycloidalDiscSystemDeflection",
    "CylindricalGearMeshSystemDeflection",
    "CylindricalGearMeshSystemDeflectionTimestep",
    "CylindricalGearMeshSystemDeflectionWithLTCAResults",
    "CylindricalGearSetSystemDeflection",
    "CylindricalGearSetSystemDeflectionTimestep",
    "CylindricalGearSetSystemDeflectionWithLTCAResults",
    "CylindricalGearSystemDeflection",
    "CylindricalGearSystemDeflectionTimestep",
    "CylindricalGearSystemDeflectionWithLTCAResults",
    "CylindricalMeshedGearFlankSystemDeflection",
    "CylindricalMeshedGearSystemDeflection",
    "CylindricalPlanetGearSystemDeflection",
    "DatumSystemDeflection",
    "ExternalCADModelSystemDeflection",
    "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "FaceGearMeshSystemDeflection",
    "FaceGearSetSystemDeflection",
    "FaceGearSystemDeflection",
    "FEPartSystemDeflection",
    "FlexiblePinAssemblySystemDeflection",
    "GearMeshSystemDeflection",
    "GearSetSystemDeflection",
    "GearSystemDeflection",
    "GuideDxfModelSystemDeflection",
    "HypoidGearMeshSystemDeflection",
    "HypoidGearSetSystemDeflection",
    "HypoidGearSystemDeflection",
    "InformationForContactAtPointAlongFaceWidth",
    "InterMountableComponentConnectionSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
    "LoadCaseOverallEfficiencyResult",
    "LoadSharingFactorReporter",
    "MassDiscSystemDeflection",
    "MeasurementComponentSystemDeflection",
    "MeshSeparationsAtFaceWidth",
    "MountableComponentSystemDeflection",
    "ObservedPinStiffnessReporter",
    "OilSealSystemDeflection",
    "PartSystemDeflection",
    "PartToPartShearCouplingConnectionSystemDeflection",
    "PartToPartShearCouplingHalfSystemDeflection",
    "PartToPartShearCouplingSystemDeflection",
    "PlanetaryConnectionSystemDeflection",
    "PlanetCarrierSystemDeflection",
    "PointLoadSystemDeflection",
    "PowerLoadSystemDeflection",
    "PulleySystemDeflection",
    "RingPinsSystemDeflection",
    "RingPinsToDiscConnectionSystemDeflection",
    "RingPinToDiscContactReporting",
    "RollingRingAssemblySystemDeflection",
    "RollingRingConnectionSystemDeflection",
    "RollingRingSystemDeflection",
    "RootAssemblySystemDeflection",
    "ShaftHubConnectionSystemDeflection",
    "ShaftSectionEndResultsSystemDeflection",
    "ShaftSectionSystemDeflection",
    "ShaftSystemDeflection",
    "ShaftToMountableComponentConnectionSystemDeflection",
    "SpecialisedAssemblySystemDeflection",
    "SpiralBevelGearMeshSystemDeflection",
    "SpiralBevelGearSetSystemDeflection",
    "SpiralBevelGearSystemDeflection",
    "SpringDamperConnectionSystemDeflection",
    "SpringDamperHalfSystemDeflection",
    "SpringDamperSystemDeflection",
    "StraightBevelDiffGearMeshSystemDeflection",
    "StraightBevelDiffGearSetSystemDeflection",
    "StraightBevelDiffGearSystemDeflection",
    "StraightBevelGearMeshSystemDeflection",
    "StraightBevelGearSetSystemDeflection",
    "StraightBevelGearSystemDeflection",
    "StraightBevelPlanetGearSystemDeflection",
    "StraightBevelSunGearSystemDeflection",
    "SynchroniserHalfSystemDeflection",
    "SynchroniserPartSystemDeflection",
    "SynchroniserSleeveSystemDeflection",
    "SynchroniserSystemDeflection",
    "SystemDeflection",
    "SystemDeflectionDrawStyle",
    "SystemDeflectionOptions",
    "TorqueConverterConnectionSystemDeflection",
    "TorqueConverterPumpSystemDeflection",
    "TorqueConverterSystemDeflection",
    "TorqueConverterTurbineSystemDeflection",
    "TorsionalSystemDeflection",
    "TransmissionErrorResult",
    "UnbalancedMassSystemDeflection",
    "VirtualComponentSystemDeflection",
    "WormGearMeshSystemDeflection",
    "WormGearSetSystemDeflection",
    "WormGearSystemDeflection",
    "ZerolBevelGearMeshSystemDeflection",
    "ZerolBevelGearSetSystemDeflection",
    "ZerolBevelGearSystemDeflection",
)
