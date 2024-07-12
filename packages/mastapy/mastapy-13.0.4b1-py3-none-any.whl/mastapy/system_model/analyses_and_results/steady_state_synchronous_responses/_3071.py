"""KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3036,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2338
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3074,
        _3077,
        _3063,
        _3070,
        _3039,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
)


class KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse(
    _3036.ConicalGearMeshSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3036.ConicalGearMeshSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3036.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3063.GearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(_3063.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3070.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3070,
            )

            return self._parent._cast(
                _3070.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3039.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(_3039.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> (
            "_3074.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(
                _3074.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "_3077.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3077,
            )

            return self._parent._cast(
                _3077.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2338.KlingelnbergCycloPalloidConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse(
            self
        )
