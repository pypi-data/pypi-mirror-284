"""CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6207,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6079,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6218,
        _6237,
        _6185,
        _6239,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation"
)


class CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation(
    _6207.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
):
    """CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6207.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6207.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6218.GearCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6237.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6185.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6079.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6079.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation]

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
    ) -> "CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
        return (
            self._Cast_CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation(
                self
            )
        )
