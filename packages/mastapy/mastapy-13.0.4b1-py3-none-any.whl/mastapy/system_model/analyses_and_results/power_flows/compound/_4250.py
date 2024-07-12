"""HypoidGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4192
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "HypoidGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.power_flows import _4119
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4220,
        _4246,
        _4265,
        _4213,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="HypoidGearCompoundPowerFlow")


class HypoidGearCompoundPowerFlow(_4192.AGMAGleasonConicalGearCompoundPowerFlow):
    """HypoidGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearCompoundPowerFlow")

    class _Cast_HypoidGearCompoundPowerFlow:
        """Special nested class for casting HypoidGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
            parent: "HypoidGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
        ) -> "_4192.AGMAGleasonConicalGearCompoundPowerFlow":
            return self._parent._cast(_4192.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
        ) -> "_4220.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
        ) -> "_4246.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
        ) -> "_4265.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
        ) -> "_4213.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def hypoid_gear_compound_power_flow(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
        ) -> "HypoidGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4119.HypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_4119.HypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearCompoundPowerFlow._Cast_HypoidGearCompoundPowerFlow":
        return self._Cast_HypoidGearCompoundPowerFlow(self)
