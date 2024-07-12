"""ClutchCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6466
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ClutchCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6527,
        _6429,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ClutchCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ClutchCompoundDynamicAnalysis")


class ClutchCompoundDynamicAnalysis(_6466.CouplingCompoundDynamicAnalysis):
    """ClutchCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchCompoundDynamicAnalysis")

    class _Cast_ClutchCompoundDynamicAnalysis:
        """Special nested class for casting ClutchCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis",
            parent: "ClutchCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_dynamic_analysis(
            self: "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis",
        ) -> "_6466.CouplingCompoundDynamicAnalysis":
            return self._parent._cast(_6466.CouplingCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis",
        ) -> "_6527.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis",
        ) -> "_6429.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis",
        ) -> "ClutchCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2598.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

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
    ) -> "List[_6320.ClutchDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchDynamicAnalysis]

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
    def assembly_analysis_cases(self: Self) -> "List[_6320.ClutchDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchDynamicAnalysis]

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
    ) -> "ClutchCompoundDynamicAnalysis._Cast_ClutchCompoundDynamicAnalysis":
        return self._Cast_ClutchCompoundDynamicAnalysis(self)
