"""AGMAGleasonConicalGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "AGMAGleasonConicalGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6575,
        _6578,
        _6579,
        _6580,
        _6629,
        _6666,
        _6672,
        _6675,
        _6678,
        _6679,
        _6693,
        _6625,
        _6644,
        _6589,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCriticalSpeedAnalysis")


class AGMAGleasonConicalGearCriticalSpeedAnalysis(
    _6596.ConicalGearCriticalSpeedAnalysis
):
    """AGMAGleasonConicalGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
            parent: "AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6596.ConicalGearCriticalSpeedAnalysis":
            return self._parent._cast(_6596.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6625.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6644.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6589.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6575.BevelDifferentialGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6578.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(
                _6578.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6579.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6579,
            )

            return self._parent._cast(
                _6579.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6580.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.BevelGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6629.HypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.HypoidGearCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6666.SpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6666,
            )

            return self._parent._cast(_6666.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6672.StraightBevelDiffGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6672,
            )

            return self._parent._cast(_6672.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6675.StraightBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6675,
            )

            return self._parent._cast(_6675.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6678.StraightBevelPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6678,
            )

            return self._parent._cast(
                _6678.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6679.StraightBevelSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6679,
            )

            return self._parent._cast(_6679.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "_6693.ZerolBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6693,
            )

            return self._parent._cast(_6693.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "AGMAGleasonConicalGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis":
        return self._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis(self)
