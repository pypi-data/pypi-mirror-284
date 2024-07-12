"""PulleyCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PulleyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2611
    from mastapy.system_model.analyses_and_results.power_flows import _4146
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4230,
        _4265,
        _4213,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCompoundPowerFlow",)


Self = TypeVar("Self", bound="PulleyCompoundPowerFlow")


class PulleyCompoundPowerFlow(_4227.CouplingHalfCompoundPowerFlow):
    """PulleyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyCompoundPowerFlow")

    class _Cast_PulleyCompoundPowerFlow:
        """Special nested class for casting PulleyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
            parent: "PulleyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_4227.CouplingHalfCompoundPowerFlow":
            return self._parent._cast(_4227.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_4265.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_4213.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_4230.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(_4230.CVTPulleyCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "PulleyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2611.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4146.PulleyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PulleyPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4146.PulleyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PulleyPowerFlow]

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
    def cast_to(self: Self) -> "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow":
        return self._Cast_PulleyCompoundPowerFlow(self)
