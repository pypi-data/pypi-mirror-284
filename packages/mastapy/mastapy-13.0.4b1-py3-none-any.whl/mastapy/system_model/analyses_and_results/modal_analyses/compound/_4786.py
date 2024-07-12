"""CouplingCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4847
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CouplingCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4633
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4770,
        _4775,
        _4829,
        _4851,
        _4866,
        _4749,
        _4828,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CouplingCompoundModalAnalysis")


class CouplingCompoundModalAnalysis(_4847.SpecialisedAssemblyCompoundModalAnalysis):
    """CouplingCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingCompoundModalAnalysis")

    class _Cast_CouplingCompoundModalAnalysis:
        """Special nested class for casting CouplingCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
            parent: "CouplingCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_4847.SpecialisedAssemblyCompoundModalAnalysis":
            return self._parent._cast(_4847.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_4749.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_4828.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_4770.ClutchCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4770,
            )

            return self._parent._cast(_4770.ClutchCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_4775.ConceptCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4775,
            )

            return self._parent._cast(_4775.ConceptCouplingCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_4829.PartToPartShearCouplingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(
                _4829.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def spring_damper_compound_modal_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_4851.SpringDamperCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4851,
            )

            return self._parent._cast(_4851.SpringDamperCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "_4866.TorqueConverterCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4866,
            )

            return self._parent._cast(_4866.TorqueConverterCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
        ) -> "CouplingCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4633.CouplingModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingModalAnalysis]

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
    ) -> "List[_4633.CouplingModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingModalAnalysis]

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
    ) -> "CouplingCompoundModalAnalysis._Cast_CouplingCompoundModalAnalysis":
        return self._Cast_CouplingCompoundModalAnalysis(self)
