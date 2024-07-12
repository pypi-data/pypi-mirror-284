"""GuideDxfModelLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6859
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GuideDxfModelLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.analyses_and_results.static_loads import _6950
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelLoadCase",)


Self = TypeVar("Self", bound="GuideDxfModelLoadCase")


class GuideDxfModelLoadCase(_6859.ComponentLoadCase):
    """GuideDxfModelLoadCase

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelLoadCase")

    class _Cast_GuideDxfModelLoadCase:
        """Special nested class for casting GuideDxfModelLoadCase to subclasses."""

        def __init__(
            self: "GuideDxfModelLoadCase._Cast_GuideDxfModelLoadCase",
            parent: "GuideDxfModelLoadCase",
        ):
            self._parent = parent

        @property
        def component_load_case(
            self: "GuideDxfModelLoadCase._Cast_GuideDxfModelLoadCase",
        ) -> "_6859.ComponentLoadCase":
            return self._parent._cast(_6859.ComponentLoadCase)

        @property
        def part_load_case(
            self: "GuideDxfModelLoadCase._Cast_GuideDxfModelLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "GuideDxfModelLoadCase._Cast_GuideDxfModelLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelLoadCase._Cast_GuideDxfModelLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelLoadCase._Cast_GuideDxfModelLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def guide_dxf_model_load_case(
            self: "GuideDxfModelLoadCase._Cast_GuideDxfModelLoadCase",
        ) -> "GuideDxfModelLoadCase":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelLoadCase._Cast_GuideDxfModelLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideDxfModelLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2475.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GuideDxfModelLoadCase._Cast_GuideDxfModelLoadCase":
        return self._Cast_GuideDxfModelLoadCase(self)
