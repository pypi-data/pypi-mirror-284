"""BeltDriveSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3623,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "BeltDriveSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6843
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3567,
        _3525,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="BeltDriveSteadyStateSynchronousResponseAtASpeed")


class BeltDriveSteadyStateSynchronousResponseAtASpeed(
    _3623.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
):
    """BeltDriveSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BeltDriveSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
            parent: "BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3623.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3623.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3525.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3525,
            )

            return self._parent._cast(
                _3525.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3567.CVTSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(_3567.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
        ) -> "BeltDriveSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BeltDriveSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2596.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6843.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BeltDriveSteadyStateSynchronousResponseAtASpeed(self)
