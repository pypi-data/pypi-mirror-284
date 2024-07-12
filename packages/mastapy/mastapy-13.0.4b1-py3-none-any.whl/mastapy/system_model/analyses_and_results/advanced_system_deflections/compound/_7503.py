"""MeasurementComponentCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7549,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "MeasurementComponentCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2483
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7373,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7504,
        _7452,
        _7506,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="MeasurementComponentCompoundAdvancedSystemDeflection")


class MeasurementComponentCompoundAdvancedSystemDeflection(
    _7549.VirtualComponentCompoundAdvancedSystemDeflection
):
    """MeasurementComponentCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCompoundAdvancedSystemDeflection"
    )

    class _Cast_MeasurementComponentCompoundAdvancedSystemDeflection:
        """Special nested class for casting MeasurementComponentCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
            parent: "MeasurementComponentCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7549.VirtualComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7549.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7504.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7452.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(_7452.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7506.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "MeasurementComponentCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "MeasurementComponentCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2483.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

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
    ) -> "List[_7373.MeasurementComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.MeasurementComponentAdvancedSystemDeflection]

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
    ) -> "List[_7373.MeasurementComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.MeasurementComponentAdvancedSystemDeflection]

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
    ) -> "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection":
        return self._Cast_MeasurementComponentCompoundAdvancedSystemDeflection(self)
