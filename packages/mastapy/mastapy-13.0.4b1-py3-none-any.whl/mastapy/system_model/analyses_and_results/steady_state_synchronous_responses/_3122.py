"""SynchroniserPartSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3042,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SynchroniserPartSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2626
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3121,
        _3123,
        _3082,
        _3029,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SynchroniserPartSteadyStateSynchronousResponse")


class SynchroniserPartSteadyStateSynchronousResponse(
    _3042.CouplingHalfSteadyStateSynchronousResponse
):
    """SynchroniserPartSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartSteadyStateSynchronousResponse"
    )

    class _Cast_SynchroniserPartSteadyStateSynchronousResponse:
        """Special nested class for casting SynchroniserPartSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
            parent: "SynchroniserPartSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_3042.CouplingHalfSteadyStateSynchronousResponse":
            return self._parent._cast(_3042.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_3082.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_3029.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_3121.SynchroniserHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3121,
            )

            return self._parent._cast(
                _3121.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "_3123.SynchroniserSleeveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3123,
            )

            return self._parent._cast(
                _3123.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
        ) -> "SynchroniserPartSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SynchroniserPartSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2626.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartSteadyStateSynchronousResponse._Cast_SynchroniserPartSteadyStateSynchronousResponse":
        return self._Cast_SynchroniserPartSteadyStateSynchronousResponse(self)
