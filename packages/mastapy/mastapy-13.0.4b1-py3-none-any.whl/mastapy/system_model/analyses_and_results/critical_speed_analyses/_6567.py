"""AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
        "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2285
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6588,
        _6611,
        _6613,
        _6650,
        _6664,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"
)


class AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis(
    _6599.ConnectionCriticalSpeedAnalysis
):
    """AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def connection_critical_speed_analysis(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6599.ConnectionCriticalSpeedAnalysis":
            return self._parent._cast(_6599.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_critical_speed_analysis(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6588.CoaxialConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6588,
            )

            return self._parent._cast(_6588.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6611.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6613.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(
                _6613.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_critical_speed_analysis(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6650.PlanetaryConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(_6650.PlanetaryConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "_6664.ShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(
                _6664.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2285.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

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
    ) -> "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
        return (
            self._Cast_AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis(
                self
            )
        )
