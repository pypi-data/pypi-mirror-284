"""GearMeshStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3851
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "GearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3788,
        _3795,
        _3800,
        _3813,
        _3816,
        _3832,
        _3839,
        _3848,
        _3852,
        _3855,
        _3858,
        _3885,
        _3894,
        _3897,
        _3912,
        _3915,
        _3819,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="GearMeshStabilityAnalysis")


class GearMeshStabilityAnalysis(
    _3851.InterMountableComponentConnectionStabilityAnalysis
):
    """GearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshStabilityAnalysis")

    class _Cast_GearMeshStabilityAnalysis:
        """Special nested class for casting GearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
            parent: "GearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3851.InterMountableComponentConnectionStabilityAnalysis":
            return self._parent._cast(
                _3851.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3819.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3788.AGMAGleasonConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3795.BevelDifferentialGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3800.BevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.BevelGearMeshStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3813.ConceptGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3813,
            )

            return self._parent._cast(_3813.ConceptGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3816.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.ConicalGearMeshStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3832.CylindricalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(_3832.CylindricalGearMeshStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3839.FaceGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.FaceGearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3848.HypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.HypoidGearMeshStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3852.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(
                _3852.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3855.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(
                _3855.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3858.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(
                _3858.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3885.SpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3894.StraightBevelDiffGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3894,
            )

            return self._parent._cast(_3894.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3897.StraightBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3897,
            )

            return self._parent._cast(_3897.StraightBevelGearMeshStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3912.WormGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3912,
            )

            return self._parent._cast(_3912.WormGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "_3915.ZerolBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3915,
            )

            return self._parent._cast(_3915.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis",
        ) -> "GearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2333.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshStabilityAnalysis._Cast_GearMeshStabilityAnalysis":
        return self._Cast_GearMeshStabilityAnalysis(self)
