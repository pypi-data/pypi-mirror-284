"""CouplingCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4016
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CouplingCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3823
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3939,
        _3944,
        _3998,
        _4020,
        _4035,
        _3918,
        _3997,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingCompoundStabilityAnalysis")


class CouplingCompoundStabilityAnalysis(
    _4016.SpecialisedAssemblyCompoundStabilityAnalysis
):
    """CouplingCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingCompoundStabilityAnalysis")

    class _Cast_CouplingCompoundStabilityAnalysis:
        """Special nested class for casting CouplingCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
            parent: "CouplingCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_4016.SpecialisedAssemblyCompoundStabilityAnalysis":
            return self._parent._cast(
                _4016.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_3918.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(_3918.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_3939.ClutchCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.ClutchCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_3944.ConceptCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3944,
            )

            return self._parent._cast(_3944.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_3998.PartToPartShearCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3998,
            )

            return self._parent._cast(
                _3998.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def spring_damper_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_4020.SpringDamperCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(_4020.SpringDamperCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "_4035.TorqueConverterCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4035,
            )

            return self._parent._cast(_4035.TorqueConverterCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "CouplingCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CouplingCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_3823.CouplingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CouplingStabilityAnalysis]

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
    ) -> "List[_3823.CouplingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CouplingStabilityAnalysis]

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
    ) -> "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis":
        return self._Cast_CouplingCompoundStabilityAnalysis(self)
