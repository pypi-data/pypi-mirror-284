"""BevelDifferentialSunGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "BevelDifferentialSunGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5916,
        _5904,
        _5932,
        _5958,
        _5977,
        _5925,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundHarmonicAnalysis")


class BevelDifferentialSunGearCompoundHarmonicAnalysis(
    _5911.BevelDifferentialGearCompoundHarmonicAnalysis
):
    """BevelDifferentialSunGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
            parent: "BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_5911.BevelDifferentialGearCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5911.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_5916.BevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5916,
            )

            return self._parent._cast(_5916.BevelGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_5904.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(
                _5904.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_5932.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5932,
            )

            return self._parent._cast(_5932.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_5958.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_5977.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_5925.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(_5925.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
        ) -> "BevelDifferentialSunGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5715.BevelDifferentialSunGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialSunGearHarmonicAnalysis]

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
    ) -> "List[_5715.BevelDifferentialSunGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialSunGearHarmonicAnalysis]

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
    ) -> "BevelDifferentialSunGearCompoundHarmonicAnalysis._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis":
        return self._Cast_BevelDifferentialSunGearCompoundHarmonicAnalysis(self)
