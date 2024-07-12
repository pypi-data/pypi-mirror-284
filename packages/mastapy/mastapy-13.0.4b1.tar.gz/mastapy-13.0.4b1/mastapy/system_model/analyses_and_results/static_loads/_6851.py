"""BevelGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6846,
        _6977,
        _6983,
        _6986,
        _7009,
        _6870,
        _6917,
        _6974,
        _6828,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetLoadCase",)


Self = TypeVar("Self", bound="BevelGearSetLoadCase")


class BevelGearSetLoadCase(_6837.AGMAGleasonConicalGearSetLoadCase):
    """BevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetLoadCase")

    class _Cast_BevelGearSetLoadCase:
        """Special nested class for casting BevelGearSetLoadCase to subclasses."""

        def __init__(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
            parent: "BevelGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6837.AGMAGleasonConicalGearSetLoadCase":
            return self._parent._cast(_6837.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6870.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6870

            return self._parent._cast(_6870.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6917.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(_6917.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6974.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6828.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6846.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.BevelDifferentialGearSetLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6977.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6977

            return self._parent._cast(_6977.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6983.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6986.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.StraightBevelGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_7009.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7009

            return self._parent._cast(_7009.ZerolBevelGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "BevelGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2540.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase":
        return self._Cast_BevelGearSetLoadCase(self)
