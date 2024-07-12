"""BevelDifferentialSunGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3797
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BevelDifferentialSunGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3802,
        _3790,
        _3818,
        _3846,
        _3863,
        _3809,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearStabilityAnalysis")


class BevelDifferentialSunGearStabilityAnalysis(
    _3797.BevelDifferentialGearStabilityAnalysis
):
    """BevelDifferentialSunGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearStabilityAnalysis"
    )

    class _Cast_BevelDifferentialSunGearStabilityAnalysis:
        """Special nested class for casting BevelDifferentialSunGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
            parent: "BevelDifferentialSunGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_3797.BevelDifferentialGearStabilityAnalysis":
            return self._parent._cast(_3797.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_3802.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_3790.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_3818.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_3846.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_3863.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "BevelDifferentialSunGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialSunGearStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2538.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis":
        return self._Cast_BevelDifferentialSunGearStabilityAnalysis(self)
