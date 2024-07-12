"""AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3291,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2456
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3268,
        _3312,
        _3322,
        _3362,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft"
)


class AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft(
    _3291.ComponentSteadyStateSynchronousResponseOnAShaft
):
    """AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
            parent: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3291.ComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3291.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.AbstractShaftSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.AbstractShaftSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3312.CycloidalDiscSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.CycloidalDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3322.FEPartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.FEPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3362.ShaftSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(_3362.ShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
        ) -> "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2456.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft(
            self
        )
