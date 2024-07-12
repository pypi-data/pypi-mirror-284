"""MountableComponentPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4078
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "MountableComponentPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4058,
        _4061,
        _4065,
        _4067,
        _4068,
        _4070,
        _4075,
        _4080,
        _4083,
        _4086,
        _4089,
        _4091,
        _4095,
        _4102,
        _4104,
        _4108,
        _4115,
        _4119,
        _4123,
        _4126,
        _4129,
        _4131,
        _4132,
        _4134,
        _4137,
        _4141,
        _4142,
        _4145,
        _4146,
        _4147,
        _4151,
        _4153,
        _4158,
        _4161,
        _4164,
        _4167,
        _4169,
        _4170,
        _4171,
        _4172,
        _4174,
        _4178,
        _4179,
        _4180,
        _4181,
        _4183,
        _4186,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentPowerFlow",)


Self = TypeVar("Self", bound="MountableComponentPowerFlow")


class MountableComponentPowerFlow(_4078.ComponentPowerFlow):
    """MountableComponentPowerFlow

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentPowerFlow")

    class _Cast_MountableComponentPowerFlow:
        """Special nested class for casting MountableComponentPowerFlow to subclasses."""

        def __init__(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
            parent: "MountableComponentPowerFlow",
        ):
            self._parent = parent

        @property
        def component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4058.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.AGMAGleasonConicalGearPowerFlow)

        @property
        def bearing_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4061.BearingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.BearingPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4065.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4067.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4068.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4070.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.BevelGearPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4075.ClutchHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.ClutchHalfPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4080.ConceptCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ConceptCouplingHalfPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4083.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.ConceptGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4086.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.ConicalGearPowerFlow)

        @property
        def connector_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4089.ConnectorPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4091.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.CouplingHalfPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4095.CVTPulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.CVTPulleyPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4102.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.CylindricalGearPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4104.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(_4104.CylindricalPlanetGearPowerFlow)

        @property
        def face_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4108.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.FaceGearPowerFlow)

        @property
        def gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4115.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.GearPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4119.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4123.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(
                _4123.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4126.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(_4126.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4129.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(
                _4129.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4131.MassDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(_4131.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4132.MeasurementComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.MeasurementComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4134.OilSealPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4137.PartToPartShearCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartToPartShearCouplingHalfPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4141.PlanetCarrierPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4142.PointLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4145.PowerLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4146.PulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4147.RingPinsPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.RingPinsPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4151.RollingRingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.RollingRingPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4153.ShaftHubConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.ShaftHubConnectionPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4158.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpiralBevelGearPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4161.SpringDamperHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.SpringDamperHalfPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4164.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4167.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4169.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4169

            return self._parent._cast(_4169.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4170.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4171.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4172.SynchroniserPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4172

            return self._parent._cast(_4172.SynchroniserPartPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4174.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4174

            return self._parent._cast(_4174.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4178.TorqueConverterPumpPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4178

            return self._parent._cast(_4178.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4179.TorqueConverterTurbinePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4179

            return self._parent._cast(_4179.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4180.UnbalancedMassPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4180

            return self._parent._cast(_4180.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4181.VirtualComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4181

            return self._parent._cast(_4181.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4183.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4183

            return self._parent._cast(_4183.WormGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4186.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4186

            return self._parent._cast(_4186.ZerolBevelGearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "MountableComponentPowerFlow":
            return self._parent

        def __getattr__(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

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
    ) -> "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow":
        return self._Cast_MountableComponentPowerFlow(self)
