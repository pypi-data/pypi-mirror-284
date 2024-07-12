"""KlingelnbergCycloPalloidHypoidGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4123
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidHypoidGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2558
    from mastapy.gears.rating.klingelnberg_hypoid import _412
    from mastapy.system_model.analyses_and_results.static_loads import _6937
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4086,
        _4115,
        _4133,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearPowerFlow")


class KlingelnbergCycloPalloidHypoidGearPowerFlow(
    _4123.KlingelnbergCycloPalloidConicalGearPowerFlow
):
    """KlingelnbergCycloPalloidHypoidGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
            parent: "KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_4123.KlingelnbergCycloPalloidConicalGearPowerFlow":
            return self._parent._cast(
                _4123.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def conical_gear_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_4086.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_4115.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
        ) -> "KlingelnbergCycloPalloidHypoidGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2558.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_412.KlingelnbergCycloPalloidHypoidGearRating":
        """mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6937.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearPowerFlow(self)
