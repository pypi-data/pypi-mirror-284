"""PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3176,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3086,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3214,
        _3162,
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse"
)


class PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse(
    _3176.CouplingHalfCompoundSteadyStateSynchronousResponse
):
    """PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
            parent: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3176.CouplingHalfCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3176.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3214.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

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
    ) -> "List[_3086.PartToPartShearCouplingHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PartToPartShearCouplingHalfSteadyStateSynchronousResponse]

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
    ) -> "List[_3086.PartToPartShearCouplingHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PartToPartShearCouplingHalfSteadyStateSynchronousResponse]

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
    ) -> "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
        return self._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse(
            self
        )
