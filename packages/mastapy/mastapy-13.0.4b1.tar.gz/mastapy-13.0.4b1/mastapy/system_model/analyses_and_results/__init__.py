"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2640 import CompoundAnalysis
    from ._2641 import SingleAnalysis
    from ._2642 import AdvancedSystemDeflectionAnalysis
    from ._2643 import AdvancedSystemDeflectionSubAnalysis
    from ._2644 import AdvancedTimeSteppingAnalysisForModulation
    from ._2645 import CompoundParametricStudyToolAnalysis
    from ._2646 import CriticalSpeedAnalysis
    from ._2647 import DynamicAnalysis
    from ._2648 import DynamicModelAtAStiffnessAnalysis
    from ._2649 import DynamicModelForHarmonicAnalysis
    from ._2650 import DynamicModelForModalAnalysis
    from ._2651 import DynamicModelForStabilityAnalysis
    from ._2652 import DynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2653 import HarmonicAnalysis
    from ._2654 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._2655 import HarmonicAnalysisOfSingleExcitationAnalysis
    from ._2656 import ModalAnalysis
    from ._2657 import ModalAnalysisAtASpeed
    from ._2658 import ModalAnalysisAtAStiffness
    from ._2659 import ModalAnalysisForHarmonicAnalysis
    from ._2660 import MultibodyDynamicsAnalysis
    from ._2661 import ParametricStudyToolAnalysis
    from ._2662 import PowerFlowAnalysis
    from ._2663 import StabilityAnalysis
    from ._2664 import SteadyStateSynchronousResponseAnalysis
    from ._2665 import SteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2666 import SteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2667 import SystemDeflectionAnalysis
    from ._2668 import TorsionalSystemDeflectionAnalysis
    from ._2669 import AnalysisCaseVariable
    from ._2670 import ConnectionAnalysis
    from ._2671 import Context
    from ._2672 import DesignEntityAnalysis
    from ._2673 import DesignEntityGroupAnalysis
    from ._2674 import DesignEntitySingleContextAnalysis
    from ._2678 import PartAnalysis
    from ._2679 import CompoundAdvancedSystemDeflectionAnalysis
    from ._2680 import CompoundAdvancedSystemDeflectionSubAnalysis
    from ._2681 import CompoundAdvancedTimeSteppingAnalysisForModulation
    from ._2682 import CompoundCriticalSpeedAnalysis
    from ._2683 import CompoundDynamicAnalysis
    from ._2684 import CompoundDynamicModelAtAStiffnessAnalysis
    from ._2685 import CompoundDynamicModelForHarmonicAnalysis
    from ._2686 import CompoundDynamicModelForModalAnalysis
    from ._2687 import CompoundDynamicModelForStabilityAnalysis
    from ._2688 import CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2689 import CompoundHarmonicAnalysis
    from ._2690 import (
        CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._2691 import CompoundHarmonicAnalysisOfSingleExcitationAnalysis
    from ._2692 import CompoundModalAnalysis
    from ._2693 import CompoundModalAnalysisAtASpeed
    from ._2694 import CompoundModalAnalysisAtAStiffness
    from ._2695 import CompoundModalAnalysisForHarmonicAnalysis
    from ._2696 import CompoundMultibodyDynamicsAnalysis
    from ._2697 import CompoundPowerFlowAnalysis
    from ._2698 import CompoundStabilityAnalysis
    from ._2699 import CompoundSteadyStateSynchronousResponseAnalysis
    from ._2700 import CompoundSteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2701 import CompoundSteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2702 import CompoundSystemDeflectionAnalysis
    from ._2703 import CompoundTorsionalSystemDeflectionAnalysis
    from ._2704 import TESetUpForDynamicAnalysisOptions
    from ._2705 import TimeOptions
else:
    import_structure = {
        "_2640": ["CompoundAnalysis"],
        "_2641": ["SingleAnalysis"],
        "_2642": ["AdvancedSystemDeflectionAnalysis"],
        "_2643": ["AdvancedSystemDeflectionSubAnalysis"],
        "_2644": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_2645": ["CompoundParametricStudyToolAnalysis"],
        "_2646": ["CriticalSpeedAnalysis"],
        "_2647": ["DynamicAnalysis"],
        "_2648": ["DynamicModelAtAStiffnessAnalysis"],
        "_2649": ["DynamicModelForHarmonicAnalysis"],
        "_2650": ["DynamicModelForModalAnalysis"],
        "_2651": ["DynamicModelForStabilityAnalysis"],
        "_2652": ["DynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2653": ["HarmonicAnalysis"],
        "_2654": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_2655": ["HarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2656": ["ModalAnalysis"],
        "_2657": ["ModalAnalysisAtASpeed"],
        "_2658": ["ModalAnalysisAtAStiffness"],
        "_2659": ["ModalAnalysisForHarmonicAnalysis"],
        "_2660": ["MultibodyDynamicsAnalysis"],
        "_2661": ["ParametricStudyToolAnalysis"],
        "_2662": ["PowerFlowAnalysis"],
        "_2663": ["StabilityAnalysis"],
        "_2664": ["SteadyStateSynchronousResponseAnalysis"],
        "_2665": ["SteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2666": ["SteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2667": ["SystemDeflectionAnalysis"],
        "_2668": ["TorsionalSystemDeflectionAnalysis"],
        "_2669": ["AnalysisCaseVariable"],
        "_2670": ["ConnectionAnalysis"],
        "_2671": ["Context"],
        "_2672": ["DesignEntityAnalysis"],
        "_2673": ["DesignEntityGroupAnalysis"],
        "_2674": ["DesignEntitySingleContextAnalysis"],
        "_2678": ["PartAnalysis"],
        "_2679": ["CompoundAdvancedSystemDeflectionAnalysis"],
        "_2680": ["CompoundAdvancedSystemDeflectionSubAnalysis"],
        "_2681": ["CompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_2682": ["CompoundCriticalSpeedAnalysis"],
        "_2683": ["CompoundDynamicAnalysis"],
        "_2684": ["CompoundDynamicModelAtAStiffnessAnalysis"],
        "_2685": ["CompoundDynamicModelForHarmonicAnalysis"],
        "_2686": ["CompoundDynamicModelForModalAnalysis"],
        "_2687": ["CompoundDynamicModelForStabilityAnalysis"],
        "_2688": ["CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2689": ["CompoundHarmonicAnalysis"],
        "_2690": [
            "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_2691": ["CompoundHarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2692": ["CompoundModalAnalysis"],
        "_2693": ["CompoundModalAnalysisAtASpeed"],
        "_2694": ["CompoundModalAnalysisAtAStiffness"],
        "_2695": ["CompoundModalAnalysisForHarmonicAnalysis"],
        "_2696": ["CompoundMultibodyDynamicsAnalysis"],
        "_2697": ["CompoundPowerFlowAnalysis"],
        "_2698": ["CompoundStabilityAnalysis"],
        "_2699": ["CompoundSteadyStateSynchronousResponseAnalysis"],
        "_2700": ["CompoundSteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2701": ["CompoundSteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2702": ["CompoundSystemDeflectionAnalysis"],
        "_2703": ["CompoundTorsionalSystemDeflectionAnalysis"],
        "_2704": ["TESetUpForDynamicAnalysisOptions"],
        "_2705": ["TimeOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CompoundAnalysis",
    "SingleAnalysis",
    "AdvancedSystemDeflectionAnalysis",
    "AdvancedSystemDeflectionSubAnalysis",
    "AdvancedTimeSteppingAnalysisForModulation",
    "CompoundParametricStudyToolAnalysis",
    "CriticalSpeedAnalysis",
    "DynamicAnalysis",
    "DynamicModelAtAStiffnessAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "DynamicModelForModalAnalysis",
    "DynamicModelForStabilityAnalysis",
    "DynamicModelForSteadyStateSynchronousResponseAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOfSingleExcitationAnalysis",
    "ModalAnalysis",
    "ModalAnalysisAtASpeed",
    "ModalAnalysisAtAStiffness",
    "ModalAnalysisForHarmonicAnalysis",
    "MultibodyDynamicsAnalysis",
    "ParametricStudyToolAnalysis",
    "PowerFlowAnalysis",
    "StabilityAnalysis",
    "SteadyStateSynchronousResponseAnalysis",
    "SteadyStateSynchronousResponseAtASpeedAnalysis",
    "SteadyStateSynchronousResponseOnAShaftAnalysis",
    "SystemDeflectionAnalysis",
    "TorsionalSystemDeflectionAnalysis",
    "AnalysisCaseVariable",
    "ConnectionAnalysis",
    "Context",
    "DesignEntityAnalysis",
    "DesignEntityGroupAnalysis",
    "DesignEntitySingleContextAnalysis",
    "PartAnalysis",
    "CompoundAdvancedSystemDeflectionAnalysis",
    "CompoundAdvancedSystemDeflectionSubAnalysis",
    "CompoundAdvancedTimeSteppingAnalysisForModulation",
    "CompoundCriticalSpeedAnalysis",
    "CompoundDynamicAnalysis",
    "CompoundDynamicModelAtAStiffnessAnalysis",
    "CompoundDynamicModelForHarmonicAnalysis",
    "CompoundDynamicModelForModalAnalysis",
    "CompoundDynamicModelForStabilityAnalysis",
    "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
    "CompoundHarmonicAnalysis",
    "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
    "CompoundModalAnalysis",
    "CompoundModalAnalysisAtASpeed",
    "CompoundModalAnalysisAtAStiffness",
    "CompoundModalAnalysisForHarmonicAnalysis",
    "CompoundMultibodyDynamicsAnalysis",
    "CompoundPowerFlowAnalysis",
    "CompoundStabilityAnalysis",
    "CompoundSteadyStateSynchronousResponseAnalysis",
    "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
    "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
    "CompoundSystemDeflectionAnalysis",
    "CompoundTorsionalSystemDeflectionAnalysis",
    "TESetUpForDynamicAnalysisOptions",
    "TimeOptions",
)
