"""PlanetaryGearSetCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5949
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "PlanetaryGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5815
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5960,
        _5998,
        _5900,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundHarmonicAnalysis")


class PlanetaryGearSetCompoundHarmonicAnalysis(
    _5949.CylindricalGearSetCompoundHarmonicAnalysis
):
    """PlanetaryGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundHarmonicAnalysis"
    )

    class _Cast_PlanetaryGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
            parent: "PlanetaryGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_5949.CylindricalGearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5949.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_5960.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_5998.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5998,
            )

            return self._parent._cast(_5998.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_5900.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5900,
            )

            return self._parent._cast(_5900.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_harmonic_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
        ) -> "PlanetaryGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5815.PlanetaryGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetaryGearSetHarmonicAnalysis]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5815.PlanetaryGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetaryGearSetHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundHarmonicAnalysis._Cast_PlanetaryGearSetCompoundHarmonicAnalysis":
        return self._Cast_PlanetaryGearSetCompoundHarmonicAnalysis(self)
