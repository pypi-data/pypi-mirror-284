"""ShaftToMountableComponentConnectionCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4191
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ShaftToMountableComponentConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4155
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4212,
        _4232,
        _4271,
        _4223,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionCompoundPowerFlow")


class ShaftToMountableComponentConnectionCompoundPowerFlow(
    _4191.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
):
    """ShaftToMountableComponentConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionCompoundPowerFlow"
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundPowerFlow:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
            parent: "ShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_4191.AbstractShaftToMountableComponentConnectionCompoundPowerFlow":
            return self._parent._cast(
                _4191.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_4223.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_4212.CoaxialConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CoaxialConnectionCompoundPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_4232.CycloidalDiscCentralBearingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.CycloidalDiscCentralBearingConnectionCompoundPowerFlow
            )

        @property
        def planetary_connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_4271.PlanetaryConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.PlanetaryConnectionCompoundPowerFlow)

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "ShaftToMountableComponentConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4155.ShaftToMountableComponentConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ShaftToMountableComponentConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4155.ShaftToMountableComponentConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ShaftToMountableComponentConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow":
        return self._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow(self)
