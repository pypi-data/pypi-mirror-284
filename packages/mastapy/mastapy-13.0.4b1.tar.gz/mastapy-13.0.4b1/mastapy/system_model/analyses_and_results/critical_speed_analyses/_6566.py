"""AbstractShaftOrHousingCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6589
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "AbstractShaftOrHousingCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2456
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6565,
        _6612,
        _6623,
        _6662,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCriticalSpeedAnalysis")


class AbstractShaftOrHousingCriticalSpeedAnalysis(_6589.ComponentCriticalSpeedAnalysis):
    """AbstractShaftOrHousingCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCriticalSpeedAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCriticalSpeedAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
            parent: "AbstractShaftOrHousingCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def component_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6589.ComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6589.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6565.AbstractShaftCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.AbstractShaftCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6612.CycloidalDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6612,
            )

            return self._parent._cast(_6612.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6623.FEPartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.FEPartCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "_6662.ShaftCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6662,
            )

            return self._parent._cast(_6662.ShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
        ) -> "AbstractShaftOrHousingCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2456.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis":
        return self._Cast_AbstractShaftOrHousingCriticalSpeedAnalysis(self)
