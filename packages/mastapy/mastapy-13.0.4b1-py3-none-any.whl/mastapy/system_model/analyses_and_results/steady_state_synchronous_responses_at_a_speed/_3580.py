"""FaceGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3585,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "FaceGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import _6906
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3602,
        _3550,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="FaceGearSteadyStateSynchronousResponseAtASpeed")


class FaceGearSteadyStateSynchronousResponseAtASpeed(
    _3585.GearSteadyStateSynchronousResponseAtASpeed
):
    """FaceGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_FaceGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting FaceGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
            parent: "FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.GearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(_3585.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3602.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3550.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "FaceGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "FaceGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2548.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6906.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

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
    ) -> "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed(self)
