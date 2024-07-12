"""ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3304,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.static_loads import _6861
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3343,
        _3291,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft"
)


class ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft(
    _3304.CouplingHalfSteadyStateSynchronousResponseOnAShaft
):
    """ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
            parent: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3304.CouplingHalfSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3304.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3343.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3291.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft(
            self
        )
