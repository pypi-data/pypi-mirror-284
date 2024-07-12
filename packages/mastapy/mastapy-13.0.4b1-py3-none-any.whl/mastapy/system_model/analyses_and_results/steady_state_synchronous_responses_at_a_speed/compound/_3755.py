"""SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3672,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2343
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3624,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3660,
        _3688,
        _3714,
        _3720,
        _3690,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
)


class SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(
    _3672.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
):
    """SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3672.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3672.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3660.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3660,
            )

            return self._parent._cast(
                _3660.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3688.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3688,
            )

            return self._parent._cast(
                _3688.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3714.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3714,
            )

            return self._parent._cast(
                _3714.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3720,
            )

            return self._parent._cast(
                _3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3690,
            )

            return self._parent._cast(
                _3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2343.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2343.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3624.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3624.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
