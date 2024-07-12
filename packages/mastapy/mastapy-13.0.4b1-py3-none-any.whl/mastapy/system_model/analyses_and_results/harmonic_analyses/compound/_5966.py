"""KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5932
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5796
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5969,
        _5972,
        _5958,
        _5977,
        _5925,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis"
)


class KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis(
    _5932.ConicalGearCompoundHarmonicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "_5932.ConicalGearCompoundHarmonicAnalysis":
            return self._parent._cast(_5932.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "_5958.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "_5977.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "_5925.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(_5925.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "_5969.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5969,
            )

            return self._parent._cast(
                _5969.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "_5972.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5972,
            )

            return self._parent._cast(
                _5972.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5796.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis]

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
    ) -> "List[_5796.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis(
            self
        )
