"""CouplingCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3235,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CouplingCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3043,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3158,
        _3163,
        _3217,
        _3239,
        _3254,
        _3137,
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CouplingCompoundSteadyStateSynchronousResponse")


class CouplingCompoundSteadyStateSynchronousResponse(
    _3235.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
):
    """CouplingCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_CouplingCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
            parent: "CouplingCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3235.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3235.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3137.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3137,
            )

            return self._parent._cast(
                _3137.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_compound_steady_state_synchronous_response(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3158.ClutchCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3158,
            )

            return self._parent._cast(
                _3158.ClutchCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3163.ConceptCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3163,
            )

            return self._parent._cast(
                _3163.ConceptCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3217.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3217,
            )

            return self._parent._cast(
                _3217.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3239.SpringDamperCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.SpringDamperCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3254.TorqueConverterCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3254,
            )

            return self._parent._cast(
                _3254.TorqueConverterCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
        ) -> "CouplingCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CouplingCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3043.CouplingSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CouplingSteadyStateSynchronousResponse]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3043.CouplingSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CouplingSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "CouplingCompoundSteadyStateSynchronousResponse._Cast_CouplingCompoundSteadyStateSynchronousResponse":
        return self._Cast_CouplingCompoundSteadyStateSynchronousResponse(self)
