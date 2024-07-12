"""GearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4133
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "GearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4058,
        _4065,
        _4067,
        _4068,
        _4070,
        _4083,
        _4086,
        _4102,
        _4104,
        _4108,
        _4119,
        _4123,
        _4126,
        _4129,
        _4158,
        _4164,
        _4167,
        _4169,
        _4170,
        _4183,
        _4186,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearPowerFlow",)


Self = TypeVar("Self", bound="GearPowerFlow")


class GearPowerFlow(_4133.MountableComponentPowerFlow):
    """GearPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearPowerFlow")

    class _Cast_GearPowerFlow:
        """Special nested class for casting GearPowerFlow to subclasses."""

        def __init__(
            self: "GearPowerFlow._Cast_GearPowerFlow", parent: "GearPowerFlow"
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4058.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.AGMAGleasonConicalGearPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4065.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4067.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4068.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4070.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.BevelGearPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4083.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.ConceptGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4086.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.ConicalGearPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4102.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.CylindricalGearPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4104.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(_4104.CylindricalPlanetGearPowerFlow)

        @property
        def face_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4108.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.FaceGearPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4119.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4123.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(
                _4123.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4126.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(_4126.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4129.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(
                _4129.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def spiral_bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4158.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpiralBevelGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4164.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4167.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4169.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4169

            return self._parent._cast(_4169.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4170.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.StraightBevelSunGearPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4183.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4183

            return self._parent._cast(_4183.WormGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4186.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4186

            return self._parent._cast(_4186.ZerolBevelGearPowerFlow)

        @property
        def gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "GearPowerFlow":
            return self._parent

        def __getattr__(self: "GearPowerFlow._Cast_GearPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def component_design(self: Self) -> "_2550.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearPowerFlow._Cast_GearPowerFlow":
        return self._Cast_GearPowerFlow(self)
