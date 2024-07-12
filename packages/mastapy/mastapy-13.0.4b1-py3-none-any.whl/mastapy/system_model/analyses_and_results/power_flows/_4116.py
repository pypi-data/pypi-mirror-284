"""GearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4156
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "GearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.gears.rating import _366
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4115,
        _4114,
        _4059,
        _4066,
        _4071,
        _4084,
        _4087,
        _4103,
        _4109,
        _4120,
        _4124,
        _4127,
        _4130,
        _4140,
        _4159,
        _4165,
        _4168,
        _4184,
        _4187,
        _4053,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearSetPowerFlow",)


Self = TypeVar("Self", bound="GearSetPowerFlow")


class GearSetPowerFlow(_4156.SpecialisedAssemblyPowerFlow):
    """GearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetPowerFlow")

    class _Cast_GearSetPowerFlow:
        """Special nested class for casting GearSetPowerFlow to subclasses."""

        def __init__(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow", parent: "GearSetPowerFlow"
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4156.SpecialisedAssemblyPowerFlow":
            return self._parent._cast(_4156.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4053.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4059.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4066.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4071.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.BevelGearSetPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4084.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.ConceptGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4087.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.ConicalGearSetPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4103.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.CylindricalGearSetPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4109.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.FaceGearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4120.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4124.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(
                _4124.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4127.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(
                _4127.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4130.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(
                _4130.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def planetary_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4140.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.PlanetaryGearSetPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4159.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4165.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4168.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4168

            return self._parent._cast(_4168.StraightBevelGearSetPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4184.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4184

            return self._parent._cast(_4184.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4187.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4187

            return self._parent._cast(_4187.ZerolBevelGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "GearSetPowerFlow":
            return self._parent

        def __getattr__(self: "GearSetPowerFlow._Cast_GearSetPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2552.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_366.GearSetRating":
        """mastapy.gears.rating.GearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4115.GearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(self: Self) -> "List[_4114.GearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def set_face_widths_for_specified_safety_factors(self: Self):
        """Method does not return."""
        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()

    @property
    def cast_to(self: Self) -> "GearSetPowerFlow._Cast_GearSetPowerFlow":
        return self._Cast_GearSetPowerFlow(self)
