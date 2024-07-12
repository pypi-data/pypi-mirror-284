"""AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3688,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3529,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3667,
        _3672,
        _3718,
        _3755,
        _3761,
        _3764,
        _3782,
        _3714,
        _3720,
        _3690,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
)


class AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(
    _3688.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
):
    """AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3688.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3688.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3714.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3714,
            )

            return self._parent._cast(
                _3714.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3720,
            )

            return self._parent._cast(
                _3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3690,
            )

            return self._parent._cast(
                _3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3667.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3672.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3672,
            )

            return self._parent._cast(
                _3672.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3718.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3718,
            )

            return self._parent._cast(
                _3718.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3755.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3761.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3761,
            )

            return self._parent._cast(
                _3761.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3764.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3764,
            )

            return self._parent._cast(
                _3764.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3782.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3782,
            )

            return self._parent._cast(
                _3782.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3529.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3529.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
