"""AGMAGleasonConicalGearSetSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3037,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3016,
        _3021,
        _3068,
        _3105,
        _3114,
        _3117,
        _3135,
        _3064,
        _3103,
        _3004,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetSteadyStateSynchronousResponse")


class AGMAGleasonConicalGearSetSteadyStateSynchronousResponse(
    _3037.ConicalGearSetSteadyStateSynchronousResponse
):
    """AGMAGleasonConicalGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
    )

    class _Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting AGMAGleasonConicalGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
            parent: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3037.ConicalGearSetSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3037.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3064.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(_3064.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3103.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(
                _3103.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3004.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(
                _3004.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3016.BevelDifferentialGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(
                _3016.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3021.BevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(_3021.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3068.HypoidGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3068,
            )

            return self._parent._cast(_3068.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3105.SpiralBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3114.StraightBevelDiffGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3114,
            )

            return self._parent._cast(
                _3114.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3117.StraightBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3117,
            )

            return self._parent._cast(
                _3117.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "_3135.ZerolBevelGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3135,
            )

            return self._parent._cast(
                _3135.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
        ) -> "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2534.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

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
    ) -> "AGMAGleasonConicalGearSetSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse":
        return self._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponse(self)
