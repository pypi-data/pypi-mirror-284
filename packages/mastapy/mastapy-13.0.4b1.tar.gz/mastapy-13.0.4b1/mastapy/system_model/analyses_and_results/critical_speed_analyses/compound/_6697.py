"""AbstractShaftCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6698,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AbstractShaftCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6565
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6741,
        _6791,
        _6721,
        _6775,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundCriticalSpeedAnalysis")


class AbstractShaftCompoundCriticalSpeedAnalysis(
    _6698.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
):
    """AbstractShaftCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundCriticalSpeedAnalysis"
    )

    class _Cast_AbstractShaftCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AbstractShaftCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
            parent: "AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_6698.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6698.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_6721.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(_6721.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_6741.CycloidalDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(_6741.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_6791.ShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6791,
            )

            return self._parent._cast(_6791.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "AbstractShaftCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6565.AbstractShaftCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractShaftCriticalSpeedAnalysis]

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
    ) -> "List[_6565.AbstractShaftCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractShaftCriticalSpeedAnalysis]

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
    ) -> "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis":
        return self._Cast_AbstractShaftCompoundCriticalSpeedAnalysis(self)
