"""PartToPartShearCouplingCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3955
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PartToPartShearCouplingCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2609
    from mastapy.system_model.analyses_and_results.stability_analyses import _3868
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _4016,
        _3918,
        _3997,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingCompoundStabilityAnalysis")


class PartToPartShearCouplingCompoundStabilityAnalysis(
    _3955.CouplingCompoundStabilityAnalysis
):
    """PartToPartShearCouplingCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingCompoundStabilityAnalysis"
    )

    class _Cast_PartToPartShearCouplingCompoundStabilityAnalysis:
        """Special nested class for casting PartToPartShearCouplingCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis",
            parent: "PartToPartShearCouplingCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_stability_analysis(
            self: "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis",
        ) -> "_3955.CouplingCompoundStabilityAnalysis":
            return self._parent._cast(_3955.CouplingCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis",
        ) -> "_4016.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(
                _4016.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis",
        ) -> "_3918.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(_3918.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis",
        ) -> "PartToPartShearCouplingCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2609.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2609.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

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
    ) -> "List[_3868.PartToPartShearCouplingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PartToPartShearCouplingStabilityAnalysis]

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
    ) -> "List[_3868.PartToPartShearCouplingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PartToPartShearCouplingStabilityAnalysis]

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
    ) -> "PartToPartShearCouplingCompoundStabilityAnalysis._Cast_PartToPartShearCouplingCompoundStabilityAnalysis":
        return self._Cast_PartToPartShearCouplingCompoundStabilityAnalysis(self)
