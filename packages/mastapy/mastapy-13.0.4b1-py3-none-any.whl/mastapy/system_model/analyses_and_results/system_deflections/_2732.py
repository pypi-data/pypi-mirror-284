"""ClutchConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2750
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ClutchConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2362
    from mastapy.system_model.analyses_and_results.static_loads import _6854
    from mastapy.system_model.analyses_and_results.power_flows import _4074
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2788,
        _2748,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7561,
        _7562,
        _7559,
    )
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionSystemDeflection",)


Self = TypeVar("Self", bound="ClutchConnectionSystemDeflection")


class ClutchConnectionSystemDeflection(_2750.CouplingConnectionSystemDeflection):
    """ClutchConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchConnectionSystemDeflection")

    class _Cast_ClutchConnectionSystemDeflection:
        """Special nested class for casting ClutchConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
            parent: "ClutchConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_system_deflection(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
        ) -> "_2750.CouplingConnectionSystemDeflection":
            return self._parent._cast(_2750.CouplingConnectionSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
        ) -> "_2788.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(
                _2788.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
        ) -> "_2748.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
        ) -> "_7561.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_system_deflection(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
        ) -> "ClutchConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchConnectionSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2362.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6854.ClutchConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4074.ClutchConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ClutchConnectionPowerFlow

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
    ) -> "ClutchConnectionSystemDeflection._Cast_ClutchConnectionSystemDeflection":
        return self._Cast_ClutchConnectionSystemDeflection(self)
