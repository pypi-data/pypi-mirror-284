"""BevelGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2876
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BevelGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2729
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2883,
        _2886,
        _2887,
        _2973,
        _2979,
        _2982,
        _2985,
        _2986,
        _3000,
        _2904,
        _2931,
        _2950,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearCompoundSystemDeflection")


class BevelGearCompoundSystemDeflection(
    _2876.AGMAGleasonConicalGearCompoundSystemDeflection
):
    """BevelGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearCompoundSystemDeflection")

    class _Cast_BevelGearCompoundSystemDeflection:
        """Special nested class for casting BevelGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
            parent: "BevelGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2876.AGMAGleasonConicalGearCompoundSystemDeflection":
            return self._parent._cast(
                _2876.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2904.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2931.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2883.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(
                _2883.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2886.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(
                _2886.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2887.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(
                _2887.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2973.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(_2973.SpiralBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2979.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2979,
            )

            return self._parent._cast(
                _2979.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2982.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2982,
            )

            return self._parent._cast(_2982.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2985.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2985,
            )

            return self._parent._cast(
                _2985.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_2986.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2986,
            )

            return self._parent._cast(
                _2986.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "_3000.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3000,
            )

            return self._parent._cast(_3000.ZerolBevelGearCompoundSystemDeflection)

        @property
        def bevel_gear_compound_system_deflection(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
        ) -> "BevelGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "BevelGearCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_2729.BevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2729.BevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearCompoundSystemDeflection._Cast_BevelGearCompoundSystemDeflection":
        return self._Cast_BevelGearCompoundSystemDeflection(self)
