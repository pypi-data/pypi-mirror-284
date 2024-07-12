"""AbstractShaftStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AbstractShaftStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3831,
        _3882,
        _3809,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftStabilityAnalysis")


class AbstractShaftStabilityAnalysis(_3785.AbstractShaftOrHousingStabilityAnalysis):
    """AbstractShaftStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftStabilityAnalysis")

    class _Cast_AbstractShaftStabilityAnalysis:
        """Special nested class for casting AbstractShaftStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
            parent: "AbstractShaftStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "_3785.AbstractShaftOrHousingStabilityAnalysis":
            return self._parent._cast(_3785.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "_3831.CycloidalDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(_3831.CycloidalDiscStabilityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "_3882.ShaftStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.ShaftStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "AbstractShaftStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis":
        return self._Cast_AbstractShaftStabilityAnalysis(self)
