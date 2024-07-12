"""HypoidGearMeshSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3529,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2335
    from mastapy.system_model.analyses_and_results.static_loads import _6928
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3557,
        _3583,
        _3590,
        _3560,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="HypoidGearMeshSteadyStateSynchronousResponseAtASpeed")


class HypoidGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3529.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
):
    """HypoidGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting HypoidGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3529.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3557.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3557,
            )

            return self._parent._cast(
                _3557.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.GearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3590.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3590,
            )

            return self._parent._cast(
                _3590.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3560.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2335.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6928.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

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
    ) -> "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_HypoidGearMeshSteadyStateSynchronousResponseAtASpeed(self)
