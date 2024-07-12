"""ConicalGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6625
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConicalGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6568,
        _6575,
        _6578,
        _6579,
        _6580,
        _6629,
        _6633,
        _6636,
        _6639,
        _6666,
        _6672,
        _6675,
        _6678,
        _6679,
        _6693,
        _6644,
        _6589,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConicalGearCriticalSpeedAnalysis")


class ConicalGearCriticalSpeedAnalysis(_6625.GearCriticalSpeedAnalysis):
    """ConicalGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearCriticalSpeedAnalysis")

    class _Cast_ConicalGearCriticalSpeedAnalysis:
        """Special nested class for casting ConicalGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
            parent: "ConicalGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6625.GearCriticalSpeedAnalysis":
            return self._parent._cast(_6625.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6644.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6589.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6568.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6575.BevelDifferentialGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6578.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(
                _6578.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6579.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6579,
            )

            return self._parent._cast(
                _6579.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6580.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.BevelGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6629.HypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6633.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(
                _6633.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6636.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6636,
            )

            return self._parent._cast(
                _6636.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6639.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6639,
            )

            return self._parent._cast(
                _6639.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6666.SpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6666,
            )

            return self._parent._cast(_6666.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6672.StraightBevelDiffGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6672,
            )

            return self._parent._cast(_6672.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6675.StraightBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6675,
            )

            return self._parent._cast(_6675.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6678.StraightBevelPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6678,
            )

            return self._parent._cast(
                _6678.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6679.StraightBevelSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6679,
            )

            return self._parent._cast(_6679.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "_6693.ZerolBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6693,
            )

            return self._parent._cast(_6693.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
        ) -> "ConicalGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearCriticalSpeedAnalysis._Cast_ConicalGearCriticalSpeedAnalysis":
        return self._Cast_ConicalGearCriticalSpeedAnalysis(self)
