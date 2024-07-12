"""PlanetaryConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3883
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PlanetaryConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2307
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3787,
        _3819,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionStabilityAnalysis")


class PlanetaryConnectionStabilityAnalysis(
    _3883.ShaftToMountableComponentConnectionStabilityAnalysis
):
    """PlanetaryConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectionStabilityAnalysis")

    class _Cast_PlanetaryConnectionStabilityAnalysis:
        """Special nested class for casting PlanetaryConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
            parent: "PlanetaryConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
        ) -> "_3883.ShaftToMountableComponentConnectionStabilityAnalysis":
            return self._parent._cast(
                _3883.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
        ) -> "_3787.AbstractShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(
                _3787.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
        ) -> "_3819.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_connection_stability_analysis(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
        ) -> "PlanetaryConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2307.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6954.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

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
    ) -> "PlanetaryConnectionStabilityAnalysis._Cast_PlanetaryConnectionStabilityAnalysis":
        return self._Cast_PlanetaryConnectionStabilityAnalysis(self)
