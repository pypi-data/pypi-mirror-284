"""HypoidGearCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "HypoidGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.stability_analyses import _3850
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3950,
        _3976,
        _3995,
        _3943,
        _3997,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="HypoidGearCompoundStabilityAnalysis")


class HypoidGearCompoundStabilityAnalysis(
    _3922.AGMAGleasonConicalGearCompoundStabilityAnalysis
):
    """HypoidGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearCompoundStabilityAnalysis")

    class _Cast_HypoidGearCompoundStabilityAnalysis:
        """Special nested class for casting HypoidGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
            parent: "HypoidGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
        ) -> "_3922.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            return self._parent._cast(
                _3922.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
        ) -> "_3950.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
        ) -> "_3976.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
        ) -> "_3995.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
        ) -> "_3943.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(_3943.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
        ) -> "HypoidGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3850.HypoidGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.HypoidGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3850.HypoidGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.HypoidGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "HypoidGearCompoundStabilityAnalysis._Cast_HypoidGearCompoundStabilityAnalysis"
    ):
        return self._Cast_HypoidGearCompoundStabilityAnalysis(self)
