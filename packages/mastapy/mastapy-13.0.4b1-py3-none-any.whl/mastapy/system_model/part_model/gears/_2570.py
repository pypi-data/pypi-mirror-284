"""StraightBevelSunGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelSunGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539, _2533, _2543, _2550
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGear",)


Self = TypeVar("Self", bound="StraightBevelSunGear")


class StraightBevelSunGear(_2565.StraightBevelDiffGear):
    """StraightBevelSunGear

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGear")

    class _Cast_StraightBevelSunGear:
        """Special nested class for casting StraightBevelSunGear to subclasses."""

        def __init__(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
            parent: "StraightBevelSunGear",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2565.StraightBevelDiffGear":
            return self._parent._cast(_2565.StraightBevelDiffGear)

        @property
        def bevel_gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2539.BevelGear":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2533.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2543.ConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.ConicalGear)

        @property
        def gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2550.Gear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.Gear)

        @property
        def mountable_component(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def straight_bevel_sun_gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "StraightBevelSunGear":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelSunGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "StraightBevelSunGear._Cast_StraightBevelSunGear":
        return self._Cast_StraightBevelSunGear(self)
