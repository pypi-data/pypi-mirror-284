"""CycloidalDiscPlanetaryBearingConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4056
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CycloidalDiscPlanetaryBearingConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2358
    from mastapy.system_model.analyses_and_results.static_loads import _6882
    from mastapy.system_model.analyses_and_results.power_flows import _4088
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionPowerFlow",)


Self = TypeVar("Self", bound="CycloidalDiscPlanetaryBearingConnectionPowerFlow")


class CycloidalDiscPlanetaryBearingConnectionPowerFlow(
    _4056.AbstractShaftToMountableComponentConnectionPowerFlow
):
    """CycloidalDiscPlanetaryBearingConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow"
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionPowerFlow to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow",
            parent: "CycloidalDiscPlanetaryBearingConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow",
        ) -> "_4056.AbstractShaftToMountableComponentConnectionPowerFlow":
            return self._parent._cast(
                _4056.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def connection_power_flow(
            self: "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow",
        ) -> "_4088.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_power_flow(
            self: "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow",
        ) -> "CycloidalDiscPlanetaryBearingConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2358.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6882.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscPlanetaryBearingConnectionPowerFlow._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionPowerFlow(self)
