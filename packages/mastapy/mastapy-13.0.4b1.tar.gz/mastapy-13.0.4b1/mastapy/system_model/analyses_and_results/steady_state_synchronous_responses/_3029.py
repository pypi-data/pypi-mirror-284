"""ComponentSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3084,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ComponentSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3005,
        _3006,
        _3010,
        _3012,
        _3017,
        _3018,
        _3019,
        _3022,
        _3024,
        _3026,
        _3031,
        _3035,
        _3038,
        _3040,
        _3042,
        _3045,
        _3050,
        _3053,
        _3054,
        _3055,
        _3057,
        _3060,
        _3061,
        _3065,
        _3066,
        _3069,
        _3073,
        _3076,
        _3079,
        _3080,
        _3081,
        _3082,
        _3083,
        _3086,
        _3090,
        _3091,
        _3092,
        _3093,
        _3094,
        _3098,
        _3100,
        _3101,
        _3106,
        _3108,
        _3115,
        _3118,
        _3119,
        _3120,
        _3121,
        _3122,
        _3123,
        _3126,
        _3128,
        _3129,
        _3130,
        _3133,
        _3136,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ComponentSteadyStateSynchronousResponse")


class ComponentSteadyStateSynchronousResponse(_3084.PartSteadyStateSynchronousResponse):
    """ComponentSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentSteadyStateSynchronousResponse"
    )

    class _Cast_ComponentSteadyStateSynchronousResponse:
        """Special nested class for casting ComponentSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
            parent: "ComponentSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3084.PartSteadyStateSynchronousResponse":
            return self._parent._cast(_3084.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3005.AbstractShaftOrHousingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(
                _3005.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3006.AbstractShaftSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(_3006.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3010.AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(
                _3010.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def bearing_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3012.BearingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(_3012.BearingSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3017.BevelDifferentialGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3017,
            )

            return self._parent._cast(
                _3017.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3018.BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3019.BevelDifferentialSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(
                _3019.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3022.BevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3022,
            )

            return self._parent._cast(_3022.BevelGearSteadyStateSynchronousResponse)

        @property
        def bolt_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3024.BoltSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(_3024.BoltSteadyStateSynchronousResponse)

        @property
        def clutch_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3026.ClutchHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3031.ConceptCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(
                _3031.ConceptCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3035.ConceptGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3035,
            )

            return self._parent._cast(_3035.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3038.ConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3038,
            )

            return self._parent._cast(_3038.ConicalGearSteadyStateSynchronousResponse)

        @property
        def connector_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3040.ConnectorSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.ConnectorSteadyStateSynchronousResponse)

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3042.CouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3042,
            )

            return self._parent._cast(_3042.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3045.CVTPulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.CVTPulleySteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3050.CycloidalDiscSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3050,
            )

            return self._parent._cast(_3050.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3053.CylindricalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3053,
            )

            return self._parent._cast(
                _3053.CylindricalGearSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3054.CylindricalPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.CylindricalPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def datum_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3055.DatumSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3055,
            )

            return self._parent._cast(_3055.DatumSteadyStateSynchronousResponse)

        @property
        def external_cad_model_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3057.ExternalCADModelSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.ExternalCADModelSteadyStateSynchronousResponse
            )

        @property
        def face_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3060.FaceGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.FaceGearSteadyStateSynchronousResponse)

        @property
        def fe_part_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3061.FEPartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.FEPartSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3065.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.GearSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3066.GuideDxfModelSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(_3066.GuideDxfModelSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3069.HypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(_3069.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3073.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3073,
            )

            return self._parent._cast(
                _3073.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3076.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3076,
            )

            return self._parent._cast(
                _3076.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3079.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(
                _3079.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3080.MassDiscSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3080,
            )

            return self._parent._cast(_3080.MassDiscSteadyStateSynchronousResponse)

        @property
        def measurement_component_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3081.MeasurementComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(
                _3081.MeasurementComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3082.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3083.OilSealSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3083,
            )

            return self._parent._cast(_3083.OilSealSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3086.PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(
                _3086.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3090.PlanetCarrierSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(_3090.PlanetCarrierSteadyStateSynchronousResponse)

        @property
        def point_load_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3091.PointLoadSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3091,
            )

            return self._parent._cast(_3091.PointLoadSteadyStateSynchronousResponse)

        @property
        def power_load_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3092.PowerLoadSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3092,
            )

            return self._parent._cast(_3092.PowerLoadSteadyStateSynchronousResponse)

        @property
        def pulley_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3093.PulleySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(_3093.PulleySteadyStateSynchronousResponse)

        @property
        def ring_pins_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3094.RingPinsSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3094,
            )

            return self._parent._cast(_3094.RingPinsSteadyStateSynchronousResponse)

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3098.RollingRingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3098,
            )

            return self._parent._cast(_3098.RollingRingSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3100.ShaftHubConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3100,
            )

            return self._parent._cast(
                _3100.ShaftHubConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3101.ShaftSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3101,
            )

            return self._parent._cast(_3101.ShaftSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3106.SpiralBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3108.SpringDamperHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3108,
            )

            return self._parent._cast(
                _3108.SpringDamperHalfSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3115.StraightBevelDiffGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3115,
            )

            return self._parent._cast(
                _3115.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3118.StraightBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3118,
            )

            return self._parent._cast(
                _3118.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3119.StraightBevelPlanetGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3119,
            )

            return self._parent._cast(
                _3119.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3120.StraightBevelSunGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3120,
            )

            return self._parent._cast(
                _3120.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3121.SynchroniserHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3121,
            )

            return self._parent._cast(
                _3121.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3122.SynchroniserPartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3122,
            )

            return self._parent._cast(
                _3122.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3123.SynchroniserSleeveSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3123,
            )

            return self._parent._cast(
                _3123.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3126.TorqueConverterPumpSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3126,
            )

            return self._parent._cast(
                _3126.TorqueConverterPumpSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3128.TorqueConverterTurbineSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3128,
            )

            return self._parent._cast(
                _3128.TorqueConverterTurbineSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3129.UnbalancedMassSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3129,
            )

            return self._parent._cast(
                _3129.UnbalancedMassSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3130.VirtualComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3130,
            )

            return self._parent._cast(
                _3130.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3133.WormGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3133,
            )

            return self._parent._cast(_3133.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "_3136.ZerolBevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3136,
            )

            return self._parent._cast(
                _3136.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
        ) -> "ComponentSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "ComponentSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2464.Component":
        """mastapy.system_model.part_model.Component

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
    ) -> "ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse":
        return self._Cast_ComponentSteadyStateSynchronousResponse(self)
