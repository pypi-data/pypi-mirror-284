"""ConceptCouplingCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5305,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ConceptCouplingCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2601
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5166,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5366,
        _5268,
        _5347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConceptCouplingCompoundModalAnalysisAtASpeed")


class ConceptCouplingCompoundModalAnalysisAtASpeed(
    _5305.CouplingCompoundModalAnalysisAtASpeed
):
    """ConceptCouplingCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ConceptCouplingCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ConceptCouplingCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
            parent: "ConceptCouplingCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ) -> "_5305.CouplingCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5305.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ) -> "_5366.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ) -> "_5268.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(
                _5268.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ) -> "_5347.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(_5347.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ) -> "ConceptCouplingCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "ConceptCouplingCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2601.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2601.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5166.ConceptCouplingModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConceptCouplingModalAnalysisAtASpeed]

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
    ) -> "List[_5166.ConceptCouplingModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConceptCouplingModalAnalysisAtASpeed]

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
    ) -> "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed":
        return self._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed(self)
