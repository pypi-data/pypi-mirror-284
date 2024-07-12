"""CoaxialConnectionDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CoaxialConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2289
    from mastapy.system_model.analyses_and_results.static_loads import _6858
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6342,
        _6301,
        _6333,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7561,
        _7562,
        _7559,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionDynamicAnalysis")


class CoaxialConnectionDynamicAnalysis(
    _6397.ShaftToMountableComponentConnectionDynamicAnalysis
):
    """CoaxialConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionDynamicAnalysis")

    class _Cast_CoaxialConnectionDynamicAnalysis:
        """Special nested class for casting CoaxialConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
            parent: "CoaxialConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_6397.ShaftToMountableComponentConnectionDynamicAnalysis":
            return self._parent._cast(
                _6397.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_6301.AbstractShaftToMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(
                _6301.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_6333.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_7561.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "_6342.CycloidalDiscCentralBearingConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(
                _6342.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def coaxial_connection_dynamic_analysis(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
        ) -> "CoaxialConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoaxialConnectionDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2289.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6858.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

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
    ) -> "CoaxialConnectionDynamicAnalysis._Cast_CoaxialConnectionDynamicAnalysis":
        return self._Cast_CoaxialConnectionDynamicAnalysis(self)
