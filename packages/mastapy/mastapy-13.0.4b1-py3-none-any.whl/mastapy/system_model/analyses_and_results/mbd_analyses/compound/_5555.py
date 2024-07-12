"""AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5583
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5401
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5562,
        _5567,
        _5613,
        _5650,
        _5656,
        _5659,
        _5677,
        _5609,
        _5615,
        _5585,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7560, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis"
)


class AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis(
    _5583.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
            parent: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5583.ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5583.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5609.GearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(_5609.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5615.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(
                _5615.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5585.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(_5585.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7560.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7560

            return self._parent._cast(_7560.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(
                _5562.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5567.BevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(
                _5567.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5613.HypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5650.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5656.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5659.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5659,
            )

            return self._parent._cast(
                _5659.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5677.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5677,
            )

            return self._parent._cast(
                _5677.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5401.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "List[_5401.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis(
            self
        )
