"""StraightBevelSunGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6801,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "StraightBevelSunGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6679
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6712,
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
__all__ = ("StraightBevelSunGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundCriticalSpeedAnalysis")


class StraightBevelSunGearCompoundCriticalSpeedAnalysis(
    _6801.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
):
    """StraightBevelSunGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelSunGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
            parent: "StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6801.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6801.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6712.BevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6712,
            )

            return self._parent._cast(_6712.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6700.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(
                _6700.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6728.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(_6728.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6754.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6773.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6721.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(_6721.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
        ) -> "StraightBevelSunGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "StraightBevelSunGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6679.StraightBevelSunGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelSunGearCriticalSpeedAnalysis]

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
    ) -> "List[_6679.StraightBevelSunGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelSunGearCriticalSpeedAnalysis]

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
    ) -> "StraightBevelSunGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis":
        return self._Cast_StraightBevelSunGearCompoundCriticalSpeedAnalysis(self)
