"""KlingelnbergCycloPalloidConicalGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3857,
        _3860,
        _3846,
        _3863,
        _3809,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearStabilityAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearStabilityAnalysis")


class KlingelnbergCycloPalloidConicalGearStabilityAnalysis(
    _3818.ConicalGearStabilityAnalysis
):
    """KlingelnbergCycloPalloidConicalGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_3818.ConicalGearStabilityAnalysis":
            return self._parent._cast(_3818.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_3846.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_3863.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_3857.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(
                _3857.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "_3860.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(
                _3860.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2556.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis(self)
