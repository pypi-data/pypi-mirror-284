"""GearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4016
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "GearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3845
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3924,
        _3931,
        _3936,
        _3949,
        _3952,
        _3967,
        _3973,
        _3982,
        _3986,
        _3989,
        _3992,
        _4002,
        _4019,
        _4025,
        _4028,
        _4043,
        _4046,
        _3918,
        _3997,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="GearSetCompoundStabilityAnalysis")


class GearSetCompoundStabilityAnalysis(
    _4016.SpecialisedAssemblyCompoundStabilityAnalysis
):
    """GearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCompoundStabilityAnalysis")

    class _Cast_GearSetCompoundStabilityAnalysis:
        """Special nested class for casting GearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
            parent: "GearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_4016.SpecialisedAssemblyCompoundStabilityAnalysis":
            return self._parent._cast(
                _4016.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3918.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(_3918.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3997.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3924.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(
                _3924.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3931.BevelDifferentialGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(
                _3931.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3936.BevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.BevelGearSetCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3949.ConceptGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(_3949.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3952.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3967.CylindricalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(_3967.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3973.FaceGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.FaceGearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3982.HypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3986.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3986,
            )

            return self._parent._cast(
                _3986.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_3989.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(
                _3989.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> (
            "_3992.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_4002.PlanetaryGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(_4002.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_4019.SpiralBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_4025.StraightBevelDiffGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4025,
            )

            return self._parent._cast(
                _4025.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_4028.StraightBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4028,
            )

            return self._parent._cast(
                _4028.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_4043.WormGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4043,
            )

            return self._parent._cast(_4043.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "_4046.ZerolBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4046,
            )

            return self._parent._cast(_4046.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
        ) -> "GearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_3845.GearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3845.GearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetCompoundStabilityAnalysis._Cast_GearSetCompoundStabilityAnalysis":
        return self._Cast_GearSetCompoundStabilityAnalysis(self)
