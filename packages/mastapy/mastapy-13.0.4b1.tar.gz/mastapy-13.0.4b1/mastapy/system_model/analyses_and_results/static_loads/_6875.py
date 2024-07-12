"""CouplingLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6974
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6856,
        _6862,
        _6953,
        _6980,
        _6995,
        _6828,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingLoadCase",)


Self = TypeVar("Self", bound="CouplingLoadCase")


class CouplingLoadCase(_6974.SpecialisedAssemblyLoadCase):
    """CouplingLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingLoadCase")

    class _Cast_CouplingLoadCase:
        """Special nested class for casting CouplingLoadCase to subclasses."""

        def __init__(
            self: "CouplingLoadCase._Cast_CouplingLoadCase", parent: "CouplingLoadCase"
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6974.SpecialisedAssemblyLoadCase":
            return self._parent._cast(_6974.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6828.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6856.ClutchLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.ClutchLoadCase)

        @property
        def concept_coupling_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6862.ConceptCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6862

            return self._parent._cast(_6862.ConceptCouplingLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6953.PartToPartShearCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.PartToPartShearCouplingLoadCase)

        @property
        def spring_damper_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6980.SpringDamperLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.SpringDamperLoadCase)

        @property
        def torque_converter_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "_6995.TorqueConverterLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6995

            return self._parent._cast(_6995.TorqueConverterLoadCase)

        @property
        def coupling_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "CouplingLoadCase":
            return self._parent

        def __getattr__(self: "CouplingLoadCase._Cast_CouplingLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2604.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingLoadCase._Cast_CouplingLoadCase":
        return self._Cast_CouplingLoadCase(self)
