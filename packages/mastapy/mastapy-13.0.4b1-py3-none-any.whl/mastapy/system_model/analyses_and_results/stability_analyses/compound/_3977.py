"""GearMeshCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3983
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "GearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3844
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3923,
        _3930,
        _3935,
        _3948,
        _3951,
        _3966,
        _3972,
        _3981,
        _3985,
        _3988,
        _3991,
        _4018,
        _4024,
        _4027,
        _4042,
        _4045,
        _3953,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundStabilityAnalysis")


class GearMeshCompoundStabilityAnalysis(
    _3983.InterMountableComponentConnectionCompoundStabilityAnalysis
):
    """GearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundStabilityAnalysis")

    class _Cast_GearMeshCompoundStabilityAnalysis:
        """Special nested class for casting GearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
            parent: "GearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3983.InterMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent._cast(
                _3983.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3953.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(
                _3923.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3930.BevelDifferentialGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(
                _3930.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3935.BevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(_3935.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def concept_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3948.ConceptGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3951.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3966.CylindricalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.CylindricalGearMeshCompoundStabilityAnalysis
            )

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3972.FaceGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3981.HypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(_3981.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3985.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_3988.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(
                _3988.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> (
            "_3991.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(
                _3991.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_4018.SpiralBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_4024.StraightBevelDiffGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(
                _4024.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_4027.StraightBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(
                _4027.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_4042.WormGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4042,
            )

            return self._parent._cast(_4042.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "_4045.ZerolBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4045,
            )

            return self._parent._cast(_4045.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "GearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "GearMeshCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3844.GearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearMeshStabilityAnalysis]

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
    ) -> "List[_3844.GearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearMeshStabilityAnalysis]

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
    ) -> "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis":
        return self._Cast_GearMeshCompoundStabilityAnalysis(self)
