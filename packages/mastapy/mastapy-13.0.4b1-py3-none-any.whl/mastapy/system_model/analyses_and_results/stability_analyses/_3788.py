"""AGMAGleasonConicalGearMeshStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AGMAGleasonConicalGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3795,
        _3800,
        _3848,
        _3885,
        _3894,
        _3897,
        _3915,
        _3844,
        _3851,
        _3819,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshStabilityAnalysis")


class AGMAGleasonConicalGearMeshStabilityAnalysis(
    _3816.ConicalGearMeshStabilityAnalysis
):
    """AGMAGleasonConicalGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
            parent: "AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3816.ConicalGearMeshStabilityAnalysis":
            return self._parent._cast(_3816.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3844.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3851.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(
                _3851.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3819.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3795.BevelDifferentialGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3800.BevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.BevelGearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3848.HypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.HypoidGearMeshStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3885.SpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3894.StraightBevelDiffGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3894,
            )

            return self._parent._cast(_3894.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3897.StraightBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3897,
            )

            return self._parent._cast(_3897.StraightBevelGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "_3915.ZerolBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3915,
            )

            return self._parent._cast(_3915.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis(self)
