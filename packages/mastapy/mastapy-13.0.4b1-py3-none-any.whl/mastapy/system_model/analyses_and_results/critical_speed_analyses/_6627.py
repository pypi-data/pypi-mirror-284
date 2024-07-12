"""GearSetCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6665
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "GearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6570,
        _6577,
        _6582,
        _6595,
        _6598,
        _6616,
        _6622,
        _6631,
        _6635,
        _6638,
        _6641,
        _6651,
        _6668,
        _6674,
        _6677,
        _6692,
        _6695,
        _6564,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearSetCriticalSpeedAnalysis")


class GearSetCriticalSpeedAnalysis(_6665.SpecialisedAssemblyCriticalSpeedAnalysis):
    """GearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCriticalSpeedAnalysis")

    class _Cast_GearSetCriticalSpeedAnalysis:
        """Special nested class for casting GearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
            parent: "GearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6665.SpecialisedAssemblyCriticalSpeedAnalysis":
            return self._parent._cast(_6665.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6564.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6570.AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(
                _6570.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6577.BevelDifferentialGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(
                _6577.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6582.BevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(_6582.BevelGearSetCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6595.ConceptGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6595,
            )

            return self._parent._cast(_6595.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6598.ConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6616.CylindricalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6616,
            )

            return self._parent._cast(_6616.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6622.FaceGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.FaceGearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6631.HypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6635.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(
                _6635.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6638.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(
                _6638.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6641.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(
                _6641.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6651.PlanetaryGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6668.SpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6674.StraightBevelDiffGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6674,
            )

            return self._parent._cast(
                _6674.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6677.StraightBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6677,
            )

            return self._parent._cast(_6677.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6692.WormGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6692,
            )

            return self._parent._cast(_6692.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "_6695.ZerolBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6695,
            )

            return self._parent._cast(_6695.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
        ) -> "GearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2552.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetCriticalSpeedAnalysis._Cast_GearSetCriticalSpeedAnalysis":
        return self._Cast_GearSetCriticalSpeedAnalysis(self)
