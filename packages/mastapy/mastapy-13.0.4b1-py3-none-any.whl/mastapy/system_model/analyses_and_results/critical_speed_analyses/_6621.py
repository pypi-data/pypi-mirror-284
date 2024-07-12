"""FaceGearMeshCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6626
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "FaceGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.static_loads import _6907
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6632,
        _6599,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="FaceGearMeshCriticalSpeedAnalysis")


class FaceGearMeshCriticalSpeedAnalysis(_6626.GearMeshCriticalSpeedAnalysis):
    """FaceGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshCriticalSpeedAnalysis")

    class _Cast_FaceGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting FaceGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
            parent: "FaceGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_critical_speed_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ) -> "_6626.GearMeshCriticalSpeedAnalysis":
            return self._parent._cast(_6626.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ) -> "_6632.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6632,
            )

            return self._parent._cast(
                _6632.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ) -> "_6599.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6599,
            )

            return self._parent._cast(_6599.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ) -> "FaceGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "FaceGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2331.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6907.FaceGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

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
    ) -> "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis":
        return self._Cast_FaceGearMeshCriticalSpeedAnalysis(self)
