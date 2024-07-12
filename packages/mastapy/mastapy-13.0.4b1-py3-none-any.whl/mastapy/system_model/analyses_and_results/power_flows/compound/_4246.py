"""GearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "GearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _361
    from mastapy.system_model.analyses_and_results.power_flows import _4115
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4192,
        _4199,
        _4202,
        _4203,
        _4204,
        _4217,
        _4220,
        _4235,
        _4238,
        _4241,
        _4250,
        _4254,
        _4257,
        _4260,
        _4287,
        _4293,
        _4296,
        _4299,
        _4300,
        _4311,
        _4314,
        _4213,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundPowerFlow",)


Self = TypeVar("Self", bound="GearCompoundPowerFlow")


class GearCompoundPowerFlow(_4265.MountableComponentCompoundPowerFlow):
    """GearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundPowerFlow")

    class _Cast_GearCompoundPowerFlow:
        """Special nested class for casting GearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
            parent: "GearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4265.MountableComponentCompoundPowerFlow":
            return self._parent._cast(_4265.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4213.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4192.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4199.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4202.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(
                _4202.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4203.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4204.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.BevelGearCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4217.ConceptGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4220.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.ConicalGearCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4235.CylindricalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(_4235.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4238.CylindricalPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(_4238.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4241.FaceGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.FaceGearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4250.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4254.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(
                _4254.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4257.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(
                _4257.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4260.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4260,
            )

            return self._parent._cast(
                _4260.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4287.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.SpiralBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4293.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4293,
            )

            return self._parent._cast(_4293.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4296.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4296,
            )

            return self._parent._cast(_4296.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4299.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4299,
            )

            return self._parent._cast(_4299.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4300.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4300,
            )

            return self._parent._cast(_4300.StraightBevelSunGearCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4311.WormGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4311,
            )

            return self._parent._cast(_4311.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4314.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4314,
            )

            return self._parent._cast(_4314.ZerolBevelGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "GearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self: Self) -> "_361.GearDutyCycleRating":
        """mastapy.gears.rating.GearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_4115.GearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow]

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
    def component_analysis_cases_ready(self: Self) -> "List[_4115.GearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow]

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
    def cast_to(self: Self) -> "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow":
        return self._Cast_GearCompoundPowerFlow(self)
