"""KlingelnbergCycloPalloidConicalGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4087
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4127,
        _4130,
        _4116,
        _4156,
        _4053,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetPowerFlow")


class KlingelnbergCycloPalloidConicalGearSetPowerFlow(_4087.ConicalGearSetPowerFlow):
    """KlingelnbergCycloPalloidConicalGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
            parent: "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4087.ConicalGearSetPowerFlow":
            return self._parent._cast(_4087.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4116.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4156.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4053.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4127.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(
                _4127.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4130.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(
                _4130.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2557.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow(self)
