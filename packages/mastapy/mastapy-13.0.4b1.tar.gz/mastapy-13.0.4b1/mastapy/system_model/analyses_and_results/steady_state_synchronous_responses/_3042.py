"""CouplingHalfSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3082,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CouplingHalfSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3026,
        _3031,
        _3045,
        _3086,
        _3093,
        _3098,
        _3108,
        _3121,
        _3122,
        _3123,
        _3126,
        _3128,
        _3029,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CouplingHalfSteadyStateSynchronousResponse")


class CouplingHalfSteadyStateSynchronousResponse(
    _3082.MountableComponentSteadyStateSynchronousResponse
):
    """CouplingHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfSteadyStateSynchronousResponse"
    )

    class _Cast_CouplingHalfSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingHalfSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
            parent: "CouplingHalfSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3082.MountableComponentSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3082.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3029.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3026.ClutchHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3031.ConceptCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(
                _3031.ConceptCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3045.CVTPulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.CVTPulleySteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3086.PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(
                _3086.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def pulley_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3093.PulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(_3093.PulleySteadyStateSynchronousResponse)

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3098.RollingRingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3098,
            )

            return self._parent._cast(_3098.RollingRingSteadyStateSynchronousResponse)

        @property
        def spring_damper_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3108.SpringDamperHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3108,
            )

            return self._parent._cast(
                _3108.SpringDamperHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3121.SynchroniserHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3121,
            )

            return self._parent._cast(
                _3121.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3122.SynchroniserPartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3122,
            )

            return self._parent._cast(
                _3122.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3123.SynchroniserSleeveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3123,
            )

            return self._parent._cast(
                _3123.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3126.TorqueConverterPumpSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3126,
            )

            return self._parent._cast(
                _3126.TorqueConverterPumpSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3128.TorqueConverterTurbineSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3128,
            )

            return self._parent._cast(
                _3128.TorqueConverterTurbineSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "CouplingHalfSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CouplingHalfSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse":
        return self._Cast_CouplingHalfSteadyStateSynchronousResponse(self)
