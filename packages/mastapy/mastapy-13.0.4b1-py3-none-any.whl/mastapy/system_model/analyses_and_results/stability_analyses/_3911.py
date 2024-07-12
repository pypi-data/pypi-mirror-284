"""VirtualComponentStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3863
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "VirtualComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3861,
        _3862,
        _3872,
        _3873,
        _3910,
        _3809,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentStabilityAnalysis")


class VirtualComponentStabilityAnalysis(_3863.MountableComponentStabilityAnalysis):
    """VirtualComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentStabilityAnalysis")

    class _Cast_VirtualComponentStabilityAnalysis:
        """Special nested class for casting VirtualComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
            parent: "VirtualComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3863.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3863.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3861.MassDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3862.MeasurementComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.MeasurementComponentStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3872.PointLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3873.PowerLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.PowerLoadStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "_3910.UnbalancedMassStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3910,
            )

            return self._parent._cast(_3910.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "VirtualComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentStabilityAnalysis.TYPE"
    ):
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
    ) -> "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis":
        return self._Cast_VirtualComponentStabilityAnalysis(self)
