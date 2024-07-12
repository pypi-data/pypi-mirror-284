"""RollingRingConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5470
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "RollingRingConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2312
    from mastapy.system_model.analyses_and_results.static_loads import _6968
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5435
    from mastapy.system_model.analyses_and_results.analysis_cases import _7563, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="RollingRingConnectionMultibodyDynamicsAnalysis")


class RollingRingConnectionMultibodyDynamicsAnalysis(
    _5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """RollingRingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_RollingRingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting RollingRingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
            parent: "RollingRingConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5435.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7563.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7563

            return self._parent._cast(_7563.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
        ) -> "RollingRingConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "RollingRingConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force_on_ring_a(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceOnRingA

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def normal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def separation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Separation

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2312.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6968.RollingRingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[RollingRingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.RollingRingConnectionMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionMultibodyDynamicsAnalysis._Cast_RollingRingConnectionMultibodyDynamicsAnalysis":
        return self._Cast_RollingRingConnectionMultibodyDynamicsAnalysis(self)
