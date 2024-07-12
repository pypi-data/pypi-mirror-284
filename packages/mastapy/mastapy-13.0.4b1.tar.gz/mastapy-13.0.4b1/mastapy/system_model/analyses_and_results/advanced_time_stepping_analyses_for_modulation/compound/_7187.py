"""ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7241,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7057,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7163,
        _7164,
        _7166,
        _7170,
        _7173,
        _7176,
        _7177,
        _7178,
        _7181,
        _7185,
        _7190,
        _7191,
        _7194,
        _7198,
        _7201,
        _7204,
        _7207,
        _7209,
        _7212,
        _7213,
        _7214,
        _7215,
        _7218,
        _7220,
        _7223,
        _7224,
        _7228,
        _7231,
        _7234,
        _7237,
        _7238,
        _7239,
        _7240,
        _7244,
        _7247,
        _7248,
        _7249,
        _7250,
        _7251,
        _7254,
        _7257,
        _7258,
        _7261,
        _7266,
        _7267,
        _7270,
        _7273,
        _7274,
        _7276,
        _7277,
        _7278,
        _7281,
        _7282,
        _7283,
        _7284,
        _7285,
        _7288,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class ComponentCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7241.PartCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """ComponentCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ComponentCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7241.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7241.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7163.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7163,
            )

            return self._parent._cast(
                _7163.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7164.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7164,
            )

            return self._parent._cast(
                _7164.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7166.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7170.BearingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7170,
            )

            return self._parent._cast(
                _7170.BearingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7173.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7173,
            )

            return self._parent._cast(
                _7173.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7176.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7176,
            )

            return self._parent._cast(
                _7176.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7177.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7177,
            )

            return self._parent._cast(
                _7177.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7178.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7178,
            )

            return self._parent._cast(
                _7178.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7181.BoltCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7181,
            )

            return self._parent._cast(
                _7181.BoltCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7185.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7185,
            )

            return self._parent._cast(
                _7185.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7190.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7190,
            )

            return self._parent._cast(
                _7190.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7191.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7191,
            )

            return self._parent._cast(
                _7191.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7194.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7194,
            )

            return self._parent._cast(
                _7194.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7198.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7198,
            )

            return self._parent._cast(
                _7198.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7201.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7201,
            )

            return self._parent._cast(
                _7201.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7204.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7204,
            )

            return self._parent._cast(
                _7204.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7207.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7207,
            )

            return self._parent._cast(
                _7207.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7209.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7209,
            )

            return self._parent._cast(
                _7209.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7212.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7212,
            )

            return self._parent._cast(
                _7212.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def datum_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7213.DatumCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7213,
            )

            return self._parent._cast(
                _7213.DatumCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def external_cad_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7214.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7214,
            )

            return self._parent._cast(
                _7214.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7215.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7215,
            )

            return self._parent._cast(
                _7215.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7218.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7218,
            )

            return self._parent._cast(
                _7218.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7220.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def guide_dxf_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7223.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7223,
            )

            return self._parent._cast(
                _7223.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7224.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7224,
            )

            return self._parent._cast(
                _7224.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7231.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7231,
            )

            return self._parent._cast(
                _7231.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7234.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7234,
            )

            return self._parent._cast(
                _7234.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7237.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7237,
            )

            return self._parent._cast(
                _7237.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7238.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7238,
            )

            return self._parent._cast(
                _7238.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7239.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7239,
            )

            return self._parent._cast(
                _7239.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7240.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7240,
            )

            return self._parent._cast(
                _7240.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7244.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7247.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7248.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7248,
            )

            return self._parent._cast(
                _7248.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7249.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7249,
            )

            return self._parent._cast(
                _7249.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7250.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7250,
            )

            return self._parent._cast(
                _7250.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7251.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7251,
            )

            return self._parent._cast(
                _7251.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7254.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7254,
            )

            return self._parent._cast(
                _7254.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7257.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7257,
            )

            return self._parent._cast(
                _7257.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7258.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7258,
            )

            return self._parent._cast(
                _7258.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7261.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7261,
            )

            return self._parent._cast(
                _7261.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7266.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7266,
            )

            return self._parent._cast(
                _7266.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7267.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7267,
            )

            return self._parent._cast(
                _7267.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7270.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7270,
            )

            return self._parent._cast(
                _7270.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7273.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7273,
            )

            return self._parent._cast(
                _7273.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7274.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7274,
            )

            return self._parent._cast(
                _7274.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7276.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7276,
            )

            return self._parent._cast(
                _7276.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7277.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7277,
            )

            return self._parent._cast(
                _7277.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7278.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7278,
            )

            return self._parent._cast(
                _7278.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7281.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7281,
            )

            return self._parent._cast(
                _7281.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7282.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7282,
            )

            return self._parent._cast(
                _7282.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7283.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7283,
            )

            return self._parent._cast(
                _7283.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7284.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7284,
            )

            return self._parent._cast(
                _7284.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7285.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7285,
            )

            return self._parent._cast(
                _7285.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7288.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7288,
            )

            return self._parent._cast(
                _7288.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7057.ComponentAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ComponentAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7057.ComponentAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ComponentAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
