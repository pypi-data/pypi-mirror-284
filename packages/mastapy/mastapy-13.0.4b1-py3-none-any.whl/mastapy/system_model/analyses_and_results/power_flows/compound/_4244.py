"""FEPartCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4190
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "FEPartCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.power_flows import _4112
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4213,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCompoundPowerFlow",)


Self = TypeVar("Self", bound="FEPartCompoundPowerFlow")


class FEPartCompoundPowerFlow(_4190.AbstractShaftOrHousingCompoundPowerFlow):
    """FEPartCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartCompoundPowerFlow")

    class _Cast_FEPartCompoundPowerFlow:
        """Special nested class for casting FEPartCompoundPowerFlow to subclasses."""

        def __init__(
            self: "FEPartCompoundPowerFlow._Cast_FEPartCompoundPowerFlow",
            parent: "FEPartCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "FEPartCompoundPowerFlow._Cast_FEPartCompoundPowerFlow",
        ) -> "_4190.AbstractShaftOrHousingCompoundPowerFlow":
            return self._parent._cast(_4190.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "FEPartCompoundPowerFlow._Cast_FEPartCompoundPowerFlow",
        ) -> "_4213.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "FEPartCompoundPowerFlow._Cast_FEPartCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "FEPartCompoundPowerFlow._Cast_FEPartCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FEPartCompoundPowerFlow._Cast_FEPartCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCompoundPowerFlow._Cast_FEPartCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def fe_part_compound_power_flow(
            self: "FEPartCompoundPowerFlow._Cast_FEPartCompoundPowerFlow",
        ) -> "FEPartCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "FEPartCompoundPowerFlow._Cast_FEPartCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2473.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4112.FEPartPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.FEPartPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4112.FEPartPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.FEPartPowerFlow]

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
    def cast_to(self: Self) -> "FEPartCompoundPowerFlow._Cast_FEPartCompoundPowerFlow":
        return self._Cast_FEPartCompoundPowerFlow(self)
