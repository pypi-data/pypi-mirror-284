"""KlingelnbergCycloPalloidHypoidGearDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2558
    from mastapy.system_model.analyses_and_results.static_loads import _6937
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6330,
        _6358,
        _6377,
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
__all__ = ("KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearDynamicAnalysis")


class KlingelnbergCycloPalloidHypoidGearDynamicAnalysis(
    _6366.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_6366.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            return self._parent._cast(
                _6366.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def conical_gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_6330.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_6358.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_6377.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_6323.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_6379.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2558.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6937.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis(self)
