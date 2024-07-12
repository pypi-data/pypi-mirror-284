"""ShaftToMountableComponentConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2709
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ShaftToMountableComponentConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2315
    from mastapy.system_model.analyses_and_results.power_flows import _4155
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2735,
        _2757,
        _2810,
        _2748,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7561,
        _7562,
        _7559,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionSystemDeflection",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionSystemDeflection")


class ShaftToMountableComponentConnectionSystemDeflection(
    _2709.AbstractShaftToMountableComponentConnectionSystemDeflection
):
    """ShaftToMountableComponentConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionSystemDeflection"
    )

    class _Cast_ShaftToMountableComponentConnectionSystemDeflection:
        """Special nested class for casting ShaftToMountableComponentConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
            parent: "ShaftToMountableComponentConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2709.AbstractShaftToMountableComponentConnectionSystemDeflection":
            return self._parent._cast(
                _2709.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2748.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_7561.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def coaxial_connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2735.CoaxialConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.CoaxialConnectionSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2757.CycloidalDiscCentralBearingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(
                _2757.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def planetary_connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "_2810.PlanetaryConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.PlanetaryConnectionSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
        ) -> "ShaftToMountableComponentConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionSystemDeflection.TYPE",
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
    def power_flow_results(
        self: Self,
    ) -> "_4155.ShaftToMountableComponentConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ShaftToMountableComponentConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionSystemDeflection._Cast_ShaftToMountableComponentConnectionSystemDeflection":
        return self._Cast_ShaftToMountableComponentConnectionSystemDeflection(self)
