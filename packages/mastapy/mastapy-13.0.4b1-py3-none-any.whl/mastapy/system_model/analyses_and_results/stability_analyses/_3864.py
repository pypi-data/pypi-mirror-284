"""OilSealStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3820
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "OilSealStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.static_loads import _6948
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3863,
        _3809,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("OilSealStabilityAnalysis",)


Self = TypeVar("Self", bound="OilSealStabilityAnalysis")


class OilSealStabilityAnalysis(_3820.ConnectorStabilityAnalysis):
    """OilSealStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealStabilityAnalysis")

    class _Cast_OilSealStabilityAnalysis:
        """Special nested class for casting OilSealStabilityAnalysis to subclasses."""

        def __init__(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
            parent: "OilSealStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connector_stability_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_3820.ConnectorStabilityAnalysis":
            return self._parent._cast(_3820.ConnectorStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_3863.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "OilSealStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2486.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6948.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis":
        return self._Cast_OilSealStabilityAnalysis(self)
