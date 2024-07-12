"""StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3282,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2347
    from mastapy.system_model.analyses_and_results.static_loads import _6985
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3270,
        _3298,
        _3324,
        _3331,
        _3301,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft"
)


class StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3282.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
):
    """StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3282.BevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3282.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3270.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3298.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3298,
            )

            return self._parent._cast(
                _3298.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.GearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3301.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2347.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6985.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

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
    ) -> "StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft(
            self
        )
