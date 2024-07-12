"""BevelGearCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BevelGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3802
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3929,
        _3932,
        _3933,
        _4017,
        _4023,
        _4026,
        _4029,
        _4030,
        _4044,
        _3950,
        _3976,
        _3995,
        _3943,
        _3997,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelGearCompoundStabilityAnalysis")


class BevelGearCompoundStabilityAnalysis(
    _3922.AGMAGleasonConicalGearCompoundStabilityAnalysis
):
    """BevelGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearCompoundStabilityAnalysis")

    class _Cast_BevelGearCompoundStabilityAnalysis:
        """Special nested class for casting BevelGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
            parent: "BevelGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3922.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            return self._parent._cast(
                _3922.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3950.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3976.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3995.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3943.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(_3943.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3929.BevelDifferentialGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(
                _3929.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3932.BevelDifferentialPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(
                _3932.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_3933.BevelDifferentialSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(
                _3933.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4017.SpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(_4017.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4023.StraightBevelDiffGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4023,
            )

            return self._parent._cast(
                _4023.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4026.StraightBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4026,
            )

            return self._parent._cast(_4026.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4029.StraightBevelPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4029,
            )

            return self._parent._cast(
                _4029.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4030.StraightBevelSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4030,
            )

            return self._parent._cast(
                _4030.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "_4044.ZerolBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4044,
            )

            return self._parent._cast(_4044.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_compound_stability_analysis(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
        ) -> "BevelGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3802.BevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearStabilityAnalysis]

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
    ) -> "List[_3802.BevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearStabilityAnalysis]

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
    ) -> "BevelGearCompoundStabilityAnalysis._Cast_BevelGearCompoundStabilityAnalysis":
        return self._Cast_BevelGearCompoundStabilityAnalysis(self)
