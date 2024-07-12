"""ComponentCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7506,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ComponentCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7319,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7428,
        _7429,
        _7431,
        _7435,
        _7438,
        _7441,
        _7442,
        _7443,
        _7446,
        _7450,
        _7455,
        _7456,
        _7459,
        _7463,
        _7466,
        _7469,
        _7472,
        _7474,
        _7477,
        _7478,
        _7479,
        _7480,
        _7483,
        _7485,
        _7488,
        _7489,
        _7493,
        _7496,
        _7499,
        _7502,
        _7503,
        _7504,
        _7505,
        _7509,
        _7512,
        _7513,
        _7514,
        _7515,
        _7516,
        _7519,
        _7522,
        _7523,
        _7526,
        _7531,
        _7532,
        _7535,
        _7538,
        _7539,
        _7541,
        _7542,
        _7543,
        _7546,
        _7547,
        _7548,
        _7549,
        _7550,
        _7553,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ComponentCompoundAdvancedSystemDeflection")


class ComponentCompoundAdvancedSystemDeflection(
    _7506.PartCompoundAdvancedSystemDeflection
):
    """ComponentCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundAdvancedSystemDeflection"
    )

    class _Cast_ComponentCompoundAdvancedSystemDeflection:
        """Special nested class for casting ComponentCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
            parent: "ComponentCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7428.AbstractShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(
                _7428.AbstractShaftCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7429.AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(
                _7429.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7431.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(
                _7431.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def bearing_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7435.BearingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7435,
            )

            return self._parent._cast(_7435.BearingCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7438.BevelDifferentialGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(
                _7438.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7441.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(
                _7441.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7442.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7443.BevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(_7443.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def bolt_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7446.BoltCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7446,
            )

            return self._parent._cast(_7446.BoltCompoundAdvancedSystemDeflection)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7450.ClutchHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7450,
            )

            return self._parent._cast(_7450.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7455.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7455,
            )

            return self._parent._cast(
                _7455.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7456.ConceptGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7456,
            )

            return self._parent._cast(_7456.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7459.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(_7459.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def connector_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7463.ConnectorCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7463,
            )

            return self._parent._cast(_7463.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7466.CouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(
                _7466.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7469.CVTPulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(_7469.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7472.CycloidalDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7472,
            )

            return self._parent._cast(
                _7472.CycloidalDiscCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7474.CylindricalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7474,
            )

            return self._parent._cast(
                _7474.CylindricalGearCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7477.CylindricalPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7477,
            )

            return self._parent._cast(
                _7477.CylindricalPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def datum_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7478.DatumCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7478,
            )

            return self._parent._cast(_7478.DatumCompoundAdvancedSystemDeflection)

        @property
        def external_cad_model_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7479.ExternalCADModelCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.ExternalCADModelCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7480.FaceGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7480,
            )

            return self._parent._cast(_7480.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7483.FEPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(_7483.FEPartCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7485.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.GearCompoundAdvancedSystemDeflection)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7488.GuideDxfModelCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(
                _7488.GuideDxfModelCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7489.HypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7489,
            )

            return self._parent._cast(_7489.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> (
            "_7493.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(
                _7493.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7496.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7499.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7502.MassDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(_7502.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7503.MeasurementComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(
                _7503.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7504.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7505.OilSealCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7505,
            )

            return self._parent._cast(_7505.OilSealCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7509.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def planet_carrier_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7512.PlanetCarrierCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.PlanetCarrierCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7513.PointLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(_7513.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7514.PowerLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7514,
            )

            return self._parent._cast(_7514.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def pulley_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7515.PulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(_7515.PulleyCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7516.RingPinsCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(_7516.RingPinsCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7519.RollingRingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7519,
            )

            return self._parent._cast(_7519.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def shaft_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7522.ShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7522,
            )

            return self._parent._cast(_7522.ShaftCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7523.ShaftHubConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.ShaftHubConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7526.SpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7526,
            )

            return self._parent._cast(
                _7526.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7531.SpringDamperHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7531,
            )

            return self._parent._cast(
                _7531.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7532.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7532,
            )

            return self._parent._cast(
                _7532.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7535.StraightBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7535,
            )

            return self._parent._cast(
                _7535.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7538.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7538,
            )

            return self._parent._cast(
                _7538.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7539.StraightBevelSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7539,
            )

            return self._parent._cast(
                _7539.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7541.SynchroniserHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7541,
            )

            return self._parent._cast(
                _7541.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7542.SynchroniserPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7542,
            )

            return self._parent._cast(
                _7542.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7543.SynchroniserSleeveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7543,
            )

            return self._parent._cast(
                _7543.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7546.TorqueConverterPumpCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7546,
            )

            return self._parent._cast(
                _7546.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7547.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7547,
            )

            return self._parent._cast(
                _7547.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7548.UnbalancedMassCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7548,
            )

            return self._parent._cast(
                _7548.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7549.VirtualComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7549,
            )

            return self._parent._cast(
                _7549.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7550.WormGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7550,
            )

            return self._parent._cast(_7550.WormGearCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "_7553.ZerolBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7553,
            )

            return self._parent._cast(
                _7553.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "ComponentCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ComponentCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7319.ComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ComponentAdvancedSystemDeflection]

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
    ) -> "List[_7319.ComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ComponentAdvancedSystemDeflection]

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
    ) -> "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection":
        return self._Cast_ComponentCompoundAdvancedSystemDeflection(self)
