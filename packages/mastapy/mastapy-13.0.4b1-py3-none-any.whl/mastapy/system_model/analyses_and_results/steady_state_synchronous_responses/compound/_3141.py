"""AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3169,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3010,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3148,
        _3151,
        _3152,
        _3153,
        _3199,
        _3236,
        _3242,
        _3245,
        _3248,
        _3249,
        _3263,
        _3195,
        _3214,
        _3162,
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse"
)


class AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse(
    _3169.ConicalGearCompoundSteadyStateSynchronousResponse
):
    """AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
            parent: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3169.ConicalGearCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3169.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(_3195.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3214.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3148.BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3148,
            )

            return self._parent._cast(
                _3148.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3152.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3153.BevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3153,
            )

            return self._parent._cast(
                _3153.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3199.HypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3199,
            )

            return self._parent._cast(
                _3199.HypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3236.SpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3236,
            )

            return self._parent._cast(
                _3236.SpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3242.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3242,
            )

            return self._parent._cast(
                _3242.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3245.StraightBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3245,
            )

            return self._parent._cast(
                _3245.StraightBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3248.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3248,
            )

            return self._parent._cast(
                _3248.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3249.StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3249,
            )

            return self._parent._cast(
                _3249.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3263.ZerolBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3263,
            )

            return self._parent._cast(
                _3263.ZerolBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3010.AGMAGleasonConicalGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AGMAGleasonConicalGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3010.AGMAGleasonConicalGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AGMAGleasonConicalGearSteadyStateSynchronousResponse]

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
    ) -> "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse(
            self
        )
