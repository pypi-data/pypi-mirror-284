"""RootAssemblyCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5016,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "RootAssemblyCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4974,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5009,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="RootAssemblyCompoundModalAnalysisAtAStiffness")


class RootAssemblyCompoundModalAnalysisAtAStiffness(
    _5016.AssemblyCompoundModalAnalysisAtAStiffness
):
    """RootAssemblyCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_RootAssemblyCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting RootAssemblyCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness",
            parent: "RootAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def assembly_compound_modal_analysis_at_a_stiffness(
            self: "RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5016.AssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(_5016.AssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5009.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(
                _5009.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def root_assembly_compound_modal_analysis_at_a_stiffness(
            self: "RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "RootAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "RootAssemblyCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4974.RootAssemblyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.RootAssemblyModalAnalysisAtAStiffness]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4974.RootAssemblyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.RootAssemblyModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "RootAssemblyCompoundModalAnalysisAtAStiffness._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness":
        return self._Cast_RootAssemblyCompoundModalAnalysisAtAStiffness(self)
