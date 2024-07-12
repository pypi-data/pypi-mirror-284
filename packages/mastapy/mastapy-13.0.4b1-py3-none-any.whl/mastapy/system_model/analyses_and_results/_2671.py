"""Context"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTEXT = python_net_import("SMT.MastaAPI.SystemModel.AnalysesAndResults", "Context")

if TYPE_CHECKING:
    from mastapy.utility import _1601
    from mastapy.system_model import _2220
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
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4408,
        _4409,
    )
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
        _5791,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6091,
        _6107,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6604
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6825,
        _6826,
        _6827,
        _6833,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7031,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7295,
        _7297,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7556,
        _7558,
        _7565,
        _7571,
        _7572,
    )


__docformat__ = "restructuredtext en"
__all__ = ("Context",)


Self = TypeVar("Self", bound="Context")


class Context(_0.APIBase):
    """Context

    This is a mastapy class.
    """

    TYPE = _CONTEXT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Context")

    class _Cast_Context:
        """Special nested class for casting Context to subclasses."""

        def __init__(self: "Context._Cast_Context", parent: "Context"):
            self._parent = parent

        @property
        def system_deflection(
            self: "Context._Cast_Context",
        ) -> "_2846.SystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2846,
            )

            return self._parent._cast(_2846.SystemDeflection)

        @property
        def torsional_system_deflection(
            self: "Context._Cast_Context",
        ) -> "_2853.TorsionalSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2853,
            )

            return self._parent._cast(_2853.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "Context._Cast_Context",
        ) -> "_3056.DynamicModelForSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(
                _3056.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def steady_state_synchronous_response(
            self: "Context._Cast_Context",
        ) -> "_3110.SteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(_3110.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(
            self: "Context._Cast_Context",
        ) -> "_3371.SteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3371,
            )

            return self._parent._cast(_3371.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(
            self: "Context._Cast_Context",
        ) -> "_3630.SteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(_3630.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(
            self: "Context._Cast_Context",
        ) -> "_3837.DynamicModelForStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(_3837.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(
            self: "Context._Cast_Context",
        ) -> "_3891.StabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3891,
            )

            return self._parent._cast(_3891.StabilityAnalysis)

        @property
        def power_flow(self: "Context._Cast_Context") -> "_4143.PowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.PowerFlow)

        @property
        def parametric_study_static_load(
            self: "Context._Cast_Context",
        ) -> "_4408.ParametricStudyStaticLoad":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.ParametricStudyStaticLoad)

        @property
        def parametric_study_tool(
            self: "Context._Cast_Context",
        ) -> "_4409.ParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.ParametricStudyTool)

        @property
        def dynamic_model_for_modal_analysis(
            self: "Context._Cast_Context",
        ) -> "_4646.DynamicModelForModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(_4646.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(self: "Context._Cast_Context") -> "_4675.ModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(
            self: "Context._Cast_Context",
        ) -> "_4930.DynamicModelAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4930,
            )

            return self._parent._cast(_4930.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(
            self: "Context._Cast_Context",
        ) -> "_4956.ModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(_4956.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(
            self: "Context._Cast_Context",
        ) -> "_5215.ModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5215,
            )

            return self._parent._cast(_5215.ModalAnalysisAtASpeed)

        @property
        def multibody_dynamics_analysis(
            self: "Context._Cast_Context",
        ) -> "_5486.MultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(_5486.MultibodyDynamicsAnalysis)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "Context._Cast_Context",
        ) -> "_5753.DynamicModelForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(
            self: "Context._Cast_Context",
        ) -> "_5782.HarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(_5782.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "Context._Cast_Context",
        ) -> "_5786.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(
                _5786.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_with_varying_stiffness_static_load_case(
            self: "Context._Cast_Context",
        ) -> "_5791.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(
                _5791.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
            )

        @property
        def harmonic_analysis_of_single_excitation(
            self: "Context._Cast_Context",
        ) -> "_6091.HarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "Context._Cast_Context",
        ) -> "_6107.ModalAnalysisForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6107,
            )

            return self._parent._cast(_6107.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(self: "Context._Cast_Context") -> "_6350.DynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(_6350.DynamicAnalysis)

        @property
        def critical_speed_analysis(
            self: "Context._Cast_Context",
        ) -> "_6604.CriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.CriticalSpeedAnalysis)

        @property
        def load_case(self: "Context._Cast_Context") -> "_6825.LoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.LoadCase)

        @property
        def static_load_case(self: "Context._Cast_Context") -> "_6826.StaticLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.StaticLoadCase)

        @property
        def time_series_load_case(
            self: "Context._Cast_Context",
        ) -> "_6827.TimeSeriesLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.TimeSeriesLoadCase)

        @property
        def advanced_time_stepping_analysis_for_modulation_static_load_case(
            self: "Context._Cast_Context",
        ) -> "_6833.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(
                _6833.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
            )

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "Context._Cast_Context",
        ) -> "_7031.AdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7031,
            )

            return self._parent._cast(_7031.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(
            self: "Context._Cast_Context",
        ) -> "_7295.AdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "Context._Cast_Context",
        ) -> "_7297.AdvancedSystemDeflectionSubAnalysis":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.AdvancedSystemDeflectionSubAnalysis)

        @property
        def analysis_case(self: "Context._Cast_Context") -> "_7556.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.AnalysisCase)

        @property
        def compound_analysis_case(
            self: "Context._Cast_Context",
        ) -> "_7558.CompoundAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7558

            return self._parent._cast(_7558.CompoundAnalysisCase)

        @property
        def fe_analysis(self: "Context._Cast_Context") -> "_7565.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "Context._Cast_Context",
        ) -> "_7571.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.StaticLoadAnalysisCase)

        @property
        def time_series_load_analysis_case(
            self: "Context._Cast_Context",
        ) -> "_7572.TimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.TimeSeriesLoadAnalysisCase)

        @property
        def context(self: "Context._Cast_Context") -> "Context":
            return self._parent

        def __getattr__(self: "Context._Cast_Context", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Context.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def save_history_information(self: Self) -> "_1601.FileHistoryItem":
        """mastapy.utility.FileHistoryItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SaveHistoryInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def design_properties(self: Self) -> "_2220.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "Context._Cast_Context":
        return self._Cast_Context(self)
