"""SpringDamperLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6875
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpringDamperLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2621
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6974,
        _6828,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperLoadCase",)


Self = TypeVar("Self", bound="SpringDamperLoadCase")


class SpringDamperLoadCase(_6875.CouplingLoadCase):
    """SpringDamperLoadCase

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperLoadCase")

    class _Cast_SpringDamperLoadCase:
        """Special nested class for casting SpringDamperLoadCase to subclasses."""

        def __init__(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
            parent: "SpringDamperLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_6875.CouplingLoadCase":
            return self._parent._cast(_6875.CouplingLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_6974.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_6828.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_load_case(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase",
        ) -> "SpringDamperLoadCase":
            return self._parent

        def __getattr__(
            self: "SpringDamperLoadCase._Cast_SpringDamperLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2621.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SpringDamperLoadCase._Cast_SpringDamperLoadCase":
        return self._Cast_SpringDamperLoadCase(self)
