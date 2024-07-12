"""AGMAGleasonConicalGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3952
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3789
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3931,
        _3936,
        _3982,
        _4019,
        _4025,
        _4028,
        _4046,
        _3978,
        _4016,
        _3918,
        _3997,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundStabilityAnalysis")


class AGMAGleasonConicalGearSetCompoundStabilityAnalysis(
    _3952.ConicalGearSetCompoundStabilityAnalysis
):
    """AGMAGleasonConicalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3952.ConicalGearSetCompoundStabilityAnalysis":
            return self._parent._cast(_3952.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3978.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4016.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(
                _4016.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3918.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(_3918.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3931.BevelDifferentialGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(
                _3931.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3936.BevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.BevelGearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3982.HypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4019.SpiralBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4025.StraightBevelDiffGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4025,
            )

            return self._parent._cast(
                _4025.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4028.StraightBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4028,
            )

            return self._parent._cast(
                _4028.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4046.ZerolBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4046,
            )

            return self._parent._cast(_4046.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3789.AGMAGleasonConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearSetStabilityAnalysis]

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
    ) -> "List[_3789.AGMAGleasonConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearSetStabilityAnalysis]

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
    ) -> "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis(self)
