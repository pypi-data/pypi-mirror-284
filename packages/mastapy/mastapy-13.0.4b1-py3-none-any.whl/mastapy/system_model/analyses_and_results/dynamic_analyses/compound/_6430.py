"""AbstractShaftCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6431
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "AbstractShaftCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6474,
        _6524,
        _6454,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundDynamicAnalysis")


class AbstractShaftCompoundDynamicAnalysis(
    _6431.AbstractShaftOrHousingCompoundDynamicAnalysis
):
    """AbstractShaftCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftCompoundDynamicAnalysis")

    class _Cast_AbstractShaftCompoundDynamicAnalysis:
        """Special nested class for casting AbstractShaftCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
            parent: "AbstractShaftCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ) -> "_6431.AbstractShaftOrHousingCompoundDynamicAnalysis":
            return self._parent._cast(
                _6431.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def component_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ) -> "_6454.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(_6454.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ) -> "_6474.CycloidalDiscCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(_6474.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ) -> "_6524.ShaftCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.ShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
        ) -> "AbstractShaftCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6299.AbstractShaftDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftDynamicAnalysis]

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
    ) -> "List[_6299.AbstractShaftDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftDynamicAnalysis]

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
    ) -> "AbstractShaftCompoundDynamicAnalysis._Cast_AbstractShaftCompoundDynamicAnalysis":
        return self._Cast_AbstractShaftCompoundDynamicAnalysis(self)
