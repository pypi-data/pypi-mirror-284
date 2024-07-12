"""PartPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7569
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PartPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2488
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4143,
        _4053,
        _4054,
        _4055,
        _4058,
        _4059,
        _4060,
        _4061,
        _4063,
        _4065,
        _4066,
        _4067,
        _4068,
        _4070,
        _4071,
        _4072,
        _4073,
        _4075,
        _4076,
        _4078,
        _4080,
        _4081,
        _4083,
        _4084,
        _4086,
        _4087,
        _4089,
        _4091,
        _4092,
        _4094,
        _4095,
        _4096,
        _4099,
        _4102,
        _4103,
        _4104,
        _4105,
        _4106,
        _4108,
        _4109,
        _4112,
        _4113,
        _4115,
        _4116,
        _4117,
        _4119,
        _4120,
        _4123,
        _4124,
        _4126,
        _4127,
        _4129,
        _4130,
        _4131,
        _4132,
        _4133,
        _4134,
        _4137,
        _4138,
        _4140,
        _4141,
        _4142,
        _4145,
        _4146,
        _4147,
        _4149,
        _4151,
        _4152,
        _4153,
        _4154,
        _4156,
        _4158,
        _4159,
        _4161,
        _4162,
        _4164,
        _4165,
        _4167,
        _4168,
        _4169,
        _4170,
        _4171,
        _4172,
        _4173,
        _4174,
        _4177,
        _4178,
        _4179,
        _4180,
        _4181,
        _4183,
        _4184,
        _4186,
        _4187,
    )
    from mastapy.system_model.drawing import _2274
    from mastapy.system_model.analyses_and_results.analysis_cases import _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartPowerFlow",)


Self = TypeVar("Self", bound="PartPowerFlow")


class PartPowerFlow(_7569.PartStaticLoadAnalysisCase):
    """PartPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartPowerFlow")

    class _Cast_PartPowerFlow:
        """Special nested class for casting PartPowerFlow to subclasses."""

        def __init__(
            self: "PartPowerFlow._Cast_PartPowerFlow", parent: "PartPowerFlow"
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4053.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4054.AbstractShaftOrHousingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4055.AbstractShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4058.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4059.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4060.AssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.AssemblyPowerFlow)

        @property
        def bearing_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4061.BearingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.BearingPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4063.BeltDrivePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4065.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4066.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4067.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4068.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4070.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4071.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4072.BoltedJointPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4073.BoltPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.BoltPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4075.ClutchHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4076.ClutchPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(_4076.ClutchPowerFlow)

        @property
        def component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4080.ConceptCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4081.ConceptCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4083.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4084.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4086.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4087.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4089.ConnectorPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4091.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4092.CouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.CouplingPowerFlow)

        @property
        def cvt_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4094.CVTPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4095.CVTPulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4096.CycloidalAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4099.CycloidalDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(_4099.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4102.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4103.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4104.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(_4104.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4105.DatumPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(_4105.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4106.ExternalCADModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(_4106.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4108.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4109.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4112.FEPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4113.FlexiblePinAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4115.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.GearPowerFlow)

        @property
        def gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4116.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4117.GuideDxfModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4119.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4120.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4123.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(
                _4123.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4124.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(
                _4124.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4126.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(_4126.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4127.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(
                _4127.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4129.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(
                _4129.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4130.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(
                _4130.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4131.MassDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(_4131.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4132.MeasurementComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4134.OilSealPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4137.PartToPartShearCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4138.PartToPartShearCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4140.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4141.PlanetCarrierPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4142.PointLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4145.PowerLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4146.PulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4147.RingPinsPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4149.RollingRingAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4151.RollingRingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4152.RootAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4153.ShaftHubConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4154.ShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4156.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4158.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4159.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4161.SpringDamperHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4162.SpringDamperPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4164.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4165.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4167.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4168.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4168

            return self._parent._cast(_4168.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4169.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4169

            return self._parent._cast(_4169.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4170.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4171.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4172.SynchroniserPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4172

            return self._parent._cast(_4172.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4173.SynchroniserPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4173

            return self._parent._cast(_4173.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4174.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4174

            return self._parent._cast(_4174.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4177.TorqueConverterPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4177

            return self._parent._cast(_4177.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4178.TorqueConverterPumpPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4178

            return self._parent._cast(_4178.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4179.TorqueConverterTurbinePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4179

            return self._parent._cast(_4179.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4180.UnbalancedMassPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4180

            return self._parent._cast(_4180.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4181.VirtualComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4181

            return self._parent._cast(_4181.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4183.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4183

            return self._parent._cast(_4183.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4184.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4184

            return self._parent._cast(_4184.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4186.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4186

            return self._parent._cast(_4186.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4187.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4187

            return self._parent._cast(_4187.ZerolBevelGearSetPowerFlow)

        @property
        def part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "PartPowerFlow":
            return self._parent

        def __getattr__(self: "PartPowerFlow._Cast_PartPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_power_flow(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

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
    def power_flow(self: Self) -> "_4143.PowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2274.PowerFlowViewable":
        """mastapy.system_model.drawing.PowerFlowViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartPowerFlow._Cast_PartPowerFlow":
        return self._Cast_PartPowerFlow(self)
