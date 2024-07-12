"""VirtualComponentSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3602,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "VirtualComponentSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3600,
        _3601,
        _3611,
        _3612,
        _3647,
        _3550,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="VirtualComponentSteadyStateSynchronousResponseAtASpeed")


class VirtualComponentSteadyStateSynchronousResponseAtASpeed(
    _3602.MountableComponentSteadyStateSynchronousResponseAtASpeed
):
    """VirtualComponentSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting VirtualComponentSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
            parent: "VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3602.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3602.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3550.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3600.MassDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(
                _3600.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3601.MeasurementComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3611.PointLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3611,
            )

            return self._parent._cast(
                _3611.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3612.PowerLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3647.UnbalancedMassSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3647,
            )

            return self._parent._cast(
                _3647.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "VirtualComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "VirtualComponentSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2499.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_VirtualComponentSteadyStateSynchronousResponseAtASpeed(self)
