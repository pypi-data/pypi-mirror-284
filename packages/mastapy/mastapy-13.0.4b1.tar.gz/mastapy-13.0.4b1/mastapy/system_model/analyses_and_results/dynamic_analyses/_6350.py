"""DynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses", "DynamicAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3056,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import _3837
    from mastapy.system_model.analyses_and_results.modal_analyses import _4646
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4930,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571, _7556
    from mastapy.system_model.analyses_and_results import _2671


__docformat__ = "restructuredtext en"
__all__ = ("DynamicAnalysis",)


Self = TypeVar("Self", bound="DynamicAnalysis")


class DynamicAnalysis(_7565.FEAnalysis):
    """DynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicAnalysis")

    class _Cast_DynamicAnalysis:
        """Special nested class for casting DynamicAnalysis to subclasses."""

        def __init__(
            self: "DynamicAnalysis._Cast_DynamicAnalysis", parent: "DynamicAnalysis"
        ):
            self._parent = parent

        @property
        def fe_analysis(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ) -> "_7565.FEAnalysis":
            return self._parent._cast(_7565.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ) -> "_7571.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ) -> "_7556.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.AnalysisCase)

        @property
        def context(self: "DynamicAnalysis._Cast_DynamicAnalysis") -> "_2671.Context":
            from mastapy.system_model.analyses_and_results import _2671

            return self._parent._cast(_2671.Context)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ) -> "_3056.DynamicModelForSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(
                _3056.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def dynamic_model_for_stability_analysis(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ) -> "_3837.DynamicModelForStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(_3837.DynamicModelForStabilityAnalysis)

        @property
        def dynamic_model_for_modal_analysis(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ) -> "_4646.DynamicModelForModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(_4646.DynamicModelForModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ) -> "_4930.DynamicModelAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4930,
            )

            return self._parent._cast(_4930.DynamicModelAtAStiffness)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ) -> "_5753.DynamicModelForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.DynamicModelForHarmonicAnalysis)

        @property
        def dynamic_analysis(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ) -> "DynamicAnalysis":
            return self._parent

        def __getattr__(self: "DynamicAnalysis._Cast_DynamicAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DynamicAnalysis._Cast_DynamicAnalysis":
        return self._Cast_DynamicAnalysis(self)
