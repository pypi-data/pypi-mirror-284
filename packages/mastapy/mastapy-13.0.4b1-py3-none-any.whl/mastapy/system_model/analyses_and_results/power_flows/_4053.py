"""AbstractAssemblyPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "AbstractAssemblyPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4059,
        _4060,
        _4063,
        _4066,
        _4071,
        _4072,
        _4076,
        _4081,
        _4084,
        _4087,
        _4092,
        _4094,
        _4096,
        _4103,
        _4109,
        _4113,
        _4116,
        _4120,
        _4124,
        _4127,
        _4130,
        _4138,
        _4140,
        _4149,
        _4152,
        _4156,
        _4159,
        _4162,
        _4165,
        _4168,
        _4173,
        _4177,
        _4184,
        _4187,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyPowerFlow",)


Self = TypeVar("Self", bound="AbstractAssemblyPowerFlow")


class AbstractAssemblyPowerFlow(_4135.PartPowerFlow):
    """AbstractAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyPowerFlow")

    class _Cast_AbstractAssemblyPowerFlow:
        """Special nested class for casting AbstractAssemblyPowerFlow to subclasses."""

        def __init__(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
            parent: "AbstractAssemblyPowerFlow",
        ):
            self._parent = parent

        @property
        def part_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4135.PartPowerFlow":
            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4059.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4060.AssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.AssemblyPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4063.BeltDrivePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4066.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4071.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4072.BoltedJointPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.BoltedJointPowerFlow)

        @property
        def clutch_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4076.ClutchPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(_4076.ClutchPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4081.ConceptCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.ConceptCouplingPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4084.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.ConceptGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4087.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.ConicalGearSetPowerFlow)

        @property
        def coupling_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4092.CouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.CouplingPowerFlow)

        @property
        def cvt_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4094.CVTPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.CVTPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4096.CycloidalAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.CycloidalAssemblyPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4103.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.CylindricalGearSetPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4109.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.FaceGearSetPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4113.FlexiblePinAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4116.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.GearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4120.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4124.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(
                _4124.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4127.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(
                _4127.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4130.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(
                _4130.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4138.PartToPartShearCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4140.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.PlanetaryGearSetPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4149.RollingRingAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.RollingRingAssemblyPowerFlow)

        @property
        def root_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4152.RootAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.RootAssemblyPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4156.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4159.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4162.SpringDamperPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4165.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4168.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4168

            return self._parent._cast(_4168.StraightBevelGearSetPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4173.SynchroniserPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4173

            return self._parent._cast(_4173.SynchroniserPowerFlow)

        @property
        def torque_converter_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4177.TorqueConverterPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4177

            return self._parent._cast(_4177.TorqueConverterPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4184.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4184

            return self._parent._cast(_4184.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4187.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4187

            return self._parent._cast(_4187.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "AbstractAssemblyPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2454.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow":
        return self._Cast_AbstractAssemblyPowerFlow(self)
