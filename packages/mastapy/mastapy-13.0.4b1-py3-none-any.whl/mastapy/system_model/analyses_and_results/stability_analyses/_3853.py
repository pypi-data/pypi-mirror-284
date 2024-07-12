"""KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3817
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3856,
        _3859,
        _3845,
        _3884,
        _3784,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis")


class KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis(
    _3817.ConicalGearSetStabilityAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_3817.ConicalGearSetStabilityAnalysis":
            return self._parent._cast(_3817.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_3845.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_3884.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_3784.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_3856.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(
                _3856.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "_3859.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(
                _3859.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2557.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis(self)
