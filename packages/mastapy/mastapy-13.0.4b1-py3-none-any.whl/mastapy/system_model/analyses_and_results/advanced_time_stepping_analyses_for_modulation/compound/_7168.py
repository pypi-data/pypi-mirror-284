"""AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7196,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7037,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7175,
        _7180,
        _7226,
        _7263,
        _7269,
        _7272,
        _7290,
        _7222,
        _7260,
        _7162,
        _7241,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = (
    "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7196.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7196.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7196.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7222.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7260.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7260,
            )

            return self._parent._cast(
                _7260.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7162.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7162,
            )

            return self._parent._cast(
                _7162.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7241.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7241,
            )

            return self._parent._cast(
                _7241.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7175.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7175,
            )

            return self._parent._cast(
                _7175.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7180.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7180,
            )

            return self._parent._cast(
                _7180.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7226.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7226,
            )

            return self._parent._cast(
                _7226.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7263.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7263,
            )

            return self._parent._cast(
                _7263.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7269.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7269,
            )

            return self._parent._cast(
                _7269.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7272.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7272,
            )

            return self._parent._cast(
                _7272.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7290.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7290,
            )

            return self._parent._cast(
                _7290.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> (
        "List[_7037.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation]"
    ):
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> (
        "List[_7037.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation]"
    ):
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
