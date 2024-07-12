"""FEPartDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "FEPartDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.static_loads import _6909
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323, _6379
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("FEPartDynamicAnalysis",)


Self = TypeVar("Self", bound="FEPartDynamicAnalysis")


class FEPartDynamicAnalysis(_6300.AbstractShaftOrHousingDynamicAnalysis):
    """FEPartDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartDynamicAnalysis")

    class _Cast_FEPartDynamicAnalysis:
        """Special nested class for casting FEPartDynamicAnalysis to subclasses."""

        def __init__(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
            parent: "FEPartDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
        ) -> "_6300.AbstractShaftOrHousingDynamicAnalysis":
            return self._parent._cast(_6300.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
        ) -> "_6323.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis",
        ) -> "FEPartDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2473.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6909.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[FEPartDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.FEPartDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FEPartDynamicAnalysis._Cast_FEPartDynamicAnalysis":
        return self._Cast_FEPartDynamicAnalysis(self)
