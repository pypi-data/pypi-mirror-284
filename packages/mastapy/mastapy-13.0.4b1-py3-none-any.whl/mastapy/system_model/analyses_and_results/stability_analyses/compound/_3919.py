"""AbstractShaftCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3920
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AbstractShaftCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3786
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3963,
        _4013,
        _3943,
        _3997,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundStabilityAnalysis")


class AbstractShaftCompoundStabilityAnalysis(
    _3920.AbstractShaftOrHousingCompoundStabilityAnalysis
):
    """AbstractShaftCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundStabilityAnalysis"
    )

    class _Cast_AbstractShaftCompoundStabilityAnalysis:
        """Special nested class for casting AbstractShaftCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
            parent: "AbstractShaftCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3920.AbstractShaftOrHousingCompoundStabilityAnalysis":
            return self._parent._cast(
                _3920.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def component_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3943.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(_3943.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3963.CycloidalDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(_3963.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_4013.ShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(_4013.ShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "AbstractShaftCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3786.AbstractShaftStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftStabilityAnalysis]

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
    ) -> "List[_3786.AbstractShaftStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftStabilityAnalysis]

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
    ) -> "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis":
        return self._Cast_AbstractShaftCompoundStabilityAnalysis(self)
