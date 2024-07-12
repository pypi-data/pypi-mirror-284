"""StraightBevelGearMeshStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3800
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StraightBevelGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2347
    from mastapy.system_model.analyses_and_results.static_loads import _6985
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3788,
        _3816,
        _3844,
        _3851,
        _3819,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearMeshStabilityAnalysis")


class StraightBevelGearMeshStabilityAnalysis(_3800.BevelGearMeshStabilityAnalysis):
    """StraightBevelGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshStabilityAnalysis"
    )

    class _Cast_StraightBevelGearMeshStabilityAnalysis:
        """Special nested class for casting StraightBevelGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
            parent: "StraightBevelGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_3800.BevelGearMeshStabilityAnalysis":
            return self._parent._cast(_3800.BevelGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_3788.AGMAGleasonConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_3816.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_3844.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_3851.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(
                _3851.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_3819.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
        ) -> "StraightBevelGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelGearMeshStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2347.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6985.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearMeshStabilityAnalysis._Cast_StraightBevelGearMeshStabilityAnalysis":
        return self._Cast_StraightBevelGearMeshStabilityAnalysis(self)
