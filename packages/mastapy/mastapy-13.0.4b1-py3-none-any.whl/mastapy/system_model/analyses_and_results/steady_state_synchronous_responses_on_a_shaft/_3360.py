"""RootAssemblySteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3273,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "RootAssemblySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2494
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3371,
        _3266,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblySteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="RootAssemblySteadyStateSynchronousResponseOnAShaft")


class RootAssemblySteadyStateSynchronousResponseOnAShaft(
    _3273.AssemblySteadyStateSynchronousResponseOnAShaft
):
    """RootAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting RootAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
            parent: "RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3273.AssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3273.AssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3266.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "RootAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "RootAssemblySteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2494.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response_on_a_shaft_inputs(
        self: Self,
    ) -> "_3371.SteadyStateSynchronousResponseOnAShaft":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SteadyStateSynchronousResponseOnAShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponseOnAShaftInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft":
        return self._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft(self)
