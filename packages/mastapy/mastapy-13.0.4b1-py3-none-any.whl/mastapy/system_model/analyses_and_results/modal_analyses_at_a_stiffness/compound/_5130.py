"""UnbalancedMassCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5131,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "UnbalancedMassCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2497
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _5001,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5086,
        _5034,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundModalAnalysisAtAStiffness")


class UnbalancedMassCompoundModalAnalysisAtAStiffness(
    _5131.VirtualComponentCompoundModalAnalysisAtAStiffness
):
    """UnbalancedMassCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting UnbalancedMassCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness",
            parent: "UnbalancedMassCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness",
        ) -> "_5131.VirtualComponentCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5131.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness",
        ) -> "_5086.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(_5034.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness",
        ) -> "UnbalancedMassCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "UnbalancedMassCompoundModalAnalysisAtAStiffness.TYPE",
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
    ) -> "List[_5001.UnbalancedMassModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.UnbalancedMassModalAnalysisAtAStiffness]

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
    ) -> "List[_5001.UnbalancedMassModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.UnbalancedMassModalAnalysisAtAStiffness]

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
    ) -> "UnbalancedMassCompoundModalAnalysisAtAStiffness._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness":
        return self._Cast_UnbalancedMassCompoundModalAnalysisAtAStiffness(self)
