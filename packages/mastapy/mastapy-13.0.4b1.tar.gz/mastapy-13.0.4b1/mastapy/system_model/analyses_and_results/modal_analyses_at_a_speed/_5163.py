"""ComponentModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ComponentModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5139,
        _5140,
        _5143,
        _5146,
        _5150,
        _5152,
        _5153,
        _5155,
        _5158,
        _5160,
        _5165,
        _5168,
        _5171,
        _5174,
        _5176,
        _5180,
        _5183,
        _5186,
        _5188,
        _5189,
        _5190,
        _5192,
        _5194,
        _5197,
        _5199,
        _5201,
        _5205,
        _5208,
        _5211,
        _5213,
        _5214,
        _5216,
        _5217,
        _5220,
        _5224,
        _5225,
        _5226,
        _5227,
        _5228,
        _5232,
        _5234,
        _5235,
        _5239,
        _5242,
        _5245,
        _5248,
        _5250,
        _5251,
        _5252,
        _5254,
        _5255,
        _5258,
        _5259,
        _5260,
        _5261,
        _5263,
        _5266,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ComponentModalAnalysisAtASpeed")


class ComponentModalAnalysisAtASpeed(_5218.PartModalAnalysisAtASpeed):
    """ComponentModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentModalAnalysisAtASpeed")

    class _Cast_ComponentModalAnalysisAtASpeed:
        """Special nested class for casting ComponentModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
            parent: "ComponentModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def part_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5218.PartModalAnalysisAtASpeed":
            return self._parent._cast(_5218.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5139.AbstractShaftModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5139,
            )

            return self._parent._cast(_5139.AbstractShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5140.AbstractShaftOrHousingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(_5140.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5143.AGMAGleasonConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5143,
            )

            return self._parent._cast(_5143.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def bearing_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5146.BearingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(_5146.BearingModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5150.BevelDifferentialGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5152.BevelDifferentialPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(
                _5152.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5153.BevelDifferentialSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(
                _5153.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5155.BevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(_5155.BevelGearModalAnalysisAtASpeed)

        @property
        def bolt_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5158.BoltModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5158,
            )

            return self._parent._cast(_5158.BoltModalAnalysisAtASpeed)

        @property
        def clutch_half_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5160.ClutchHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.ClutchHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5165.ConceptCouplingHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5168.ConceptGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5168,
            )

            return self._parent._cast(_5168.ConceptGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5171.ConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5171,
            )

            return self._parent._cast(_5171.ConicalGearModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5174.ConnectorModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5174,
            )

            return self._parent._cast(_5174.ConnectorModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5176.CouplingHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5176,
            )

            return self._parent._cast(_5176.CouplingHalfModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5180.CVTPulleyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5180,
            )

            return self._parent._cast(_5180.CVTPulleyModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5183.CycloidalDiscModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5183,
            )

            return self._parent._cast(_5183.CycloidalDiscModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5186.CylindricalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5186,
            )

            return self._parent._cast(_5186.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5188.CylindricalPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(_5188.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def datum_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5189.DatumModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5189,
            )

            return self._parent._cast(_5189.DatumModalAnalysisAtASpeed)

        @property
        def external_cad_model_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5190.ExternalCADModelModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(_5190.ExternalCADModelModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5192.FaceGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5192,
            )

            return self._parent._cast(_5192.FaceGearModalAnalysisAtASpeed)

        @property
        def fe_part_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5194.FEPartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.FEPartModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5197.GearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.GearModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5199.GuideDxfModelModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.GuideDxfModelModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5201.HypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5201,
            )

            return self._parent._cast(_5201.HypoidGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5205.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(
                _5205.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5208.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5208,
            )

            return self._parent._cast(
                _5208.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5211.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5211,
            )

            return self._parent._cast(
                _5211.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5213.MassDiscModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5214.MeasurementComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(_5214.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5216.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.MountableComponentModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5217.OilSealModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5217,
            )

            return self._parent._cast(_5217.OilSealModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5220.PartToPartShearCouplingHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(
                _5220.PartToPartShearCouplingHalfModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5224.PlanetCarrierModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5224,
            )

            return self._parent._cast(_5224.PlanetCarrierModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5225.PointLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(_5225.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5226.PowerLoadModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(_5226.PowerLoadModalAnalysisAtASpeed)

        @property
        def pulley_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5227.PulleyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5227,
            )

            return self._parent._cast(_5227.PulleyModalAnalysisAtASpeed)

        @property
        def ring_pins_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5228.RingPinsModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.RingPinsModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5232.RollingRingModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5232,
            )

            return self._parent._cast(_5232.RollingRingModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5234.ShaftHubConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5234,
            )

            return self._parent._cast(_5234.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def shaft_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5235.ShaftModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5235,
            )

            return self._parent._cast(_5235.ShaftModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5239.SpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5242.SpringDamperHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5242,
            )

            return self._parent._cast(_5242.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5245.StraightBevelDiffGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5245,
            )

            return self._parent._cast(_5245.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5248.StraightBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5248,
            )

            return self._parent._cast(_5248.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5250.StraightBevelPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5250,
            )

            return self._parent._cast(
                _5250.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5251.StraightBevelSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5251,
            )

            return self._parent._cast(_5251.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5252.SynchroniserHalfModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5252,
            )

            return self._parent._cast(_5252.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5254.SynchroniserPartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5254,
            )

            return self._parent._cast(_5254.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5255.SynchroniserSleeveModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5255,
            )

            return self._parent._cast(_5255.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5258.TorqueConverterPumpModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5258,
            )

            return self._parent._cast(_5258.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5259.TorqueConverterTurbineModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5259,
            )

            return self._parent._cast(_5259.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5260.UnbalancedMassModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5260,
            )

            return self._parent._cast(_5260.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5261.VirtualComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5261,
            )

            return self._parent._cast(_5261.VirtualComponentModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5263.WormGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5263,
            )

            return self._parent._cast(_5263.WormGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "_5266.ZerolBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5266,
            )

            return self._parent._cast(_5266.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
        ) -> "ComponentModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentModalAnalysisAtASpeed.TYPE"):
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
    ) -> "ComponentModalAnalysisAtASpeed._Cast_ComponentModalAnalysisAtASpeed":
        return self._Cast_ComponentModalAnalysisAtASpeed(self)
