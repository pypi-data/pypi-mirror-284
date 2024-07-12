"""HypoidGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2533
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _989
    from mastapy.system_model.part_model.gears import _2543, _2550
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGear",)


Self = TypeVar("Self", bound="HypoidGear")


class HypoidGear(_2533.AGMAGleasonConicalGear):
    """HypoidGear

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGear")

    class _Cast_HypoidGear:
        """Special nested class for casting HypoidGear to subclasses."""

        def __init__(self: "HypoidGear._Cast_HypoidGear", parent: "HypoidGear"):
            self._parent = parent

        @property
        def agma_gleason_conical_gear(
            self: "HypoidGear._Cast_HypoidGear",
        ) -> "_2533.AGMAGleasonConicalGear":
            return self._parent._cast(_2533.AGMAGleasonConicalGear)

        @property
        def conical_gear(self: "HypoidGear._Cast_HypoidGear") -> "_2543.ConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.ConicalGear)

        @property
        def gear(self: "HypoidGear._Cast_HypoidGear") -> "_2550.Gear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.Gear)

        @property
        def mountable_component(
            self: "HypoidGear._Cast_HypoidGear",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(self: "HypoidGear._Cast_HypoidGear") -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(self: "HypoidGear._Cast_HypoidGear") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(self: "HypoidGear._Cast_HypoidGear") -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def hypoid_gear(self: "HypoidGear._Cast_HypoidGear") -> "HypoidGear":
            return self._parent

        def __getattr__(self: "HypoidGear._Cast_HypoidGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(self: Self) -> "_989.HypoidGearDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_design(self: Self) -> "_989.HypoidGearDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGear._Cast_HypoidGear":
        return self._Cast_HypoidGear(self)
