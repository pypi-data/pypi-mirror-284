"""ClutchConnectionAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7333
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ClutchConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2362
    from mastapy.system_model.analyses_and_results.static_loads import _6854
    from mastapy.system_model.analyses_and_results.system_deflections import _2732
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7361,
        _7329,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ClutchConnectionAdvancedSystemDeflection")


class ClutchConnectionAdvancedSystemDeflection(
    _7333.CouplingConnectionAdvancedSystemDeflection
):
    """ClutchConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchConnectionAdvancedSystemDeflection"
    )

    class _Cast_ClutchConnectionAdvancedSystemDeflection:
        """Special nested class for casting ClutchConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
            parent: "ClutchConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_advanced_system_deflection(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
        ) -> "_7333.CouplingConnectionAdvancedSystemDeflection":
            return self._parent._cast(_7333.CouplingConnectionAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
        ) -> "_7361.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(
                _7361.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
        ) -> "_7329.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_advanced_system_deflection(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
        ) -> "ClutchConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ClutchConnectionAdvancedSystemDeflection.TYPE"
    ):
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
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2732.ClutchConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ClutchConnectionSystemDeflection]

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
    ) -> "ClutchConnectionAdvancedSystemDeflection._Cast_ClutchConnectionAdvancedSystemDeflection":
        return self._Cast_ClutchConnectionAdvancedSystemDeflection(self)
