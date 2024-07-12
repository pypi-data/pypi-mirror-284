"""MountableComponentCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3162,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "MountableComponentCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3082,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3141,
        _3145,
        _3148,
        _3151,
        _3152,
        _3153,
        _3160,
        _3165,
        _3166,
        _3169,
        _3173,
        _3176,
        _3179,
        _3184,
        _3187,
        _3190,
        _3195,
        _3199,
        _3203,
        _3206,
        _3209,
        _3212,
        _3213,
        _3215,
        _3219,
        _3222,
        _3223,
        _3224,
        _3225,
        _3226,
        _3229,
        _3233,
        _3236,
        _3241,
        _3242,
        _3245,
        _3248,
        _3249,
        _3251,
        _3252,
        _3253,
        _3256,
        _3257,
        _3258,
        _3259,
        _3260,
        _3263,
        _3216,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="MountableComponentCompoundSteadyStateSynchronousResponse")


class MountableComponentCompoundSteadyStateSynchronousResponse(
    _3162.ComponentCompoundSteadyStateSynchronousResponse
):
    """MountableComponentCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_MountableComponentCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting MountableComponentCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
            parent: "MountableComponentCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.ComponentCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3162.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(_3216.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3141.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bearing_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3145.BearingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3145,
            )

            return self._parent._cast(
                _3145.BearingCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3148.BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3148,
            )

            return self._parent._cast(
                _3148.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3152.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3153.BevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3153,
            )

            return self._parent._cast(
                _3153.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3160.ClutchHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3160,
            )

            return self._parent._cast(
                _3160.ClutchHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3165.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3165,
            )

            return self._parent._cast(
                _3165.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3166.ConceptGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3166,
            )

            return self._parent._cast(
                _3166.ConceptGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3169.ConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3169,
            )

            return self._parent._cast(
                _3169.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def connector_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3173.ConnectorCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.ConnectorCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3176.CouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3176,
            )

            return self._parent._cast(
                _3176.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3179.CVTPulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3179,
            )

            return self._parent._cast(
                _3179.CVTPulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3184.CylindricalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.CylindricalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3187.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3187,
            )

            return self._parent._cast(
                _3187.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3190.FaceGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.FaceGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(_3195.GearCompoundSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3199.HypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3199,
            )

            return self._parent._cast(
                _3199.HypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(
                _3203.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3206.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3206,
            )

            return self._parent._cast(
                _3206.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3209.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3209,
            )

            return self._parent._cast(
                _3209.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3212.MassDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.MassDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3213.MeasurementComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3213,
            )

            return self._parent._cast(
                _3213.MeasurementComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3215.OilSealCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3215,
            )

            return self._parent._cast(
                _3215.OilSealCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3219.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3219,
            )

            return self._parent._cast(
                _3219.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3222.PlanetCarrierCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.PlanetCarrierCompoundSteadyStateSynchronousResponse
            )

        @property
        def point_load_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3223.PointLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.PointLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def power_load_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3224.PowerLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3224,
            )

            return self._parent._cast(
                _3224.PowerLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def pulley_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3225.PulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.PulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3226.RingPinsCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3226,
            )

            return self._parent._cast(
                _3226.RingPinsCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3229.RollingRingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3229,
            )

            return self._parent._cast(
                _3229.RollingRingCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3233.ShaftHubConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3233,
            )

            return self._parent._cast(
                _3233.ShaftHubConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3236.SpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3236,
            )

            return self._parent._cast(
                _3236.SpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3241.SpringDamperHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.SpringDamperHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3242.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3242,
            )

            return self._parent._cast(
                _3242.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3245.StraightBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3245,
            )

            return self._parent._cast(
                _3245.StraightBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3248.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3248,
            )

            return self._parent._cast(
                _3248.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3249.StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3249,
            )

            return self._parent._cast(
                _3249.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3251.SynchroniserHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3251,
            )

            return self._parent._cast(
                _3251.SynchroniserHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3252.SynchroniserPartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3252,
            )

            return self._parent._cast(
                _3252.SynchroniserPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3253.SynchroniserSleeveCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3253,
            )

            return self._parent._cast(
                _3253.SynchroniserSleeveCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3256.TorqueConverterPumpCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3256,
            )

            return self._parent._cast(
                _3256.TorqueConverterPumpCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3257.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3257,
            )

            return self._parent._cast(
                _3257.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3258.UnbalancedMassCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3258,
            )

            return self._parent._cast(
                _3258.UnbalancedMassCompoundSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3259.VirtualComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3259,
            )

            return self._parent._cast(
                _3259.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3260.WormGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3260,
            )

            return self._parent._cast(
                _3260.WormGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3263.ZerolBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3263,
            )

            return self._parent._cast(
                _3263.ZerolBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
        ) -> "MountableComponentCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "MountableComponentCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3082.MountableComponentSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.MountableComponentSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3082.MountableComponentSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.MountableComponentSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentCompoundSteadyStateSynchronousResponse._Cast_MountableComponentCompoundSteadyStateSynchronousResponse":
        return self._Cast_MountableComponentCompoundSteadyStateSynchronousResponse(self)
