"""VirtualComponentSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3343,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "VirtualComponentSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3341,
        _3342,
        _3352,
        _3353,
        _3388,
        _3291,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="VirtualComponentSteadyStateSynchronousResponseOnAShaft")


class VirtualComponentSteadyStateSynchronousResponseOnAShaft(
    _3343.MountableComponentSteadyStateSynchronousResponseOnAShaft
):
    """VirtualComponentSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting VirtualComponentSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
            parent: "VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3343.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3343.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3291.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_steady_state_synchronous_response_on_a_shaft(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3341.MassDiscSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.MassDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_steady_state_synchronous_response_on_a_shaft(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3342.MeasurementComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3342,
            )

            return self._parent._cast(
                _3342.MeasurementComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_steady_state_synchronous_response_on_a_shaft(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3352.PointLoadSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.PointLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_steady_state_synchronous_response_on_a_shaft(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3353.PowerLoadSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3353,
            )

            return self._parent._cast(
                _3353.PowerLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_on_a_shaft(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3388.UnbalancedMassSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3388,
            )

            return self._parent._cast(
                _3388.UnbalancedMassSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "VirtualComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "VirtualComponentSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "VirtualComponentSteadyStateSynchronousResponseOnAShaft._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_VirtualComponentSteadyStateSynchronousResponseOnAShaft(self)
