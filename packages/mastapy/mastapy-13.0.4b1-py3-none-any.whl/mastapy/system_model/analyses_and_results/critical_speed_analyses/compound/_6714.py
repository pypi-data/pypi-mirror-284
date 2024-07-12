"""BevelGearSetCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6702,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6582
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6709,
        _6797,
        _6803,
        _6806,
        _6824,
        _6730,
        _6756,
        _6794,
        _6696,
        _6775,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetCompoundCriticalSpeedAnalysis")


class BevelGearSetCompoundCriticalSpeedAnalysis(
    _6702.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
):
    """BevelGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetCompoundCriticalSpeedAnalysis"
    )

    class _Cast_BevelGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
            parent: "BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6702.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6702.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6730.ConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6756.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(_6756.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6696.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(
                _6696.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6709.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(
                _6709.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6797.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(
                _6797.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6803.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6803,
            )

            return self._parent._cast(
                _6803.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6806.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6806,
            )

            return self._parent._cast(
                _6806.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6824.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6824,
            )

            return self._parent._cast(
                _6824.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "BevelGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearSetCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6582.BevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelGearSetCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6582.BevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelGearSetCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelGearSetCompoundCriticalSpeedAnalysis(self)
