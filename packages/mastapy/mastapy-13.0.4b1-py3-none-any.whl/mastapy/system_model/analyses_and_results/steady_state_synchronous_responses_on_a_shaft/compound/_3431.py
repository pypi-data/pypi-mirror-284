"""ConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3301,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3399,
        _3401,
        _3405,
        _3408,
        _3413,
        _3418,
        _3420,
        _3423,
        _3426,
        _3429,
        _3434,
        _3436,
        _3440,
        _3442,
        _3444,
        _3450,
        _3455,
        _3459,
        _3461,
        _3463,
        _3466,
        _3469,
        _3477,
        _3479,
        _3486,
        _3489,
        _3493,
        _3496,
        _3499,
        _3502,
        _3505,
        _3514,
        _3520,
        _3523,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ConnectionCompoundSteadyStateSynchronousResponseOnAShaft")


class ConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _7560.ConnectionCompoundAnalysis
):
    """ConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7560.ConnectionCompoundAnalysis":
            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3399.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3399,
            )

            return self._parent._cast(
                _3399.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3401.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3401,
            )

            return self._parent._cast(
                _3401.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3405.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3405,
            )

            return self._parent._cast(
                _3405.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3413.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3418.ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3418,
            )

            return self._parent._cast(
                _3418.ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3420.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3420,
            )

            return self._parent._cast(
                _3420.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3423.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3423,
            )

            return self._parent._cast(
                _3423.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3426.ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3426,
            )

            return self._parent._cast(
                _3426.ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3429.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3429,
            )

            return self._parent._cast(
                _3429.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3434.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3434,
            )

            return self._parent._cast(
                _3434.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3436.CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3436,
            )

            return self._parent._cast(
                _3436.CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3440.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3440,
            )

            return self._parent._cast(
                _3440.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3442.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3442,
            )

            return self._parent._cast(
                _3442.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3444.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3444,
            )

            return self._parent._cast(
                _3444.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3450.FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3450,
            )

            return self._parent._cast(
                _3450.FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3455.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3459.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3459,
            )

            return self._parent._cast(
                _3459.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3461.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3461,
            )

            return self._parent._cast(
                _3461.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3463.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3463,
            )

            return self._parent._cast(
                _3463.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3466.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3466,
            )

            return self._parent._cast(
                _3466.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3469.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3469,
            )

            return self._parent._cast(
                _3469.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3479.PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3479,
            )

            return self._parent._cast(
                _3479.PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3486.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3486,
            )

            return self._parent._cast(
                _3486.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3493.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3493,
            )

            return self._parent._cast(
                _3493.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3496.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3496,
            )

            return self._parent._cast(
                _3496.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3502.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3514.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3514,
            )

            return self._parent._cast(
                _3514.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3520.WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3520,
            )

            return self._parent._cast(
                _3520.WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3523.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3523,
            )

            return self._parent._cast(
                _3523.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3301.ConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3301.ConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConnectionCompoundSteadyStateSynchronousResponseOnAShaft(self)
