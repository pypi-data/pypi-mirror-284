"""ComponentCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5979
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ComponentCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5726
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5901,
        _5902,
        _5904,
        _5908,
        _5911,
        _5914,
        _5915,
        _5916,
        _5919,
        _5923,
        _5928,
        _5929,
        _5932,
        _5936,
        _5939,
        _5942,
        _5945,
        _5947,
        _5950,
        _5951,
        _5952,
        _5953,
        _5956,
        _5958,
        _5961,
        _5962,
        _5966,
        _5969,
        _5972,
        _5975,
        _5976,
        _5977,
        _5978,
        _5982,
        _5985,
        _5986,
        _5987,
        _5988,
        _5989,
        _5992,
        _5995,
        _5996,
        _5999,
        _6004,
        _6005,
        _6008,
        _6011,
        _6012,
        _6014,
        _6015,
        _6016,
        _6019,
        _6020,
        _6021,
        _6022,
        _6023,
        _6026,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundHarmonicAnalysis")


class ComponentCompoundHarmonicAnalysis(_5979.PartCompoundHarmonicAnalysis):
    """ComponentCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundHarmonicAnalysis")

    class _Cast_ComponentCompoundHarmonicAnalysis:
        """Special nested class for casting ComponentCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
            parent: "ComponentCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5901.AbstractShaftCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(_5901.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5902.AbstractShaftOrHousingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5902,
            )

            return self._parent._cast(
                _5902.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5904.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(
                _5904.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def bearing_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5908.BearingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5908,
            )

            return self._parent._cast(_5908.BearingCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5911.BevelDifferentialGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(
                _5911.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5914.BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5914,
            )

            return self._parent._cast(
                _5914.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5915.BevelDifferentialSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5915,
            )

            return self._parent._cast(
                _5915.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5916.BevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5916,
            )

            return self._parent._cast(_5916.BevelGearCompoundHarmonicAnalysis)

        @property
        def bolt_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5919.BoltCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5919,
            )

            return self._parent._cast(_5919.BoltCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5923.ClutchHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5923,
            )

            return self._parent._cast(_5923.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5928.ConceptCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5928,
            )

            return self._parent._cast(_5928.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5929.ConceptGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5929,
            )

            return self._parent._cast(_5929.ConceptGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5932.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5932,
            )

            return self._parent._cast(_5932.ConicalGearCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5936.ConnectorCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5936,
            )

            return self._parent._cast(_5936.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5939.CouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5942.CVTPulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(_5942.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5945.CycloidalDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(_5945.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5947.CylindricalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(_5947.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5950.CylindricalPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(
                _5950.CylindricalPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def datum_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5951.DatumCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5951,
            )

            return self._parent._cast(_5951.DatumCompoundHarmonicAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5952.ExternalCADModelCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(_5952.ExternalCADModelCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5953.FaceGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(_5953.FaceGearCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5956.FEPartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.FEPartCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5958.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.GearCompoundHarmonicAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5961.GuideDxfModelCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5961,
            )

            return self._parent._cast(_5961.GuideDxfModelCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5962.HypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5962,
            )

            return self._parent._cast(_5962.HypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5966.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(
                _5966.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5969.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5969,
            )

            return self._parent._cast(
                _5969.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5972.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5972,
            )

            return self._parent._cast(
                _5972.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5975.MassDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5975,
            )

            return self._parent._cast(_5975.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5976.MeasurementComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(
                _5976.MeasurementComponentCompoundHarmonicAnalysis
            )

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5977.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.MountableComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5978.OilSealCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5978,
            )

            return self._parent._cast(_5978.OilSealCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5982.PartToPartShearCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(
                _5982.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def planet_carrier_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5985.PlanetCarrierCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(_5985.PlanetCarrierCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5986.PointLoadCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5986,
            )

            return self._parent._cast(_5986.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5987.PowerLoadCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(_5987.PowerLoadCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5988.PulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(_5988.PulleyCompoundHarmonicAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5989.RingPinsCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5989,
            )

            return self._parent._cast(_5989.RingPinsCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5992.RollingRingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(_5992.RollingRingCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5995.ShaftCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5995,
            )

            return self._parent._cast(_5995.ShaftCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5996.ShaftHubConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5996,
            )

            return self._parent._cast(_5996.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_5999.SpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5999,
            )

            return self._parent._cast(_5999.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6004.SpringDamperHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6005.StraightBevelDiffGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6005,
            )

            return self._parent._cast(
                _6005.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6008.StraightBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6008,
            )

            return self._parent._cast(_6008.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6011.StraightBevelPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6011,
            )

            return self._parent._cast(
                _6011.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6012.StraightBevelSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6012,
            )

            return self._parent._cast(
                _6012.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6014.SynchroniserHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6014,
            )

            return self._parent._cast(_6014.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6015.SynchroniserPartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6015,
            )

            return self._parent._cast(_6015.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6016.SynchroniserSleeveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6016,
            )

            return self._parent._cast(_6016.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6019.TorqueConverterPumpCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6019,
            )

            return self._parent._cast(_6019.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6020.TorqueConverterTurbineCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6020,
            )

            return self._parent._cast(
                _6020.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6021.UnbalancedMassCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6021,
            )

            return self._parent._cast(_6021.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6022.VirtualComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6022,
            )

            return self._parent._cast(_6022.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6023.WormGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6023,
            )

            return self._parent._cast(_6023.WormGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "_6026.ZerolBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6026,
            )

            return self._parent._cast(_6026.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "ComponentCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ComponentCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_5726.ComponentHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ComponentHarmonicAnalysis]

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
    ) -> "List[_5726.ComponentHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ComponentHarmonicAnalysis]

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
    ) -> "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis":
        return self._Cast_ComponentCompoundHarmonicAnalysis(self)
