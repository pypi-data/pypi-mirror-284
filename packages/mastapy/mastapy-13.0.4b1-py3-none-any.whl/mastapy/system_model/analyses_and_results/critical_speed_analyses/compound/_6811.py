"""SynchroniserPartCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6735,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "SynchroniserPartCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6682
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6810,
        _6812,
        _6773,
        _6721,
        _6775,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundCriticalSpeedAnalysis")


class SynchroniserPartCompoundCriticalSpeedAnalysis(
    _6735.CouplingHalfCompoundCriticalSpeedAnalysis
):
    """SynchroniserPartCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundCriticalSpeedAnalysis"
    )

    class _Cast_SynchroniserPartCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SynchroniserPartCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
            parent: "SynchroniserPartCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6735.CouplingHalfCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6735.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6773.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6721.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(_6721.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6810.SynchroniserHalfCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6810,
            )

            return self._parent._cast(
                _6810.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "_6812.SynchroniserSleeveCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6812,
            )

            return self._parent._cast(
                _6812.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
        ) -> "SynchroniserPartCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "SynchroniserPartCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6682.SynchroniserPartCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SynchroniserPartCriticalSpeedAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6682.SynchroniserPartCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SynchroniserPartCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartCompoundCriticalSpeedAnalysis._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis":
        return self._Cast_SynchroniserPartCompoundCriticalSpeedAnalysis(self)
