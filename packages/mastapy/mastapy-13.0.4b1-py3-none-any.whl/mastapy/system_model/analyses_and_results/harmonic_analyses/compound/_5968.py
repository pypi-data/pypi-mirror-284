"""KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5934
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5798
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5971,
        _5974,
        _5960,
        _5998,
        _5900,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis(
    _5934.ConicalGearSetCompoundHarmonicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5934.ConicalGearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5934.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5960.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5998.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5998,
            )

            return self._parent._cast(_5998.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5900.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5900,
            )

            return self._parent._cast(_5900.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5971.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5971,
            )

            return self._parent._cast(
                _5971.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5974.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(
                _5974.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5798.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis]

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
    ) -> "List[_5798.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis(
                self
            )
        )
