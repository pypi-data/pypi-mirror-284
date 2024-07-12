"""ConicalGearMeshCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5959
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConicalGearMeshCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5734
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5905,
        _5912,
        _5917,
        _5963,
        _5967,
        _5970,
        _5973,
        _6000,
        _6006,
        _6009,
        _6027,
        _5965,
        _5935,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundHarmonicAnalysis")


class ConicalGearMeshCompoundHarmonicAnalysis(_5959.GearMeshCompoundHarmonicAnalysis):
    """ConicalGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundHarmonicAnalysis"
    )

    class _Cast_ConicalGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting ConicalGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
            parent: "ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5959.GearMeshCompoundHarmonicAnalysis":
            return self._parent._cast(_5959.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5965.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(
                _5965.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5935.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5905.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(
                _5905.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5912.BevelDifferentialGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(
                _5912.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5917.BevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(_5917.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5963.HypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(_5963.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5967.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(
                _5967.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5970.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(
                _5970.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> (
            "_5973.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5973,
            )

            return self._parent._cast(
                _5973.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_6000.SpiralBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_6006.StraightBevelDiffGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6006,
            )

            return self._parent._cast(
                _6006.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_6009.StraightBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6009,
            )

            return self._parent._cast(
                _6009.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_6027.ZerolBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6027,
            )

            return self._parent._cast(_6027.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "ConicalGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearMeshCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.ConicalGearMeshCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5734.ConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5734.ConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis":
        return self._Cast_ConicalGearMeshCompoundHarmonicAnalysis(self)
