"""AGMAGleasonConicalGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5733
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AGMAGleasonConicalGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.system_deflections import _2712
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5711,
        _5714,
        _5715,
        _5716,
        _5792,
        _5833,
        _5840,
        _5843,
        _5846,
        _5847,
        _5862,
        _5774,
        _5807,
        _5726,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearHarmonicAnalysis")


class AGMAGleasonConicalGearHarmonicAnalysis(_5733.ConicalGearHarmonicAnalysis):
    """AGMAGleasonConicalGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearHarmonicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
            parent: "AGMAGleasonConicalGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5733.ConicalGearHarmonicAnalysis":
            return self._parent._cast(_5733.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5774.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(_5774.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5807.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(_5807.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5711.BevelDifferentialGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5714.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5715.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5716.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.BevelGearHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5792.HypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5792,
            )

            return self._parent._cast(_5792.HypoidGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5833.SpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.SpiralBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5840.StraightBevelDiffGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5843.StraightBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5846.StraightBevelPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5846,
            )

            return self._parent._cast(_5846.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5847.StraightBevelSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5847,
            )

            return self._parent._cast(_5847.StraightBevelSunGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5862.ZerolBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5862,
            )

            return self._parent._cast(_5862.ZerolBevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "AGMAGleasonConicalGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearHarmonicAnalysis.TYPE"
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
    def system_deflection_results(
        self: Self,
    ) -> "_2712.AGMAGleasonConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis":
        return self._Cast_AGMAGleasonConicalGearHarmonicAnalysis(self)
