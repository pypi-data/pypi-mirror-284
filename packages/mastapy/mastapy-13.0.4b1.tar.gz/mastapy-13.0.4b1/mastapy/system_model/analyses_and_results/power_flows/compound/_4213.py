"""ComponentCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4267
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4078
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4189,
        _4190,
        _4192,
        _4196,
        _4199,
        _4202,
        _4203,
        _4204,
        _4207,
        _4211,
        _4216,
        _4217,
        _4220,
        _4224,
        _4227,
        _4230,
        _4233,
        _4235,
        _4238,
        _4239,
        _4240,
        _4241,
        _4244,
        _4246,
        _4249,
        _4250,
        _4254,
        _4257,
        _4260,
        _4263,
        _4264,
        _4265,
        _4266,
        _4270,
        _4273,
        _4274,
        _4275,
        _4276,
        _4277,
        _4280,
        _4283,
        _4284,
        _4287,
        _4292,
        _4293,
        _4296,
        _4299,
        _4300,
        _4302,
        _4303,
        _4304,
        _4307,
        _4308,
        _4309,
        _4310,
        _4311,
        _4314,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="ComponentCompoundPowerFlow")


class ComponentCompoundPowerFlow(_4267.PartCompoundPowerFlow):
    """ComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundPowerFlow")

    class _Cast_ComponentCompoundPowerFlow:
        """Special nested class for casting ComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
            parent: "ComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4189.AbstractShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4190.AbstractShaftOrHousingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4192.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4196.BearingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.BearingCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4199.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4202.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(
                _4202.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4203.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4204.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.BevelGearCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4207.BoltCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4207,
            )

            return self._parent._cast(_4207.BoltCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4211.ClutchHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4211,
            )

            return self._parent._cast(_4211.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4216.ConceptCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4217.ConceptGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4220.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.ConicalGearCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4224.ConnectorCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.ConnectorCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4227.CouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4230.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(_4230.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4233.CycloidalDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(_4233.CycloidalDiscCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4235.CylindricalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(_4235.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4238.CylindricalPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(_4238.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4239.DatumCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(_4239.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4240.ExternalCADModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(_4240.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4241.FaceGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.FaceGearCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4244.FEPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.FEPartCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4246.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.GearCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4249.GuideDxfModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(_4249.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4250.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4254.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(
                _4254.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4257.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(
                _4257.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4260.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4260,
            )

            return self._parent._cast(
                _4260.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4263.MassDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4264.MeasurementComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4265.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4266.OilSealCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.OilSealCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4270.PartToPartShearCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(
                _4270.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planet_carrier_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4273.PlanetCarrierCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4274.PointLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4275.PowerLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4276.PulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4277.RingPinsCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4280.RollingRingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.RollingRingCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4283.ShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4284.ShaftHubConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.ShaftHubConnectionCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4287.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.SpiralBevelGearCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4292.SpringDamperHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4293.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4293,
            )

            return self._parent._cast(_4293.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4296.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4296,
            )

            return self._parent._cast(_4296.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4299.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4299,
            )

            return self._parent._cast(_4299.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4300.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4300,
            )

            return self._parent._cast(_4300.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4302.SynchroniserHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4302,
            )

            return self._parent._cast(_4302.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4303.SynchroniserPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4303,
            )

            return self._parent._cast(_4303.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4304.SynchroniserSleeveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4304,
            )

            return self._parent._cast(_4304.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4307.TorqueConverterPumpCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4307,
            )

            return self._parent._cast(_4307.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4308.TorqueConverterTurbineCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4308,
            )

            return self._parent._cast(_4308.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4309.UnbalancedMassCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4309,
            )

            return self._parent._cast(_4309.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4310.VirtualComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4310,
            )

            return self._parent._cast(_4310.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4311.WormGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4311,
            )

            return self._parent._cast(_4311.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4314.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4314,
            )

            return self._parent._cast(_4314.ZerolBevelGearCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "ComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4078.ComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow]

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
    def component_analysis_cases_ready(self: Self) -> "List[_4078.ComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow]

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
    ) -> "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow":
        return self._Cast_ComponentCompoundPowerFlow(self)
