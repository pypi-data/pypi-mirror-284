"""UnbalancedMassCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6818,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "UnbalancedMassCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2497
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6688
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6773,
        _6721,
        _6775,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundCriticalSpeedAnalysis")


class UnbalancedMassCompoundCriticalSpeedAnalysis(
    _6818.VirtualComponentCompoundCriticalSpeedAnalysis
):
    """UnbalancedMassCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundCriticalSpeedAnalysis"
    )

    class _Cast_UnbalancedMassCompoundCriticalSpeedAnalysis:
        """Special nested class for casting UnbalancedMassCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
            parent: "UnbalancedMassCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_6818.VirtualComponentCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6818.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_6773.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_6721.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(_6721.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "UnbalancedMassCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "UnbalancedMassCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2497.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

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
    ) -> "List[_6688.UnbalancedMassCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.UnbalancedMassCriticalSpeedAnalysis]

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
    ) -> "List[_6688.UnbalancedMassCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.UnbalancedMassCriticalSpeedAnalysis]

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
    ) -> "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis":
        return self._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis(self)
