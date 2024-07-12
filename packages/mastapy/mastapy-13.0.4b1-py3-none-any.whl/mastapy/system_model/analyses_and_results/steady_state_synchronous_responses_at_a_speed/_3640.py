"""SynchroniserPartSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3563,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2626
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3639,
        _3641,
        _3602,
        _3550,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="SynchroniserPartSteadyStateSynchronousResponseAtASpeed")


class SynchroniserPartSteadyStateSynchronousResponseAtASpeed(
    _3563.CouplingHalfSteadyStateSynchronousResponseAtASpeed
):
    """SynchroniserPartSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SynchroniserPartSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
            parent: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3563.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3563.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3602.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3550.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3639.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3639,
            )

            return self._parent._cast(
                _3639.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3641.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3641,
            )

            return self._parent._cast(
                _3641.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "SynchroniserPartSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed.TYPE",
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
    ) -> "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed(self)
