"""CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3161,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3048,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3234,
        _3140,
        _3172,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
)


class CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse(
    _3161.CoaxialConnectionCompoundSteadyStateSynchronousResponse
):
    """CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
            parent: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3161.CoaxialConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3161.CoaxialConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3234.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3234,
            )

            return self._parent._cast(
                _3234.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3140.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3140,
            )

            return self._parent._cast(
                _3140.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3048.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3048.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse(
            self
        )
