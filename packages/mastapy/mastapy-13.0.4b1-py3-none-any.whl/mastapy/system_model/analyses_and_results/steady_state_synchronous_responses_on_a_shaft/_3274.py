"""BearingSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3302,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "BearingSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.static_loads import _6841
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3343,
        _3291,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BearingSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="BearingSteadyStateSynchronousResponseOnAShaft")


class BearingSteadyStateSynchronousResponseOnAShaft(
    _3302.ConnectorSteadyStateSynchronousResponseOnAShaft
):
    """BearingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEARING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BearingSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_BearingSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BearingSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
            parent: "BearingSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def connector_steady_state_synchronous_response_on_a_shaft(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3302.ConnectorSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3302.ConnectorSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3343.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3291.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
        ) -> "BearingSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BearingSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.Bearing":
        """mastapy.system_model.part_model.Bearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6841.BearingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[BearingSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BearingSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BearingSteadyStateSynchronousResponseOnAShaft._Cast_BearingSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BearingSteadyStateSynchronousResponseOnAShaft(self)
