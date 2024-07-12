"""AGMAGleasonConicalGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AGMAGleasonConicalGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3797,
        _3798,
        _3799,
        _3802,
        _3850,
        _3887,
        _3896,
        _3899,
        _3900,
        _3901,
        _3917,
        _3846,
        _3863,
        _3809,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearStabilityAnalysis")


class AGMAGleasonConicalGearStabilityAnalysis(_3818.ConicalGearStabilityAnalysis):
    """AGMAGleasonConicalGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
            parent: "AGMAGleasonConicalGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3818.ConicalGearStabilityAnalysis":
            return self._parent._cast(_3818.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3846.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3863.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3797.BevelDifferentialGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3798.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(
                _3798.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3799.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3802.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.BevelGearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3850.HypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.HypoidGearStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3887.SpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.SpiralBevelGearStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3896.StraightBevelDiffGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3896,
            )

            return self._parent._cast(_3896.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3899.StraightBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3899,
            )

            return self._parent._cast(_3899.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3900.StraightBevelPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3900,
            )

            return self._parent._cast(_3900.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3901.StraightBevelSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3901,
            )

            return self._parent._cast(_3901.StraightBevelSunGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3917.ZerolBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3917,
            )

            return self._parent._cast(_3917.ZerolBevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearStabilityAnalysis.TYPE"
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
    ) -> "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearStabilityAnalysis(self)
