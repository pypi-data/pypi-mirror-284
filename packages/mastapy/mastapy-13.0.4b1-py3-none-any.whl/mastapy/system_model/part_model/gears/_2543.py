"""ConicalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2551,
        _2533,
        _2535,
        _2537,
        _2538,
        _2539,
        _2554,
        _2556,
        _2558,
        _2560,
        _2563,
        _2565,
        _2567,
        _2569,
        _2570,
        _2573,
    )
    from mastapy.gears.gear_designs.conical import _1172
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGear",)


Self = TypeVar("Self", bound="ConicalGear")


class ConicalGear(_2550.Gear):
    """ConicalGear

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGear")

    class _Cast_ConicalGear:
        """Special nested class for casting ConicalGear to subclasses."""

        def __init__(self: "ConicalGear._Cast_ConicalGear", parent: "ConicalGear"):
            self._parent = parent

        @property
        def gear(self: "ConicalGear._Cast_ConicalGear") -> "_2550.Gear":
            return self._parent._cast(_2550.Gear)

        @property
        def mountable_component(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(self: "ConicalGear._Cast_ConicalGear") -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(self: "ConicalGear._Cast_ConicalGear") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def agma_gleason_conical_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2533.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2535.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2537.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2538.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "ConicalGear._Cast_ConicalGear") -> "_2539.BevelGear":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.BevelGear)

        @property
        def hypoid_gear(self: "ConicalGear._Cast_ConicalGear") -> "_2554.HypoidGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2556.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2558.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2560.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2563.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2563

            return self._parent._cast(_2563.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2565.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2565

            return self._parent._cast(_2565.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2567.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2567

            return self._parent._cast(_2567.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2569.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2569

            return self._parent._cast(_2569.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2570.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2570

            return self._parent._cast(_2570.StraightBevelSunGear)

        @property
        def zerol_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2573.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2573

            return self._parent._cast(_2573.ZerolBevelGear)

        @property
        def conical_gear(self: "ConicalGear._Cast_ConicalGear") -> "ConicalGear":
            return self._parent

        def __getattr__(self: "ConicalGear._Cast_ConicalGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

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
    def active_gear_design(self: Self) -> "_1172.ConicalGearDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_design(self: Self) -> "_1172.ConicalGearDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGear._Cast_ConicalGear":
        return self._Cast_ConicalGear(self)
