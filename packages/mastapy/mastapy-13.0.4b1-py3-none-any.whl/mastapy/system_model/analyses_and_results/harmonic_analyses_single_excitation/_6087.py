"""GearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6108,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "GearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6033,
        _6040,
        _6043,
        _6044,
        _6045,
        _6058,
        _6061,
        _6076,
        _6079,
        _6082,
        _6092,
        _6096,
        _6099,
        _6102,
        _6130,
        _6136,
        _6139,
        _6142,
        _6143,
        _6154,
        _6157,
        _6054,
        _6110,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GearHarmonicAnalysisOfSingleExcitation")


class GearHarmonicAnalysisOfSingleExcitation(
    _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
):
    """GearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
            parent: "GearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.MountableComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6108.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6054.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(_6054.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(_6110.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6033.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(
                _6033.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6040.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6043.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6044.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(
                _6044.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6045.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(_6045.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6058.ConceptGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(
                _6058.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6061.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(
                _6061.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6076.CylindricalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(
                _6076.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6079.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6082.FaceGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(_6082.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6092.HypoidGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6096.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6096,
            )

            return self._parent._cast(
                _6096.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
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
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6102.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(
                _6102.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6130.SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6130,
            )

            return self._parent._cast(
                _6130.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6136.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6139.StraightBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6139,
            )

            return self._parent._cast(
                _6139.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6142.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6142,
            )

            return self._parent._cast(
                _6142.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6143.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6143,
            )

            return self._parent._cast(
                _6143.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6154.WormGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6154,
            )

            return self._parent._cast(_6154.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6157.ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6157,
            )

            return self._parent._cast(
                _6157.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
        ) -> "GearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "GearHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.Gear":
        """mastapy.system_model.part_model.gears.Gear

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
    ) -> "GearHarmonicAnalysisOfSingleExcitation._Cast_GearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GearHarmonicAnalysisOfSingleExcitation(self)
