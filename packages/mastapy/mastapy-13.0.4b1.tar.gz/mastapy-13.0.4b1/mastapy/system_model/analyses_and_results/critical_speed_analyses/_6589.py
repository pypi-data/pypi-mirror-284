"""ComponentCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6646
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ComponentCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6565,
        _6566,
        _6568,
        _6572,
        _6575,
        _6578,
        _6579,
        _6580,
        _6583,
        _6587,
        _6592,
        _6593,
        _6596,
        _6600,
        _6603,
        _6609,
        _6612,
        _6614,
        _6617,
        _6618,
        _6619,
        _6620,
        _6623,
        _6625,
        _6628,
        _6629,
        _6633,
        _6636,
        _6639,
        _6642,
        _6643,
        _6644,
        _6645,
        _6649,
        _6652,
        _6653,
        _6654,
        _6655,
        _6656,
        _6660,
        _6662,
        _6663,
        _6666,
        _6671,
        _6672,
        _6675,
        _6678,
        _6679,
        _6681,
        _6682,
        _6683,
        _6686,
        _6687,
        _6688,
        _6689,
        _6690,
        _6693,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ComponentCriticalSpeedAnalysis")


class ComponentCriticalSpeedAnalysis(_6646.PartCriticalSpeedAnalysis):
    """ComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCriticalSpeedAnalysis")

    class _Cast_ComponentCriticalSpeedAnalysis:
        """Special nested class for casting ComponentCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
            parent: "ComponentCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def part_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6565.AbstractShaftCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6566.AbstractShaftOrHousingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6566,
            )

            return self._parent._cast(_6566.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6568.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def bearing_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6572.BearingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6572,
            )

            return self._parent._cast(_6572.BearingCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6575.BevelDifferentialGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6578.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(
                _6578.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6579.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6579,
            )

            return self._parent._cast(
                _6579.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6580.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.BevelGearCriticalSpeedAnalysis)

        @property
        def bolt_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6583.BoltCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(_6583.BoltCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6587.ClutchHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6587,
            )

            return self._parent._cast(_6587.ClutchHalfCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6592.ConceptCouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(_6592.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6593.ConceptGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6593,
            )

            return self._parent._cast(_6593.ConceptGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6596.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6596,
            )

            return self._parent._cast(_6596.ConicalGearCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6600.ConnectorCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(_6600.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6603.CouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6609.CVTPulleyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6609,
            )

            return self._parent._cast(_6609.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6612.CycloidalDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6612,
            )

            return self._parent._cast(_6612.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6614.CylindricalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(_6614.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6617.CylindricalPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(_6617.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def datum_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6618.DatumCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6618,
            )

            return self._parent._cast(_6618.DatumCriticalSpeedAnalysis)

        @property
        def external_cad_model_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6619.ExternalCADModelCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.ExternalCADModelCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6620.FaceGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(_6620.FaceGearCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6623.FEPartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.FEPartCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6625.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.GearCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6628.GuideDxfModelCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(_6628.GuideDxfModelCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6629.HypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6633.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(
                _6633.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6636.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6636,
            )

            return self._parent._cast(
                _6636.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6639.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6639,
            )

            return self._parent._cast(
                _6639.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def mass_disc_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6642.MassDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6642,
            )

            return self._parent._cast(_6642.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6643.MeasurementComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6643,
            )

            return self._parent._cast(_6643.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6644.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.MountableComponentCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6645.OilSealCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6645,
            )

            return self._parent._cast(_6645.OilSealCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6649.PartToPartShearCouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(
                _6649.PartToPartShearCouplingHalfCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6652.PlanetCarrierCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.PlanetCarrierCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6653.PointLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(_6653.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6654.PowerLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(_6654.PowerLoadCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6655.PulleyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.PulleyCriticalSpeedAnalysis)

        @property
        def ring_pins_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6656.RingPinsCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.RingPinsCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6660.RollingRingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(_6660.RollingRingCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6662.ShaftCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6662,
            )

            return self._parent._cast(_6662.ShaftCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6663.ShaftHubConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6666.SpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6666,
            )

            return self._parent._cast(_6666.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6671.SpringDamperHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6671,
            )

            return self._parent._cast(_6671.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6672.StraightBevelDiffGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6672,
            )

            return self._parent._cast(_6672.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6675.StraightBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6675,
            )

            return self._parent._cast(_6675.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6678.StraightBevelPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6678,
            )

            return self._parent._cast(
                _6678.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6679.StraightBevelSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6679,
            )

            return self._parent._cast(_6679.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6681.SynchroniserHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6681,
            )

            return self._parent._cast(_6681.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6682.SynchroniserPartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6682,
            )

            return self._parent._cast(_6682.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6683.SynchroniserSleeveCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6683,
            )

            return self._parent._cast(_6683.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6686.TorqueConverterPumpCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6686,
            )

            return self._parent._cast(_6686.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6687.TorqueConverterTurbineCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6687,
            )

            return self._parent._cast(_6687.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6688.UnbalancedMassCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6688,
            )

            return self._parent._cast(_6688.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6689.VirtualComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6689,
            )

            return self._parent._cast(_6689.VirtualComponentCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6690.WormGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6690,
            )

            return self._parent._cast(_6690.WormGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6693.ZerolBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6693,
            )

            return self._parent._cast(_6693.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "ComponentCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCriticalSpeedAnalysis.TYPE"):
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
    ) -> "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis":
        return self._Cast_ComponentCriticalSpeedAnalysis(self)
