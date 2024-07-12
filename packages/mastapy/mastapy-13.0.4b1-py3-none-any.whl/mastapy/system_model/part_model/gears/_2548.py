"""FaceGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGear")

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.gears.gear_designs.face import _993
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("FaceGear",)


Self = TypeVar("Self", bound="FaceGear")


class FaceGear(_2550.Gear):
    """FaceGear

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGear")

    class _Cast_FaceGear:
        """Special nested class for casting FaceGear to subclasses."""

        def __init__(self: "FaceGear._Cast_FaceGear", parent: "FaceGear"):
            self._parent = parent

        @property
        def gear(self: "FaceGear._Cast_FaceGear") -> "_2550.Gear":
            return self._parent._cast(_2550.Gear)

        @property
        def mountable_component(
            self: "FaceGear._Cast_FaceGear",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(self: "FaceGear._Cast_FaceGear") -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(self: "FaceGear._Cast_FaceGear") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(self: "FaceGear._Cast_FaceGear") -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def face_gear(self: "FaceGear._Cast_FaceGear") -> "FaceGear":
            return self._parent

        def __getattr__(self: "FaceGear._Cast_FaceGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orientation(self: Self) -> "_2551.GearOrientations":
        """mastapy.system_model.part_model.gears.GearOrientations"""
        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.gears._2551", "GearOrientations"
        )(value)

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: Self, value: "_2551.GearOrientations"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations"
        )
        self.wrapped.Orientation = value

    @property
    def active_gear_design(self: Self) -> "_993.FaceGearDesign":
        """mastapy.gears.gear_designs.face.FaceGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gear_design(self: Self) -> "_993.FaceGearDesign":
        """mastapy.gears.gear_designs.face.FaceGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FaceGear._Cast_FaceGear":
        return self._Cast_FaceGear(self)
