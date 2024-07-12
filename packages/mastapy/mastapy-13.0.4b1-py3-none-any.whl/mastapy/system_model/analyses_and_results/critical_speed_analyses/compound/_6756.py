"""GearSetCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6794,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "GearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6627
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6702,
        _6709,
        _6714,
        _6727,
        _6730,
        _6745,
        _6751,
        _6760,
        _6764,
        _6767,
        _6770,
        _6780,
        _6797,
        _6803,
        _6806,
        _6821,
        _6824,
        _6696,
        _6775,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearSetCompoundCriticalSpeedAnalysis")


class GearSetCompoundCriticalSpeedAnalysis(
    _6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
):
    """GearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCompoundCriticalSpeedAnalysis")

    class _Cast_GearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting GearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
            parent: "GearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6794.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6696.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(
                _6696.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6775.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(_6775.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6702.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(
                _6702.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6709.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(
                _6709.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6714.BevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6714,
            )

            return self._parent._cast(_6714.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6727.ConceptGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(_6727.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6730.ConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6745.CylindricalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6745,
            )

            return self._parent._cast(
                _6745.CylindricalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6751.FaceGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(_6751.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6760.HypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(_6760.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6764.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6764,
            )

            return self._parent._cast(
                _6764.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6767.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6767,
            )

            return self._parent._cast(
                _6767.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6770.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(
                _6770.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PlanetaryGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(
                _6780.PlanetaryGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6797.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(
                _6797.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6803.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6803,
            )

            return self._parent._cast(
                _6803.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6806.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6806,
            )

            return self._parent._cast(
                _6806.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6821.WormGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6821,
            )

            return self._parent._cast(_6821.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6824.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6824,
            )

            return self._parent._cast(
                _6824.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
        ) -> "GearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "GearSetCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6627.GearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearSetCriticalSpeedAnalysis]

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
    ) -> "List[_6627.GearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearSetCriticalSpeedAnalysis]

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
    ) -> "GearSetCompoundCriticalSpeedAnalysis._Cast_GearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_GearSetCompoundCriticalSpeedAnalysis(self)
