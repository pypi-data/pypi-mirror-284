"""InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3431,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3331,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3401,
        _3405,
        _3408,
        _3413,
        _3418,
        _3423,
        _3426,
        _3429,
        _3434,
        _3436,
        _3444,
        _3450,
        _3455,
        _3459,
        _3463,
        _3466,
        _3469,
        _3477,
        _3486,
        _3489,
        _3496,
        _3499,
        _3502,
        _3505,
        _3514,
        _3520,
        _3523,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)


class InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3431.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3431.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3431.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3401.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3401,
            )

            return self._parent._cast(
                _3401.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3405.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3405,
            )

            return self._parent._cast(
                _3405.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3413.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3418.ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3418,
            )

            return self._parent._cast(
                _3418.ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3423.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3423,
            )

            return self._parent._cast(
                _3423.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3426.ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3426,
            )

            return self._parent._cast(
                _3426.ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3429.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3429,
            )

            return self._parent._cast(
                _3429.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3434.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3434,
            )

            return self._parent._cast(
                _3434.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3436.CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3436,
            )

            return self._parent._cast(
                _3436.CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3444.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3444,
            )

            return self._parent._cast(
                _3444.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3450.FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3450,
            )

            return self._parent._cast(
                _3450.FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3455.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3459.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3459,
            )

            return self._parent._cast(
                _3459.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3463.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3463,
            )

            return self._parent._cast(
                _3463.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3466.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3466,
            )

            return self._parent._cast(
                _3466.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3469.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3469,
            )

            return self._parent._cast(
                _3469.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3486.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3486,
            )

            return self._parent._cast(
                _3486.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3489.RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3489,
            )

            return self._parent._cast(
                _3489.RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3496.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3496,
            )

            return self._parent._cast(
                _3496.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3499.SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3499,
            )

            return self._parent._cast(
                _3499.SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3502.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3505.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3505,
            )

            return self._parent._cast(
                _3505.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3514.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3514,
            )

            return self._parent._cast(
                _3514.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3520.WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3520,
            )

            return self._parent._cast(
                _3520.WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3523.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3523,
            )

            return self._parent._cast(
                _3523.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3331.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
