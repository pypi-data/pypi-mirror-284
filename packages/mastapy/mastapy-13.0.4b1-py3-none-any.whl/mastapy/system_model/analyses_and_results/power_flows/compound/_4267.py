"""PartCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PartCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4135
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4188,
        _4189,
        _4190,
        _4192,
        _4194,
        _4195,
        _4196,
        _4198,
        _4199,
        _4201,
        _4202,
        _4203,
        _4204,
        _4206,
        _4207,
        _4208,
        _4209,
        _4211,
        _4213,
        _4214,
        _4216,
        _4217,
        _4219,
        _4220,
        _4222,
        _4224,
        _4225,
        _4227,
        _4229,
        _4230,
        _4231,
        _4233,
        _4235,
        _4237,
        _4238,
        _4239,
        _4240,
        _4241,
        _4243,
        _4244,
        _4245,
        _4246,
        _4248,
        _4249,
        _4250,
        _4252,
        _4254,
        _4256,
        _4257,
        _4259,
        _4260,
        _4262,
        _4263,
        _4264,
        _4265,
        _4266,
        _4268,
        _4270,
        _4272,
        _4273,
        _4274,
        _4275,
        _4276,
        _4277,
        _4279,
        _4280,
        _4282,
        _4283,
        _4284,
        _4286,
        _4287,
        _4289,
        _4290,
        _4292,
        _4293,
        _4295,
        _4296,
        _4298,
        _4299,
        _4300,
        _4301,
        _4302,
        _4303,
        _4304,
        _4305,
        _4307,
        _4308,
        _4309,
        _4310,
        _4311,
        _4313,
        _4314,
        _4316,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundPowerFlow",)


Self = TypeVar("Self", bound="PartCompoundPowerFlow")


class PartCompoundPowerFlow(_7567.PartCompoundAnalysis):
    """PartCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundPowerFlow")

    class _Cast_PartCompoundPowerFlow:
        """Special nested class for casting PartCompoundPowerFlow to subclasses."""

        def __init__(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
            parent: "PartCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4188.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.AbstractAssemblyCompoundPowerFlow)

        @property
        def abstract_shaft_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4189.AbstractShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4190.AbstractShaftOrHousingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4192.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4194.AGMAGleasonConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def assembly_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4195.AssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.AssemblyCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4196.BearingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.BearingCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4198.BeltDriveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4199.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4201.BevelDifferentialGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4202.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(
                _4202.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4203.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4204.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.BevelGearCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4206.BevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.BevelGearSetCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4207.BoltCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4207,
            )

            return self._parent._cast(_4207.BoltCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4208.BoltedJointCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4209.ClutchCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4209,
            )

            return self._parent._cast(_4209.ClutchCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4211.ClutchHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4211,
            )

            return self._parent._cast(_4211.ClutchHalfCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4213.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.ComponentCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4214.ConceptCouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4216.ConceptCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4217.ConceptGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.ConceptGearCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4219.ConceptGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4220.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.ConicalGearCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4222.ConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.ConicalGearSetCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4224.ConnectorCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.ConnectorCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4225.CouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.CouplingCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4227.CouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4229.CVTCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(_4229.CVTCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4230.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(_4230.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4231.CycloidalAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(_4231.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4233.CycloidalDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(_4233.CycloidalDiscCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4235.CylindricalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(_4235.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4237.CylindricalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(_4237.CylindricalGearSetCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4238.CylindricalPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(_4238.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4239.DatumCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(_4239.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4240.ExternalCADModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(_4240.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4241.FaceGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.FaceGearCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4243.FaceGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.FaceGearSetCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4244.FEPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.FEPartCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4245.FlexiblePinAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4246.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.GearCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4248.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.GearSetCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4249.GuideDxfModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(_4249.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4250.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.HypoidGearCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4252.HypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4254.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(
                _4254.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4256.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(
                _4256.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4257.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(
                _4257.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4259.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(
                _4259.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4260.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4260,
            )

            return self._parent._cast(
                _4260.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4262.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(
                _4262.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4263.MassDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4264.MeasurementComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4265.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4266.OilSealCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.OilSealCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4268.PartToPartShearCouplingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4270.PartToPartShearCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(
                _4270.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planetary_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4272.PlanetaryGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(_4272.PlanetaryGearSetCompoundPowerFlow)

        @property
        def planet_carrier_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4273.PlanetCarrierCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4274.PointLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4275.PowerLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4276.PulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4277.RingPinsCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4279.RollingRingAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.RollingRingAssemblyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4280.RollingRingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.RollingRingCompoundPowerFlow)

        @property
        def root_assembly_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4282.RootAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.RootAssemblyCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4283.ShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4284.ShaftHubConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.ShaftHubConnectionCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4286.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4287.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.SpiralBevelGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4289.SpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4290.SpringDamperCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.SpringDamperCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4292.SpringDamperHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4293.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4293,
            )

            return self._parent._cast(_4293.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4295.StraightBevelDiffGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4296.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4296,
            )

            return self._parent._cast(_4296.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4298.StraightBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4298,
            )

            return self._parent._cast(_4298.StraightBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4299.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4299,
            )

            return self._parent._cast(_4299.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4300.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4300,
            )

            return self._parent._cast(_4300.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4301.SynchroniserCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4301,
            )

            return self._parent._cast(_4301.SynchroniserCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4302.SynchroniserHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4302,
            )

            return self._parent._cast(_4302.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4303.SynchroniserPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4303,
            )

            return self._parent._cast(_4303.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4304.SynchroniserSleeveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4304,
            )

            return self._parent._cast(_4304.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4305.TorqueConverterCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4305,
            )

            return self._parent._cast(_4305.TorqueConverterCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4307.TorqueConverterPumpCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4307,
            )

            return self._parent._cast(_4307.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4308.TorqueConverterTurbineCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4308,
            )

            return self._parent._cast(_4308.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4309.UnbalancedMassCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4309,
            )

            return self._parent._cast(_4309.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4310.VirtualComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4310,
            )

            return self._parent._cast(_4310.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4311.WormGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4311,
            )

            return self._parent._cast(_4311.WormGearCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4313.WormGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4313,
            )

            return self._parent._cast(_4313.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4314.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4314,
            )

            return self._parent._cast(_4314.ZerolBevelGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "_4316.ZerolBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4316,
            )

            return self._parent._cast(_4316.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow",
        ) -> "PartCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4135.PartPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PartPowerFlow]

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
    def component_analysis_cases_ready(self: Self) -> "List[_4135.PartPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PartPowerFlow]

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
    def cast_to(self: Self) -> "PartCompoundPowerFlow._Cast_PartCompoundPowerFlow":
        return self._Cast_PartCompoundPowerFlow(self)
