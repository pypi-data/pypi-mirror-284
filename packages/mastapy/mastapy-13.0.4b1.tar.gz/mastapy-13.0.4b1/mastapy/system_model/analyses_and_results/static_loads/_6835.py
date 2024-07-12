"""AGMAGleasonConicalGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6866
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6844,
        _6847,
        _6848,
        _6849,
        _6927,
        _6975,
        _6981,
        _6984,
        _6987,
        _6988,
        _7007,
        _6912,
        _6946,
        _6859,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearLoadCase",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearLoadCase")


class AGMAGleasonConicalGearLoadCase(_6866.ConicalGearLoadCase):
    """AGMAGleasonConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearLoadCase")

    class _Cast_AGMAGleasonConicalGearLoadCase:
        """Special nested class for casting AGMAGleasonConicalGearLoadCase to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
            parent: "AGMAGleasonConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6866.ConicalGearLoadCase":
            return self._parent._cast(_6866.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6912.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6946.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6859.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ComponentLoadCase)

        @property
        def part_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6844.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6847.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6848.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6849.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.BevelGearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6927.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.HypoidGearLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6975.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6981.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6984.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6987.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_6988.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.StraightBevelSunGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "_7007.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7007

            return self._parent._cast(_7007.ZerolBevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "AGMAGleasonConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearLoadCase.TYPE"):
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
    ) -> "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase":
        return self._Cast_AGMAGleasonConicalGearLoadCase(self)
