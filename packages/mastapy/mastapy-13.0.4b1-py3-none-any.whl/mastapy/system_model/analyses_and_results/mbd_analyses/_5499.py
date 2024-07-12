"""RingPinsToDiscConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5470
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2361
    from mastapy.system_model.analyses_and_results.static_loads import _6966
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5435
    from mastapy.system_model.analyses_and_results.analysis_cases import _7563, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionMultibodyDynamicsAnalysis")


class RingPinsToDiscConnectionMultibodyDynamicsAnalysis(
    _5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """RingPinsToDiscConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
            parent: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
        ) -> "_5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
        ) -> "_5435.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
        ) -> "_7563.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7563

            return self._parent._cast(_7563.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(
            self: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
        ) -> "RingPinsToDiscConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "RingPinsToDiscConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2361.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6966.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

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
    ) -> "RingPinsToDiscConnectionMultibodyDynamicsAnalysis._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis":
        return self._Cast_RingPinsToDiscConnectionMultibodyDynamicsAnalysis(self)
