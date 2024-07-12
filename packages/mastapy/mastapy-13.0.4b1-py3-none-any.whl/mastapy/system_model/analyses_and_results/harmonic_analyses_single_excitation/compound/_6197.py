"""CouplingCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6258,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CouplingCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6068,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6181,
        _6186,
        _6240,
        _6262,
        _6277,
        _6160,
        _6239,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CouplingCompoundHarmonicAnalysisOfSingleExcitation")


class CouplingCompoundHarmonicAnalysisOfSingleExcitation(
    _6258.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
):
    """CouplingCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6258.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6258.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6160.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6160,
            )

            return self._parent._cast(
                _6160.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6181.ClutchCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6181,
            )

            return self._parent._cast(
                _6181.ClutchCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6186.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6186,
            )

            return self._parent._cast(
                _6186.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6240.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6240,
            )

            return self._parent._cast(
                _6240.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6262.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6262,
            )

            return self._parent._cast(
                _6262.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6277.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6277,
            )

            return self._parent._cast(
                _6277.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CouplingCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CouplingCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6068.CouplingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CouplingHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6068.CouplingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CouplingHarmonicAnalysisOfSingleExcitation]

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
    ) -> "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation(self)
