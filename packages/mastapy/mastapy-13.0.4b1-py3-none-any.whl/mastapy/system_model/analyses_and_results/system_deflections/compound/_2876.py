"""AGMAGleasonConicalGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2904
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AGMAGleasonConicalGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2712
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2883,
        _2886,
        _2887,
        _2888,
        _2935,
        _2973,
        _2979,
        _2982,
        _2985,
        _2986,
        _3000,
        _2931,
        _2950,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundSystemDeflection")


class AGMAGleasonConicalGearCompoundSystemDeflection(
    _2904.ConicalGearCompoundSystemDeflection
):
    """AGMAGleasonConicalGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearCompoundSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
            parent: "AGMAGleasonConicalGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2904.ConicalGearCompoundSystemDeflection":
            return self._parent._cast(_2904.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2931.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2883.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(
                _2883.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2886.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(
                _2886.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2887.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(
                _2887.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2888.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.BevelGearCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2935.HypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.HypoidGearCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2973.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(_2973.SpiralBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2979.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2979,
            )

            return self._parent._cast(
                _2979.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2982.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2982,
            )

            return self._parent._cast(_2982.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2985.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2985,
            )

            return self._parent._cast(
                _2985.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_2986.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2986,
            )

            return self._parent._cast(
                _2986.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "_3000.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3000,
            )

            return self._parent._cast(_3000.ZerolBevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
        ) -> "AGMAGleasonConicalGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection",
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
        self: Self,
        instance_to_wrap: "AGMAGleasonConicalGearCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2712.AGMAGleasonConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection]

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
    ) -> "List[_2712.AGMAGleasonConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection]

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
    ) -> "AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearCompoundSystemDeflection(self)
