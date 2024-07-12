"""PartToPartShearCouplingHalfCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "PartToPartShearCouplingHalfCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.system_deflections import _2808
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2950,
        _2897,
        _2952,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundSystemDeflection",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfCompoundSystemDeflection")


class PartToPartShearCouplingHalfCompoundSystemDeflection(
    _2911.CouplingHalfCompoundSystemDeflection
):
    """PartToPartShearCouplingHalfCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfCompoundSystemDeflection"
    )

    class _Cast_PartToPartShearCouplingHalfCompoundSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection",
            parent: "PartToPartShearCouplingHalfCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_system_deflection(
            self: "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection",
        ) -> "_2911.CouplingHalfCompoundSystemDeflection":
            return self._parent._cast(_2911.CouplingHalfCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection",
        ) -> "_2950.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection",
        ) -> "_2897.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection",
        ) -> "_2952.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection",
        ) -> "PartToPartShearCouplingHalfCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

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
    ) -> "List[_2808.PartToPartShearCouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection]

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
    ) -> "List[_2808.PartToPartShearCouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection]

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
    ) -> "PartToPartShearCouplingHalfCompoundSystemDeflection._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection":
        return self._Cast_PartToPartShearCouplingHalfCompoundSystemDeflection(self)
