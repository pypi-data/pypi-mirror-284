"""TorqueConverterPumpPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4091
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "TorqueConverterPumpPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2629
    from mastapy.system_model.analyses_and_results.static_loads import _6996
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4133,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpPowerFlow",)


Self = TypeVar("Self", bound="TorqueConverterPumpPowerFlow")


class TorqueConverterPumpPowerFlow(_4091.CouplingHalfPowerFlow):
    """TorqueConverterPumpPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterPumpPowerFlow")

    class _Cast_TorqueConverterPumpPowerFlow:
        """Special nested class for casting TorqueConverterPumpPowerFlow to subclasses."""

        def __init__(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
            parent: "TorqueConverterPumpPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_4091.CouplingHalfPowerFlow":
            return self._parent._cast(_4091.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_pump_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "TorqueConverterPumpPowerFlow":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterPumpPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2629.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6996.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

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
    ) -> "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow":
        return self._Cast_TorqueConverterPumpPowerFlow(self)
