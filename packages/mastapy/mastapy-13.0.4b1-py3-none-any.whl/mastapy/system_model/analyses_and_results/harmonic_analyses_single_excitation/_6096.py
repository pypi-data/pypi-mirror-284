"""KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6061,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6099,
        _6102,
        _6087,
        _6108,
        _6054,
        _6110,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
)


class KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation(
    _6061.ConicalGearHarmonicAnalysisOfSingleExcitation
):
    """KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
            parent: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6061.ConicalGearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6061.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(_6087.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(_6054.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6099.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(
                _6099.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6102.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(
                _6102.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation(
            self
        )
