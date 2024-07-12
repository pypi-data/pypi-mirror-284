"""StraightBevelDiffGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2540
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _971
    from mastapy.system_model.part_model.gears import _2565, _2534, _2544, _2552
    from mastapy.system_model.connections_and_sockets.gears import _2345
    from mastapy.system_model.part_model import _2496, _2454, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSet",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSet")


class StraightBevelDiffGearSet(_2540.BevelGearSet):
    """StraightBevelDiffGearSet

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearSet")

    class _Cast_StraightBevelDiffGearSet:
        """Special nested class for casting StraightBevelDiffGearSet to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
            parent: "StraightBevelDiffGearSet",
        ):
            self._parent = parent

        @property
        def bevel_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2540.BevelGearSet":
            return self._parent._cast(_2540.BevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2534.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2544.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.ConicalGearSet)

        @property
        def gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2552.GearSet":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.GearSet)

        @property
        def specialised_assembly(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2496.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2496

            return self._parent._cast(_2496.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2454.AbstractAssembly":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def part(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def straight_bevel_diff_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "StraightBevelDiffGearSet":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_971.StraightBevelDiffGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gear_set_design(
        self: Self,
    ) -> "_971.StraightBevelDiffGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears(self: Self) -> "List[_2565.StraightBevelDiffGear]":
        """List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes(
        self: Self,
    ) -> "List[_2345.StraightBevelDiffGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet":
        return self._Cast_StraightBevelDiffGearSet(self)
