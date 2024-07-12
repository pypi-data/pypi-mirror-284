"""PlanetaryConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PlanetaryConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2307
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5400, _5435
    from mastapy.system_model.analyses_and_results.analysis_cases import _7563, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionMultibodyDynamicsAnalysis")


class PlanetaryConnectionMultibodyDynamicsAnalysis(
    _5508.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """PlanetaryConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_PlanetaryConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting PlanetaryConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
            parent: "PlanetaryConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_5508.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5508.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> (
            "_5400.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(
                _5400.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_5435.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_7563.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7563

            return self._parent._cast(_7563.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
        ) -> "PlanetaryConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "PlanetaryConnectionMultibodyDynamicsAnalysis.TYPE",
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
    ) -> "PlanetaryConnectionMultibodyDynamicsAnalysis._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis":
        return self._Cast_PlanetaryConnectionMultibodyDynamicsAnalysis(self)
