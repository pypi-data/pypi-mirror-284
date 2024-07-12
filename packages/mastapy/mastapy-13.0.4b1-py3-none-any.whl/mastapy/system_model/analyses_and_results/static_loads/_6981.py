"""StraightBevelDiffGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6849
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2565
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6987,
        _6988,
        _6835,
        _6866,
        _6912,
        _6946,
        _6859,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearLoadCase",)


Self = TypeVar("Self", bound="StraightBevelDiffGearLoadCase")


class StraightBevelDiffGearLoadCase(_6849.BevelGearLoadCase):
    """StraightBevelDiffGearLoadCase

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearLoadCase")

    class _Cast_StraightBevelDiffGearLoadCase:
        """Special nested class for casting StraightBevelDiffGearLoadCase to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
            parent: "StraightBevelDiffGearLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6849.BevelGearLoadCase":
            return self._parent._cast(_6849.BevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6835.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6866.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6912.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6946.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6859.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ComponentLoadCase)

        @property
        def part_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6987.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "_6988.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.StraightBevelSunGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
        ) -> "StraightBevelDiffGearLoadCase":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2565.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

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
    ) -> "StraightBevelDiffGearLoadCase._Cast_StraightBevelDiffGearLoadCase":
        return self._Cast_StraightBevelDiffGearLoadCase(self)
