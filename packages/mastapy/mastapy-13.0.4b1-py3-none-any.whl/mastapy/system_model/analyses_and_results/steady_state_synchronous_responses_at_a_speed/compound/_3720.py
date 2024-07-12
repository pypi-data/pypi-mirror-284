"""InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3690,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3590,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3660,
        _3664,
        _3667,
        _3672,
        _3677,
        _3682,
        _3685,
        _3688,
        _3693,
        _3695,
        _3703,
        _3709,
        _3714,
        _3718,
        _3722,
        _3725,
        _3728,
        _3736,
        _3745,
        _3748,
        _3755,
        _3758,
        _3761,
        _3764,
        _3773,
        _3779,
        _3782,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)


Self = TypeVar(
    "Self",
    bound="InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
)


class InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
    _3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
):
    """InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3690.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3660.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3660,
            )

            return self._parent._cast(
                _3660.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3664.BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3664,
            )

            return self._parent._cast(
                _3664.BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3667.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3672.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3672,
            )

            return self._parent._cast(
                _3672.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3677.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3677,
            )

            return self._parent._cast(
                _3677.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3682.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3685.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3685,
            )

            return self._parent._cast(
                _3685.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3688.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3688,
            )

            return self._parent._cast(
                _3688.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3693.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3693,
            )

            return self._parent._cast(
                _3693.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3695.CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3695,
            )

            return self._parent._cast(
                _3695.CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3703.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3703,
            )

            return self._parent._cast(
                _3703.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3709.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3709,
            )

            return self._parent._cast(
                _3709.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3714.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3714,
            )

            return self._parent._cast(
                _3714.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3718.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3718,
            )

            return self._parent._cast(
                _3718.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3722.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3722,
            )

            return self._parent._cast(
                _3722.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3725.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3725,
            )

            return self._parent._cast(
                _3725.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3728.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3728,
            )

            return self._parent._cast(
                _3728.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3745.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3745,
            )

            return self._parent._cast(
                _3745.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3748.RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3748,
            )

            return self._parent._cast(
                _3748.RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3755.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
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
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3761.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3761,
            )

            return self._parent._cast(
                _3761.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3764.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3764,
            )

            return self._parent._cast(
                _3764.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3773.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3773,
            )

            return self._parent._cast(
                _3773.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3779.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3779,
            )

            return self._parent._cast(
                _3779.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3782.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3782,
            )

            return self._parent._cast(
                _3782.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3590.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3590.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
