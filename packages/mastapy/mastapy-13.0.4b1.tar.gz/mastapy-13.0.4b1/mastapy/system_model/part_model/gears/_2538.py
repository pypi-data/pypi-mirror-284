"""BevelDifferentialSunGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialSunGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539, _2533, _2543, _2550
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGear",)


Self = TypeVar("Self", bound="BevelDifferentialSunGear")


class BevelDifferentialSunGear(_2535.BevelDifferentialGear):
    """BevelDifferentialSunGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialSunGear")

    class _Cast_BevelDifferentialSunGear:
        """Special nested class for casting BevelDifferentialSunGear to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
            parent: "BevelDifferentialSunGear",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2535.BevelDifferentialGear":
            return self._parent._cast(_2535.BevelDifferentialGear)

        @property
        def bevel_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2539.BevelGear":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2533.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2543.ConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.ConicalGear)

        @property
        def gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2550.Gear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.Gear)

        @property
        def mountable_component(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def bevel_differential_sun_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "BevelDifferentialSunGear":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialSunGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear":
        return self._Cast_BevelDifferentialSunGear(self)
