"""ShaftPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4055
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ShaftPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2502
    from mastapy.system_model.analyses_and_results.static_loads import _6972
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4054,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftPowerFlow",)


Self = TypeVar("Self", bound="ShaftPowerFlow")


class ShaftPowerFlow(_4055.AbstractShaftPowerFlow):
    """ShaftPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftPowerFlow")

    class _Cast_ShaftPowerFlow:
        """Special nested class for casting ShaftPowerFlow to subclasses."""

        def __init__(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow", parent: "ShaftPowerFlow"
        ):
            self._parent = parent

        @property
        def abstract_shaft_power_flow(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "_4055.AbstractShaftPowerFlow":
            return self._parent._cast(_4055.AbstractShaftPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "_4054.AbstractShaftOrHousingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.AbstractShaftOrHousingPowerFlow)

        @property
        def component_power_flow(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def shaft_power_flow(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "ShaftPowerFlow":
            return self._parent

        def __getattr__(self: "ShaftPowerFlow._Cast_ShaftPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pin_tangential_oscillation_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinTangentialOscillationFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2502.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6972.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ShaftPowerFlow._Cast_ShaftPowerFlow":
        return self._Cast_ShaftPowerFlow(self)
