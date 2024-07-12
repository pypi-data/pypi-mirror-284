"""MountableComponentSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3550,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "MountableComponentSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3531,
        _3533,
        _3538,
        _3539,
        _3540,
        _3543,
        _3547,
        _3552,
        _3556,
        _3559,
        _3561,
        _3563,
        _3566,
        _3574,
        _3575,
        _3580,
        _3585,
        _3589,
        _3593,
        _3596,
        _3599,
        _3600,
        _3601,
        _3603,
        _3606,
        _3610,
        _3611,
        _3612,
        _3613,
        _3614,
        _3618,
        _3620,
        _3626,
        _3628,
        _3633,
        _3636,
        _3637,
        _3638,
        _3639,
        _3640,
        _3641,
        _3644,
        _3646,
        _3647,
        _3648,
        _3651,
        _3654,
        _3604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="MountableComponentSteadyStateSynchronousResponseAtASpeed")


class MountableComponentSteadyStateSynchronousResponseAtASpeed(
    _3550.ComponentSteadyStateSynchronousResponseAtASpeed
):
    """MountableComponentSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting MountableComponentSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
            parent: "MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3550.ComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3550.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(_3604.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3533.BearingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3533,
            )

            return self._parent._cast(
                _3533.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3538.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3538,
            )

            return self._parent._cast(
                _3538.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3539.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3540.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3543.BevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(
                _3543.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3547.ClutchHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.ClutchHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3552.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3556.ConceptGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3556,
            )

            return self._parent._cast(
                _3556.ConceptGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3559.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3559,
            )

            return self._parent._cast(
                _3559.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3561.ConnectorSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3563.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3563,
            )

            return self._parent._cast(
                _3563.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3566.CVTPulleySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(
                _3566.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3574.CylindricalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3574,
            )

            return self._parent._cast(
                _3574.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3575.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3580.FaceGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(
                _3580.FaceGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(_3585.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.HypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3593.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3593,
            )

            return self._parent._cast(
                _3593.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3596.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3596,
            )

            return self._parent._cast(
                _3596.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3599.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3600.MassDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(
                _3600.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3601.MeasurementComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3603.OilSealSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3603,
            )

            return self._parent._cast(
                _3603.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(
                _3606.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3610.PlanetCarrierSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3611.PointLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3611,
            )

            return self._parent._cast(
                _3611.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3612.PowerLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3613.PulleySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3614.RingPinsSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3614,
            )

            return self._parent._cast(
                _3614.RingPinsSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3618.RollingRingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3618,
            )

            return self._parent._cast(
                _3618.RollingRingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3620.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3626.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3628.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3628,
            )

            return self._parent._cast(
                _3628.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3633.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3633,
            )

            return self._parent._cast(
                _3633.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3636.StraightBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3636,
            )

            return self._parent._cast(
                _3636.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3637.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3637,
            )

            return self._parent._cast(
                _3637.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3638.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3638,
            )

            return self._parent._cast(
                _3638.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3639.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3639,
            )

            return self._parent._cast(
                _3639.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3640.SynchroniserPartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3640,
            )

            return self._parent._cast(
                _3640.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3641.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3641,
            )

            return self._parent._cast(
                _3641.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3644.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3644,
            )

            return self._parent._cast(
                _3644.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3646.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3646,
            )

            return self._parent._cast(
                _3646.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3647.UnbalancedMassSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3647,
            )

            return self._parent._cast(
                _3647.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3648.VirtualComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3648,
            )

            return self._parent._cast(
                _3648.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3651.WormGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3651,
            )

            return self._parent._cast(
                _3651.WormGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3654.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3654,
            )

            return self._parent._cast(
                _3654.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "MountableComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "MountableComponentSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

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
    ) -> "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed(self)
