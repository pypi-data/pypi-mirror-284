"""ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3140,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3102,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3161,
        _3181,
        _3220,
        _3172,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)


class ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
    _3140.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
):
    """ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
            parent: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3140.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3140.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3161.CoaxialConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3161,
            )

            return self._parent._cast(
                _3161.CoaxialConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3181.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3220.PlanetaryConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.PlanetaryConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> (
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse"
        ):
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> (
        "List[_3102.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]

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
    ) -> (
        "List[_3102.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]

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
    ) -> "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
            self
        )
