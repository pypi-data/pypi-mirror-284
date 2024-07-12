"""SpringDamperHalfCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6735,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "SpringDamperHalfCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2622
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6671
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6773,
        _6721,
        _6775,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundCriticalSpeedAnalysis")


class SpringDamperHalfCompoundCriticalSpeedAnalysis(
    _6735.CouplingHalfCompoundCriticalSpeedAnalysis
):
    """SpringDamperHalfCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis"
    )

    class _Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SpringDamperHalfCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis",
            parent: "SpringDamperHalfCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6735.CouplingHalfCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6735.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6773.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6721.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(_6721.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_critical_speed_analysis(
            self: "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis",
        ) -> "SpringDamperHalfCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "SpringDamperHalfCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2622.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6671.SpringDamperHalfCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpringDamperHalfCriticalSpeedAnalysis]

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
    ) -> "List[_6671.SpringDamperHalfCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpringDamperHalfCriticalSpeedAnalysis]

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
    ) -> "SpringDamperHalfCompoundCriticalSpeedAnalysis._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis":
        return self._Cast_SpringDamperHalfCompoundCriticalSpeedAnalysis(self)
