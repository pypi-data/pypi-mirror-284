"""ComponentCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3734,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3550,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3656,
        _3657,
        _3659,
        _3663,
        _3666,
        _3669,
        _3670,
        _3671,
        _3674,
        _3678,
        _3683,
        _3684,
        _3687,
        _3691,
        _3694,
        _3697,
        _3700,
        _3702,
        _3705,
        _3706,
        _3707,
        _3708,
        _3711,
        _3713,
        _3716,
        _3717,
        _3721,
        _3724,
        _3727,
        _3730,
        _3731,
        _3732,
        _3733,
        _3737,
        _3740,
        _3741,
        _3742,
        _3743,
        _3744,
        _3747,
        _3750,
        _3751,
        _3754,
        _3759,
        _3760,
        _3763,
        _3766,
        _3767,
        _3769,
        _3770,
        _3771,
        _3774,
        _3775,
        _3776,
        _3777,
        _3778,
        _3781,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ComponentCompoundSteadyStateSynchronousResponseAtASpeed")


class ComponentCompoundSteadyStateSynchronousResponseAtASpeed(
    _3734.PartCompoundSteadyStateSynchronousResponseAtASpeed
):
    """ComponentCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ComponentCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3734.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3734.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3656.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3656,
            )

            return self._parent._cast(
                _3656.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3657.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3659.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3659,
            )

            return self._parent._cast(
                _3659.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3663.BearingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3663,
            )

            return self._parent._cast(
                _3663.BearingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3666.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3666,
            )

            return self._parent._cast(
                _3666.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3669.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3669,
            )

            return self._parent._cast(
                _3669.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3670.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3670,
            )

            return self._parent._cast(
                _3670.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3671.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3671,
            )

            return self._parent._cast(
                _3671.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3674.BoltCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3674,
            )

            return self._parent._cast(
                _3674.BoltCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3678.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3678,
            )

            return self._parent._cast(
                _3678.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3683.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3683,
            )

            return self._parent._cast(
                _3683.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3684.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3684,
            )

            return self._parent._cast(
                _3684.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3687.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3687,
            )

            return self._parent._cast(
                _3687.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3691.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3694.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3694,
            )

            return self._parent._cast(
                _3694.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3697.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3697,
            )

            return self._parent._cast(
                _3697.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3700.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3700,
            )

            return self._parent._cast(
                _3700.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3702.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3702,
            )

            return self._parent._cast(
                _3702.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3705.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3705,
            )

            return self._parent._cast(
                _3705.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3706.DatumCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3706,
            )

            return self._parent._cast(
                _3706.DatumCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3707.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3707,
            )

            return self._parent._cast(
                _3707.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3708.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3708,
            )

            return self._parent._cast(
                _3708.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3711.FEPartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.FEPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3713.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3716.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3716,
            )

            return self._parent._cast(
                _3716.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3717.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3717,
            )

            return self._parent._cast(
                _3717.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3724.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3724,
            )

            return self._parent._cast(
                _3724.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3727.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3727,
            )

            return self._parent._cast(
                _3727.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3730.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3730,
            )

            return self._parent._cast(
                _3730.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3731.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3731,
            )

            return self._parent._cast(
                _3731.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3732.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3732,
            )

            return self._parent._cast(
                _3732.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3733.OilSealCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3733,
            )

            return self._parent._cast(
                _3733.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3737.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3737,
            )

            return self._parent._cast(
                _3737.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3740.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3740,
            )

            return self._parent._cast(
                _3740.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3741.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3741,
            )

            return self._parent._cast(
                _3741.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3742.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3742,
            )

            return self._parent._cast(
                _3742.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3743.PulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3743,
            )

            return self._parent._cast(
                _3743.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3744.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3744,
            )

            return self._parent._cast(
                _3744.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3747.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3747,
            )

            return self._parent._cast(
                _3747.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3750.ShaftCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3750,
            )

            return self._parent._cast(
                _3750.ShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3751.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3751,
            )

            return self._parent._cast(
                _3751.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3754.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3754,
            )

            return self._parent._cast(
                _3754.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3759.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3759,
            )

            return self._parent._cast(
                _3759.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3760.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3760,
            )

            return self._parent._cast(
                _3760.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3763.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3763,
            )

            return self._parent._cast(
                _3763.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3766.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3766,
            )

            return self._parent._cast(
                _3766.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3767.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3767,
            )

            return self._parent._cast(
                _3767.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3769.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3769,
            )

            return self._parent._cast(
                _3769.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3770.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3770,
            )

            return self._parent._cast(
                _3770.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3771.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3771,
            )

            return self._parent._cast(
                _3771.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3774.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3774,
            )

            return self._parent._cast(
                _3774.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3775.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3775,
            )

            return self._parent._cast(
                _3775.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3776.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3776,
            )

            return self._parent._cast(
                _3776.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3777.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3777,
            )

            return self._parent._cast(
                _3777.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3778.WormGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3778,
            )

            return self._parent._cast(
                _3778.WormGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3781.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3781,
            )

            return self._parent._cast(
                _3781.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3550.ComponentSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ComponentSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3550.ComponentSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ComponentSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed(self)
