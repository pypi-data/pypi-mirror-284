"""CVTPulleyCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6655
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CVTPulleyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6603,
        _6644,
        _6589,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyCriticalSpeedAnalysis")


class CVTPulleyCriticalSpeedAnalysis(_6655.PulleyCriticalSpeedAnalysis):
    """CVTPulleyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyCriticalSpeedAnalysis")

    class _Cast_CVTPulleyCriticalSpeedAnalysis:
        """Special nested class for casting CVTPulleyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
            parent: "CVTPulleyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6655.PulleyCriticalSpeedAnalysis":
            return self._parent._cast(_6655.PulleyCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6603.CouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6644.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6589.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
        ) -> "CVTPulleyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

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
    ) -> "CVTPulleyCriticalSpeedAnalysis._Cast_CVTPulleyCriticalSpeedAnalysis":
        return self._Cast_CVTPulleyCriticalSpeedAnalysis(self)
