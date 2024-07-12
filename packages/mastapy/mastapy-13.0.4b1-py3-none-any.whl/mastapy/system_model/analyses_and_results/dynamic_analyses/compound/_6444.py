"""BevelDifferentialSunGearCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6440
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelDifferentialSunGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6445,
        _6433,
        _6461,
        _6487,
        _6506,
        _6454,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundDynamicAnalysis")


class BevelDifferentialSunGearCompoundDynamicAnalysis(
    _6440.BevelDifferentialGearCompoundDynamicAnalysis
):
    """BevelDifferentialSunGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCompoundDynamicAnalysis"
    )

    class _Cast_BevelDifferentialSunGearCompoundDynamicAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
            parent: "BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_6440.BevelDifferentialGearCompoundDynamicAnalysis":
            return self._parent._cast(
                _6440.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_6445.BevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.BevelGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_6433.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(
                _6433.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_6461.ConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_6487.GearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_6506.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_6454.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(_6454.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "BevelDifferentialSunGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6313.BevelDifferentialSunGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialSunGearDynamicAnalysis]

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
    ) -> "List[_6313.BevelDifferentialSunGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialSunGearDynamicAnalysis]

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
    ) -> "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis":
        return self._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis(self)
