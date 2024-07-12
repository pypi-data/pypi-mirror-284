"""KlingelnbergCycloPalloidConicalGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4086
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidConicalGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4126,
        _4129,
        _4115,
        _4133,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearPowerFlow")


class KlingelnbergCycloPalloidConicalGearPowerFlow(_4086.ConicalGearPowerFlow):
    """KlingelnbergCycloPalloidConicalGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
            parent: "KlingelnbergCycloPalloidConicalGearPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4086.ConicalGearPowerFlow":
            return self._parent._cast(_4086.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4115.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4126.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(_4126.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4129.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(
                _4129.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "KlingelnbergCycloPalloidConicalGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearPowerFlow.TYPE",
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
    ) -> "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow(self)
