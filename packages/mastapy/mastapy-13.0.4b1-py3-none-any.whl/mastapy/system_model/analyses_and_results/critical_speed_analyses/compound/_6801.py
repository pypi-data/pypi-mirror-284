"""StraightBevelDiffGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6712,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2565
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6672
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6807,
        _6808,
        _6700,
        _6728,
        _6754,
        _6773,
        _6721,
        _6775,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundCriticalSpeedAnalysis")


class StraightBevelDiffGearCompoundCriticalSpeedAnalysis(
    _6712.BevelGearCompoundCriticalSpeedAnalysis
):
    """StraightBevelDiffGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelDiffGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
            parent: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_6712.BevelGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6712.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_6700.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(
                _6700.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_6728.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(_6728.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_6754.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_6773.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_6721.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(_6721.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_6807.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6807,
            )

            return self._parent._cast(
                _6807.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "_6808.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6808,
            )

            return self._parent._cast(
                _6808.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
        ) -> "StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6672.StraightBevelDiffGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelDiffGearCriticalSpeedAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6672.StraightBevelDiffGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelDiffGearCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
        return self._Cast_StraightBevelDiffGearCompoundCriticalSpeedAnalysis(self)
