"""SpiralBevelGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5916
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "SpiralBevelGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2563
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5833
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5904,
        _5932,
        _5958,
        _5977,
        _5925,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearCompoundHarmonicAnalysis")


class SpiralBevelGearCompoundHarmonicAnalysis(_5916.BevelGearCompoundHarmonicAnalysis):
    """SpiralBevelGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearCompoundHarmonicAnalysis"
    )

    class _Cast_SpiralBevelGearCompoundHarmonicAnalysis:
        """Special nested class for casting SpiralBevelGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
            parent: "SpiralBevelGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5916.BevelGearCompoundHarmonicAnalysis":
            return self._parent._cast(_5916.BevelGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5904.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(
                _5904.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5932.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5932,
            )

            return self._parent._cast(_5932.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5958.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5977.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5925.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(_5925.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "SpiralBevelGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2563.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5833.SpiralBevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5833.SpiralBevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearCompoundHarmonicAnalysis._Cast_SpiralBevelGearCompoundHarmonicAnalysis":
        return self._Cast_SpiralBevelGearCompoundHarmonicAnalysis(self)
