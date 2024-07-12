"""RootAssemblySteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3011,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "RootAssemblySteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2494
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3110,
        _3004,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblySteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="RootAssemblySteadyStateSynchronousResponse")


class RootAssemblySteadyStateSynchronousResponse(
    _3011.AssemblySteadyStateSynchronousResponse
):
    """RootAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblySteadyStateSynchronousResponse"
    )

    class _Cast_RootAssemblySteadyStateSynchronousResponse:
        """Special nested class for casting RootAssemblySteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
            parent: "RootAssemblySteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def assembly_steady_state_synchronous_response(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
        ) -> "_3011.AssemblySteadyStateSynchronousResponse":
            return self._parent._cast(_3011.AssemblySteadyStateSynchronousResponse)

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
        ) -> "_3004.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(
                _3004.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def root_assembly_steady_state_synchronous_response(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
        ) -> "RootAssemblySteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "RootAssemblySteadyStateSynchronousResponse.TYPE"
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
    def steady_state_synchronous_response_inputs(
        self: Self,
    ) -> "_3110.SteadyStateSynchronousResponse":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SteadyStateSynchronousResponse

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponseInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblySteadyStateSynchronousResponse._Cast_RootAssemblySteadyStateSynchronousResponse":
        return self._Cast_RootAssemblySteadyStateSynchronousResponse(self)
