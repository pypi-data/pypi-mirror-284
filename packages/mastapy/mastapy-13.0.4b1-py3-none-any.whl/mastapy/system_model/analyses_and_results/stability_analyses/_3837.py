"""DynamicModelForStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "DynamicModelForStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7565,
        _7571,
        _7556,
    )
    from mastapy.system_model.analyses_and_results import _2671


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelForStabilityAnalysis",)


Self = TypeVar("Self", bound="DynamicModelForStabilityAnalysis")


class DynamicModelForStabilityAnalysis(_6350.DynamicAnalysis):
    """DynamicModelForStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicModelForStabilityAnalysis")

    class _Cast_DynamicModelForStabilityAnalysis:
        """Special nested class for casting DynamicModelForStabilityAnalysis to subclasses."""

        def __init__(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
            parent: "DynamicModelForStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def dynamic_analysis(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_6350.DynamicAnalysis":
            return self._parent._cast(_6350.DynamicAnalysis)

        @property
        def fe_analysis(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_7565.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_7571.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_7556.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.AnalysisCase)

        @property
        def context(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_2671.Context":
            from mastapy.system_model.analyses_and_results import _2671

            return self._parent._cast(_2671.Context)

        @property
        def dynamic_model_for_stability_analysis(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "DynamicModelForStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicModelForStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis":
        return self._Cast_DynamicModelForStabilityAnalysis(self)
