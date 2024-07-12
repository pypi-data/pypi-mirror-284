"""PlanetaryGearSetSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3052,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "PlanetaryGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2562
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3064,
        _3103,
        _3004,
        _3084,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="PlanetaryGearSetSteadyStateSynchronousResponse")


class PlanetaryGearSetSteadyStateSynchronousResponse(
    _3052.CylindricalGearSetSteadyStateSynchronousResponse
):
    """PlanetaryGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetSteadyStateSynchronousResponse"
    )

    class _Cast_PlanetaryGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting PlanetaryGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
            parent: "PlanetaryGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "_3052.CylindricalGearSetSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3052.CylindricalGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "_3064.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(_3064.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "_3103.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(
                _3103.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "_3004.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(
                _3004.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
        ) -> "PlanetaryGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PlanetaryGearSetSteadyStateSynchronousResponse.TYPE",
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
    ) -> "PlanetaryGearSetSteadyStateSynchronousResponse._Cast_PlanetaryGearSetSteadyStateSynchronousResponse":
        return self._Cast_PlanetaryGearSetSteadyStateSynchronousResponse(self)
