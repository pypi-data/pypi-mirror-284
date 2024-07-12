"""ConnectorCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7504,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConnectorCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7330,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7435,
        _7505,
        _7523,
        _7452,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConnectorCompoundAdvancedSystemDeflection")


class ConnectorCompoundAdvancedSystemDeflection(
    _7504.MountableComponentCompoundAdvancedSystemDeflection
):
    """ConnectorCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectorCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConnectorCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConnectorCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
            parent: "ConnectorCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7504.MountableComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7504.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7452.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(_7452.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7435.BearingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7435,
            )

            return self._parent._cast(_7435.BearingCompoundAdvancedSystemDeflection)

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7505.OilSealCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7505,
            )

            return self._parent._cast(_7505.OilSealCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7523.ShaftHubConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.ShaftHubConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connector_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "ConnectorCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConnectorCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7330.ConnectorAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConnectorAdvancedSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7330.ConnectorAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConnectorAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection":
        return self._Cast_ConnectorCompoundAdvancedSystemDeflection(self)
