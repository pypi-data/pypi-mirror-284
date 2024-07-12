"""BevelGearSetCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6435
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6442,
        _6530,
        _6536,
        _6539,
        _6557,
        _6463,
        _6489,
        _6527,
        _6429,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetCompoundDynamicAnalysis")


class BevelGearSetCompoundDynamicAnalysis(
    _6435.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
):
    """BevelGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetCompoundDynamicAnalysis")

    class _Cast_BevelGearSetCompoundDynamicAnalysis:
        """Special nested class for casting BevelGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
            parent: "BevelGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6435.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            return self._parent._cast(
                _6435.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6463.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6489.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6527.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6429.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6442.BevelDifferentialGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(
                _6442.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6530.SpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6530,
            )

            return self._parent._cast(_6530.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6536.StraightBevelDiffGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6536,
            )

            return self._parent._cast(
                _6536.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6539.StraightBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6539,
            )

            return self._parent._cast(_6539.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6557.ZerolBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6557,
            )

            return self._parent._cast(_6557.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "BevelGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearSetCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6316.BevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearSetDynamicAnalysis]

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
    ) -> "List[_6316.BevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearSetDynamicAnalysis]

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
    ) -> (
        "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis"
    ):
        return self._Cast_BevelGearSetCompoundDynamicAnalysis(self)
