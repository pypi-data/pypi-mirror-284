"""StraightBevelPlanetGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5840
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "StraightBevelPlanetGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2569
    from mastapy.system_model.analyses_and_results.system_deflections import _2840
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5716,
        _5704,
        _5733,
        _5774,
        _5807,
        _5726,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearHarmonicAnalysis")


class StraightBevelPlanetGearHarmonicAnalysis(
    _5840.StraightBevelDiffGearHarmonicAnalysis
):
    """StraightBevelPlanetGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearHarmonicAnalysis"
    )

    class _Cast_StraightBevelPlanetGearHarmonicAnalysis:
        """Special nested class for casting StraightBevelPlanetGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
            parent: "StraightBevelPlanetGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_5840.StraightBevelDiffGearHarmonicAnalysis":
            return self._parent._cast(_5840.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_5716.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_5704.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_5733.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5733,
            )

            return self._parent._cast(_5733.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_5774.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(_5774.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_5807.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(_5807.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "StraightBevelPlanetGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

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
    ) -> "_2840.StraightBevelPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection

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
    ) -> "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis":
        return self._Cast_StraightBevelPlanetGearHarmonicAnalysis(self)
