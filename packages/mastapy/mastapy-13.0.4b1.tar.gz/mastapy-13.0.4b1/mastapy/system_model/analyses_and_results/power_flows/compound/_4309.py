"""UnbalancedMassCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4310
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "UnbalancedMassCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2497
    from mastapy.system_model.analyses_and_results.power_flows import _4180
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4265,
        _4213,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundPowerFlow",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundPowerFlow")


class UnbalancedMassCompoundPowerFlow(_4310.VirtualComponentCompoundPowerFlow):
    """UnbalancedMassCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassCompoundPowerFlow")

    class _Cast_UnbalancedMassCompoundPowerFlow:
        """Special nested class for casting UnbalancedMassCompoundPowerFlow to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow",
            parent: "UnbalancedMassCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_power_flow(
            self: "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow",
        ) -> "_4310.VirtualComponentCompoundPowerFlow":
            return self._parent._cast(_4310.VirtualComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow",
        ) -> "_4265.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow",
        ) -> "_4213.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow",
        ) -> "UnbalancedMassCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnbalancedMassCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2497.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4180.UnbalancedMassPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.UnbalancedMassPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4180.UnbalancedMassPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.UnbalancedMassPowerFlow]

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
    ) -> "UnbalancedMassCompoundPowerFlow._Cast_UnbalancedMassCompoundPowerFlow":
        return self._Cast_UnbalancedMassCompoundPowerFlow(self)
