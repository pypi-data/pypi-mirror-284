"""BevelDifferentialGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BevelDifferentialGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.static_loads import _6844
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6578,
        _6579,
        _6568,
        _6596,
        _6625,
        _6644,
        _6589,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearCriticalSpeedAnalysis")


class BevelDifferentialGearCriticalSpeedAnalysis(_6580.BevelGearCriticalSpeedAnalysis):
    """BevelDifferentialGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCriticalSpeedAnalysis"
    )

    class _Cast_BevelDifferentialGearCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
            parent: "BevelDifferentialGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6580.BevelGearCriticalSpeedAnalysis":
            return self._parent._cast(_6580.BevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6568.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6596.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6596,
            )

            return self._parent._cast(_6596.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6625.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6644.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6589.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6578.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(
                _6578.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "_6579.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6579,
            )

            return self._parent._cast(
                _6579.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
        ) -> "BevelDifferentialGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2535.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6844.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

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
    ) -> "BevelDifferentialGearCriticalSpeedAnalysis._Cast_BevelDifferentialGearCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialGearCriticalSpeedAnalysis(self)
