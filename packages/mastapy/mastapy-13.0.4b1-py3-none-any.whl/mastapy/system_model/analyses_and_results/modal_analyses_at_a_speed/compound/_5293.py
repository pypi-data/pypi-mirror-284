"""ComponentCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5347,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ComponentCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5163,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5269,
        _5270,
        _5272,
        _5276,
        _5279,
        _5282,
        _5283,
        _5284,
        _5287,
        _5291,
        _5296,
        _5297,
        _5300,
        _5304,
        _5307,
        _5310,
        _5313,
        _5315,
        _5318,
        _5319,
        _5320,
        _5321,
        _5324,
        _5326,
        _5329,
        _5330,
        _5334,
        _5337,
        _5340,
        _5343,
        _5344,
        _5345,
        _5346,
        _5350,
        _5353,
        _5354,
        _5355,
        _5356,
        _5357,
        _5360,
        _5363,
        _5364,
        _5367,
        _5372,
        _5373,
        _5376,
        _5379,
        _5380,
        _5382,
        _5383,
        _5384,
        _5387,
        _5388,
        _5389,
        _5390,
        _5391,
        _5394,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ComponentCompoundModalAnalysisAtASpeed")


class ComponentCompoundModalAnalysisAtASpeed(_5347.PartCompoundModalAnalysisAtASpeed):
    """ComponentCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ComponentCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ComponentCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
            parent: "ComponentCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5269.AbstractShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(_5269.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5270.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(
                _5270.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5272.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(
                _5272.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bearing_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5276.BearingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5276,
            )

            return self._parent._cast(_5276.BearingCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5279.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(
                _5279.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5282.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(
                _5282.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5283.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5283,
            )

            return self._parent._cast(
                _5283.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5284.BevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def bolt_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5287.BoltCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(_5287.BoltCompoundModalAnalysisAtASpeed)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5291.ClutchHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5291,
            )

            return self._parent._cast(_5291.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5296.ConceptCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5296,
            )

            return self._parent._cast(
                _5296.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5297.ConceptGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5297,
            )

            return self._parent._cast(_5297.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5300.ConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5300,
            )

            return self._parent._cast(_5300.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def connector_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5304.ConnectorCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5307.CouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5310.CVTPulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5310,
            )

            return self._parent._cast(_5310.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5313.CycloidalDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5313,
            )

            return self._parent._cast(_5313.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5315.CylindricalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(
                _5315.CylindricalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5318.CylindricalPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5318,
            )

            return self._parent._cast(
                _5318.CylindricalPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def datum_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5319.DatumCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5319,
            )

            return self._parent._cast(_5319.DatumCompoundModalAnalysisAtASpeed)

        @property
        def external_cad_model_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5320.ExternalCADModelCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.ExternalCADModelCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5321.FaceGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(_5321.FaceGearCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5324.FEPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5324,
            )

            return self._parent._cast(_5324.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5326.GearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.GearCompoundModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5329.GuideDxfModelCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5329,
            )

            return self._parent._cast(_5329.GuideDxfModelCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5330.HypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(_5330.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5334.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(
                _5334.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5337.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(
                _5337.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5340.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5340,
            )

            return self._parent._cast(
                _5340.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5343.MassDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5343,
            )

            return self._parent._cast(_5343.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5344.MeasurementComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.MeasurementComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5345.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5346.OilSealCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5346,
            )

            return self._parent._cast(_5346.OilSealCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5350.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5353.PlanetCarrierCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(_5353.PlanetCarrierCompoundModalAnalysisAtASpeed)

        @property
        def point_load_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5354.PointLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(_5354.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5355.PowerLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5355,
            )

            return self._parent._cast(_5355.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5356.PulleyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(_5356.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5357.RingPinsCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(_5357.RingPinsCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5360.RollingRingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(_5360.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5363.ShaftCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5363,
            )

            return self._parent._cast(_5363.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5364.ShaftHubConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5364,
            )

            return self._parent._cast(
                _5364.ShaftHubConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5367.SpiralBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5367,
            )

            return self._parent._cast(
                _5367.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5372.SpringDamperHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5372,
            )

            return self._parent._cast(
                _5372.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5373.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5373,
            )

            return self._parent._cast(
                _5373.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5376.StraightBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5376,
            )

            return self._parent._cast(
                _5376.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5379.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5379,
            )

            return self._parent._cast(
                _5379.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5380.StraightBevelSunGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5380,
            )

            return self._parent._cast(
                _5380.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5382.SynchroniserHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5382,
            )

            return self._parent._cast(
                _5382.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5383.SynchroniserPartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5383,
            )

            return self._parent._cast(
                _5383.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5384.SynchroniserSleeveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5384,
            )

            return self._parent._cast(
                _5384.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5387.TorqueConverterPumpCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5387,
            )

            return self._parent._cast(
                _5387.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5388.TorqueConverterTurbineCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5388,
            )

            return self._parent._cast(
                _5388.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5389.UnbalancedMassCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5389,
            )

            return self._parent._cast(_5389.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5390.VirtualComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5390,
            )

            return self._parent._cast(
                _5390.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5391.WormGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5391,
            )

            return self._parent._cast(_5391.WormGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5394.ZerolBevelGearCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5394,
            )

            return self._parent._cast(_5394.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
        ) -> "ComponentCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ComponentCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5163.ComponentModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ComponentModalAnalysisAtASpeed]

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
    ) -> "List[_5163.ComponentModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ComponentModalAnalysisAtASpeed]

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
    ) -> "ComponentCompoundModalAnalysisAtASpeed._Cast_ComponentCompoundModalAnalysisAtASpeed":
        return self._Cast_ComponentCompoundModalAnalysisAtASpeed(self)
