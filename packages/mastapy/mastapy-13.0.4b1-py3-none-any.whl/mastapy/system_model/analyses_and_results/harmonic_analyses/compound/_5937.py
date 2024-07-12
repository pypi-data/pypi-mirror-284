"""CouplingCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5998
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CouplingCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5740
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5921,
        _5926,
        _5980,
        _6002,
        _6017,
        _5900,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingCompoundHarmonicAnalysis")


class CouplingCompoundHarmonicAnalysis(
    _5998.SpecialisedAssemblyCompoundHarmonicAnalysis
):
    """CouplingCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingCompoundHarmonicAnalysis")

    class _Cast_CouplingCompoundHarmonicAnalysis:
        """Special nested class for casting CouplingCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
            parent: "CouplingCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5998.SpecialisedAssemblyCompoundHarmonicAnalysis":
            return self._parent._cast(_5998.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5900.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5900,
            )

            return self._parent._cast(_5900.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5921.ClutchCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.ClutchCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5926.ConceptCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5926,
            )

            return self._parent._cast(_5926.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_5980.PartToPartShearCouplingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(
                _5980.PartToPartShearCouplingCompoundHarmonicAnalysis
            )

        @property
        def spring_damper_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_6002.SpringDamperCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(_6002.SpringDamperCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "_6017.TorqueConverterCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6017,
            )

            return self._parent._cast(_6017.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
        ) -> "CouplingCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_5740.CouplingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHarmonicAnalysis]

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
    ) -> "List[_5740.CouplingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHarmonicAnalysis]

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
    ) -> "CouplingCompoundHarmonicAnalysis._Cast_CouplingCompoundHarmonicAnalysis":
        return self._Cast_CouplingCompoundHarmonicAnalysis(self)
