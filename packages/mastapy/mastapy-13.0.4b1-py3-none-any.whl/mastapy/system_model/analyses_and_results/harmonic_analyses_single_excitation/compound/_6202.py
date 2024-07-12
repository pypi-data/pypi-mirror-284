"""CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6248,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6071,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6199,
        _6237,
        _6185,
        _6239,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation")


class CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation(
    _6248.PulleyCompoundHarmonicAnalysisOfSingleExcitation
):
    """CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6248.PulleyCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6248.PulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6199.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6237.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6185.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6071.CVTPulleyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CVTPulleyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6071.CVTPulleyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CVTPulleyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation(self)
