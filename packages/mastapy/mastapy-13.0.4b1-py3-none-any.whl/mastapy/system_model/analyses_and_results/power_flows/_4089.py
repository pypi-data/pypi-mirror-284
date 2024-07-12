"""ConnectorPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4133
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConnectorPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2467
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4061,
        _4134,
        _4153,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorPowerFlow",)


Self = TypeVar("Self", bound="ConnectorPowerFlow")


class ConnectorPowerFlow(_4133.MountableComponentPowerFlow):
    """ConnectorPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorPowerFlow")

    class _Cast_ConnectorPowerFlow:
        """Special nested class for casting ConnectorPowerFlow to subclasses."""

        def __init__(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
            parent: "ConnectorPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_power_flow(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_4061.BearingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.BearingPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_4134.OilSealPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.OilSealPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "_4153.ShaftHubConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.ShaftHubConnectionPowerFlow)

        @property
        def connector_power_flow(
            self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow",
        ) -> "ConnectorPowerFlow":
            return self._parent

        def __getattr__(self: "ConnectorPowerFlow._Cast_ConnectorPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2467.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectorPowerFlow._Cast_ConnectorPowerFlow":
        return self._Cast_ConnectorPowerFlow(self)
