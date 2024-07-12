"""PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3573,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2562
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3584,
        _3623,
        _3525,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed")


class PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed(
    _3573.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
):
    """PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
            parent: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3573.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3573.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3584.GearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3584,
            )

            return self._parent._cast(
                _3584.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3623.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(
                _3623.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3525.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3525,
            )

            return self._parent._cast(
                _3525.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2562.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed(self)
