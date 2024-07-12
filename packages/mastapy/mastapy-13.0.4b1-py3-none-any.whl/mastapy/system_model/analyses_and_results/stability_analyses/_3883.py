"""ShaftToMountableComponentConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3787
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ShaftToMountableComponentConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2315
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3808,
        _3829,
        _3869,
        _3819,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionStabilityAnalysis")


class ShaftToMountableComponentConnectionStabilityAnalysis(
    _3787.AbstractShaftToMountableComponentConnectionStabilityAnalysis
):
    """ShaftToMountableComponentConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionStabilityAnalysis"
    )

    class _Cast_ShaftToMountableComponentConnectionStabilityAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
            parent: "ShaftToMountableComponentConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3787.AbstractShaftToMountableComponentConnectionStabilityAnalysis":
            return self._parent._cast(
                _3787.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3819.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_stability_analysis(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3808.CoaxialConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(_3808.CoaxialConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3829.CycloidalDiscCentralBearingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(
                _3829.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def planetary_connection_stability_analysis(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3869.PlanetaryConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3869,
            )

            return self._parent._cast(_3869.PlanetaryConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "ShaftToMountableComponentConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionStabilityAnalysis.TYPE",
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
    ) -> "ShaftToMountableComponentConnectionStabilityAnalysis._Cast_ShaftToMountableComponentConnectionStabilityAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionStabilityAnalysis(self)
