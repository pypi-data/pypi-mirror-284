"""CVTBeltConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4062
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CVTBeltConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2293
    from mastapy.system_model.analyses_and_results.power_flows import _4121, _4088
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionPowerFlow",)


Self = TypeVar("Self", bound="CVTBeltConnectionPowerFlow")


class CVTBeltConnectionPowerFlow(_4062.BeltConnectionPowerFlow):
    """CVTBeltConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionPowerFlow")

    class _Cast_CVTBeltConnectionPowerFlow:
        """Special nested class for casting CVTBeltConnectionPowerFlow to subclasses."""

        def __init__(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
            parent: "CVTBeltConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def belt_connection_power_flow(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ) -> "_4062.BeltConnectionPowerFlow":
            return self._parent._cast(_4062.BeltConnectionPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ) -> "_4121.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ) -> "_4088.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_power_flow(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ) -> "CVTBeltConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTBeltConnectionPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2293.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

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
    ) -> "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow":
        return self._Cast_CVTBeltConnectionPowerFlow(self)
