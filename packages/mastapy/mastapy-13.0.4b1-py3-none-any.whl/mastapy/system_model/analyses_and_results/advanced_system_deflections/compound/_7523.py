"""ShaftHubConnectionCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7463,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ShaftHubConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2619
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7393,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7504,
        _7452,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ShaftHubConnectionCompoundAdvancedSystemDeflection")


class ShaftHubConnectionCompoundAdvancedSystemDeflection(
    _7463.ConnectorCompoundAdvancedSystemDeflection
):
    """ShaftHubConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection"
    )

    class _Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting ShaftHubConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection",
            parent: "ShaftHubConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connector_compound_advanced_system_deflection(
            self: "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7463.ConnectorCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7463.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7504.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7452.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(_7452.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection",
        ) -> "ShaftHubConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ShaftHubConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2619.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7393.ShaftHubConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ShaftHubConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(
        self: Self,
    ) -> "List[ShaftHubConnectionCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ShaftHubConnectionCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7393.ShaftHubConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ShaftHubConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftHubConnectionCompoundAdvancedSystemDeflection._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_ShaftHubConnectionCompoundAdvancedSystemDeflection(self)
