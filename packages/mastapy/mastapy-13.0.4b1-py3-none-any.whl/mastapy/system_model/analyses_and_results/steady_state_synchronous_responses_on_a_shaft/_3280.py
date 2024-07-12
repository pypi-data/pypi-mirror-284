"""BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3279,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3284,
        _3272,
        _3300,
        _3326,
        _3343,
        _3291,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft"
)


class BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft(
    _3279.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
):
    """BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
            parent: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3279.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3279.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3284.BevelGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3284,
            )

            return self._parent._cast(
                _3284.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3272.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3300.ConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3300,
            )

            return self._parent._cast(
                _3300.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3326.GearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(_3326.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3343.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3291.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2537.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

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
    ) -> "BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft(
            self
        )
