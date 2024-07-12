"""ComponentAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7376
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ComponentAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7292,
        _7293,
        _7298,
        _7302,
        _7305,
        _7308,
        _7309,
        _7310,
        _7313,
        _7317,
        _7322,
        _7323,
        _7326,
        _7330,
        _7334,
        _7337,
        _7339,
        _7342,
        _7346,
        _7347,
        _7348,
        _7349,
        _7352,
        _7354,
        _7357,
        _7358,
        _7362,
        _7365,
        _7368,
        _7372,
        _7373,
        _7374,
        _7375,
        _7379,
        _7382,
        _7383,
        _7384,
        _7385,
        _7386,
        _7388,
        _7392,
        _7393,
        _7396,
        _7401,
        _7402,
        _7405,
        _7408,
        _7409,
        _7411,
        _7412,
        _7413,
        _7416,
        _7417,
        _7419,
        _7420,
        _7421,
        _7424,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ComponentAdvancedSystemDeflection")


class ComponentAdvancedSystemDeflection(_7376.PartAdvancedSystemDeflection):
    """ComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentAdvancedSystemDeflection")

    class _Cast_ComponentAdvancedSystemDeflection:
        """Special nested class for casting ComponentAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
            parent: "ComponentAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7376.PartAdvancedSystemDeflection":
            return self._parent._cast(_7376.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7292.AbstractShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(_7292.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7293.AbstractShaftOrHousingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7293,
            )

            return self._parent._cast(
                _7293.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7298.AGMAGleasonConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(
                _7298.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def bearing_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7302.BearingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(_7302.BearingAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7305.BevelDifferentialGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(
                _7305.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7308.BevelDifferentialPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(
                _7308.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7309.BevelDifferentialSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(
                _7309.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7310.BevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7310,
            )

            return self._parent._cast(_7310.BevelGearAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7313.BoltAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.BoltAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7317.ClutchHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.ClutchHalfAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7322.ConceptCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(_7322.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7323.ConceptGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7323,
            )

            return self._parent._cast(_7323.ConceptGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7326.ConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(_7326.ConicalGearAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7330.ConnectorAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7334.CouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7337.CVTPulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(_7337.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7339.CycloidalDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(_7339.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7342.CylindricalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(_7342.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7346.CylindricalPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7346,
            )

            return self._parent._cast(
                _7346.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def datum_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7347.DatumAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(_7347.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7348.ExternalCADModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(_7348.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7349.FaceGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(_7349.FaceGearAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7352.FEPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.FEPartAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7354.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.GearAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7357.GuideDxfModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7358.HypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7358,
            )

            return self._parent._cast(_7358.HypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7362.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(
                _7362.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7365.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7365,
            )

            return self._parent._cast(
                _7365.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7368.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(
                _7368.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7372.MassDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7373.MeasurementComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(
                _7373.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def mountable_component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7374.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(_7374.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7375.OilSealAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(_7375.OilSealAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7379.PartToPartShearCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planet_carrier_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7382.PlanetCarrierAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(_7382.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7383.PointLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(_7383.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7384.PowerLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(_7384.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7385.PulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(_7385.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7386.RingPinsAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(_7386.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7388.RollingRingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(_7388.RollingRingAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7392.ShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(_7392.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7393.ShaftHubConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7393,
            )

            return self._parent._cast(_7393.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7396.SpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(_7396.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7401.SpringDamperHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7402.StraightBevelDiffGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7402,
            )

            return self._parent._cast(
                _7402.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7405.StraightBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7405,
            )

            return self._parent._cast(_7405.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7408.StraightBevelPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7408,
            )

            return self._parent._cast(
                _7408.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7409.StraightBevelSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7409,
            )

            return self._parent._cast(
                _7409.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7411.SynchroniserHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7411,
            )

            return self._parent._cast(_7411.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7412.SynchroniserPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7412,
            )

            return self._parent._cast(_7412.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7413.SynchroniserSleeveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7413,
            )

            return self._parent._cast(_7413.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7416.TorqueConverterPumpAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7416,
            )

            return self._parent._cast(_7416.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7417.TorqueConverterTurbineAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7417,
            )

            return self._parent._cast(
                _7417.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7419.UnbalancedMassAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7419,
            )

            return self._parent._cast(_7419.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7420.VirtualComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7420,
            )

            return self._parent._cast(_7420.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7421.WormGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7421,
            )

            return self._parent._cast(_7421.WormGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7424.ZerolBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7424,
            )

            return self._parent._cast(_7424.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "ComponentAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ComponentAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude_of_rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MagnitudeOfRotation

        if temp is None:
            return 0.0

        return temp

    @magnitude_of_rotation.setter
    @enforce_parameter_types
    def magnitude_of_rotation(self: Self, value: "float"):
        self.wrapped.MagnitudeOfRotation = float(value) if value is not None else 0.0

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
    ) -> "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection":
        return self._Cast_ComponentAdvancedSystemDeflection(self)
