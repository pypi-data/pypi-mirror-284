"""ComponentCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3997
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ComponentCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3809
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3919,
        _3920,
        _3922,
        _3926,
        _3929,
        _3932,
        _3933,
        _3934,
        _3937,
        _3941,
        _3946,
        _3947,
        _3950,
        _3954,
        _3957,
        _3960,
        _3963,
        _3965,
        _3968,
        _3969,
        _3970,
        _3971,
        _3974,
        _3976,
        _3979,
        _3980,
        _3984,
        _3987,
        _3990,
        _3993,
        _3994,
        _3995,
        _3996,
        _4000,
        _4003,
        _4004,
        _4005,
        _4006,
        _4007,
        _4010,
        _4013,
        _4014,
        _4017,
        _4022,
        _4023,
        _4026,
        _4029,
        _4030,
        _4032,
        _4033,
        _4034,
        _4037,
        _4038,
        _4039,
        _4040,
        _4041,
        _4044,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundStabilityAnalysis")


class ComponentCompoundStabilityAnalysis(_3997.PartCompoundStabilityAnalysis):
    """ComponentCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundStabilityAnalysis")

    class _Cast_ComponentCompoundStabilityAnalysis:
        """Special nested class for casting ComponentCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
            parent: "ComponentCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3919.AbstractShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3920.AbstractShaftOrHousingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(
                _3920.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3922.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(
                _3922.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def bearing_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3926.BearingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.BearingCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3929.BevelDifferentialGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(
                _3929.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3932.BevelDifferentialPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(
                _3932.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3933.BevelDifferentialSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(
                _3933.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3934.BevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3934,
            )

            return self._parent._cast(_3934.BevelGearCompoundStabilityAnalysis)

        @property
        def bolt_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3937.BoltCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.BoltCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3941.ClutchHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(_3941.ClutchHalfCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3946.ConceptCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3946,
            )

            return self._parent._cast(
                _3946.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def concept_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3947.ConceptGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3947,
            )

            return self._parent._cast(_3947.ConceptGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3950.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.ConicalGearCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3954.ConnectorCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3957.CouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3960.CVTPulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(_3960.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3963.CycloidalDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(_3963.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3965.CylindricalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(_3965.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3968.CylindricalPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def datum_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3969.DatumCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(_3969.DatumCompoundStabilityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3970.ExternalCADModelCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(_3970.ExternalCADModelCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3971.FaceGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(_3971.FaceGearCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3974.FEPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.FEPartCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3976.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.GearCompoundStabilityAnalysis)

        @property
        def guide_dxf_model_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3979.GuideDxfModelCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(_3979.GuideDxfModelCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3980.HypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.HypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3984.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(
                _3984.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3987.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3987,
            )

            return self._parent._cast(
                _3987.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3990.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(
                _3990.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def mass_disc_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3993.MassDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3994.MeasurementComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(
                _3994.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def mountable_component_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3995.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.MountableComponentCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_3996.OilSealCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(_3996.OilSealCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4000.PartToPartShearCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def planet_carrier_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4003.PlanetCarrierCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(_4003.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4004.PointLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(_4004.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4005.PowerLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(_4005.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4006.PulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(_4006.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4007.RingPinsCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(_4007.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4010.RollingRingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(_4010.RollingRingCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4013.ShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(_4013.ShaftCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4014.ShaftHubConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4014,
            )

            return self._parent._cast(_4014.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4017.SpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(_4017.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4022.SpringDamperHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4023.StraightBevelDiffGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4023,
            )

            return self._parent._cast(
                _4023.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4026.StraightBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4026,
            )

            return self._parent._cast(_4026.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4029.StraightBevelPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4029,
            )

            return self._parent._cast(
                _4029.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4030.StraightBevelSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4030,
            )

            return self._parent._cast(
                _4030.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4032.SynchroniserHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4032,
            )

            return self._parent._cast(_4032.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4033.SynchroniserPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4033,
            )

            return self._parent._cast(_4033.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4034.SynchroniserSleeveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4034,
            )

            return self._parent._cast(_4034.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4037.TorqueConverterPumpCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4037,
            )

            return self._parent._cast(
                _4037.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4038.TorqueConverterTurbineCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4038,
            )

            return self._parent._cast(
                _4038.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4039.UnbalancedMassCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4039,
            )

            return self._parent._cast(_4039.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4040.VirtualComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4040,
            )

            return self._parent._cast(_4040.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4041.WormGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4041,
            )

            return self._parent._cast(_4041.WormGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "_4044.ZerolBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4044,
            )

            return self._parent._cast(_4044.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "ComponentCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ComponentCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3809.ComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ComponentStabilityAnalysis]

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
    ) -> "List[_3809.ComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ComponentStabilityAnalysis]

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
    ) -> "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis":
        return self._Cast_ComponentCompoundStabilityAnalysis(self)
