"""ShaftToMountableComponentConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3007,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2315
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3028,
        _3048,
        _3088,
        _3039,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionSteadyStateSynchronousResponse"
)


class ShaftToMountableComponentConnectionSteadyStateSynchronousResponse(
    _3007.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
):
    """ShaftToMountableComponentConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
    )

    class _Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting ShaftToMountableComponentConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
            parent: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3007.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3007.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3039.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(_3039.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3028.CoaxialConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3028,
            )

            return self._parent._cast(
                _3028.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> (
            "_3048.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(
                _3048.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "_3088.PlanetaryConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3088,
            )

            return self._parent._cast(
                _3088.PlanetaryConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2315.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

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
    ) -> "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
        return self._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse(
            self
        )
