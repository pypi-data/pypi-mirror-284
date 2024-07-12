"""CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3720,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3562,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3677,
        _3682,
        _3736,
        _3758,
        _3773,
        _3690,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
)


class CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
    _3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
):
    """CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3720.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3690,
            )

            return self._parent._cast(
                _3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3677.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3677,
            )

            return self._parent._cast(
                _3677.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3682.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3758.SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3758,
            )

            return self._parent._cast(
                _3758.SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3773.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3773,
            )

            return self._parent._cast(
                _3773.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3562.CouplingConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CouplingConnectionSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3562.CouplingConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CouplingConnectionSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
