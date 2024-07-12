"""AGMAGleasonConicalGearSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3038,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AGMAGleasonConicalGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3017,
        _3018,
        _3019,
        _3022,
        _3069,
        _3106,
        _3115,
        _3118,
        _3119,
        _3120,
        _3136,
        _3065,
        _3082,
        _3029,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSteadyStateSynchronousResponse")


class AGMAGleasonConicalGearSteadyStateSynchronousResponse(
    _3038.ConicalGearSteadyStateSynchronousResponse
):
    """AGMAGleasonConicalGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse"
    )

    class _Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse:
        """Special nested class for casting AGMAGleasonConicalGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
            parent: "AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3038.ConicalGearSteadyStateSynchronousResponse":
            return self._parent._cast(_3038.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3065.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3082.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3029.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3017.BevelDifferentialGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3017,
            )

            return self._parent._cast(
                _3017.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3018.BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3019.BevelDifferentialSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(
                _3019.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3022.BevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3022,
            )

            return self._parent._cast(_3022.BevelGearSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3069.HypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(_3069.HypoidGearSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3106.SpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3115.StraightBevelDiffGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3115,
            )

            return self._parent._cast(
                _3115.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3118.StraightBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3118,
            )

            return self._parent._cast(
                _3118.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3119.StraightBevelPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3119,
            )

            return self._parent._cast(
                _3119.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3120.StraightBevelSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3120,
            )

            return self._parent._cast(
                _3120.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "_3136.ZerolBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3136,
            )

            return self._parent._cast(
                _3136.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AGMAGleasonConicalGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse":
        return self._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse(self)
