"""ShaftToMountableComponentConnectionCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2315
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6588,
        _6611,
        _6650,
        _6599,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionCriticalSpeedAnalysis")


class ShaftToMountableComponentConnectionCriticalSpeedAnalysis(
    _6567.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
):
    """ShaftToMountableComponentConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
            parent: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6567.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            return self._parent._cast(
                _6567.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6599.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6599,
            )

            return self._parent._cast(_6599.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6588.CoaxialConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6588,
            )

            return self._parent._cast(_6588.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6611.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6650.PlanetaryConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(_6650.PlanetaryConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "ShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2315.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

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
    ) -> "ShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionCriticalSpeedAnalysis(self)
