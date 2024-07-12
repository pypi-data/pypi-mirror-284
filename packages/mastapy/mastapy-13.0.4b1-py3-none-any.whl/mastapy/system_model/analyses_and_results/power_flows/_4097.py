"""CycloidalDiscCentralBearingConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4077
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CycloidalDiscCentralBearingConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2355
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4155,
        _4056,
        _4088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionPowerFlow",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionPowerFlow")


class CycloidalDiscCentralBearingConnectionPowerFlow(_4077.CoaxialConnectionPowerFlow):
    """CycloidalDiscCentralBearingConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCentralBearingConnectionPowerFlow"
    )

    class _Cast_CycloidalDiscCentralBearingConnectionPowerFlow:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionPowerFlow to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
            parent: "CycloidalDiscCentralBearingConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def coaxial_connection_power_flow(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
        ) -> "_4077.CoaxialConnectionPowerFlow":
            return self._parent._cast(_4077.CoaxialConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
        ) -> "_4155.ShaftToMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(
                _4155.ShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
        ) -> "_4056.AbstractShaftToMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4056

            return self._parent._cast(
                _4056.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def connection_power_flow(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
        ) -> "_4088.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
        ) -> "CycloidalDiscCentralBearingConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2355.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow":
        return self._Cast_CycloidalDiscCentralBearingConnectionPowerFlow(self)
