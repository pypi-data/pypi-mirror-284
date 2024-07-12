"""ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3282,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2351
    from mastapy.system_model.analyses_and_results.static_loads import _7008
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
__all__ = ("ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft")


class ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3282.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
):
    """ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3282.BevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3282.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3270.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3298.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3298,
            )

            return self._parent._cast(
                _3298.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.GearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3301.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2351.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_7008.ZerolBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase

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
    ) -> "ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft(self)
