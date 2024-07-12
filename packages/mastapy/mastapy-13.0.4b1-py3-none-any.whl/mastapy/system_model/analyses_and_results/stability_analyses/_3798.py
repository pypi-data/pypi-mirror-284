"""BevelDifferentialPlanetGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3797
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BevelDifferentialPlanetGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
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
__all__ = ("BevelDifferentialPlanetGearStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearStabilityAnalysis")


class BevelDifferentialPlanetGearStabilityAnalysis(
    _3797.BevelDifferentialGearStabilityAnalysis
):
    """BevelDifferentialPlanetGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearStabilityAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearStabilityAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
            parent: "BevelDifferentialPlanetGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_stability_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_3797.BevelDifferentialGearStabilityAnalysis":
            return self._parent._cast(_3797.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_3802.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_3790.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_3818.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_3846.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_3863.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_3809.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
        ) -> "BevelDifferentialPlanetGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2537.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

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
    ) -> "BevelDifferentialPlanetGearStabilityAnalysis._Cast_BevelDifferentialPlanetGearStabilityAnalysis":
        return self._Cast_BevelDifferentialPlanetGearStabilityAnalysis(self)
