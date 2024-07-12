"""StraightBevelDiffGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3936
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "StraightBevelDiffGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2566
    from mastapy.system_model.analyses_and_results.stability_analyses import _3895
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _4023,
        _4024,
        _3924,
        _3952,
        _3978,
        _4016,
        _3918,
        _3997,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetCompoundStabilityAnalysis")


class StraightBevelDiffGearSetCompoundStabilityAnalysis(
    _3936.BevelGearSetCompoundStabilityAnalysis
):
    """StraightBevelDiffGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
            parent: "StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "_3936.BevelGearSetCompoundStabilityAnalysis":
            return self._parent._cast(_3936.BevelGearSetCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "_3924.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(
                _3924.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "_3952.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "_3978.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "_4016.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(
                _4016.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "_3918.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(_3918.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "StraightBevelDiffGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2566.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2566.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3895.StraightBevelDiffGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearSetStabilityAnalysis]

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
    def straight_bevel_diff_gears_compound_stability_analysis(
        self: Self,
    ) -> "List[_4023.StraightBevelDiffGearCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.StraightBevelDiffGearCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_stability_analysis(
        self: Self,
    ) -> "List[_4024.StraightBevelDiffGearMeshCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.StraightBevelDiffGearMeshCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3895.StraightBevelDiffGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearSetStabilityAnalysis]

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
    ) -> "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis":
        return self._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis(self)
