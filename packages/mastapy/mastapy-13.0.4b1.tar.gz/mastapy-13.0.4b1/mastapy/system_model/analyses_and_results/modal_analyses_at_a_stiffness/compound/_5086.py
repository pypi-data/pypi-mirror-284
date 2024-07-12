"""MountableComponentCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5034,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "MountableComponentCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4957,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5013,
        _5017,
        _5020,
        _5023,
        _5024,
        _5025,
        _5032,
        _5037,
        _5038,
        _5041,
        _5045,
        _5048,
        _5051,
        _5056,
        _5059,
        _5062,
        _5067,
        _5071,
        _5075,
        _5078,
        _5081,
        _5084,
        _5085,
        _5087,
        _5091,
        _5094,
        _5095,
        _5096,
        _5097,
        _5098,
        _5101,
        _5105,
        _5108,
        _5113,
        _5114,
        _5117,
        _5120,
        _5121,
        _5123,
        _5124,
        _5125,
        _5128,
        _5129,
        _5130,
        _5131,
        _5132,
        _5135,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="MountableComponentCompoundModalAnalysisAtAStiffness")


class MountableComponentCompoundModalAnalysisAtAStiffness(
    _5034.ComponentCompoundModalAnalysisAtAStiffness
):
    """MountableComponentCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_MountableComponentCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting MountableComponentCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
            parent: "MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.ComponentCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5034.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5013.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(
                _5013.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5017.BearingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5017,
            )

            return self._parent._cast(_5017.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5020.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5020,
            )

            return self._parent._cast(
                _5020.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5023.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(
                _5023.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5024.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(
                _5024.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5025.BevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(_5025.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5032.ClutchHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(_5032.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5037.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5037,
            )

            return self._parent._cast(
                _5037.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5038.ConceptGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5038,
            )

            return self._parent._cast(
                _5038.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5041.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(
                _5041.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5045.ConnectorCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(_5045.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5048.CouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(
                _5048.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5051.CVTPulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(_5051.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5056.CylindricalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(
                _5056.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5059.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5059,
            )

            return self._parent._cast(
                _5059.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5062.FaceGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5062,
            )

            return self._parent._cast(_5062.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.GearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5071.HypoidGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(_5071.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5075.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(
                _5075.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5078.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(
                _5078.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5081.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5081,
            )

            return self._parent._cast(
                _5081.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5084.MassDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(_5084.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5085.MeasurementComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5087.OilSealCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5087,
            )

            return self._parent._cast(_5087.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5091.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(
                _5091.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5094.PlanetCarrierCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.PlanetCarrierCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5095.PointLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5095,
            )

            return self._parent._cast(_5095.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5096.PowerLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5096,
            )

            return self._parent._cast(_5096.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5097.PulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(_5097.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5098.RingPinsCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(_5098.RingPinsCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5101.RollingRingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5101,
            )

            return self._parent._cast(
                _5101.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5105.ShaftHubConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5105,
            )

            return self._parent._cast(
                _5105.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5108.SpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5108,
            )

            return self._parent._cast(
                _5108.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5113.SpringDamperHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5113,
            )

            return self._parent._cast(
                _5113.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5114.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5114,
            )

            return self._parent._cast(
                _5114.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5117.StraightBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5117,
            )

            return self._parent._cast(
                _5117.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5120.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5120,
            )

            return self._parent._cast(
                _5120.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5121.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5121,
            )

            return self._parent._cast(
                _5121.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5123.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5123,
            )

            return self._parent._cast(
                _5123.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5124.SynchroniserPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5124,
            )

            return self._parent._cast(
                _5124.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5125.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5125,
            )

            return self._parent._cast(
                _5125.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5128.TorqueConverterPumpCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5128,
            )

            return self._parent._cast(
                _5128.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5129.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5129,
            )

            return self._parent._cast(
                _5129.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5130.UnbalancedMassCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5130,
            )

            return self._parent._cast(
                _5130.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5131.VirtualComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5131,
            )

            return self._parent._cast(
                _5131.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5132.WormGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5132,
            )

            return self._parent._cast(_5132.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "_5135.ZerolBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5135,
            )

            return self._parent._cast(
                _5135.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "MountableComponentCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "MountableComponentCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4957.MountableComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.MountableComponentModalAnalysisAtAStiffness]

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
    ) -> "List[_4957.MountableComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.MountableComponentModalAnalysisAtAStiffness]

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
    ) -> "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness":
        return self._Cast_MountableComponentCompoundModalAnalysisAtAStiffness(self)
