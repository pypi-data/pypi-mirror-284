"""ComponentCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2952
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ComponentCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2736
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2873,
        _2874,
        _2876,
        _2880,
        _2883,
        _2886,
        _2887,
        _2888,
        _2891,
        _2895,
        _2900,
        _2901,
        _2904,
        _2908,
        _2911,
        _2914,
        _2917,
        _2919,
        _2922,
        _2923,
        _2925,
        _2926,
        _2929,
        _2931,
        _2934,
        _2935,
        _2939,
        _2942,
        _2945,
        _2948,
        _2949,
        _2950,
        _2951,
        _2955,
        _2958,
        _2959,
        _2960,
        _2961,
        _2962,
        _2965,
        _2968,
        _2970,
        _2973,
        _2978,
        _2979,
        _2982,
        _2985,
        _2986,
        _2988,
        _2989,
        _2990,
        _2993,
        _2994,
        _2995,
        _2996,
        _2997,
        _3000,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ComponentCompoundSystemDeflection")


class ComponentCompoundSystemDeflection(_2952.PartCompoundSystemDeflection):
    """ComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundSystemDeflection")

    class _Cast_ComponentCompoundSystemDeflection:
        """Special nested class for casting ComponentCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
            parent: "ComponentCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2873.AbstractShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2874.AbstractShaftOrHousingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(
                _2874.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2876.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(
                _2876.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def bearing_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2880.BearingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.BearingCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2883.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(
                _2883.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2886.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(
                _2886.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2887.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(
                _2887.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2888.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.BevelGearCompoundSystemDeflection)

        @property
        def bolt_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2891.BoltCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.BoltCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2895.ClutchHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.ClutchHalfCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2900.ConceptCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2900,
            )

            return self._parent._cast(_2900.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2901.ConceptGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2901,
            )

            return self._parent._cast(_2901.ConceptGearCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2904.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.ConicalGearCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2908.ConnectorCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2908,
            )

            return self._parent._cast(_2908.ConnectorCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2911.CouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2911,
            )

            return self._parent._cast(_2911.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2914.CVTPulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2914,
            )

            return self._parent._cast(_2914.CVTPulleyCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2917.CycloidalDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(_2917.CycloidalDiscCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2919.CylindricalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(_2919.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2922.CylindricalPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2922,
            )

            return self._parent._cast(
                _2922.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def datum_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2923.DatumCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(_2923.DatumCompoundSystemDeflection)

        @property
        def external_cad_model_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2925.ExternalCADModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2925,
            )

            return self._parent._cast(_2925.ExternalCADModelCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2926.FaceGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(_2926.FaceGearCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2929.FEPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.FEPartCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2931.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.GearCompoundSystemDeflection)

        @property
        def guide_dxf_model_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2934.GuideDxfModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(_2934.GuideDxfModelCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2935.HypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.HypoidGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2939.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(
                _2939.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2942.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(
                _2942.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2945.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2945,
            )

            return self._parent._cast(
                _2945.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def mass_disc_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2948.MassDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2949.MeasurementComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(
                _2949.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def mountable_component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2951.OilSealCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.OilSealCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2955.PartToPartShearCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(
                _2955.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def planet_carrier_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2958.PlanetCarrierCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2958,
            )

            return self._parent._cast(_2958.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2959.PointLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2960.PowerLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(_2960.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2961.PulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(_2961.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2962.RingPinsCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(_2962.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2965.RollingRingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(_2965.RollingRingCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2968.ShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2968,
            )

            return self._parent._cast(_2968.ShaftCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2970.ShaftHubConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(_2970.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2973.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(_2973.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2978.SpringDamperHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2979.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2979,
            )

            return self._parent._cast(
                _2979.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2982.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2982,
            )

            return self._parent._cast(_2982.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2985.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2985,
            )

            return self._parent._cast(
                _2985.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2986.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2986,
            )

            return self._parent._cast(
                _2986.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def synchroniser_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2988.SynchroniserHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2988,
            )

            return self._parent._cast(_2988.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2989.SynchroniserPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2989,
            )

            return self._parent._cast(_2989.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2990.SynchroniserSleeveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2990,
            )

            return self._parent._cast(_2990.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2993.TorqueConverterPumpCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2993,
            )

            return self._parent._cast(_2993.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2994.TorqueConverterTurbineCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2994,
            )

            return self._parent._cast(
                _2994.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2995.UnbalancedMassCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2995,
            )

            return self._parent._cast(_2995.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2996.VirtualComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2996,
            )

            return self._parent._cast(_2996.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2997.WormGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2997,
            )

            return self._parent._cast(_2997.WormGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_3000.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3000,
            )

            return self._parent._cast(_3000.ZerolBevelGearCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "ComponentCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ComponentCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_2736.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

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
    ) -> "List[_2736.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

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
    ) -> "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection":
        return self._Cast_ComponentCompoundSystemDeflection(self)
