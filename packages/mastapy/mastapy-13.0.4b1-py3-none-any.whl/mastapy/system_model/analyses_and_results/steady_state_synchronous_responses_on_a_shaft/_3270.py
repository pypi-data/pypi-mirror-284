"""AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3298,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3277,
        _3282,
        _3328,
        _3365,
        _3372,
        _3375,
        _3393,
        _3324,
        _3331,
        _3301,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft"
)


class AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3298.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
):
    """AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3298.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3298.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.GearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3301.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3277.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3277,
            )

            return self._parent._cast(
                _3277.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3282.BevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3282,
            )

            return self._parent._cast(
                _3282.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3328.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3328,
            )

            return self._parent._cast(
                _3328.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3365.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3365,
            )

            return self._parent._cast(
                _3365.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3372.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3372,
            )

            return self._parent._cast(
                _3372.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3375.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3375,
            )

            return self._parent._cast(
                _3375.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3393.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3393,
            )

            return self._parent._cast(
                _3393.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
