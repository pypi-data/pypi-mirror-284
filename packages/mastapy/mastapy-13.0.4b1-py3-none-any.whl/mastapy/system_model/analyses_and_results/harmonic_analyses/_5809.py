"""PartHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7569
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PartHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2488
    from mastapy.system_model.analyses_and_results.modal_analyses import _4683
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5782,
        _5787,
        _5699,
        _5701,
        _5702,
        _5704,
        _5706,
        _5707,
        _5708,
        _5710,
        _5711,
        _5713,
        _5714,
        _5715,
        _5716,
        _5718,
        _5719,
        _5720,
        _5722,
        _5723,
        _5726,
        _5728,
        _5729,
        _5730,
        _5732,
        _5733,
        _5735,
        _5737,
        _5739,
        _5740,
        _5742,
        _5743,
        _5744,
        _5746,
        _5748,
        _5750,
        _5751,
        _5752,
        _5767,
        _5768,
        _5770,
        _5771,
        _5772,
        _5774,
        _5779,
        _5781,
        _5792,
        _5794,
        _5796,
        _5798,
        _5799,
        _5801,
        _5802,
        _5804,
        _5805,
        _5806,
        _5807,
        _5808,
        _5811,
        _5812,
        _5815,
        _5816,
        _5817,
        _5818,
        _5819,
        _5821,
        _5823,
        _5825,
        _5826,
        _5827,
        _5828,
        _5831,
        _5833,
        _5835,
        _5837,
        _5838,
        _5840,
        _5842,
        _5843,
        _5845,
        _5846,
        _5847,
        _5848,
        _5849,
        _5850,
        _5851,
        _5853,
        _5854,
        _5855,
        _5857,
        _5858,
        _5859,
        _5861,
        _5862,
        _5864,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6091,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2806
    from mastapy.system_model.drawing import _2269
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartHarmonicAnalysis",)


Self = TypeVar("Self", bound="PartHarmonicAnalysis")


class PartHarmonicAnalysis(_7569.PartStaticLoadAnalysisCase):
    """PartHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartHarmonicAnalysis")

    class _Cast_PartHarmonicAnalysis:
        """Special nested class for casting PartHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
            parent: "PartHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5699.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5699,
            )

            return self._parent._cast(_5699.AbstractAssemblyHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5701.AbstractShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5702.AbstractShaftOrHousingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5704.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5706.AGMAGleasonConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5706,
            )

            return self._parent._cast(_5706.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5707.AssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.AssemblyHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5708.BearingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.BearingHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5710.BeltDriveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5711.BevelDifferentialGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5713.BevelDifferentialGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5714.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5715.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5716.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.BevelGearHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5718.BevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5719.BoltedJointHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.BoltedJointHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5720.BoltHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5722.ClutchHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.ClutchHalfHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5723.ClutchHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.ClutchHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5728.ConceptCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(_5728.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5729.ConceptCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5729,
            )

            return self._parent._cast(_5729.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5730.ConceptGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5730,
            )

            return self._parent._cast(_5730.ConceptGearHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5732.ConceptGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(_5732.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5733.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5733,
            )

            return self._parent._cast(_5733.ConicalGearHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5735.ConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5735,
            )

            return self._parent._cast(_5735.ConicalGearSetHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5737.ConnectorHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5737,
            )

            return self._parent._cast(_5737.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5739.CouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5739,
            )

            return self._parent._cast(_5739.CouplingHalfHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5740.CouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(_5740.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5742.CVTHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5742,
            )

            return self._parent._cast(_5742.CVTHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5743.CVTPulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(_5743.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5744.CycloidalAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5744,
            )

            return self._parent._cast(_5744.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5746.CycloidalDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5746,
            )

            return self._parent._cast(_5746.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5748.CylindricalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(_5748.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5750.CylindricalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5750,
            )

            return self._parent._cast(_5750.CylindricalGearSetHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5751.CylindricalPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(_5751.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5752.DatumHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5752,
            )

            return self._parent._cast(_5752.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5767.ExternalCADModelHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5767,
            )

            return self._parent._cast(_5767.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5768.FaceGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5768,
            )

            return self._parent._cast(_5768.FaceGearHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5770.FaceGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5770,
            )

            return self._parent._cast(_5770.FaceGearSetHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5771.FEPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(_5771.FEPartHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5772.FlexiblePinAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5772,
            )

            return self._parent._cast(_5772.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5774.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(_5774.GearHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5779.GearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(_5779.GearSetHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5781.GuideDxfModelHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(_5781.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5792.HypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5792,
            )

            return self._parent._cast(_5792.HypoidGearHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5794.HypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5796.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(
                _5796.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5798.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(
                _5798.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5799.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(
                _5799.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5801.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5801,
            )

            return self._parent._cast(
                _5801.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5802.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(
                _5802.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5804.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(
                _5804.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5805.MassDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(_5805.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5806.MeasurementComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5807.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(_5807.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5808.OilSealHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(_5808.OilSealHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5811.PartToPartShearCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5811,
            )

            return self._parent._cast(_5811.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5812.PartToPartShearCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5815.PlanetaryGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.PlanetaryGearSetHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5816.PlanetCarrierHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5817.PointLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5818.PowerLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5819.PulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5819,
            )

            return self._parent._cast(_5819.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5821.RingPinsHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5823.RollingRingAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.RollingRingAssemblyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5825.RollingRingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.RollingRingHarmonicAnalysis)

        @property
        def root_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5826.RootAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.RootAssemblyHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5827.ShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5827,
            )

            return self._parent._cast(_5827.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5828.ShaftHubConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.ShaftHubConnectionHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5831.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5831,
            )

            return self._parent._cast(_5831.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5833.SpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.SpiralBevelGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5835.SpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5835,
            )

            return self._parent._cast(_5835.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5837.SpringDamperHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.SpringDamperHalfHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5838.SpringDamperHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5840.StraightBevelDiffGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5842.StraightBevelDiffGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5842,
            )

            return self._parent._cast(_5842.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5843.StraightBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5845.StraightBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5845,
            )

            return self._parent._cast(_5845.StraightBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5846.StraightBevelPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5846,
            )

            return self._parent._cast(_5846.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5847.StraightBevelSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5847,
            )

            return self._parent._cast(_5847.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5848.SynchroniserHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5848,
            )

            return self._parent._cast(_5848.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5849.SynchroniserHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5849,
            )

            return self._parent._cast(_5849.SynchroniserHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5850.SynchroniserPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5850,
            )

            return self._parent._cast(_5850.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5851.SynchroniserSleeveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5851,
            )

            return self._parent._cast(_5851.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5853.TorqueConverterHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5853,
            )

            return self._parent._cast(_5853.TorqueConverterHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5854.TorqueConverterPumpHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5854,
            )

            return self._parent._cast(_5854.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5855.TorqueConverterTurbineHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5855,
            )

            return self._parent._cast(_5855.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5857.UnbalancedMassHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5857,
            )

            return self._parent._cast(_5857.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5858.VirtualComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5858,
            )

            return self._parent._cast(_5858.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5859.WormGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5859,
            )

            return self._parent._cast(_5859.WormGearHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5861.WormGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5861,
            )

            return self._parent._cast(_5861.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5862.ZerolBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5862,
            )

            return self._parent._cast(_5862.ZerolBevelGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5864.ZerolBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5864,
            )

            return self._parent._cast(_5864.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "PartHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2488.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def coupled_modal_analysis(self: Self) -> "_4683.PartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis(self: Self) -> "_5782.HarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_options(self: Self) -> "_5787.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analyses_of_single_excitations(
        self: Self,
    ) -> "List[_6091.HarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysesOfSingleExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2806.PartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2269.HarmonicAnalysisViewable":
        """mastapy.system_model.drawing.HarmonicAnalysisViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis":
        return self._Cast_PartHarmonicAnalysis(self)
