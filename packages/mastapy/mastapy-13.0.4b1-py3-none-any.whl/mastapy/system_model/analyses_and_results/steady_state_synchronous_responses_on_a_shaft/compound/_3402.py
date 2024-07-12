"""AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3430,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3271,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3409,
        _3414,
        _3460,
        _3497,
        _3503,
        _3506,
        _3524,
        _3456,
        _3494,
        _3396,
        _3475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)


class AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
    _3430.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
):
    """AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3430.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3430.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3456.GearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3494.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3494,
            )

            return self._parent._cast(
                _3494.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3396.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3396,
            )

            return self._parent._cast(
                _3396.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3409.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3409,
            )

            return self._parent._cast(
                _3409.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3414.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3414,
            )

            return self._parent._cast(
                _3414.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3460.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3497.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3503.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3503,
            )

            return self._parent._cast(
                _3503.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3506.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3506,
            )

            return self._parent._cast(
                _3506.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3524.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3524,
            )

            return self._parent._cast(
                _3524.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3271.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3271.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
