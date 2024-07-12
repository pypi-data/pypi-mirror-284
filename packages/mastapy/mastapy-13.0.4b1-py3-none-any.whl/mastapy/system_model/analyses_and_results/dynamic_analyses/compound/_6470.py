"""CVTCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6439
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CVTCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6527,
        _6429,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="CVTCompoundDynamicAnalysis")


class CVTCompoundDynamicAnalysis(_6439.BeltDriveCompoundDynamicAnalysis):
    """CVTCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundDynamicAnalysis")

    class _Cast_CVTCompoundDynamicAnalysis:
        """Special nested class for casting CVTCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis",
            parent: "CVTCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis",
        ) -> "_6439.BeltDriveCompoundDynamicAnalysis":
            return self._parent._cast(_6439.BeltDriveCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis",
        ) -> "_6527.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis",
        ) -> "_6429.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis",
        ) -> "CVTCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self: Self) -> "List[_6339.CVTDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CVTDynamicAnalysis]

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
    def assembly_analysis_cases(self: Self) -> "List[_6339.CVTDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CVTDynamicAnalysis]

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
    ) -> "CVTCompoundDynamicAnalysis._Cast_CVTCompoundDynamicAnalysis":
        return self._Cast_CVTCompoundDynamicAnalysis(self)
