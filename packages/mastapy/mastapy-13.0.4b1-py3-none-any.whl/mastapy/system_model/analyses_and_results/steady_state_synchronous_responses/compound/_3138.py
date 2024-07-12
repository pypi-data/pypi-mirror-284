"""AbstractShaftCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3139,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AbstractShaftCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3006,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3182,
        _3232,
        _3162,
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AbstractShaftCompoundSteadyStateSynchronousResponse")


class AbstractShaftCompoundSteadyStateSynchronousResponse(
    _3139.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
):
    """AbstractShaftCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_AbstractShaftCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
            parent: "AbstractShaftCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
        ) -> "_3139.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3139.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
        ) -> "_3182.CycloidalDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3182,
            )

            return self._parent._cast(
                _3182.CycloidalDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_compound_steady_state_synchronous_response(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
        ) -> "_3232.ShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3232,
            )

            return self._parent._cast(_3232.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
        ) -> "AbstractShaftCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AbstractShaftCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3006.AbstractShaftSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractShaftSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3006.AbstractShaftSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractShaftSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse":
        return self._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse(self)
