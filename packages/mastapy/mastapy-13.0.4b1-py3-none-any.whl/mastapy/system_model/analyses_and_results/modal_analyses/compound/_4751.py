"""AbstractShaftOrHousingCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4774
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AbstractShaftOrHousingCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4595
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4750,
        _4794,
        _4805,
        _4844,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundModalAnalysis")


class AbstractShaftOrHousingCompoundModalAnalysis(_4774.ComponentCompoundModalAnalysis):
    """AbstractShaftOrHousingCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundModalAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCompoundModalAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
            parent: "AbstractShaftOrHousingCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4774.ComponentCompoundModalAnalysis":
            return self._parent._cast(_4774.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4750.AbstractShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.AbstractShaftCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4794.CycloidalDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(_4794.CycloidalDiscCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4805.FEPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.FEPartCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "_4844.ShaftCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.ShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
        ) -> "AbstractShaftOrHousingCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4595.AbstractShaftOrHousingModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftOrHousingModalAnalysis]

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
    ) -> "List[_4595.AbstractShaftOrHousingModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftOrHousingModalAnalysis]

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
    ) -> "AbstractShaftOrHousingCompoundModalAnalysis._Cast_AbstractShaftOrHousingCompoundModalAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundModalAnalysis(self)
