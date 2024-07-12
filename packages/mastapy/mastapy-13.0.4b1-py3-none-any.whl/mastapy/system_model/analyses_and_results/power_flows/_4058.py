"""AGMAGleasonConicalGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4086
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "AGMAGleasonConicalGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4065,
        _4067,
        _4068,
        _4070,
        _4119,
        _4158,
        _4164,
        _4167,
        _4169,
        _4170,
        _4186,
        _4115,
        _4133,
        _4078,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearPowerFlow")


class AGMAGleasonConicalGearPowerFlow(_4086.ConicalGearPowerFlow):
    """AGMAGleasonConicalGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearPowerFlow")

    class _Cast_AGMAGleasonConicalGearPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
            parent: "AGMAGleasonConicalGearPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4086.ConicalGearPowerFlow":
            return self._parent._cast(_4086.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4115.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4133.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4078.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4065.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4067.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4068.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4070.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.BevelGearPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4119.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.HypoidGearPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4158.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpiralBevelGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4164.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4167.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4169.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4169

            return self._parent._cast(_4169.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4170.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.StraightBevelSunGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "_4186.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4186

            return self._parent._cast(_4186.ZerolBevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
        ) -> "AGMAGleasonConicalGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearPowerFlow._Cast_AGMAGleasonConicalGearPowerFlow":
        return self._Cast_AGMAGleasonConicalGearPowerFlow(self)
