"""KlingelnbergCycloPalloidConicalGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6866
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6937,
        _6940,
        _6912,
        _6946,
        _6859,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearLoadCase")


class KlingelnbergCycloPalloidConicalGearLoadCase(_6866.ConicalGearLoadCase):
    """KlingelnbergCycloPalloidConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
            parent: "KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6866.ConicalGearLoadCase":
            return self._parent._cast(_6866.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6912.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6946.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6859.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ComponentLoadCase)

        @property
        def part_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6937.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "_6940.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(
                _6940.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "KlingelnbergCycloPalloidConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidConicalGearLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2556.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase":
        return self._Cast_KlingelnbergCycloPalloidConicalGearLoadCase(self)
