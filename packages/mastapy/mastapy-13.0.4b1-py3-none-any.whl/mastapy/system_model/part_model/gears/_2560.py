"""KlingelnbergCycloPalloidSpiralBevelGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGear",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977
    from mastapy.system_model.part_model.gears import _2543, _2550
    from mastapy.system_model.part_model import _2484, _2464, _2488
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGear",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGear")


class KlingelnbergCycloPalloidSpiralBevelGear(
    _2556.KlingelnbergCycloPalloidConicalGear
):
    """KlingelnbergCycloPalloidSpiralBevelGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGear"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGear:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGear to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
            parent: "KlingelnbergCycloPalloidSpiralBevelGear",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2556.KlingelnbergCycloPalloidConicalGear":
            return self._parent._cast(_2556.KlingelnbergCycloPalloidConicalGear)

        @property
        def conical_gear(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2543.ConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.ConicalGear)

        @property
        def gear(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2550.Gear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.Gear)

        @property
        def mountable_component(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def component(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def part(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGear":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGear.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(
        self: Self,
    ) -> "_977.KlingelnbergCycloPalloidSpiralBevelGearDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
        self: Self,
    ) -> "_977.KlingelnbergCycloPalloidSpiralBevelGearDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGear(self)
