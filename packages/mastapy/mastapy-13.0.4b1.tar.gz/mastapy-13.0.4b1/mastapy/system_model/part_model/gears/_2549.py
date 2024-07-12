"""FaceGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _999
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.part_model import _2496, _2454, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSet",)


Self = TypeVar("Self", bound="FaceGearSet")


class FaceGearSet(_2552.GearSet):
    """FaceGearSet

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSet")

    class _Cast_FaceGearSet:
        """Special nested class for casting FaceGearSet to subclasses."""

        def __init__(self: "FaceGearSet._Cast_FaceGearSet", parent: "FaceGearSet"):
            self._parent = parent

        @property
        def gear_set(self: "FaceGearSet._Cast_FaceGearSet") -> "_2552.GearSet":
            return self._parent._cast(_2552.GearSet)

        @property
        def specialised_assembly(
            self: "FaceGearSet._Cast_FaceGearSet",
        ) -> "_2496.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2496

            return self._parent._cast(_2496.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "FaceGearSet._Cast_FaceGearSet",
        ) -> "_2454.AbstractAssembly":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def part(self: "FaceGearSet._Cast_FaceGearSet") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "FaceGearSet._Cast_FaceGearSet",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def face_gear_set(self: "FaceGearSet._Cast_FaceGearSet") -> "FaceGearSet":
            return self._parent

        def __getattr__(self: "FaceGearSet._Cast_FaceGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self: Self) -> "_999.FaceGearSetDesign":
        """mastapy.gears.gear_designs.face.FaceGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gear_set_design(self: Self) -> "_999.FaceGearSetDesign":
        """mastapy.gears.gear_designs.face.FaceGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears(self: Self) -> "List[_2548.FaceGear]":
        """List[mastapy.system_model.part_model.gears.FaceGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes(self: Self) -> "List[_2331.FaceGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.FaceGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FaceGearSet._Cast_FaceGearSet":
        return self._Cast_FaceGearSet(self)
