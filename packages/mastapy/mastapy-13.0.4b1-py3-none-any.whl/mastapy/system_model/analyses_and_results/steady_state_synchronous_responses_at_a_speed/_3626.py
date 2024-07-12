"""SpiralBevelGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3543,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2563
    from mastapy.system_model.analyses_and_results.static_loads import _6975
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3531,
        _3559,
        _3585,
        _3602,
        _3550,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="SpiralBevelGearSteadyStateSynchronousResponseAtASpeed")


class SpiralBevelGearSteadyStateSynchronousResponseAtASpeed(
    _3543.BevelGearSteadyStateSynchronousResponseAtASpeed
):
    """SpiralBevelGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SpiralBevelGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
            parent: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3543.BevelGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3543.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3559.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3559,
            )

            return self._parent._cast(
                _3559.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(_3585.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3602.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3550.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2563.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6975.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

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
    ) -> "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_SpiralBevelGearSteadyStateSynchronousResponseAtASpeed(self)
