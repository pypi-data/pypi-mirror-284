"""SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6275,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2625
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6144,
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
__all__ = ("SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation"
)


class SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation(
    _6275.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
):
    """SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6275.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6275.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6199.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6237.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6185.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2625.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "List[_6144.SynchroniserHalfHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SynchroniserHalfHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6144.SynchroniserHalfHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SynchroniserHalfHarmonicAnalysisOfSingleExcitation]

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
    ) -> "SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
