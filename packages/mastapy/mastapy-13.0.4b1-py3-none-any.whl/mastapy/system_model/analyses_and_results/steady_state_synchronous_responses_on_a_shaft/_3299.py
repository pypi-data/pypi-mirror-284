"""ConicalGearSetSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3325,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3271,
        _3278,
        _3283,
        _3329,
        _3333,
        _3336,
        _3339,
        _3366,
        _3373,
        _3376,
        _3394,
        _3364,
        _3266,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ConicalGearSetSteadyStateSynchronousResponseOnAShaft")


class ConicalGearSetSteadyStateSynchronousResponseOnAShaft(
    _3325.GearSetSteadyStateSynchronousResponseOnAShaft
):
    """ConicalGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConicalGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3325.GearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3325.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3364.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3364,
            )

            return self._parent._cast(
                _3364.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3266.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3271.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3271,
            )

            return self._parent._cast(
                _3271.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3283.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3283,
            )

            return self._parent._cast(
                _3283.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3329.HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3329,
            )

            return self._parent._cast(
                _3329.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3333.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3333,
            )

            return self._parent._cast(
                _3333.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3336.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3336,
            )

            return self._parent._cast(
                _3336.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3339.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3339,
            )

            return self._parent._cast(
                _3339.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3366.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3373.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3373,
            )

            return self._parent._cast(
                _3373.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3376.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3376,
            )

            return self._parent._cast(
                _3376.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3394.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3394,
            )

            return self._parent._cast(
                _3394.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft(self)
