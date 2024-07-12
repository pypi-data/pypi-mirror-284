"""ConceptCouplingHalfSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3042,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConceptCouplingHalfSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.static_loads import _6861
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3082,
        _3029,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConceptCouplingHalfSteadyStateSynchronousResponse")


class ConceptCouplingHalfSteadyStateSynchronousResponse(
    _3042.CouplingHalfSteadyStateSynchronousResponse
):
    """ConceptCouplingHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfSteadyStateSynchronousResponse"
    )

    class _Cast_ConceptCouplingHalfSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptCouplingHalfSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
            parent: "ConceptCouplingHalfSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3042.CouplingHalfSteadyStateSynchronousResponse":
            return self._parent._cast(_3042.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3082.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3029.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "ConceptCouplingHalfSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConceptCouplingHalfSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2602.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6861.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse":
        return self._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse(self)
