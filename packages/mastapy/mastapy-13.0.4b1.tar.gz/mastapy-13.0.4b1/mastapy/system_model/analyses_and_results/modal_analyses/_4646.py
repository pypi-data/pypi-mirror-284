"""DynamicModelForModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "DynamicModelForModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7565,
        _7571,
        _7556,
    )
    from mastapy.system_model.analyses_and_results import _2671


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelForModalAnalysis",)


Self = TypeVar("Self", bound="DynamicModelForModalAnalysis")


class DynamicModelForModalAnalysis(_6350.DynamicAnalysis):
    """DynamicModelForModalAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicModelForModalAnalysis")

    class _Cast_DynamicModelForModalAnalysis:
        """Special nested class for casting DynamicModelForModalAnalysis to subclasses."""

        def __init__(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
            parent: "DynamicModelForModalAnalysis",
        ):
            self._parent = parent

        @property
        def dynamic_analysis(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ) -> "_6350.DynamicAnalysis":
            return self._parent._cast(_6350.DynamicAnalysis)

        @property
        def fe_analysis(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ) -> "_7565.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ) -> "_7571.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ) -> "_7556.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.AnalysisCase)

        @property
        def context(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ) -> "_2671.Context":
            from mastapy.system_model.analyses_and_results import _2671

            return self._parent._cast(_2671.Context)

        @property
        def dynamic_model_for_modal_analysis(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ) -> "DynamicModelForModalAnalysis":
            return self._parent

        def __getattr__(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicModelForModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis":
        return self._Cast_DynamicModelForModalAnalysis(self)
