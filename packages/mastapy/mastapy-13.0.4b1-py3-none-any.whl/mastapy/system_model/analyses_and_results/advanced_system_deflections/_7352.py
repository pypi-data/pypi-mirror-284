"""FEPartAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7293
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "FEPartAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.static_loads import _6909
    from mastapy.system_model.analyses_and_results.system_deflections import _2778
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7319,
        _7376,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("FEPartAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="FEPartAdvancedSystemDeflection")


class FEPartAdvancedSystemDeflection(
    _7293.AbstractShaftOrHousingAdvancedSystemDeflection
):
    """FEPartAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FE_PART_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartAdvancedSystemDeflection")

    class _Cast_FEPartAdvancedSystemDeflection:
        """Special nested class for casting FEPartAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
            parent: "FEPartAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
        ) -> "_7293.AbstractShaftOrHousingAdvancedSystemDeflection":
            return self._parent._cast(
                _7293.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def component_advanced_system_deflection(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
        ) -> "_7319.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
        ) -> "_7376.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def fe_part_advanced_system_deflection(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
        ) -> "FEPartAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2473.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6909.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2778.FEPartSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[FEPartAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.FEPartAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "FEPartAdvancedSystemDeflection._Cast_FEPartAdvancedSystemDeflection":
        return self._Cast_FEPartAdvancedSystemDeflection(self)
