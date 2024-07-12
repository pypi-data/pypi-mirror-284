"""ShaftHubConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3040,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ShaftHubConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2619
    from mastapy.system_model.analyses_and_results.static_loads import _6971
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3082,
        _3029,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ShaftHubConnectionSteadyStateSynchronousResponse")


class ShaftHubConnectionSteadyStateSynchronousResponse(
    _3040.ConnectorSteadyStateSynchronousResponse
):
    """ShaftHubConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_ShaftHubConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting ShaftHubConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
            parent: "ShaftHubConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connector_steady_state_synchronous_response(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
        ) -> "_3040.ConnectorSteadyStateSynchronousResponse":
            return self._parent._cast(_3040.ConnectorSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
        ) -> "_3082.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
        ) -> "_3029.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
        ) -> "ShaftHubConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ShaftHubConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2619.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6971.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[ShaftHubConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ShaftHubConnectionSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftHubConnectionSteadyStateSynchronousResponse._Cast_ShaftHubConnectionSteadyStateSynchronousResponse":
        return self._Cast_ShaftHubConnectionSteadyStateSynchronousResponse(self)
