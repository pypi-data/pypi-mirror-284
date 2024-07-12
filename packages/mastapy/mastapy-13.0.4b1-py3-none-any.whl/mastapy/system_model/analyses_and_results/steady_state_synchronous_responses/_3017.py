"""BevelDifferentialGearSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3022,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "BevelDifferentialGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.static_loads import _6844
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3018,
        _3019,
        _3010,
        _3038,
        _3065,
        _3082,
        _3029,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BevelDifferentialGearSteadyStateSynchronousResponse")


class BevelDifferentialGearSteadyStateSynchronousResponse(
    _3022.BevelGearSteadyStateSynchronousResponse
):
    """BevelDifferentialGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSteadyStateSynchronousResponse"
    )

    class _Cast_BevelDifferentialGearSteadyStateSynchronousResponse:
        """Special nested class for casting BevelDifferentialGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
            parent: "BevelDifferentialGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_3022.BevelGearSteadyStateSynchronousResponse":
            return self._parent._cast(_3022.BevelGearSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_3010.AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(
                _3010.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_3038.ConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3038,
            )

            return self._parent._cast(_3038.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_3065.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_3082.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_3029.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_3018.BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "_3019.BevelDifferentialSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(
                _3019.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
        ) -> "BevelDifferentialGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelDifferentialGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2535.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6844.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSteadyStateSynchronousResponse":
        return self._Cast_BevelDifferentialGearSteadyStateSynchronousResponse(self)
