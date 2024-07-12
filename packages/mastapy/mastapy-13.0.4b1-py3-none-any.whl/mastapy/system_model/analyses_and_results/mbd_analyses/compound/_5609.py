"""GearMeshCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5615
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "GearMeshCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5458
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5555,
        _5562,
        _5567,
        _5580,
        _5583,
        _5598,
        _5604,
        _5613,
        _5617,
        _5620,
        _5623,
        _5650,
        _5656,
        _5659,
        _5674,
        _5677,
        _5585,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundMultibodyDynamicsAnalysis")


class GearMeshCompoundMultibodyDynamicsAnalysis(
    _5615.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
):
    """GearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_GearMeshCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting GearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
            parent: "GearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5615.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5615.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5585.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(_5585.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5555.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5555,
            )

            return self._parent._cast(
                _5555.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(
                _5562.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5567.BevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(
                _5567.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.ConceptGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(
                _5580.ConceptGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5583.ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(
                _5583.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5598.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5598,
            )

            return self._parent._cast(
                _5598.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5604.FaceGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(
                _5604.FaceGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5613.HypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5617.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(
                _5617.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5620.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(
                _5620.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5623.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5650.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5656.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5659.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5659,
            )

            return self._parent._cast(
                _5659.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5674.WormGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5674,
            )

            return self._parent._cast(
                _5674.WormGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5677.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5677,
            )

            return self._parent._cast(
                _5677.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "GearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "GearMeshCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5458.GearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMeshMultibodyDynamicsAnalysis]

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
    ) -> "List[_5458.GearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMeshMultibodyDynamicsAnalysis]

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
    ) -> "GearMeshCompoundMultibodyDynamicsAnalysis._Cast_GearMeshCompoundMultibodyDynamicsAnalysis":
        return self._Cast_GearMeshCompoundMultibodyDynamicsAnalysis(self)
