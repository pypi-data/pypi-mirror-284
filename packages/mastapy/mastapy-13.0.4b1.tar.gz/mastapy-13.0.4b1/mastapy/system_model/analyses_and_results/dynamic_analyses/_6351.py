"""DynamicAnalysisDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.drawing import _2266
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_ANALYSIS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "DynamicAnalysisDrawStyle",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4677
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5783
    from mastapy.geometry import _311


__docformat__ = "restructuredtext en"
__all__ = ("DynamicAnalysisDrawStyle",)


Self = TypeVar("Self", bound="DynamicAnalysisDrawStyle")


class DynamicAnalysisDrawStyle(_2266.ContourDrawStyle):
    """DynamicAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_ANALYSIS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicAnalysisDrawStyle")

    class _Cast_DynamicAnalysisDrawStyle:
        """Special nested class for casting DynamicAnalysisDrawStyle to subclasses."""

        def __init__(
            self: "DynamicAnalysisDrawStyle._Cast_DynamicAnalysisDrawStyle",
            parent: "DynamicAnalysisDrawStyle",
        ):
            self._parent = parent

        @property
        def contour_draw_style(
            self: "DynamicAnalysisDrawStyle._Cast_DynamicAnalysisDrawStyle",
        ) -> "_2266.ContourDrawStyle":
            return self._parent._cast(_2266.ContourDrawStyle)

        @property
        def draw_style_base(
            self: "DynamicAnalysisDrawStyle._Cast_DynamicAnalysisDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def modal_analysis_draw_style(
            self: "DynamicAnalysisDrawStyle._Cast_DynamicAnalysisDrawStyle",
        ) -> "_4677.ModalAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677

            return self._parent._cast(_4677.ModalAnalysisDrawStyle)

        @property
        def harmonic_analysis_draw_style(
            self: "DynamicAnalysisDrawStyle._Cast_DynamicAnalysisDrawStyle",
        ) -> "_5783.HarmonicAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(_5783.HarmonicAnalysisDrawStyle)

        @property
        def dynamic_analysis_draw_style(
            self: "DynamicAnalysisDrawStyle._Cast_DynamicAnalysisDrawStyle",
        ) -> "DynamicAnalysisDrawStyle":
            return self._parent

        def __getattr__(
            self: "DynamicAnalysisDrawStyle._Cast_DynamicAnalysisDrawStyle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicAnalysisDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def animate_contour(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.AnimateContour

        if temp is None:
            return False

        return temp

    @animate_contour.setter
    @enforce_parameter_types
    def animate_contour(self: Self, value: "bool"):
        self.wrapped.AnimateContour = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicAnalysisDrawStyle._Cast_DynamicAnalysisDrawStyle":
        return self._Cast_DynamicAnalysisDrawStyle(self)
