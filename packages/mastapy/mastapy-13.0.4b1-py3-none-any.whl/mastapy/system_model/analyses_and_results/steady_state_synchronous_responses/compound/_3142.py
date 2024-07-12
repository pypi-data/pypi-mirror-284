"""AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3170,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3008,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3149,
        _3154,
        _3200,
        _3237,
        _3243,
        _3246,
        _3264,
        _3196,
        _3202,
        _3172,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse"
)


class AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse(
    _3170.ConicalGearMeshCompoundSteadyStateSynchronousResponse
):
    """AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3170.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3170.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3196.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3196,
            )

            return self._parent._cast(
                _3196.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3202.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3149.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3154.BevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3154,
            )

            return self._parent._cast(
                _3154.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3200.HypoidGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3200,
            )

            return self._parent._cast(
                _3200.HypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3237.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3237,
            )

            return self._parent._cast(
                _3237.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3243.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3243,
            )

            return self._parent._cast(
                _3243.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3246.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3246,
            )

            return self._parent._cast(
                _3246.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3264.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3264,
            )

            return self._parent._cast(
                _3264.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3008.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]

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
    ) -> "List[_3008.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
        return (
            self._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse(
                self
            )
        )
