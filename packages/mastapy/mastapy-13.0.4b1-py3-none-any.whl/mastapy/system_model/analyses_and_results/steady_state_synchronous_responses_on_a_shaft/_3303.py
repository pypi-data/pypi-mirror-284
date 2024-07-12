"""CouplingConnectionSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3331,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2366
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3287,
        _3292,
        _3346,
        _3368,
        _3384,
        _3301,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CouplingConnectionSteadyStateSynchronousResponseOnAShaft")


class CouplingConnectionSteadyStateSynchronousResponseOnAShaft(
    _3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
):
    """CouplingConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CouplingConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3301.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3287.ClutchConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(
                _3287.ClutchConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3292.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3292,
            )

            return self._parent._cast(
                _3292.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3346.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3346,
            )

            return self._parent._cast(
                _3346.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3368.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3368,
            )

            return self._parent._cast(
                _3368.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3384.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3384,
            )

            return self._parent._cast(
                _3384.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "CouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CouplingConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2366.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CouplingConnectionSteadyStateSynchronousResponseOnAShaft(self)
