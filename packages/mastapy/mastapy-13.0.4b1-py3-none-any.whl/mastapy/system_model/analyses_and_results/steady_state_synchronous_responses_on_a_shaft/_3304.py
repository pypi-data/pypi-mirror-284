"""CouplingHalfSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3343,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CouplingHalfSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3288,
        _3293,
        _3307,
        _3347,
        _3354,
        _3359,
        _3369,
        _3380,
        _3381,
        _3382,
        _3385,
        _3387,
        _3291,
        _3345,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CouplingHalfSteadyStateSynchronousResponseOnAShaft")


class CouplingHalfSteadyStateSynchronousResponseOnAShaft(
    _3343.MountableComponentSteadyStateSynchronousResponseOnAShaft
):
    """CouplingHalfSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CouplingHalfSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
            parent: "CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3343.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3343.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3291.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(_3345.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3288.ClutchHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.ClutchHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3293.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(
                _3293.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3307.CVTPulleySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(
                _3307.CVTPulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(
                _3347.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3354.PulleySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3354,
            )

            return self._parent._cast(
                _3354.PulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3359.RollingRingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3359,
            )

            return self._parent._cast(
                _3359.RollingRingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3369.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3369,
            )

            return self._parent._cast(
                _3369.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3380.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3380,
            )

            return self._parent._cast(
                _3380.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3381.SynchroniserPartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3381,
            )

            return self._parent._cast(
                _3381.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3382.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3382,
            )

            return self._parent._cast(
                _3382.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3385.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3385,
            )

            return self._parent._cast(
                _3385.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3387.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3387,
            )

            return self._parent._cast(
                _3387.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "CouplingHalfSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CouplingHalfSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft(self)
