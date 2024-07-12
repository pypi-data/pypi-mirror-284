"""KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3950
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3854
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3987,
        _3990,
        _3976,
        _3995,
        _3943,
        _3997,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis"
)


class KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis(
    _3950.ConicalGearCompoundStabilityAnalysis
):
    """KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "_3950.ConicalGearCompoundStabilityAnalysis":
            return self._parent._cast(_3950.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "_3976.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "_3995.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "_3943.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(_3943.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "_3987.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3987,
            )

            return self._parent._cast(
                _3987.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "_3990.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(
                _3990.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3854.KlingelnbergCycloPalloidConicalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidConicalGearStabilityAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3854.KlingelnbergCycloPalloidConicalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidConicalGearStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis(
            self
        )
