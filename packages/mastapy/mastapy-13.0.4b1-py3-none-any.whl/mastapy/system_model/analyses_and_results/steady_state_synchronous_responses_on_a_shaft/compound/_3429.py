"""ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3455,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3298,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3401,
        _3408,
        _3413,
        _3459,
        _3463,
        _3466,
        _3469,
        _3496,
        _3502,
        _3505,
        _3523,
        _3461,
        _3431,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
)


class ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
    _3455.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
):
    """ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3455.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3455.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3461.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3461,
            )

            return self._parent._cast(
                _3461.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3431.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3431,
            )

            return self._parent._cast(
                _3431.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3401.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3401,
            )

            return self._parent._cast(
                _3401.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3413.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3459.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3459,
            )

            return self._parent._cast(
                _3459.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3463.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3463,
            )

            return self._parent._cast(
                _3463.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3466.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3466,
            )

            return self._parent._cast(
                _3466.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3469.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3469,
            )

            return self._parent._cast(
                _3469.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3496.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3496,
            )

            return self._parent._cast(
                _3496.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3502.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3505.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3505,
            )

            return self._parent._cast(
                _3505.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3523.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3523,
            )

            return self._parent._cast(
                _3523.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3298.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3298.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
