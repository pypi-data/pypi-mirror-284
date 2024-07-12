"""BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3283,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import _6846
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3279,
        _3277,
        _3271,
        _3299,
        _3325,
        _3364,
        _3266,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft"
)


class BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft(
    _3283.BevelGearSetSteadyStateSynchronousResponseOnAShaft
):
    """BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3283.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3283.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3271.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3271,
            )

            return self._parent._cast(
                _3271.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3299.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3299,
            )

            return self._parent._cast(
                _3299.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3325.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3364.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3364,
            )

            return self._parent._cast(
                _3364.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3266.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2536.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6846.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_differential_gears_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3279.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3277.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.BevelDifferentialMeshesSteadyStateSynchronousResponseOnAShaft
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
