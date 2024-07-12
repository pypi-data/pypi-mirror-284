"""DynamicModelAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "DynamicModelAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7565,
        _7571,
        _7556,
    )
    from mastapy.system_model.analyses_and_results import _2671


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelAtAStiffness",)


Self = TypeVar("Self", bound="DynamicModelAtAStiffness")


class DynamicModelAtAStiffness(_6350.DynamicAnalysis):
    """DynamicModelAtAStiffness

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicModelAtAStiffness")

    class _Cast_DynamicModelAtAStiffness:
        """Special nested class for casting DynamicModelAtAStiffness to subclasses."""

        def __init__(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
            parent: "DynamicModelAtAStiffness",
        ):
            self._parent = parent

        @property
        def dynamic_analysis(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "_6350.DynamicAnalysis":
            return self._parent._cast(_6350.DynamicAnalysis)

        @property
        def fe_analysis(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "_7565.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "_7571.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "_7556.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.AnalysisCase)

        @property
        def context(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "_2671.Context":
            from mastapy.system_model.analyses_and_results import _2671

            return self._parent._cast(_2671.Context)

        @property
        def dynamic_model_at_a_stiffness(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "DynamicModelAtAStiffness":
            return self._parent

        def __getattr__(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicModelAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness":
        return self._Cast_DynamicModelAtAStiffness(self)
