"""SpringDamperHalfCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "SpringDamperHalfCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2622
    from mastapy.system_model.analyses_and_results.system_deflections import _2832
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2950,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundSystemDeflection")


class SpringDamperHalfCompoundSystemDeflection(
    _2911.CouplingHalfCompoundSystemDeflection
):
    """SpringDamperHalfCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfCompoundSystemDeflection"
    )

    class _Cast_SpringDamperHalfCompoundSystemDeflection:
        """Special nested class for casting SpringDamperHalfCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection",
            parent: "SpringDamperHalfCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_system_deflection(
            self: "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection",
        ) -> "_2911.CouplingHalfCompoundSystemDeflection":
            return self._parent._cast(_2911.CouplingHalfCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection",
        ) -> "SpringDamperHalfCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "SpringDamperHalfCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2622.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

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
    ) -> "List[_2832.SpringDamperHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection]

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
    ) -> "List[_2832.SpringDamperHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection]

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
    ) -> "SpringDamperHalfCompoundSystemDeflection._Cast_SpringDamperHalfCompoundSystemDeflection":
        return self._Cast_SpringDamperHalfCompoundSystemDeflection(self)
