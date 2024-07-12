"""CVTPulleyCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7515,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CVTPulleyCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7337,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7466,
        _7504,
        _7452,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CVTPulleyCompoundAdvancedSystemDeflection")


class CVTPulleyCompoundAdvancedSystemDeflection(
    _7515.PulleyCompoundAdvancedSystemDeflection
):
    """CVTPulleyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyCompoundAdvancedSystemDeflection"
    )

    class _Cast_CVTPulleyCompoundAdvancedSystemDeflection:
        """Special nested class for casting CVTPulleyCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
            parent: "CVTPulleyCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def pulley_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ) -> "_7515.PulleyCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7515.PulleyCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ) -> "_7466.CouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(
                _7466.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ) -> "_7504.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ) -> "_7452.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(_7452.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ) -> "CVTPulleyCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7337.CVTPulleyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CVTPulleyAdvancedSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7337.CVTPulleyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CVTPulleyAdvancedSystemDeflection]

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
    ) -> "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection":
        return self._Cast_CVTPulleyCompoundAdvancedSystemDeflection(self)
