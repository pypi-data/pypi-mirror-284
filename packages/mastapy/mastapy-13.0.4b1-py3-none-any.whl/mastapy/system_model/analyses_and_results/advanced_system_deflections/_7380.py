"""PlanetaryConnectionAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7394
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "PlanetaryConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2307
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.system_deflections import _2810
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7294,
        _7329,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PlanetaryConnectionAdvancedSystemDeflection")


class PlanetaryConnectionAdvancedSystemDeflection(
    _7394.ShaftToMountableComponentConnectionAdvancedSystemDeflection
):
    """PlanetaryConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionAdvancedSystemDeflection"
    )

    class _Cast_PlanetaryConnectionAdvancedSystemDeflection:
        """Special nested class for casting PlanetaryConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
            parent: "PlanetaryConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
        ) -> "_7394.ShaftToMountableComponentConnectionAdvancedSystemDeflection":
            return self._parent._cast(
                _7394.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
        ) -> (
            "_7294.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(
                _7294.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
        ) -> "_7329.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_connection_advanced_system_deflection(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
        ) -> "PlanetaryConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionAdvancedSystemDeflection.TYPE"
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
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2810.PlanetaryConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectionAdvancedSystemDeflection._Cast_PlanetaryConnectionAdvancedSystemDeflection":
        return self._Cast_PlanetaryConnectionAdvancedSystemDeflection(self)
