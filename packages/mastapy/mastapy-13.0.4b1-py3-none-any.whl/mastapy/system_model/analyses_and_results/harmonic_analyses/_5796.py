"""KlingelnbergCycloPalloidConicalGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5733
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.system_deflections import _2791
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5799,
        _5802,
        _5774,
        _5807,
        _5726,
        _5809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearHarmonicAnalysis")


class KlingelnbergCycloPalloidConicalGearHarmonicAnalysis(
    _5733.ConicalGearHarmonicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_5733.ConicalGearHarmonicAnalysis":
            return self._parent._cast(_5733.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_5774.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(_5774.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_5807.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(_5807.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_5726.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_5809.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_5799.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(
                _5799.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "_5802.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(
                _5802.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2556.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "_2791.KlingelnbergCycloPalloidConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection

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
    ) -> "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysis(self)
