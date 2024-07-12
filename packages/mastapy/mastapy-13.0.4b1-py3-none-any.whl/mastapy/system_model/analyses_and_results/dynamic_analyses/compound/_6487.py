"""GearCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6506
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "GearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6433,
        _6440,
        _6443,
        _6444,
        _6445,
        _6458,
        _6461,
        _6476,
        _6479,
        _6482,
        _6491,
        _6495,
        _6498,
        _6501,
        _6528,
        _6534,
        _6537,
        _6540,
        _6541,
        _6552,
        _6555,
        _6454,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="GearCompoundDynamicAnalysis")


class GearCompoundDynamicAnalysis(_6506.MountableComponentCompoundDynamicAnalysis):
    """GearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundDynamicAnalysis")

    class _Cast_GearCompoundDynamicAnalysis:
        """Special nested class for casting GearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
            parent: "GearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6506.MountableComponentCompoundDynamicAnalysis":
            return self._parent._cast(_6506.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6454.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(_6454.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6433.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(
                _6433.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6440.BevelDifferentialGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(
                _6440.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6443.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(
                _6443.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6444.BevelDifferentialSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(
                _6444.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6445.BevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.BevelGearCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6458.ConceptGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6458,
            )

            return self._parent._cast(_6458.ConceptGearCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6461.ConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.ConicalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6476.CylindricalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(_6476.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6479.CylindricalPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(
                _6479.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def face_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6482.FaceGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.FaceGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6491.HypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6491,
            )

            return self._parent._cast(_6491.HypoidGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6495.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(
                _6495.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6498.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(
                _6498.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6501.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(
                _6501.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6528.SpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6528,
            )

            return self._parent._cast(_6528.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6534.StraightBevelDiffGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6534,
            )

            return self._parent._cast(
                _6534.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6537.StraightBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6537,
            )

            return self._parent._cast(_6537.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6540.StraightBevelPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6540,
            )

            return self._parent._cast(
                _6540.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6541.StraightBevelSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6541,
            )

            return self._parent._cast(_6541.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6552.WormGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6552,
            )

            return self._parent._cast(_6552.WormGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "_6555.ZerolBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6555,
            )

            return self._parent._cast(_6555.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
        ) -> "GearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_6358.GearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.GearDynamicAnalysis]

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
    def component_analysis_cases_ready(self: Self) -> "List[_6358.GearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.GearDynamicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "GearCompoundDynamicAnalysis._Cast_GearCompoundDynamicAnalysis":
        return self._Cast_GearCompoundDynamicAnalysis(self)
