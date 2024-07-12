"""ConnectorCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2950
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ConnectorCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2749
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2880,
        _2951,
        _2970,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ConnectorCompoundSystemDeflection")


class ConnectorCompoundSystemDeflection(
    _2950.MountableComponentCompoundSystemDeflection
):
    """ConnectorCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCompoundSystemDeflection")

    class _Cast_ConnectorCompoundSystemDeflection:
        """Special nested class for casting ConnectorCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
            parent: "ConnectorCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2880.BearingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.BearingCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2951.OilSealCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.OilSealCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "_2970.ShaftHubConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(_2970.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
        ) -> "ConnectorCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ConnectorCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_2749.ConnectorSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection]

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
    ) -> "List[_2749.ConnectorSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection]

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
    ) -> "ConnectorCompoundSystemDeflection._Cast_ConnectorCompoundSystemDeflection":
        return self._Cast_ConnectorCompoundSystemDeflection(self)
