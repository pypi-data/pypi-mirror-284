"""RootAssemblyDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "RootAssemblyDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2494
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6350,
        _6298,
        _6379,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyDynamicAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyDynamicAnalysis")


class RootAssemblyDynamicAnalysis(_6305.AssemblyDynamicAnalysis):
    """RootAssemblyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyDynamicAnalysis")

    class _Cast_RootAssemblyDynamicAnalysis:
        """Special nested class for casting RootAssemblyDynamicAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
            parent: "RootAssemblyDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_dynamic_analysis(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
        ) -> "_6305.AssemblyDynamicAnalysis":
            return self._parent._cast(_6305.AssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
        ) -> "_6298.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
        ) -> "RootAssemblyDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssemblyDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2494.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def dynamic_analysis_inputs(self: Self) -> "_6350.DynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.DynamicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicAnalysisInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyDynamicAnalysis._Cast_RootAssemblyDynamicAnalysis":
        return self._Cast_RootAssemblyDynamicAnalysis(self)
