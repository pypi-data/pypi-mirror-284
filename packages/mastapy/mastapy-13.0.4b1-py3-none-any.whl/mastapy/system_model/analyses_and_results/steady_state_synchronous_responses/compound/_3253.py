"""SynchroniserSleeveCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3252,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2627
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3123,
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
__all__ = ("SynchroniserSleeveCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundSteadyStateSynchronousResponse")


class SynchroniserSleeveCompoundSteadyStateSynchronousResponse(
    _3252.SynchroniserPartCompoundSteadyStateSynchronousResponse
):
    """SynchroniserSleeveCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting SynchroniserSleeveCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
            parent: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
        ) -> "_3252.SynchroniserPartCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3252.SynchroniserPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
        ) -> "_3176.CouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3176,
            )

            return self._parent._cast(
                _3176.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
        ) -> "_3214.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
        ) -> "SynchroniserSleeveCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SynchroniserSleeveCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2627.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3123.SynchroniserSleeveSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SynchroniserSleeveSteadyStateSynchronousResponse]

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
    ) -> "List[_3123.SynchroniserSleeveSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SynchroniserSleeveSteadyStateSynchronousResponse]

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
    ) -> "SynchroniserSleeveCompoundSteadyStateSynchronousResponse._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse":
        return self._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponse(self)
