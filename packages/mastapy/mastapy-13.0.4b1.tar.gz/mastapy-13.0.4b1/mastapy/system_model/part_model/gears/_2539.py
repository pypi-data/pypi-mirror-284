"""BevelGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2533
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1198
    from mastapy.system_model.part_model.gears import (
        _2535,
        _2537,
        _2538,
        _2563,
        _2565,
        _2567,
        _2569,
        _2570,
        _2573,
        _2543,
        _2550,
    )
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("BevelGear",)


Self = TypeVar("Self", bound="BevelGear")


class BevelGear(_2533.AGMAGleasonConicalGear):
    """BevelGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGear")

    class _Cast_BevelGear:
        """Special nested class for casting BevelGear to subclasses."""

        def __init__(self: "BevelGear._Cast_BevelGear", parent: "BevelGear"):
            self._parent = parent

        @property
        def agma_gleason_conical_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2533.AGMAGleasonConicalGear":
            return self._parent._cast(_2533.AGMAGleasonConicalGear)

        @property
        def conical_gear(self: "BevelGear._Cast_BevelGear") -> "_2543.ConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.ConicalGear)

        @property
        def gear(self: "BevelGear._Cast_BevelGear") -> "_2550.Gear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.Gear)

        @property
        def mountable_component(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(self: "BevelGear._Cast_BevelGear") -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(self: "BevelGear._Cast_BevelGear") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(self: "BevelGear._Cast_BevelGear") -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def bevel_differential_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2535.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2537.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2538.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.BevelDifferentialSunGear)

        @property
        def spiral_bevel_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2563.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2563

            return self._parent._cast(_2563.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2565.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2565

            return self._parent._cast(_2565.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2567.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2567

            return self._parent._cast(_2567.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2569.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2569

            return self._parent._cast(_2569.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2570.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2570

            return self._parent._cast(_2570.StraightBevelSunGear)

        @property
        def zerol_bevel_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2573.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2573

            return self._parent._cast(_2573.ZerolBevelGear)

        @property
        def bevel_gear(self: "BevelGear._Cast_BevelGear") -> "BevelGear":
            return self._parent

        def __getattr__(self: "BevelGear._Cast_BevelGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(self: Self) -> "_1198.BevelGearDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_design(self: Self) -> "_1198.BevelGearDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGear._Cast_BevelGear":
        return self._Cast_BevelGear(self)
