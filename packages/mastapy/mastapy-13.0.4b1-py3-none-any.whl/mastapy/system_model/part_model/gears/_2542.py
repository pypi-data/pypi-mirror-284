"""ConceptGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.concept import _1196
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.part_model import _2496, _2454, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSet",)


Self = TypeVar("Self", bound="ConceptGearSet")


class ConceptGearSet(_2552.GearSet):
    """ConceptGearSet

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSet")

    class _Cast_ConceptGearSet:
        """Special nested class for casting ConceptGearSet to subclasses."""

        def __init__(
            self: "ConceptGearSet._Cast_ConceptGearSet", parent: "ConceptGearSet"
        ):
            self._parent = parent

        @property
        def gear_set(self: "ConceptGearSet._Cast_ConceptGearSet") -> "_2552.GearSet":
            return self._parent._cast(_2552.GearSet)

        @property
        def specialised_assembly(
            self: "ConceptGearSet._Cast_ConceptGearSet",
        ) -> "_2496.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2496

            return self._parent._cast(_2496.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "ConceptGearSet._Cast_ConceptGearSet",
        ) -> "_2454.AbstractAssembly":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def part(self: "ConceptGearSet._Cast_ConceptGearSet") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "ConceptGearSet._Cast_ConceptGearSet",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def concept_gear_set(
            self: "ConceptGearSet._Cast_ConceptGearSet",
        ) -> "ConceptGearSet":
            return self._parent

        def __getattr__(self: "ConceptGearSet._Cast_ConceptGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self: Self) -> "_1196.ConceptGearSetDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gear_set_design(self: Self) -> "_1196.ConceptGearSetDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gears(self: Self) -> "List[_2541.ConceptGear]":
        """List[mastapy.system_model.part_model.gears.ConceptGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes(self: Self) -> "List[_2325.ConceptGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConceptGearSet._Cast_ConceptGearSet":
        return self._Cast_ConceptGearSet(self)
