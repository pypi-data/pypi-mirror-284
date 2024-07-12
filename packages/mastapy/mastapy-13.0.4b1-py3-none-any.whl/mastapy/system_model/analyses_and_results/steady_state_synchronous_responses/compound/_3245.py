"""StraightBevelGearCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3153,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "StraightBevelGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2567
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3118,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3141,
        _3169,
        _3195,
        _3214,
        _3162,
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="StraightBevelGearCompoundSteadyStateSynchronousResponse")


class StraightBevelGearCompoundSteadyStateSynchronousResponse(
    _3153.BevelGearCompoundSteadyStateSynchronousResponse
):
    """StraightBevelGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
            parent: "StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3153.BevelGearCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3153.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3141.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3169.ConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3169,
            )

            return self._parent._cast(
                _3169.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(_3195.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3214.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "StraightBevelGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

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
    ) -> "List[_3118.StraightBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3118.StraightBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelGearSteadyStateSynchronousResponse]

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
    ) -> "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse(self)
