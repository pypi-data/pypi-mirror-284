"""VirtualComponentDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "VirtualComponentDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6375,
        _6376,
        _6386,
        _6387,
        _6421,
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
__all__ = ("VirtualComponentDynamicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentDynamicAnalysis")


class VirtualComponentDynamicAnalysis(_6377.MountableComponentDynamicAnalysis):
    """VirtualComponentDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentDynamicAnalysis")

    class _Cast_VirtualComponentDynamicAnalysis:
        """Special nested class for casting VirtualComponentDynamicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
            parent: "VirtualComponentDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6377.MountableComponentDynamicAnalysis":
            return self._parent._cast(_6377.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6323.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6375.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6376.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.MeasurementComponentDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6386.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6387.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.PowerLoadDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "_6421.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6421

            return self._parent._cast(_6421.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "VirtualComponentDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2499.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis":
        return self._Cast_VirtualComponentDynamicAnalysis(self)
