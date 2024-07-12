"""StraightBevelGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.bevel import _1198
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevel", "StraightBevelGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.agma_gleason_conical import _1211
    from mastapy.gears.gear_designs.conical import _1172
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearDesign",)


Self = TypeVar("Self", bound="StraightBevelGearDesign")


class StraightBevelGearDesign(_1198.BevelGearDesign):
    """StraightBevelGearDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearDesign")

    class _Cast_StraightBevelGearDesign:
        """Special nested class for casting StraightBevelGearDesign to subclasses."""

        def __init__(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
            parent: "StraightBevelGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "_1198.BevelGearDesign":
            return self._parent._cast(_1198.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "_1211.AGMAGleasonConicalGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1211

            return self._parent._cast(_1211.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "_1172.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1172

            return self._parent._cast(_1172.ConicalGearDesign)

        @property
        def gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def straight_bevel_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "StraightBevelGearDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "StraightBevelGearDesign._Cast_StraightBevelGearDesign":
        return self._Cast_StraightBevelGearDesign(self)
