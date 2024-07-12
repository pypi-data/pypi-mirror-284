"""ConicalGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6917
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6869,
        _6837,
        _6846,
        _6851,
        _6929,
        _6936,
        _6939,
        _6942,
        _6977,
        _6983,
        _6986,
        _7009,
        _6974,
        _6828,
        _6950,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetLoadCase",)


Self = TypeVar("Self", bound="ConicalGearSetLoadCase")


class ConicalGearSetLoadCase(_6917.GearSetLoadCase):
    """ConicalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetLoadCase")

    class _Cast_ConicalGearSetLoadCase:
        """Special nested class for casting ConicalGearSetLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
            parent: "ConicalGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6917.GearSetLoadCase":
            return self._parent._cast(_6917.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6974.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6828.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6950.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.PartLoadCase)

        @property
        def part_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6837.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.AGMAGleasonConicalGearSetLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6846.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6851.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.BevelGearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6929.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6936.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6936

            return self._parent._cast(
                _6936.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6939.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(
                _6939.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6942.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(
                _6942.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def spiral_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6977.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6977

            return self._parent._cast(_6977.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6983.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6986.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.StraightBevelGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_7009.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7009

            return self._parent._cast(_7009.ZerolBevelGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "ConicalGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6869.ConicalGearSetHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase":
        return self._Cast_ConicalGearSetLoadCase(self)
