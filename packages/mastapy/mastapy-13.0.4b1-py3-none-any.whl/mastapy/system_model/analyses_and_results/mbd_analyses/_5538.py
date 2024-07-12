"""WormGearMeshMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5458
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "WormGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2349
    from mastapy.system_model.analyses_and_results.static_loads import _7005
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5470, _5435
    from mastapy.system_model.analyses_and_results.analysis_cases import _7563, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="WormGearMeshMultibodyDynamicsAnalysis")


class WormGearMeshMultibodyDynamicsAnalysis(_5458.GearMeshMultibodyDynamicsAnalysis):
    """WormGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_WormGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting WormGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
            parent: "WormGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5458.GearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(_5458.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(
                _5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5435.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7563.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7563

            return self._parent._cast(_7563.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
        ) -> "WormGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "WormGearMeshMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2349.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_7005.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

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
    ) -> "WormGearMeshMultibodyDynamicsAnalysis._Cast_WormGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_WormGearMeshMultibodyDynamicsAnalysis(self)
