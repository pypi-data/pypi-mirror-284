"""SynchroniserPartDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SynchroniserPartDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2626
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6414,
        _6416,
        _6377,
        _6323,
        _6379,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartDynamicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartDynamicAnalysis")


class SynchroniserPartDynamicAnalysis(_6337.CouplingHalfDynamicAnalysis):
    """SynchroniserPartDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartDynamicAnalysis")

    class _Cast_SynchroniserPartDynamicAnalysis:
        """Special nested class for casting SynchroniserPartDynamicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
            parent: "SynchroniserPartDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6337.CouplingHalfDynamicAnalysis":
            return self._parent._cast(_6337.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6377.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6323.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6414.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6414

            return self._parent._cast(_6414.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "_6416.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6416

            return self._parent._cast(_6416.SynchroniserSleeveDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "SynchroniserPartDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2626.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis":
        return self._Cast_SynchroniserPartDynamicAnalysis(self)
