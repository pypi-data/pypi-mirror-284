"""PlanetaryGearSetCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3186,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3089,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3197,
        _3235,
        _3137,
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundSteadyStateSynchronousResponse")


class PlanetaryGearSetCompoundSteadyStateSynchronousResponse(
    _3186.CylindricalGearSetCompoundSteadyStateSynchronousResponse
):
    """PlanetaryGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PlanetaryGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
            parent: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3186.CylindricalGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3186.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.GearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(
                _3197.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3235.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3235,
            )

            return self._parent._cast(
                _3235.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3137.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3137,
            )

            return self._parent._cast(
                _3137.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3089.PlanetaryGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PlanetaryGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3089.PlanetaryGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PlanetaryGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
        return self._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse(self)
