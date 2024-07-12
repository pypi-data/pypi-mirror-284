"""CouplingCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5107,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CouplingCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4917,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5030,
        _5035,
        _5089,
        _5111,
        _5126,
        _5009,
        _5088,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CouplingCompoundModalAnalysisAtAStiffness")


class CouplingCompoundModalAnalysisAtAStiffness(
    _5107.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
):
    """CouplingCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CouplingCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
            parent: "CouplingCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5107.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5107.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5009.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(
                _5009.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(_5088.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5030.ClutchCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5030,
            )

            return self._parent._cast(_5030.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5035.ConceptCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5035,
            )

            return self._parent._cast(
                _5035.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5089.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5089,
            )

            return self._parent._cast(
                _5089.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5111.SpringDamperCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(
                _5111.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "_5126.TorqueConverterCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5126,
            )

            return self._parent._cast(
                _5126.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
        ) -> "CouplingCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CouplingCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4917.CouplingModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingModalAnalysisAtAStiffness]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4917.CouplingModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CouplingModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "CouplingCompoundModalAnalysisAtAStiffness._Cast_CouplingCompoundModalAnalysisAtAStiffness":
        return self._Cast_CouplingCompoundModalAnalysisAtAStiffness(self)
