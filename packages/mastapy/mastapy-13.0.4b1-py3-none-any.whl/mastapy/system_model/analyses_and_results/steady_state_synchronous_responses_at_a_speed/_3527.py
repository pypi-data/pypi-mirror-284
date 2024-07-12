"""AbstractShaftSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3526,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "AbstractShaftSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3571,
        _3621,
        _3550,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="AbstractShaftSteadyStateSynchronousResponseAtASpeed")


class AbstractShaftSteadyStateSynchronousResponseAtASpeed(
    _3526.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
):
    """AbstractShaftSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractShaftSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
            parent: "AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3526.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3526.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3550.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3571.CycloidalDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3621.ShaftSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3621,
            )

            return self._parent._cast(_3621.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "AbstractShaftSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AbstractShaftSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_AbstractShaftSteadyStateSynchronousResponseAtASpeed(self)
