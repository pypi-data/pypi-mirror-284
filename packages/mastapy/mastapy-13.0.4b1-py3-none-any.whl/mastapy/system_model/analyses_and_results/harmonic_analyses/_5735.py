"""ConicalGearSetHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConicalGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.system_deflections import _2746
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5706,
        _5713,
        _5718,
        _5794,
        _5798,
        _5801,
        _5804,
        _5835,
        _5842,
        _5845,
        _5864,
        _5831,
        _5699,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetHarmonicAnalysis")


class ConicalGearSetHarmonicAnalysis(_5779.GearSetHarmonicAnalysis):
    """ConicalGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetHarmonicAnalysis")

    class _Cast_ConicalGearSetHarmonicAnalysis:
        """Special nested class for casting ConicalGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
            parent: "ConicalGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5779.GearSetHarmonicAnalysis":
            return self._parent._cast(_5779.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5831.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5831,
            )

            return self._parent._cast(_5831.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5699.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5699,
            )

            return self._parent._cast(_5699.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5706.AGMAGleasonConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5706,
            )

            return self._parent._cast(_5706.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5713.BevelDifferentialGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5718.BevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.BevelGearSetHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5794.HypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5798.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(
                _5798.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5801.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5801,
            )

            return self._parent._cast(
                _5801.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5804.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(
                _5804.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5835.SpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5835,
            )

            return self._parent._cast(_5835.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5842.StraightBevelDiffGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5842,
            )

            return self._parent._cast(_5842.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5845.StraightBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5845,
            )

            return self._parent._cast(_5845.StraightBevelGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5864.ZerolBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5864,
            )

            return self._parent._cast(_5864.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "ConicalGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2746.ConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection

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
    ) -> "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis":
        return self._Cast_ConicalGearSetHarmonicAnalysis(self)
