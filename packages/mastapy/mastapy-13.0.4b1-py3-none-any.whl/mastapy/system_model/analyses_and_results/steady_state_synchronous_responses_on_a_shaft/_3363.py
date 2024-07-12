"""ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3269,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2315
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3290,
        _3310,
        _3349,
        _3301,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
)


class ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft(
    _3269.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
):
    """ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3269.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3269.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3301.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3290.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3290,
            )

            return self._parent._cast(
                _3290.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3310.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3310,
            )

            return self._parent._cast(
                _3310.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3349.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft"
        ):
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft(
            self
        )
