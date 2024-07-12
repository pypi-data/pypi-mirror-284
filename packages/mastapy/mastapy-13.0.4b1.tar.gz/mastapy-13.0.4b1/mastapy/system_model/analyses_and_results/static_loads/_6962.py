"""PulleyLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6874
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PulleyLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2611
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6878,
        _6946,
        _6859,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PulleyLoadCase",)


Self = TypeVar("Self", bound="PulleyLoadCase")


class PulleyLoadCase(_6874.CouplingHalfLoadCase):
    """PulleyLoadCase

    This is a mastapy class.
    """

    TYPE = _PULLEY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyLoadCase")

    class _Cast_PulleyLoadCase:
        """Special nested class for casting PulleyLoadCase to subclasses."""

        def __init__(
            self: "PulleyLoadCase._Cast_PulleyLoadCase", parent: "PulleyLoadCase"
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "PulleyLoadCase._Cast_PulleyLoadCase",
        ) -> "_6874.CouplingHalfLoadCase":
            return self._parent._cast(_6874.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "PulleyLoadCase._Cast_PulleyLoadCase",
        ) -> "_6946.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "PulleyLoadCase._Cast_PulleyLoadCase",
        ) -> "_6859.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ComponentLoadCase)

        @property
        def part_load_case(
            self: "PulleyLoadCase._Cast_PulleyLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "PulleyLoadCase._Cast_PulleyLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleyLoadCase._Cast_PulleyLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyLoadCase._Cast_PulleyLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_load_case(
            self: "PulleyLoadCase._Cast_PulleyLoadCase",
        ) -> "_6878.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6878

            return self._parent._cast(_6878.CVTPulleyLoadCase)

        @property
        def pulley_load_case(
            self: "PulleyLoadCase._Cast_PulleyLoadCase",
        ) -> "PulleyLoadCase":
            return self._parent

        def __getattr__(self: "PulleyLoadCase._Cast_PulleyLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2611.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PulleyLoadCase._Cast_PulleyLoadCase":
        return self._Cast_PulleyLoadCase(self)
