"""SpringDamperHalfLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6874
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperHalfLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2622
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6946,
        _6859,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfLoadCase",)


Self = TypeVar("Self", bound="SpringDamperHalfLoadCase")


class SpringDamperHalfLoadCase(_6874.CouplingHalfLoadCase):
    """SpringDamperHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperHalfLoadCase")

    class _Cast_SpringDamperHalfLoadCase:
        """Special nested class for casting SpringDamperHalfLoadCase to subclasses."""

        def __init__(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
            parent: "SpringDamperHalfLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ) -> "_6874.CouplingHalfLoadCase":
            return self._parent._cast(_6874.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ) -> "_6946.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ) -> "_6859.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ComponentLoadCase)

        @property
        def part_load_case(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_half_load_case(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase",
        ) -> "SpringDamperHalfLoadCase":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperHalfLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2622.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperHalfLoadCase._Cast_SpringDamperHalfLoadCase":
        return self._Cast_SpringDamperHalfLoadCase(self)
