"""AnalysisCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2671
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "AnalysisCase"
)

if TYPE_CHECKING:
    from mastapy.utility import _1596
    from mastapy.system_model import _2223
    from mastapy.system_model.analyses_and_results import _2672
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2846,
        _2853,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3056,
        _3110,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3371,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3630,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3837,
        _3891,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4143
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4409
    from mastapy.system_model.analyses_and_results.modal_analyses import _4646, _4675
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4930,
        _4956,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5215,
    )
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5486
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5753,
        _5782,
        _5786,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6091,
        _6107,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6604
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7031,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7295,
        _7297,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7558,
        _7565,
        _7571,
        _7572,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisCase",)


Self = TypeVar("Self", bound="AnalysisCase")


class AnalysisCase(_2671.Context):
    """AnalysisCase

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AnalysisCase")

    class _Cast_AnalysisCase:
        """Special nested class for casting AnalysisCase to subclasses."""

        def __init__(self: "AnalysisCase._Cast_AnalysisCase", parent: "AnalysisCase"):
            self._parent = parent

        @property
        def context(self: "AnalysisCase._Cast_AnalysisCase") -> "_2671.Context":
            return self._parent._cast(_2671.Context)

        @property
        def system_deflection(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_2846.SystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.SystemDeflection)

        @property
        def torsional_system_deflection(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_2853.TorsionalSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2853,
            )

            return self._parent._cast(_2853.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3056.DynamicModelForSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(
                _3056.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def steady_state_synchronous_response(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3110.SteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(_3110.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3371.SteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3371,
            )

            return self._parent._cast(_3371.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3630.SteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(_3630.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3837.DynamicModelForStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(_3837.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3891.StabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3891,
            )

            return self._parent._cast(_3891.StabilityAnalysis)

        @property
        def power_flow(self: "AnalysisCase._Cast_AnalysisCase") -> "_4143.PowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.PowerFlow)

        @property
        def parametric_study_tool(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_4409.ParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.ParametricStudyTool)

        @property
        def dynamic_model_for_modal_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_4646.DynamicModelForModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(_4646.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_4675.ModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_4930.DynamicModelAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4930,
            )

            return self._parent._cast(_4930.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_4956.ModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(_4956.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_5215.ModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5215,
            )

            return self._parent._cast(_5215.ModalAnalysisAtASpeed)

        @property
        def multibody_dynamics_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_5486.MultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(_5486.MultibodyDynamicsAnalysis)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_5753.DynamicModelForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_5782.HarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(_5782.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_5786.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(
                _5786.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_of_single_excitation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_6091.HarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_6107.ModalAnalysisForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6107,
            )

            return self._parent._cast(_6107.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_6350.DynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(_6350.DynamicAnalysis)

        @property
        def critical_speed_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_6604.CriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.CriticalSpeedAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7031.AdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7031,
            )

            return self._parent._cast(_7031.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7295.AdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7297.AdvancedSystemDeflectionSubAnalysis":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.AdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_analysis_case(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7558.CompoundAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7558

            return self._parent._cast(_7558.CompoundAnalysisCase)

        @property
        def fe_analysis(self: "AnalysisCase._Cast_AnalysisCase") -> "_7565.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7571.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.StaticLoadAnalysisCase)

        @property
        def time_series_load_analysis_case(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7572.TimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.TimeSeriesLoadAnalysisCase)

        @property
        def analysis_case(self: "AnalysisCase._Cast_AnalysisCase") -> "AnalysisCase":
            return self._parent

        def __getattr__(self: "AnalysisCase._Cast_AnalysisCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_setup_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSetupTime

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseName

        if temp is None:
            return ""

        return temp

    @property
    def analysis_run_information(self: Self) -> "_1596.AnalysisRunInformation":
        """mastapy.utility.AnalysisRunInformation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisRunInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_ready(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsReady

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def results_for(
        self: Self, design_entity: "_2223.DesignEntity"
    ) -> "_2672.DesignEntityAnalysis":
        """mastapy.system_model.analyses_and_results.DesignEntityAnalysis

        Args:
            design_entity (mastapy.system_model.DesignEntity)
        """
        method_result = self.wrapped.ResultsFor(
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def perform_analysis(self: Self):
        """Method does not return."""
        self.wrapped.PerformAnalysis()

    @property
    def cast_to(self: Self) -> "AnalysisCase._Cast_AnalysisCase":
        return self._Cast_AnalysisCase(self)
