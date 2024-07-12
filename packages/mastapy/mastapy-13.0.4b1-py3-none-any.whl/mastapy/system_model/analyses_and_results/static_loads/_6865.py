"""ConceptGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6917
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6863,
        _6864,
        _6974,
        _6828,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetLoadCase",)


Self = TypeVar("Self", bound="ConceptGearSetLoadCase")


class ConceptGearSetLoadCase(_6917.GearSetLoadCase):
    """ConceptGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetLoadCase")

    class _Cast_ConceptGearSetLoadCase:
        """Special nested class for casting ConceptGearSetLoadCase to subclasses."""

        def __init__(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
            parent: "ConceptGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "_6917.GearSetLoadCase":
            return self._parent._cast(_6917.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "_6974.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "_6828.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_gear_set_load_case(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase",
        ) -> "ConceptGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6863.ConceptGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_gears_load_case(self: Self) -> "List[_6863.ConceptGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_load_case(self: Self) -> "List[_6864.ConceptGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConceptGearSetLoadCase._Cast_ConceptGearSetLoadCase":
        return self._Cast_ConceptGearSetLoadCase(self)
