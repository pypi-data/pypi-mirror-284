"""CVTPulleyCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3225,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CVTPulleyCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3045,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3176,
        _3214,
        _3162,
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CVTPulleyCompoundSteadyStateSynchronousResponse")


class CVTPulleyCompoundSteadyStateSynchronousResponse(
    _3225.PulleyCompoundSteadyStateSynchronousResponse
):
    """CVTPulleyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_CVTPulleyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CVTPulleyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
            parent: "CVTPulleyCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def pulley_compound_steady_state_synchronous_response(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_3225.PulleyCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3225.PulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_3176.CouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3176,
            )

            return self._parent._cast(
                _3176.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_3214.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
        ) -> "CVTPulleyCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CVTPulleyCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3045.CVTPulleySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CVTPulleySteadyStateSynchronousResponse]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3045.CVTPulleySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CVTPulleySteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "CVTPulleyCompoundSteadyStateSynchronousResponse._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse":
        return self._Cast_CVTPulleyCompoundSteadyStateSynchronousResponse(self)
