"""VirtualComponentCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6644
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "VirtualComponentCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2499
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6642,
        _6643,
        _6653,
        _6654,
        _6688,
        _6589,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCriticalSpeedAnalysis")


class VirtualComponentCriticalSpeedAnalysis(
    _6644.MountableComponentCriticalSpeedAnalysis
):
    """VirtualComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCriticalSpeedAnalysis"
    )

    class _Cast_VirtualComponentCriticalSpeedAnalysis:
        """Special nested class for casting VirtualComponentCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
            parent: "VirtualComponentCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6644.MountableComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6644.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6589.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6642.MassDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6642,
            )

            return self._parent._cast(_6642.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6643.MeasurementComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6643,
            )

            return self._parent._cast(_6643.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6653.PointLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(_6653.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6654.PowerLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(_6654.PowerLoadCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "_6688.UnbalancedMassCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6688,
            )

            return self._parent._cast(_6688.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
        ) -> "VirtualComponentCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentCriticalSpeedAnalysis.TYPE"
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
    ) -> "VirtualComponentCriticalSpeedAnalysis._Cast_VirtualComponentCriticalSpeedAnalysis":
        return self._Cast_VirtualComponentCriticalSpeedAnalysis(self)
