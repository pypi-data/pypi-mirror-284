"""PlanetaryGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3967
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PlanetaryGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3870
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3978,
        _4016,
        _3918,
        _3997,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundStabilityAnalysis")


class PlanetaryGearSetCompoundStabilityAnalysis(
    _3967.CylindricalGearSetCompoundStabilityAnalysis
):
    """PlanetaryGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundStabilityAnalysis"
    )

    class _Cast_PlanetaryGearSetCompoundStabilityAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
            parent: "PlanetaryGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3967.CylindricalGearSetCompoundStabilityAnalysis":
            return self._parent._cast(_3967.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3978.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_4016.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(
                _4016.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3918.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(_3918.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "PlanetaryGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3870.PlanetaryGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PlanetaryGearSetStabilityAnalysis]

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
    ) -> "List[_3870.PlanetaryGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PlanetaryGearSetStabilityAnalysis]

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
    ) -> "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis":
        return self._Cast_PlanetaryGearSetCompoundStabilityAnalysis(self)
